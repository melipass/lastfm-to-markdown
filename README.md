# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/M%C3%A5neskin/Il+ballo+della+vita"><img src="https://lastfm.freetls.fastly.net/i/u/64s/d33c7642ba1cf131fd2660382c786d1f.jpg" title="Måneskin - Il ballo della vita"></a> <a href="https://www.last.fm/music/Pierce+the+Veil/A+Flair+for+the+Dramatic"><img src="https://lastfm.freetls.fastly.net/i/u/64s/eaaf2dbd3cbc69a9520f53fb164caaa0.jpg" title="Pierce the Veil - A Flair for the Dramatic"></a> <a href="https://www.last.fm/music/Tom+Morello/The+Atlas+Underground"><img src="https://lastfm.freetls.fastly.net/i/u/64s/1ab27a795b7deb100e55de3255742d1e.png" title="Tom Morello - The Atlas Underground"></a> <a href="https://www.last.fm/music/Los+Prisioneros/Corazones"><img src="https://lastfm.freetls.fastly.net/i/u/64s/221fdf7c137879cdca2a79a375d254f8.jpg" title="Los Prisioneros - Corazones"></a> <a href="https://www.last.fm/music/Arca/KICK+ii"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ad1db1d1a6a56f372ddd52b199c9afd0.jpg" title="Arca - KICK ii"></a> <a href="https://www.last.fm/music/Perfume/GAME"><img src="https://lastfm.freetls.fastly.net/i/u/64s/4c7f94c8a796c7e455f6bc5123d94570.jpg" title="Perfume - GAME"></a> <a href="https://www.last.fm/music/Avril+Lavigne/Let+Go"><img src="https://lastfm.freetls.fastly.net/i/u/64s/5196120dec2446b840ca061ed819f300.jpg" title="Avril Lavigne - Let Go"></a> <a href="https://www.last.fm/music/M%C3%A5neskin/Teatro+d%E2%80%99ira,+Vol.+I"><img src="https://lastfm.freetls.fastly.net/i/u/64s/66dde1787a7845462e9691e61143834e.jpg" title="Måneskin - Teatro d’ira, Vol. I"></a> <a href="https://www.last.fm/music/Pet+Shop+Boys/Please"><img src="https://lastfm.freetls.fastly.net/i/u/64s/858bb688810a4cc39f6f14389072ee0c.png" title="Pet Shop Boys - Please"></a> <a href="https://www.last.fm/music/Aparato+Raro/Grandes+Exitos"><img src="https://lastfm.freetls.fastly.net/i/u/64s/d031b123e5654d03a174b527fe2eda85.jpg" title="Aparato Raro - Grandes Exitos"></a> </p>

          
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
