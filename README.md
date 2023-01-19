# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Jamiroquai/Travelling+Without+Moving"><img src="https://lastfm.freetls.fastly.net/i/u/64s/64e31acac3ddc658510eb761ed9b2cdc.jpg" title="Jamiroquai - Travelling Without Moving"></a> <a href="https://www.last.fm/music/Jamiroquai/Emergency+On+Planet+Earth"><img src="https://lastfm.freetls.fastly.net/i/u/64s/6724384d471c43e73bd210300f1813c8.jpg" title="Jamiroquai - Emergency On Planet Earth"></a> <a href="https://www.last.fm/music/SZA/SOS"><img src="https://lastfm.freetls.fastly.net/i/u/64s/b2cfb5bdf137f4d6293565205965750f.jpg" title="SZA - SOS"></a> <a href="https://www.last.fm/music/Beck/Guero"><img src="https://lastfm.freetls.fastly.net/i/u/64s/365d37ea533ea43d217137b7ba52b75a.png" title="Beck - Guero"></a> <a href="https://www.last.fm/music/Janelle+Mon%C3%A1e/The+ArchAndroid+(Suites+II+and+III)"><img src="https://lastfm.freetls.fastly.net/i/u/64s/a5ab84b1f7214178a3862961896c7c1f.png" title="Janelle Monáe - The ArchAndroid (Suites II and III)"></a> <a href="https://www.last.fm/music/Beck/Mellow+Gold"><img src="https://lastfm.freetls.fastly.net/i/u/64s/544891788e874091a1d64b0c1a796c5a.png" title="Beck - Mellow Gold"></a> <a href="https://www.last.fm/music/Heartsrevolution/Switchblade+EP"><img src="https://lastfm.freetls.fastly.net/i/u/64s/827c4bb70cf04b7480fc3576a6dd34f9.png" title="Heartsrevolution - Switchblade EP"></a> </p>

          
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
