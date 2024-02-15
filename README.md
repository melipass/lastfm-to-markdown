# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Turnstile/GLOW+ON"><img src="https://lastfm.freetls.fastly.net/i/u/64s/9bbf56b7df22d8044b0102c3ef12183a.jpg" title="Turnstile - GLOW ON"></a> <a href="https://www.last.fm/music/Lebanon+Hanover/The+World+Is+Getting+Colder"><img src="https://lastfm.freetls.fastly.net/i/u/64s/dce5be26a45443c0c3a71fc0ba55e9af.png" title="Lebanon Hanover - The World Is Getting Colder"></a> <a href="https://www.last.fm/music/Lebanon+Hanover/Why+Not+Just+Be+Solo"><img src="https://lastfm.freetls.fastly.net/i/u/64s/71b77eb86f8e4d38cdd6b8f38ee2d115.jpg" title="Lebanon Hanover - Why Not Just Be Solo"></a> <a href="https://www.last.fm/music/Lebanon+Hanover/Tomb+for+Two"><img src="https://lastfm.freetls.fastly.net/i/u/64s/8d9a1319348a4917c9714e0d311ffec9.png" title="Lebanon Hanover - Tomb for Two"></a> <a href="https://www.last.fm/music/Iron+Maiden/Piece+of+Mind"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7753e1296c3c49565bc1967f408d95d3.jpg" title="Iron Maiden - Piece of Mind"></a> <a href="https://www.last.fm/music/Javiera+Mena/Otra+Era"><img src="https://lastfm.freetls.fastly.net/i/u/64s/cdbdd328cdaa4fefcf0f37e490f29c26.png" title="Javiera Mena - Otra Era"></a> <a href="https://www.last.fm/music/Los+Jaivas/Aconcagua"><img src="https://lastfm.freetls.fastly.net/i/u/64s/880e6d8b6d14459caa4f038291039694.jpg" title="Los Jaivas - Aconcagua"></a> <a href="https://www.last.fm/music/Iron+Maiden/The+Number+of+the+Beast"><img src="https://lastfm.freetls.fastly.net/i/u/64s/4848a0ce2f98376b71c932e409e9afb4.jpg" title="Iron Maiden - The Number of the Beast"></a> <a href="https://www.last.fm/music/Javiera+Mena/Nocturna"><img src="https://lastfm.freetls.fastly.net/i/u/64s/b31d764d13843dbc6bf26c51ee556887.png" title="Javiera Mena - Nocturna"></a> <a href="https://www.last.fm/music/Fiskales+Ad-Hok/Traga!"><img src="https://lastfm.freetls.fastly.net/i/u/64s/95ab7f6a4ff640b6c08d1fd090f04db3.png" title="Fiskales Ad-Hok - Traga!"></a> </p>

          
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
