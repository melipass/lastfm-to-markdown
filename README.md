# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Evanescence/The+Open+Door"><img src="https://lastfm.freetls.fastly.net/i/u/64s/8b699c0dd766a7cad3a4353b40b2dba9.jpg" title="Evanescence - The Open Door"></a> <a href="https://www.last.fm/music/Evanescence/Origin"><img src="https://lastfm.freetls.fastly.net/i/u/64s/e2b1644c8fae4971a10d9cffbb080968.png" title="Evanescence - Origin"></a> <a href="https://www.last.fm/music/Evanescence/Synthesis"><img src="https://lastfm.freetls.fastly.net/i/u/64s/3f59b49f056d461018c02d0c5aed216f.jpg" title="Evanescence - Synthesis"></a> <a href="https://www.last.fm/music/Ghost/IMPERA"><img src="https://lastfm.freetls.fastly.net/i/u/64s/d7f5e7c6ae196d85a8c97c19129c82c9.jpg" title="Ghost - IMPERA"></a> <a href="https://www.last.fm/music/Dua+Lipa/Dua+Lipa+(Complete+Deluxe+Edition)"><img src="https://lastfm.freetls.fastly.net/i/u/64s/d16f4e6f52207a67eee7c5f4e7fc7681.jpg" title="Dua Lipa - Dua Lipa (Complete Deluxe Edition)"></a> <a href="https://www.last.fm/music/Evanescence/Fallen"><img src="https://lastfm.freetls.fastly.net/i/u/64s/709c71461153419d86742071e16426c8.png" title="Evanescence - Fallen"></a> <a href="https://www.last.fm/music/Ghost/Infestissumam"><img src="https://lastfm.freetls.fastly.net/i/u/64s/b43b667dd7fe4542a71560271359eda1.png" title="Ghost - Infestissumam"></a> <a href="https://www.last.fm/music/Ghost/Meliora"><img src="https://lastfm.freetls.fastly.net/i/u/64s/e2e0dd3520300674b8640f45817d8542.png" title="Ghost - Meliora"></a> <a href="https://www.last.fm/music/Ghost/Prequelle"><img src="https://lastfm.freetls.fastly.net/i/u/64s/9344e9c24a21f641c1ed2e6a9d6afef9.jpg" title="Ghost - Prequelle"></a> <a href="https://www.last.fm/music/Uffie/Sunshine+Factory"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ad3d4d2d9a7608820286c187f8de3d08.jpg" title="Uffie - Sunshine Factory"></a> </p>

          
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
