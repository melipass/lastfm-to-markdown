# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Manu+Chao/Pr%C3%B3xima+Estaci%C3%B3n:+Esperanza"><img src="https://lastfm.freetls.fastly.net/i/u/64s/3fbea2a003731dfc69295ee48b04b9b5.jpg" title="Manu Chao - Próxima Estación: Esperanza"></a> <a href="https://www.last.fm/music/Garbage/Garbage"><img src="https://lastfm.freetls.fastly.net/i/u/64s/e1ee4a6e9e1e40c28ed510e0272b8ceb.png" title="Garbage - Garbage"></a> <a href="https://www.last.fm/music/Gepe/Gepinto"><img src="https://lastfm.freetls.fastly.net/i/u/64s/88633cbec943a54faf0c35449d3c10a6.jpg" title="Gepe - Gepinto"></a> <a href="https://www.last.fm/music/The+Who/My+Generation"><img src="https://lastfm.freetls.fastly.net/i/u/64s/6f3e58bea03bab88f8e73e04959b094c.png" title="The Who - My Generation"></a> <a href="https://www.last.fm/music/The+Who/A+Quick+One"><img src="https://lastfm.freetls.fastly.net/i/u/64s/05844750b0be40d997eb262d2ef6aaed.png" title="The Who - A Quick One"></a> <a href="https://www.last.fm/music/Iron+Maiden/Piece+of+Mind"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7753e1296c3c49565bc1967f408d95d3.jpg" title="Iron Maiden - Piece of Mind"></a> <a href="https://www.last.fm/music/Javiera+Mena/Otra+Era"><img src="https://lastfm.freetls.fastly.net/i/u/64s/cdbdd328cdaa4fefcf0f37e490f29c26.png" title="Javiera Mena - Otra Era"></a> <a href="https://www.last.fm/music/Violeta+Parra/Recordando+a+Chile+(Una+chilena+en+Par%C3%ADs)"><img src="https://lastfm.freetls.fastly.net/i/u/64s/f555827e24b041a59c58de25bc098cd8.png" title="Violeta Parra - Recordando a Chile (Una chilena en París)"></a> <a href="https://www.last.fm/music/Los+Jaivas/Aconcagua"><img src="https://lastfm.freetls.fastly.net/i/u/64s/880e6d8b6d14459caa4f038291039694.jpg" title="Los Jaivas - Aconcagua"></a> <a href="https://www.last.fm/music/Mike+Patton/Mondo+cane"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7703428dab35153fc6ab74b279de6134.jpg" title="Mike Patton - Mondo cane"></a> </p>

          
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
