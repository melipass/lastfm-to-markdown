# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/64s/105cb10ff4b24b44aea729f386b3a2e5.jpg" title="God Is My Co-Pilot - I Am Not This Body"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/5691db23fd8f409c8a2cf6e4f0d69911.jpg" title="God Is My Co-Pilot - Straight Not"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/3bc4a513725a4bf787e0b502f542cd0c.jpg" title="God Is My Co-Pilot - How to Be"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/0d1db5e521ab43d3a85fdae027cc16d2.jpg" title="God Is My Co-Pilot - Mir Shlufn Nisht"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/6577974bfa2e41d9af4d9a2499cad3ee.png" title="God Is My Co-Pilot - Sex Is for Making Babies"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/c3cee2a8188c4a4ba5e9232ddc36105b.jpg" title="God Is My Co-Pilot - Speed Yr Trip"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/465c822a8de64690a9bf5e1df3c97452.png" title="Gold Panda - Lucky Shiner"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/7cca22966906be978ef06b1db481bd87.jpg" title="Buena Vista Social Club - Buena Vista Social Club"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/793452b5f71342bbb323fcfa0493c40d.jpg" title="God Is My Co-Pilot - Neko No Akubi: Nihon No Fi"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/c261c1696ec3583bc94961f8229338ce.png" title="Godspeed You! Black Emperor - F♯ A♯ ∞"> </p>

          
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
