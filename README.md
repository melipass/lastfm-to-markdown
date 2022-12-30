# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Bring+Me+the+Horizon/Live+At+The+Royal+Albert+Hall"><img src="https://lastfm.freetls.fastly.net/i/u/64s/33ec317504d57a6ddbcf1236b47f5342.jpg" title="Bring Me the Horizon - Live At The Royal Albert Hall"></a> <a href="https://www.last.fm/music/Bring+Me+the+Horizon/That%27s+The+Spirit"><img src="https://lastfm.freetls.fastly.net/i/u/64s/e7a508490c30452c4524f74984279698.png" title="Bring Me the Horizon - That's The Spirit"></a> <a href="https://www.last.fm/music/Bring+Me+the+Horizon/amo"><img src="https://lastfm.freetls.fastly.net/i/u/64s/98ac0125284c3de2af1c0a6a1ddf301f.jpg" title="Bring Me the Horizon - amo"></a> <a href="https://www.last.fm/music/Arca/KiCk+i"><img src="https://lastfm.freetls.fastly.net/i/u/64s/f427010a793f4dccd4f8214b8c6021a2.jpg" title="Arca - KiCk i"></a> <a href="https://www.last.fm/music/Bring+Me+the+Horizon/Sempiternal"><img src="https://lastfm.freetls.fastly.net/i/u/64s/b665c029fbe8489f8e6a45dde56215d4.png" title="Bring Me the Horizon - Sempiternal"></a> </p>

          
## 👩🏽‍💻 What you'll need
* A README.md file.
* Last.fm API key
  * Fill [this form](https://www.last.fm/api/account/create) to instantly get one. Requires a last.fm account.
* Set up a GitHub Secret called ```LASTFM_API_KEY``` with the value given by last.fm.
* Also set up a ```LASTFM_USER``` GitHub Secret with the user you'll get the weekly charts for.
* Add a ```<!-- lastfm -->``` tag in your README.md file, with two blank lines below it. The album covers will be placed here.

## Instructions
To use this release, add a ```lastfm.yml``` workflow file to the ```.github/workflows``` folder in your repository with the following code:
```diff
name: lastfm-to-markdown

on:
  schedule:
    - cron: '2 0 * * *'
  workflow_dispatch:

jobs:
  lastfm:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: lastfm to markdown
        uses: melipass/lastfm-to-markdown@v1.3.1
        with:
          LASTFM_API_KEY: ${{ secrets.LASTFM_API_KEY }}
          LASTFM_USER: ${{ secrets.LASTFM_USER }}
#         INCLUDE_LINK: true # Optional. Defaults is false. If you want to include the link to the album page, set this to true.
#         IMAGE_COUNT: 6 # Optional. Defaults to 10. Feel free to remove this line if you want.
      - name: commit changes
        continue-on-error: true
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add -A
          git commit -m "Updated last.fm's weekly chart" -a

      - name: push changes
        continue-on-error: true
        uses: ad-m/github-push-action@v0.6.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}\
          branch: main
```
The cron job is scheduled to run once a day because Last.fm's API updates weekly chart data daily at 00:00, it's useless to make more than 1 request per day because you'll get the same information back every time. You can manually run the workflow in case Last.fm's API was down at the time, going to the Actions tab in your repository.

## 🚧 To do
* Allow users to choose the image size for the album covers.
* Feel free to open an issue or send a pull request for anything you believe would be useful.
