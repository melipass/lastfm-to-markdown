# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/ROSAL%C3%8DA/MOTOMAMI"><img src="https://lastfm.freetls.fastly.net/i/u/64s/28495e4395ad5e8037d992a8fbd5f132.jpg" title="ROSALÍA - MOTOMAMI"></a> <a href="https://www.last.fm/music/Hiromi/Time+Control"><img src="https://lastfm.freetls.fastly.net/i/u/64s/467579398a5c416e84dac37cb23d8065.jpg" title="Hiromi - Time Control"></a> <a href="https://www.last.fm/music/Hiromi/Spiral"><img src="https://lastfm.freetls.fastly.net/i/u/64s/72ad0b6be4e0429282f5f68106206d81.png" title="Hiromi - Spiral"></a> <a href="https://www.last.fm/music/Hiromi/Brain"><img src="https://lastfm.freetls.fastly.net/i/u/64s/fd2abec2452a4b71b6592303b506cd60.png" title="Hiromi - Brain"></a> <a href="https://www.last.fm/music/Electrodom%C3%A9sticos/%C2%A1Viva+Chile!"><img src="https://lastfm.freetls.fastly.net/i/u/64s/6325ec5cb1ad4d82cd41c28311700155.jpg" title="Electrodomésticos - ¡Viva Chile!"></a> <a href="https://www.last.fm/music/Hiromi/Beyond+Standard"><img src="https://lastfm.freetls.fastly.net/i/u/64s/935abda0333f479ba5571e2f038542aa.jpg" title="Hiromi - Beyond Standard"></a> <a href="https://www.last.fm/music/Electrodom%C3%A9sticos/La+Nueva+Canci%C3%B3n+Chilena"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7c26a4ab70cf4acbaa9f78638862c53f.jpg" title="Electrodomésticos - La Nueva Canción Chilena"></a> <a href="https://www.last.fm/music/Bomba+Est%C3%A9reo/Elegancia+Tropical"><img src="https://lastfm.freetls.fastly.net/i/u/64s/9246a532c32448e9987f0d0db536a1b4.jpg" title="Bomba Estéreo - Elegancia Tropical"></a> <a href="https://www.last.fm/music/Electrodom%C3%A9sticos/Grandes+%C3%89xitos"><img src="https://lastfm.freetls.fastly.net/i/u/64s/6075e3c9e9ce44928017144bf9ac7d2b.jpg" title="Electrodomésticos - Grandes Éxitos"></a> <a href="https://www.last.fm/music/Electrodom%C3%A9sticos/Se+Caiga+El+Cielo"><img src="https://lastfm.freetls.fastly.net/i/u/64s/10d4cc85f1524d679f13ff77201f98b7.jpg" title="Electrodomésticos - Se Caiga El Cielo"></a> </p>

          
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
