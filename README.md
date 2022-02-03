# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/64s/a0beb5604cbf4731ae6856863b82761a.png" title="Avril Lavigne - Under My Skin"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/dbb8d45e500042dab7de9e1c651250f4.png" title="The Gun Club - Mother Juno"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/9442ac02cd8f4392b3842ed22428e590.png" title="The Gun Club - Pastoral Hide and Seek"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/5196120dec2446b840ca061ed819f300.jpg" title="Avril Lavigne - Let Go"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/5eed69d03242465db531f4c9fd1888c3.png" title="The Gun Club - Divinity"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/ce5eeeedb09bcf65b70a6406340a03af.jpg" title="Avril Lavigne - The Best Damn Thing"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/f9456d3a4efa4e34a67c4fe74664f201.png" title="The Gun Club - The Las Vegas Story"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/78388f395c78e5b6c5db6be5ac1d0a18.jpg" title="Aventura - God's Project"> </p>

          
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
