# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/My+Chemical+Romance/The+Black+Parade"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7675defb2787ce67cd030081eb8ff77c.png" title="My Chemical Romance - The Black Parade"></a> <a href="https://www.last.fm/music/Simple+Plan/No+Pads,+No+Helmets...Just+Balls"><img src="https://lastfm.freetls.fastly.net/i/u/64s/b95f7b7b3849441a88cbcbe6f408db88.png" title="Simple Plan - No Pads, No Helmets...Just Balls"></a> <a href="https://www.last.fm/music/A+Day+to+Remember/Homesick"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ee2c1861c992445fa15e43b4af6db55e.png" title="A Day to Remember - Homesick"></a> <a href="https://www.last.fm/music/Jimmy+Eat+World/Bleed+American"><img src="https://lastfm.freetls.fastly.net/i/u/64s/5f6bed4795106f6a5ace9295accf4493.jpg" title="Jimmy Eat World - Bleed American"></a> <a href="https://www.last.fm/music/The+Red+Jumpsuit+Apparatus/Don%27t+You+Fake+It"><img src="https://lastfm.freetls.fastly.net/i/u/64s/82698b70482fa952b5c83acea2595285.jpg" title="The Red Jumpsuit Apparatus - Don't You Fake It"></a> <a href="https://www.last.fm/music/Thursday/Full+Collapse"><img src="https://lastfm.freetls.fastly.net/i/u/64s/79e84c0c10c79a1a25859919e351028d.jpg" title="Thursday - Full Collapse"></a> <a href="https://www.last.fm/music/We+the+Kings/We+the+Kings"><img src="https://lastfm.freetls.fastly.net/i/u/64s/8307ba3b2c774c0d927fd558906866c0.png" title="We the Kings - We the Kings"></a> <a href="https://www.last.fm/music/The+Wonder+Years/The+Greatest+Generation"><img src="https://lastfm.freetls.fastly.net/i/u/64s/c0d7e865f2f4470682c177d57266864d.jpg" title="The Wonder Years - The Greatest Generation"></a> <a href="https://www.last.fm/music/My+Chemical+Romance/The+Foundations+of+Decay"><img src="https://lastfm.freetls.fastly.net/i/u/64s/55e0eb295310209bd9b9271092460187.jpg" title="My Chemical Romance - The Foundations of Decay"></a> <a href="https://www.last.fm/music/Pierce+the+Veil/Collide+With+the+Sky"><img src="https://lastfm.freetls.fastly.net/i/u/64s/557643a8faaa35768cb6088f576fed30.jpg" title="Pierce the Veil - Collide With the Sky"></a> </p>

          
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
