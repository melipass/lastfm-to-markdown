# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Lady+Gaga/Born+This+Way"><img src="https://lastfm.freetls.fastly.net/i/u/64s/b4a91bda3fbf54d364b4f0373f422cf3.jpg" title="Lady Gaga - Born This Way"></a> <a href="https://www.last.fm/music/Lacrimosa/Hoffnung"><img src="https://lastfm.freetls.fastly.net/i/u/64s/2b3ea2b9153fc57b465a644ef98e49da.jpg" title="Lacrimosa - Hoffnung"></a> <a href="https://www.last.fm/music/Mike+Patton/Mondo+cane"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7703428dab35153fc6ab74b279de6134.jpg" title="Mike Patton - Mondo cane"></a> <a href="https://www.last.fm/music/Lady+Gaga/The+Fame+(Special+Edition)"><img src="https://lastfm.freetls.fastly.net/i/u/64s/f090e64b5e8bbe1bdd8f0b3456acef80.jpg" title="Lady Gaga - The Fame (Special Edition)"></a> <a href="https://www.last.fm/music/Slowdive/everything+is+alive"><img src="https://lastfm.freetls.fastly.net/i/u/64s/4f3dd53076a4760c6394e68a3ebe9683.jpg" title="Slowdive - everything is alive"></a> <a href="https://www.last.fm/music/Lady+Gaga/The+Fame+Monster"><img src="https://lastfm.freetls.fastly.net/i/u/64s/6e99d7f6aabe610e95fb85358bd1a7d5.png" title="Lady Gaga - The Fame Monster"></a> <a href="https://www.last.fm/music/Evanescence/The+Open+Door"><img src="https://lastfm.freetls.fastly.net/i/u/64s/8b699c0dd766a7cad3a4353b40b2dba9.jpg" title="Evanescence - The Open Door"></a> <a href="https://www.last.fm/music/De+Kiruza/De+Kiruza"><img src="https://lastfm.freetls.fastly.net/i/u/64s/8086ea28889117b4ea263cdfb43b2d97.jpg" title="De Kiruza - De Kiruza"></a> <a href="https://www.last.fm/music/Evanescence/Fallen"><img src="https://lastfm.freetls.fastly.net/i/u/64s/709c71461153419d86742071e16426c8.png" title="Evanescence - Fallen"></a> <a href="https://www.last.fm/music/Los+Jaivas/Aconcagua"><img src="https://lastfm.freetls.fastly.net/i/u/64s/880e6d8b6d14459caa4f038291039694.jpg" title="Los Jaivas - Aconcagua"></a> </p>

          
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
