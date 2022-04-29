# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Kendrick+Lamar/DAMN."><img src="https://lastfm.freetls.fastly.net/i/u/64s/243a7444e2d59ff9b38e123f7267e3be.jpg" title="Kendrick Lamar - DAMN."></a> <a href="https://www.last.fm/music/Hey+Paulette/long+ball+into+nowhere"><img src="https://lastfm.freetls.fastly.net/i/u/64s/e385c32828a5e8b099e57d59f1e1d3c3.jpg" title="Hey Paulette - long ball into nowhere"></a> <a href="https://www.last.fm/music/Hiromi/Brain"><img src="https://lastfm.freetls.fastly.net/i/u/64s/fd2abec2452a4b71b6592303b506cd60.png" title="Hiromi - Brain"></a> <a href="https://www.last.fm/music/Hiromi/Time+Control"><img src="https://lastfm.freetls.fastly.net/i/u/64s/467579398a5c416e84dac37cb23d8065.jpg" title="Hiromi - Time Control"></a> <a href="https://www.last.fm/music/Hiromi/Another+Mind"><img src="https://lastfm.freetls.fastly.net/i/u/64s/156e38fa3c5046899eb1c7f7b1681d0e.jpg" title="Hiromi - Another Mind"></a> <a href="https://www.last.fm/music/Hiromi/Spiral"><img src="https://lastfm.freetls.fastly.net/i/u/64s/72ad0b6be4e0429282f5f68106206d81.png" title="Hiromi - Spiral"></a> <a href="https://www.last.fm/music/Kanye+West/My+Beautiful+Dark+Twisted+Fantasy"><img src="https://lastfm.freetls.fastly.net/i/u/64s/8a071c4b073625018de5f0ac58727511.png" title="Kanye West - My Beautiful Dark Twisted Fantasy"></a> <a href="https://www.last.fm/music/Kanye+West/Yeezus"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7112c14a18abbea3803731457b3f1407.jpg" title="Kanye West - Yeezus"></a> </p>

          
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
