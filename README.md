# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Corporaci%C3%B3n+Fonogr%C3%A1fica+Aut%C3%B3noma/Uno"><img src="https://lastfm.freetls.fastly.net/i/u/64s/53b7f4a82d5e4c689e4c1b3a7a837b55.png" title="Corporación Fonográfica Autónoma - Uno"></a> <a href="https://www.last.fm/music/Rina+Sawayama/SAWAYAMA"><img src="https://lastfm.freetls.fastly.net/i/u/64s/1d2f49caa9f7ab3881c22833e50443fd.jpg" title="Rina Sawayama - SAWAYAMA"></a> <a href="https://www.last.fm/music/Dua+Lipa/Future+Nostalgia"><img src="https://lastfm.freetls.fastly.net/i/u/64s/0035400731bc49c94c70d82b8c31accf.jpg" title="Dua Lipa - Future Nostalgia"></a> <a href="https://www.last.fm/music/Evanescence/The+Open+Door"><img src="https://lastfm.freetls.fastly.net/i/u/64s/8b699c0dd766a7cad3a4353b40b2dba9.jpg" title="Evanescence - The Open Door"></a> <a href="https://www.last.fm/music/Bring+Me+the+Horizon/Suicide+Season"><img src="https://lastfm.freetls.fastly.net/i/u/64s/594142ef2a94491fe45bc96598bf8005.jpg" title="Bring Me the Horizon - Suicide Season"></a> <a href="https://www.last.fm/music/Neutral+Milk+Hotel/In+the+Aeroplane+Over+the+Sea"><img src="https://lastfm.freetls.fastly.net/i/u/64s/d95051e07a714889c8f7fbbccf61bf8b.jpg" title="Neutral Milk Hotel - In the Aeroplane Over the Sea"></a> <a href="https://www.last.fm/music/Rina+Sawayama/RINA"><img src="https://lastfm.freetls.fastly.net/i/u/64s/cb77e3b22f24aac7ea7369de32cd216c.png" title="Rina Sawayama - RINA"></a> <a href="https://www.last.fm/music/M%C3%A5neskin/RUSH!"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7b9a7459af674f9f0726df055bccf13d.jpg" title="Måneskin - RUSH!"></a> <a href="https://www.last.fm/music/Omar+Souleyman/Wenu+Wenu"><img src="https://lastfm.freetls.fastly.net/i/u/64s/d56aeb3cd96d402ea4552dfebcd61a0c.png" title="Omar Souleyman - Wenu Wenu"></a> <a href="https://www.last.fm/music/LOO%CE%A0%CE%94/%5B%C3%97+%C3%97%5D"><img src="https://lastfm.freetls.fastly.net/i/u/64s/e12bb6206e20bc7703a59e27db6f68d2.jpg" title="LOOΠΔ - [× ×]"></a> </p>

          
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
