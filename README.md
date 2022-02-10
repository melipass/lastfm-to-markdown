# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/64s/9e03af413acd5cfe3fa803a0fe3a9788.png" title="Godspeed You! Black Emperor - all lights fucked on the hairy amp drooling"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/d45a81ba79d075f28e97c513f1eff2a1.png" title="Gustavo Cerati - Siempre Es Hoy"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/b9e3f62f82e8961e034052b7dc0e8bf1.png" title="Gustavo Cerati - Bocanada"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/294a519c3790db3b3a905978dcbcf213.png" title="HAIM - Women In Music Pt. III"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/066ab6e58d461dbc3d29f96e6845191d.jpg" title="Hatari - Neyslutrans"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/ba6e017b582df85272254274d21690b7.png" title="Gwen Stefani - Love. Angel. Music. Baby."> <img src="https://lastfm.freetls.fastly.net/i/u/64s/ef8acca9d5cb424ec244b21710825118.jpg" title="Harold Budd/Brian Eno - The Pearl"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/5c904f4ea5821435e3dcaef7b249769e.jpg" title="Haddaway - The Album"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/e5176863de5a4f24b8330f89d089ef39.png" title="The Gun Club - Lucky Jim"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/433656941a78d5d94ef39ab8a7e65c5a.png" title="HAIM - Days Are Gone"> </p>

          
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
