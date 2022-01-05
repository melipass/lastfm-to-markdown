# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/64s/254e2ed0799a218db9f476ffe4b54a72.jpg" title="David Byrne - Grown Backwards"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/c03e014f960b452a808d3167335876c6.png" title="Grouper - Dragging a Dead Deer Up a Hill"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/7cca22966906be978ef06b1db481bd87.jpg" title="Buena Vista Social Club - Buena Vista Social Club"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/160e777bddee4afbbe127f5e9accbab0.jpg" title="Grouper - Way Their Crept"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/6531304035b44fad9d455c477799e666.jpg" title="Grouper - Wide"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/f5ece1d252b04b689ff6b821c1f0c395.jpg" title="David Byrne - Look Into The Eyeball"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/806323c613f4318e4d29c86c25f8468b.jpg" title="BENEE - FIRE ON MARZZ"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/3192a82d2dc99bc42d9fa9dd02f280e4.jpg" title="Green Day - Woodstock 1994"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/5fb0ed8c165249b4ab6541872242abd3.png" title="Grouper - Cover the Windows and the Walls"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/1a34f6bb47144c409f7862eafe6f5654.jpg" title="Makiza - Aerolineas Makiza"> </p>

          
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
