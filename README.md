# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/64s/e9fc11176e774692c6ee5104f197c0d8.png" title="Cream - Wheels of Fire"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/996a3f46b6494165b4cec60776509d15.png" title="Franz Ferdinand - You Could Have It So Much Better"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/9bdb8fb80e35856be323bd4a50cc54c6.jpg" title="Cream - Fresh Cream"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/5bdf8bc902214fe4cfca8a44d302e867.jpg" title="Frank Turner - Poetry of the Deed"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/d626440881e69e85f9cdc8f45d710fa9.jpg" title="Franz Ferdinand - Franz Ferdinand"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/557397c58f19a5a89a003056ab196692.jpg" title="Frank Zappa - Hot Rats"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/881bd27191543eef056663b1b6d95639.jpg" title="Frank Zappa - Over-Nite Sensation"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/969d21d4cf364df2cde0d791de7a0ebb.jpg" title="Frank Turner - Sleep Is For the Week"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/52907e184f756b6f351f7b87acd7005a.jpg" title="Cream - Disraeli Gears"> </p>

          
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
