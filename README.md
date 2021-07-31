# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/64s/d16f4e6f52207a67eee7c5f4e7fc7681.jpg" title="Dua Lipa - Dua Lipa (Complete Deluxe Edition)"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/80007962120351b908d7d355b140350d.png" title="Foals - Antidotes"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/cdbdd328cdaa4fefcf0f37e490f29c26.png" title="Javiera Mena - Otra Era"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/61b269414d3fa768c56e5e00fa9f8588.jpg" title="Dua Lipa - Future Nostalgia"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/11e6379ebbd342e9c2c36fd61ffd050e.png" title="Foals - Total Life Forever"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/e03c6fe59b86f66d1b04ed7a06b66d9c.png" title="杏里 - TIMELY!!"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/e340ade5c6374dbf80f424666f66ecde.png" title="Föllakzoid - Föllakzoid"> </p>

          
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
        uses: melipass/lastfm-to-markdown@v1.2
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
