# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/64s/465c822a8de64690a9bf5e1df3c97452.png" title="Gold Panda - Lucky Shiner"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/a0a887bbce8a4813ac3af09097a05db9.jpg" title="BBS Paranoicos - Hardcore Para Señoritas"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/4c93429b4d4d4c34cc8f54c53ea61095.jpg" title="Astro - Astro"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/109a9bbdeafc4c26acc42e5e53a87524.jpg" title="Camila Moreno - Almismotiempo"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/30bda7521c6d460d9ec260b982a6c342.png" title="Goldfrapp - Black Cherry"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/e9649d7124824dee8b1392304cde797d.png" title="Duran Duran - Duran Duran"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/ecf57990ef4dfffe8c36d15cec7820ba.png" title="Goldfrapp - Felt Mountain"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/14ce4c92cdfe4341a8f064f652745098.png" title="CHC - La Cosa"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/5fe08f241a0cff7d5f6e916933cc4eaa.jpg" title="Como Asesinar a Felipes - MMXX"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/14da32ad2e824017a78a733918ba7d4e.png" title="Duran Duran - Rio"> </p>

          
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
