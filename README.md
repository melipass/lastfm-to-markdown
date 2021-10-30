# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/64s/1b18d22ddcd85184153b8d74b7202ae0.jpg" title="ADR - Deceptionista"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/a5cc7f9c1b2d6cc346a3d1436ea726d2.jpg" title="Gacharic Spin - ガチャっとBEST<2010−2014>"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/01f5846ccd9041cd91886962dc717574.png" title="ADR - Chunky Monkey"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/ffe7d3e9d94249808cf0e6bcc94d70e7.jpg" title="ADR - Solitary Pursuits"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/ecb9607459cdfa5702b6c95468bf27b3.jpg" title="ADR - Throat"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/eb8ec48b993c4b034673bf422ba50ba9.jpg" title="Blanck Mass - Animated Violence Mild"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/8a77d79bd1607310bfef30930fb78b02.jpg" title="Blanck Mass - Dumb Flesh"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/d45b28a3c1ad104ce44ff569f4bf4cc2.jpg" title="Blanck Mass - World Eater"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/ae37587d24e34055c03e7d781fb442c9.jpg" title="Gacharic Spin - WINNER"> </p>

          
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
        uses: melipass/lastfm-to-markdown@v1.3
        with:
          LASTFM_API_KEY: ${{ secrets.LASTFM_API_KEY }}
          LASTFM_USER: ${{ secrets.LASTFM_USER }}
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
