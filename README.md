# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/64s/3b4cc06fcf86423ac273b286bab456a2.jpg" title="Fulano - En El Bunker"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/a2983eb279584e98b97492e4f6b6f724.jpg" title="Fulano - Trabajos Inútiles"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/67a85fdff282efa6d4fee02fd9c3dea7.jpg" title="Fulano - Animal en extinción"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/8b482fe271aa429483bf0ac8f4c49bd7.jpg" title="Fulano - El Infierno de los Payasos"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/ae37587d24e34055c03e7d781fb442c9.jpg" title="Gacharic Spin - WINNER"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/bc2ed40affae4adf82238e8b4f6bae85.png" title="Fuck Buttons - Slow Focus"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/86d68664fccfa3b16c435d6abd98c2b5.jpg" title="Fuck Buttons - Tarot Sport"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/10a0223e15fa7dd5c060b317e91c2723.png" title="Fulano - Fulano"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/934541b38b624659909d1cb5e0f333a6.jpg" title="fun. - Aim and Ignite"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/816714bb22444d9db49bf57b0f064477.jpg" title="Funeral Party - Funeral Party"> </p>

          
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
