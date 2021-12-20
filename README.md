# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/64s/f2fcac6dc7454a2dca442d2df3ec2ef5.jpg" title="Descendents - Everything Sucks"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/f6b3a85f39a656aaa61d30d1d2ec8d85.png" title="Grimes - Art Angels"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/10e9c890a16b4b49c26da06310d78089.jpg" title="BENEE - Hey u x"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/94cfdb5f36a7f935b6837f5fe8840ed6.jpg" title="Grimes - Visions"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/cc6607f6d18a4ee4ee95dec47fd26084.jpg" title="3776 - 3776を聴かない理由があるとすれば"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/9196a46c5993ae2bf86ec10487dcdb90.jpg" title="Ashnikko - DEMIDEVIL"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/8b6fe1faacdcd997fc221e1ef90d230a.jpg" title="Beak> - >>>"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/eaea26139233c24c5942d78bd1ef4136.jpg" title="Bleachers - Strange Desire"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/b17ef84f8af34d5f194d090b7a937417.jpg" title="Grimes - Miss Anthropocene"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/ee96e6a12a7f454998d3b320aeb2ecc3.png" title="Groove Armada - Goodbye Country (Hello Nightclub)"> </p>

          
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
