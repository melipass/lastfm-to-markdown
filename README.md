# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Blur/Parklife"><img src="https://lastfm.freetls.fastly.net/i/u/64s/19e7df241eead2786c81e5f50c4f3364.png" title="Blur - Parklife"></a> <a href="https://www.last.fm/music/Crystal+Castles/Crystal+Castles"><img src="https://lastfm.freetls.fastly.net/i/u/64s/8da6d80eb32a8b6f35fdf09d89a004f0.jpg" title="Crystal Castles - Crystal Castles"></a> <a href="https://www.last.fm/music/Blur/Blur"><img src="https://lastfm.freetls.fastly.net/i/u/64s/5cc94288ee91f2bf085204ea693f8607.jpg" title="Blur - Blur"></a> <a href="https://www.last.fm/music/DJ+Okawari/Diorama"><img src="https://lastfm.freetls.fastly.net/i/u/64s/0432e0ec6dab425fa6373d10fd3630b6.jpg" title="DJ Okawari - Diorama"></a> <a href="https://www.last.fm/music/DJ+Okawari/Compass"><img src="https://lastfm.freetls.fastly.net/i/u/64s/13ae30dab69f4bb79582f198580660c8.jpg" title="DJ Okawari - Compass"></a> <a href="https://www.last.fm/music/Crystal+Castles/Crystal+Castles+(II)"><img src="https://lastfm.freetls.fastly.net/i/u/64s/6ee5936b857f66ac31be6082eb66e5a5.jpg" title="Crystal Castles - Crystal Castles (II)"></a> <a href="https://www.last.fm/music/DJ+Okawari/Mirror"><img src="https://lastfm.freetls.fastly.net/i/u/64s/22f2b82f1b6c9de177509f01ec72330a.jpg" title="DJ Okawari - Mirror"></a> <a href="https://www.last.fm/music/Blur/The+Great+Escape"><img src="https://lastfm.freetls.fastly.net/i/u/64s/a3e5e041b33885e07f90d5b1efd687b8.png" title="Blur - The Great Escape"></a> <a href="https://www.last.fm/music/Crystal+Castles/Crystal+Castles+(III)"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7261a45a2f8f43b1be664083bca47df4.png" title="Crystal Castles - Crystal Castles (III)"></a> <a href="https://www.last.fm/music/DJ+Okawari/Kaleidoscope"><img src="https://lastfm.freetls.fastly.net/i/u/64s/c0210bbbaec6454a93dc900e9f043732.jpg" title="DJ Okawari - Kaleidoscope"></a> </p>

          
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
