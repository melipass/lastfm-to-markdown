# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Lady+Gaga/The+Fame+(Special+Edition)"><img src="https://lastfm.freetls.fastly.net/i/u/64s/f090e64b5e8bbe1bdd8f0b3456acef80.jpg" title="Lady Gaga - The Fame (Special Edition)"></a> <a href="https://www.last.fm/music/Lady+Gaga/Born+This+Way"><img src="https://lastfm.freetls.fastly.net/i/u/64s/b4a91bda3fbf54d364b4f0373f422cf3.jpg" title="Lady Gaga - Born This Way"></a> <a href="https://www.last.fm/music/Sleigh+Bells/Treats"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ce20760300aa191a41b71d5e33e9d014.png" title="Sleigh Bells - Treats"></a> <a href="https://www.last.fm/music/HIM/Greatest+Lovesongs+Vol.+666"><img src="https://lastfm.freetls.fastly.net/i/u/64s/e84b5bb1aadf93cfdbc6c26c8ade2bf5.jpg" title="HIM - Greatest Lovesongs Vol. 666"></a> <a href="https://www.last.fm/music/Lady+Gaga/The+Fame+Monster"><img src="https://lastfm.freetls.fastly.net/i/u/64s/6e99d7f6aabe610e95fb85358bd1a7d5.png" title="Lady Gaga - The Fame Monster"></a> <a href="https://www.last.fm/music/Sleigh+Bells/Reign+of+Terror"><img src="https://lastfm.freetls.fastly.net/i/u/64s/f1cce48f13aa4839c8bfbcb1c6ec5f7b.png" title="Sleigh Bells - Reign of Terror"></a> <a href="https://www.last.fm/music/Los+Jaivas/Aconcagua"><img src="https://lastfm.freetls.fastly.net/i/u/64s/880e6d8b6d14459caa4f038291039694.jpg" title="Los Jaivas - Aconcagua"></a> <a href="https://www.last.fm/music/Apocalyptica/Apocalyptica"><img src="https://lastfm.freetls.fastly.net/i/u/64s/3c850bbbc8b586dcd4dbc7c6fef329d9.jpg" title="Apocalyptica - Apocalyptica"></a> <a href="https://www.last.fm/music/Los+Jaivas/Alturas+de+Machu+Picchu"><img src="https://lastfm.freetls.fastly.net/i/u/64s/4ed138adf34449ab8ced32606cd41160.jpg" title="Los Jaivas - Alturas de Machu Picchu"></a> <a href="https://www.last.fm/music/M.I.A./VICKI+LEEKX+MIXTAPE"><img src="https://lastfm.freetls.fastly.net/i/u/64s/5724182d8f1d33210a216a3326ef5890.jpg" title="M.I.A. - VICKI LEEKX MIXTAPE"></a> </p>

          
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
