# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/64s/61a88c1f242fb24a834301782e80f5c2.jpg" title="Girlpool - Chaos Demos"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/87fadb66e1e11573f1ffaed9dd92d741.jpg" title="Girlpool - Powerplant"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/8489b52f6862ba8ceb48ffb0ac8459e3.png" title="Girls - Album"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/55967bf374e18beb2348f5e644eee6b7.png" title="Girlpool - What Chaos Is Imaginary"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/1b387805fe62401fc0fec477b9356877.png" title="Girlpool - Before the World Was Big"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/7ee97a7c0e884ca6cc0da389481fafe8.png" title="Genesis - A Trick Of The Tail"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/15ef1c034e1f6a71d0d69d3b6f5c534f.png" title="Lady Gaga - ARTPOP"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/bbaab7fdb58daddd02385e8f7931ef95.jpg" title="Girlpool - Girlpool"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/806ddd07e9e64e1a1ceae81dc8191f1e.jpg" title="girl in red - chapter 2"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/1d20439b8467234f5e083884792cc5c6.png" title="Genesis - Selling England by the Pound"> </p>

          
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
