# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/The+Mars+Volta/De-Loused+in+the+Comatorium"><img src="https://lastfm.freetls.fastly.net/i/u/64s/bd757ae20efd45dfb68d8303646afa7d.png" title="The Mars Volta - De-Loused in the Comatorium"></a> <a href="https://www.last.fm/music/Kraftwerk/Computerwelt"><img src="https://lastfm.freetls.fastly.net/i/u/64s/38d00092fb17e400c846243fdec54f03.jpg" title="Kraftwerk - Computerwelt"></a> <a href="https://www.last.fm/music/BADBADNOTGOOD/BBNG"><img src="https://lastfm.freetls.fastly.net/i/u/64s/916f3d6862fb2d90e4d54dacdf7bb880.jpg" title="BADBADNOTGOOD - BBNG"></a> <a href="https://www.last.fm/music/Rage+Against+the+Machine/Rage+Against+the+Machine"><img src="https://lastfm.freetls.fastly.net/i/u/64s/8f25a0a061254740c74a40a4e16337d6.png" title="Rage Against the Machine - Rage Against the Machine"></a> <a href="https://www.last.fm/music/BADBADNOTGOOD/IV"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ee6a03301fe2bfc3f5f75645e49a2c5c.jpg" title="BADBADNOTGOOD - IV"></a> <a href="https://www.last.fm/music/BADBADNOTGOOD/Talk+Memory"><img src="https://lastfm.freetls.fastly.net/i/u/64s/efa7d132ac763cc1580a0f3b8f9d4dfc.png" title="BADBADNOTGOOD - Talk Memory"></a> <a href="https://www.last.fm/music/blink-182/Dude+Ranch"><img src="https://lastfm.freetls.fastly.net/i/u/64s/e0293fc9bd4a499197517a01e6a3e1e9.png" title="blink-182 - Dude Ranch"></a> <a href="https://www.last.fm/music/blink-182/Enema+of+the+State"><img src="https://lastfm.freetls.fastly.net/i/u/64s/9f84a1b9b2634750bdd014c2bb646d96.png" title="blink-182 - Enema of the State"></a> <a href="https://www.last.fm/music/BLACKPINK/BLACKPINK"><img src="https://lastfm.freetls.fastly.net/i/u/64s/821939858a1ad08a0eed74353d30a26e.png" title="BLACKPINK - BLACKPINK"></a> <a href="https://www.last.fm/music/BADBADNOTGOOD/BBNG2"><img src="https://lastfm.freetls.fastly.net/i/u/64s/9e5fdbc3873c438fa307b4034cfe375d.jpg" title="BADBADNOTGOOD - BBNG2"></a> </p>

          
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
