# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/64s/c39acf89cdec4250a7fbb9147a9ae499.jpg" title="The Herbaliser - There Were Seven"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/570021b68d3d9d2db08bc99a473303b0.jpg" title="Nirvana - Nevermind"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/d0db0df27ff529808834ce38465559c8.jpg" title="The Herbaliser - Take London"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/d0f3bafffecf42fcb53ea38c9dbed6a1.jpg" title="The Herbaliser Band - Session 2"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/a543dd4fd89e42d4c22f067325ff742e.jpg" title="The Herbaliser - Something Wicked This Way Comes"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/2362aacacd87ed77bda7cacbcab34155.jpg" title="The Herbaliser Band - Session One"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/7fb450815d3d8b9874e1bbecd35fe917.jpg" title="The Herbaliser - BRING OUT THE SOUND"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/f87609e9ecee469f940f4dd208f229b9.png" title="Nirvana - In Utero"> </p>

          
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
