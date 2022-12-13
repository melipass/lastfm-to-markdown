# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Jack+White/Blunderbuss"><img src="https://lastfm.freetls.fastly.net/i/u/64s/9dbff5e7be08d5d1e364c0e501be866b.jpg" title="Jack White - Blunderbuss"></a> <a href="https://www.last.fm/music/Jai+Paul/Leak+04-13+(Bait+Ones)"><img src="https://lastfm.freetls.fastly.net/i/u/64s/6ee602d5e4d9f0640db87f0841ad3be5.jpg" title="Jai Paul - Leak 04-13 (Bait Ones)"></a> <a href="https://www.last.fm/music/James+Blake/James+Blake"><img src="https://lastfm.freetls.fastly.net/i/u/64s/811308d575da4fe9cfa5d582b5d36f47.jpg" title="James Blake - James Blake"></a> <a href="https://www.last.fm/music/Javiera+Mena/Nocturna"><img src="https://lastfm.freetls.fastly.net/i/u/64s/b31d764d13843dbc6bf26c51ee556887.png" title="Javiera Mena - Nocturna"></a> <a href="https://www.last.fm/music/Bring+Me+the+Horizon/Count+Your+Blessings"><img src="https://lastfm.freetls.fastly.net/i/u/64s/1bf149b70d0b497794258726b18e6260.jpg" title="Bring Me the Horizon - Count Your Blessings"></a> <a href="https://www.last.fm/music/Jack+White/Lazaretto"><img src="https://lastfm.freetls.fastly.net/i/u/64s/d631be95305a4e90ce8fb3f6ee33baac.png" title="Jack White - Lazaretto"></a> </p>

          
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
