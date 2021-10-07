# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/64s/078739815d75895bbdd422ef402e40b1.jpg" title="Miley Cyrus - Miley Cyrus & Her Dead Petz"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/8d80ecd72b1e8571edd326ba1c163551.png" title="Garbage - Version 2.0"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/874a7d1829124caccc4eae14387ef76a.png" title="Garbage - beautifulgarbage"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/e1ee4a6e9e1e40c28ed510e0272b8ceb.png" title="Garbage - Garbage"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/1f6bc5ca0a2a67a810e5701ce08fd9d5.jpg" title="Gary Numan - The Pleasure Principle"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/40ee931be9554760c7c808787dfd5051.png" title="Garbage - Bleed Like Me"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/04b5bf0daa0c45648b279239c5e36ec7.png" title="Gary Numan - Telekon"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/8860bfd3ea86680bac8cb2decae33f06.jpg" title="Michael Jackson - Bad"> </p>

          
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
