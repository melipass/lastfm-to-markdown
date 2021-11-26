# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/64s/e1bc206bc6484635c604364498cd16b1.jpg" title="CeeLo Green - Cee-Lo Green And His Perfect Imperfections"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/5a63459995c343faba1fdd8b9038ecc3.jpg" title="God Help the Girl - God Help The Girl"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/11421ccb37594b389f704247c3cabbdf.png" title="The Go! Team - Thunder, Lightning, Strike"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/0937d6798ac89d5e18baec882825eee9.jpg" title="Belle and Sebastian - The Life Pursuit"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/cab81011cf06483097a891589c7d1745.jpg" title="Belle and Sebastian - Dear Catastrophe Waitress"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/7144c3a57ba04209c2cc165afe65bab9.png" title="Belle and Sebastian - Fold Your Hands Child, You Walk Like a Peasant"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/abda74a385ff1f72c9f3516fa3c9043c.jpg" title="Belle and Sebastian - Write About Love"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/019d6208698e4bf6cb1b089b8dfb4c89.png" title="Belle and Sebastian - Tigermilk"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/a9a1347fe5731ec790aef9d59a7f1b30.jpg" title="CHVRCHES - Screen Violence"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/9200892f8e5731de0f5052433d286345.jpg" title="Hayley Williams - Petals for Armor"> </p>

          
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
