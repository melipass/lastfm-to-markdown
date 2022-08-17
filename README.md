# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Hugh+Laurie/Didn%27t+It+Rain"><img src="https://lastfm.freetls.fastly.net/i/u/64s/53e1c03031fe4553995728b1e3d26d93.jpg" title="Hugh Laurie - Didn't It Rain"></a> <a href="https://www.last.fm/music/Hype+Williams/Find+Out+What+Happens+When+People+Stop+Being+Polite,+And+Start+Gettin%27+Reel"><img src="https://lastfm.freetls.fastly.net/i/u/64s/54636b4ad18b408fc0e83248c112ded3.png" title="Hype Williams - Find Out What Happens When People Stop Being Polite, And Start Gettin' Reel"></a> <a href="https://www.last.fm/music/Hugh+Laurie/Let+Them+Talk"><img src="https://lastfm.freetls.fastly.net/i/u/64s/cdc2574573f148dd901edf316b18221d.png" title="Hugh Laurie - Let Them Talk"></a> <a href="https://www.last.fm/music/Hype+Williams/One+Nation"><img src="https://lastfm.freetls.fastly.net/i/u/64s/a0c76880a0b24ec1bccbae83d52d66cc.png" title="Hype Williams - One Nation"></a> <a href="https://www.last.fm/music/Hot+Chip/A+Bath+Full+of+Ecstasy"><img src="https://lastfm.freetls.fastly.net/i/u/64s/85e41eaa5698a41f152071b47c7cd0a8.jpg" title="Hot Chip - A Bath Full of Ecstasy"></a> <a href="https://www.last.fm/music/iamamiwhoami/BLUE"><img src="https://lastfm.freetls.fastly.net/i/u/64s/1612e2c9d0d53952de9495d5b9f25b20.jpg" title="iamamiwhoami - BLUE"></a> <a href="https://www.last.fm/music/iamamiwhoami/kin"><img src="https://lastfm.freetls.fastly.net/i/u/64s/6f88500297974a548bae6f9855cbcef1.jpg" title="iamamiwhoami - kin"></a> <a href="https://www.last.fm/music/iamamiwhoami/bounty"><img src="https://lastfm.freetls.fastly.net/i/u/64s/38be7785d622440c91a696eb62654c26.png" title="iamamiwhoami - bounty"></a> <a href="https://www.last.fm/music/Elysia+Crampton/The+Light+That+You+Gave+Me+To+See+You"><img src="https://lastfm.freetls.fastly.net/i/u/64s/d02a07a8f4a0dae1228adb3674cc67c4.jpg" title="Elysia Crampton - The Light That You Gave Me To See You"></a> <a href="https://www.last.fm/music/Elysia+Crampton/American+Drift"><img src="https://lastfm.freetls.fastly.net/i/u/64s/912ce37b99beb0e56ff44fe0a5e09ef7.jpg" title="Elysia Crampton - American Drift"></a> </p>

          
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
