# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Black+Pumas/Black+Pumas"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ef439d0047f456170ef7bdb57f971bd6.png" title="Black Pumas - Black Pumas"></a> <a href="https://www.last.fm/music/Adrian+Quesada/Boleros+Psicod%C3%A9licos"><img src="https://lastfm.freetls.fastly.net/i/u/64s/bf3749ed7776c716393ca47ac91418cf.jpg" title="Adrian Quesada - Boleros Psicodélicos"></a> <a href="https://www.last.fm/music/Black+Pumas/Chronicles+of+a+Diamond"><img src="https://lastfm.freetls.fastly.net/i/u/64s/24a4db882f5b53414845e6c50ae1fedf.png" title="Black Pumas - Chronicles of a Diamond"></a> <a href="https://www.last.fm/music/ASIAN+KUNG-FU+GENERATION/%E3%82%BD%E3%83%AB%E3%83%95%E3%82%A1+(2016)"><img src="https://lastfm.freetls.fastly.net/i/u/64s/c49d93805fdee9e86da64eb9ee7b6dd0.jpg" title="ASIAN KUNG-FU GENERATION - ソルファ (2016)"></a> <a href="https://www.last.fm/music/Electrodom%C3%A9sticos/Ex+la+Humanidad"><img src="https://lastfm.freetls.fastly.net/i/u/64s/8c4ea2168cfd3d4bb5ddc17b91ca9656.jpg" title="Electrodomésticos - Ex la Humanidad"></a> <a href="https://www.last.fm/music/Los+Prisioneros/Corazones"><img src="https://lastfm.freetls.fastly.net/i/u/64s/221fdf7c137879cdca2a79a375d254f8.jpg" title="Los Prisioneros - Corazones"></a> <a href="https://www.last.fm/music/Los+Jaivas/Alturas+de+Machu+Picchu"><img src="https://lastfm.freetls.fastly.net/i/u/64s/4ed138adf34449ab8ced32606cd41160.jpg" title="Los Jaivas - Alturas de Machu Picchu"></a> <a href="https://www.last.fm/music/Los+Prisioneros/La+Cultura+De+La+Basura"><img src="https://lastfm.freetls.fastly.net/i/u/64s/21f65166f9b5d8f3a0a6bec5b4ab832e.jpg" title="Los Prisioneros - La Cultura De La Basura"></a> <a href="https://www.last.fm/music/Los+Prisioneros/Pateando+Piedras"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ae1df16a50d44195897a30ef36918584.png" title="Los Prisioneros - Pateando Piedras"></a> <a href="https://www.last.fm/music/ASIAN+KUNG-FU+GENERATION/%E3%82%BD%E3%83%AB%E3%83%95%E3%82%A1"><img src="https://lastfm.freetls.fastly.net/i/u/64s/4a345ef05690bfd9cfaaabb796f2e478.jpg" title="ASIAN KUNG-FU GENERATION - ソルファ"></a> </p>

          
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
