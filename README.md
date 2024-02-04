# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/King+Krule/The+OOZ"><img src="https://lastfm.freetls.fastly.net/i/u/64s/3fe337e8f3ae27a8ca00143755031334.jpg" title="King Krule - The OOZ"></a> <a href="https://www.last.fm/music/Panico/Pornostar"><img src="https://lastfm.freetls.fastly.net/i/u/64s/d8df451046624f85cf69e9d7e16b509b.jpg" title="Panico - Pornostar"></a> <a href="https://www.last.fm/music/King+Krule/6+Feet+Beneath+the+Moon"><img src="https://lastfm.freetls.fastly.net/i/u/64s/32618fce0370ea48771b8e9d4cd47f4f.jpg" title="King Krule - 6 Feet Beneath the Moon"></a> <a href="https://www.last.fm/music/King+Krule/Man+Alive!"><img src="https://lastfm.freetls.fastly.net/i/u/64s/f696f58c83a17df71f51c2b9819cdff6.jpg" title="King Krule - Man Alive!"></a> <a href="https://www.last.fm/music/IC3PEAK/%D0%A1%D0%BB%D0%B0%D0%B4%D0%BA%D0%B0%D1%8F+%D0%B6%D0%B8%D0%B7%D0%BD%D1%8C"><img src="https://lastfm.freetls.fastly.net/i/u/64s/5012ae8978c36c72906d4fe0ae57a293.jpg" title="IC3PEAK - Сладкая жизнь"></a> <a href="https://www.last.fm/music/Fiskales+Ad-Hok/Traga!"><img src="https://lastfm.freetls.fastly.net/i/u/64s/95ab7f6a4ff640b6c08d1fd090f04db3.png" title="Fiskales Ad-Hok - Traga!"></a> <a href="https://www.last.fm/music/ATARASHII+GAKKO!/Ichijikikoku"><img src="https://lastfm.freetls.fastly.net/i/u/64s/8a6869bce406a164d97f34c648bed5b6.jpg" title="ATARASHII GAKKO! - Ichijikikoku"></a> <a href="https://www.last.fm/music/IC3PEAK/%D0%A1%D0%BA%D0%B0%D0%B7%D0%BA%D0%B0"><img src="https://lastfm.freetls.fastly.net/i/u/64s/c402a0fdf4fd871e926154ae81d20fac.jpg" title="IC3PEAK - Сказка"></a> <a href="https://www.last.fm/music/Death+Grips/Exmilitary"><img src="https://lastfm.freetls.fastly.net/i/u/64s/831e96df3afd4777c7ac562537bdb356.png" title="Death Grips - Exmilitary"></a> <a href="https://www.last.fm/music/King+Krule/Space+Heavy"><img src="https://lastfm.freetls.fastly.net/i/u/64s/f01256f02989c3ff607a9f42543fa7bf.png" title="King Krule - Space Heavy"></a> </p>

          
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
