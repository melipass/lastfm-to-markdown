# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/64s/d8e7aba872c3e02549d5d09e5c3580e5.jpg" title="Health - DISCO4+"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/ab6e8fa1f2ed48099f7f2e719516d9c4.png" title="Heartsrevolution - Are We Having Fun Yet?"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/dd2f48547dd2f5d0f2d988deeaab15e1.jpg" title="Heavenly - Le Jardin de Heavenly"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/cace46d994d840d5b2ad7e2b7eeb5802.png" title="Heartsrevolution - Revolution Rising"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/2a4c3316377e99c1dfa3e7fbe72da95f.jpg" title="Health - DISCO4 :: PART I"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/bc339877d2974795873c052ed5c3a976.jpg" title="Heartsrevolution - HEARTS 日本"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/941c6786835d455cc5427a447119ba6a.jpg" title="Heartsrevolution - Ride or Die EP"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/af3a1e9ce70c1eba2b31364a00af3381.jpg" title="Heartsrevolution - Ride or Die"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/827c4bb70cf04b7480fc3576a6dd34f9.png" title="Heartsrevolution - Switchblade EP"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/601b29af883372ea3094499efff1286c.jpg" title="Heavenly - Heavenly Vs. Satan"> </p>

          
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
