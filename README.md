# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/64s/105cb10ff4b24b44aea729f386b3a2e5.jpg" title="God Is My Co-Pilot - I Am Not This Body"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/5691db23fd8f409c8a2cf6e4f0d69911.jpg" title="God Is My Co-Pilot - Straight Not"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/3bc4a513725a4bf787e0b502f542cd0c.jpg" title="God Is My Co-Pilot - How to Be"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/0d1db5e521ab43d3a85fdae027cc16d2.jpg" title="God Is My Co-Pilot - Mir Shlufn Nisht"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/6577974bfa2e41d9af4d9a2499cad3ee.png" title="God Is My Co-Pilot - Sex Is for Making Babies"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/c3cee2a8188c4a4ba5e9232ddc36105b.jpg" title="God Is My Co-Pilot - Speed Yr Trip"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/033b256f69ce0e33d498e9c6b91d1af9.png" title="The Cure - Kiss Me, Kiss Me, Kiss Me"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/e1bc206bc6484635c604364498cd16b1.jpg" title="CeeLo Green - Cee-Lo Green And His Perfect Imperfections"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/bbd56a8d2fc1f3753c54070e94662263.jpg" title="AFI - Shut Your Mouth and Open Your Eyes"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/4a710e50ed1f1bc266918646d52c2d05.jpg" title="CeeLo Green - The Lady Killer"> </p>

          
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
