# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Rodrigo+y+Gabriela/Live+in+Japan"><img src="https://lastfm.freetls.fastly.net/i/u/64s/5ed56ad96ce44c8a95f8b68bb4726cca.jpg" title="Rodrigo y Gabriela - Live in Japan"></a> <a href="https://www.last.fm/music/Alice+Glass/PREY%2F%2FIV"><img src="https://lastfm.freetls.fastly.net/i/u/64s/90f40e43eea4d0ccf7c29cc9c5bbd749.jpg" title="Alice Glass - PREY//IV"></a> <a href="https://www.last.fm/music/Rina+Sawayama/SAWAYAMA"><img src="https://lastfm.freetls.fastly.net/i/u/64s/1d2f49caa9f7ab3881c22833e50443fd.jpg" title="Rina Sawayama - SAWAYAMA"></a> <a href="https://www.last.fm/music/Pabllo+Vittar/N%C3%A3o+Para+N%C3%A3o"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7f3c57200c00589c36daf456b441b1cf.png" title="Pabllo Vittar - Não Para Não"></a> <a href="https://www.last.fm/music/Sleigh+Bells/Treats"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ce20760300aa191a41b71d5e33e9d014.png" title="Sleigh Bells - Treats"></a> <a href="https://www.last.fm/music/Rodrigo+y+Gabriela/Rodrigo+y+Gabriela"><img src="https://lastfm.freetls.fastly.net/i/u/64s/4e1db651ac484f00b870ff081ef46290.jpg" title="Rodrigo y Gabriela - Rodrigo y Gabriela"></a> <a href="https://www.last.fm/music/Draconian/Under+a+Godless+Veil"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ad4651d95e12d6860ff3de129eb0568c.jpg" title="Draconian - Under a Godless Veil"></a> <a href="https://www.last.fm/music/Rina+Sawayama/RINA"><img src="https://lastfm.freetls.fastly.net/i/u/64s/cb77e3b22f24aac7ea7369de32cd216c.png" title="Rina Sawayama - RINA"></a> <a href="https://www.last.fm/music/The+Front+Bottoms/Talon+of+the+Hawk"><img src="https://lastfm.freetls.fastly.net/i/u/64s/35462860530d9b0b3dfabe37c3bb4ec6.jpg" title="The Front Bottoms - Talon of the Hawk"></a> <a href="https://www.last.fm/music/CHAI/PINK"><img src="https://lastfm.freetls.fastly.net/i/u/64s/c7061f6efaeb277c1accdb75b5e50ce3.jpg" title="CHAI - PINK"></a> </p>

          
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
