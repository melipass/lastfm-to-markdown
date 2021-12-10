# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/64s/6808f4e458317814a6a22d01ed49bcc2.jpg" title="The Gories - I Know You Fine, but How You Doin'"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/3de13555c9888b4e94090a11e2a3a2ad.jpg" title="GoldLink - Diaspora"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/a0a887bbce8a4813ac3af09097a05db9.jpg" title="BBS Paranoicos - Hardcore Para Señoritas"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/ce6e2af584a5480b85b79371b219a92e.png" title="Gorillaz - Plastic Beach"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/4c93429b4d4d4c34cc8f54c53ea61095.jpg" title="Astro - Astro"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/271483e955d2b255160f3361a7f5fb78.jpg" title="Gorillaz - Demon Days"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/109a9bbdeafc4c26acc42e5e53a87524.jpg" title="Camila Moreno - Almismotiempo"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/218951e7e102da46c49b4f8e18e8ccfd.jpg" title="ELECTR / Emray / kawaii amen girl / I.W. / 魔装少女 - Fuwa Fuwa Spring Storm"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/30bda7521c6d460d9ec260b982a6c342.png" title="Goldfrapp - Black Cherry"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/2723700fdd4b4648939a32e2ed36262c.png" title="goreshit - tomboyish love for daughter"> </p>

          
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
