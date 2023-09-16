# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Thundercat/It+Is+What+It+Is"><img src="https://lastfm.freetls.fastly.net/i/u/64s/3827c0e1ab025bddfc1b7533a711a1ed.jpg" title="Thundercat - It Is What It Is"></a> <a href="https://www.last.fm/music/Fever+Ray/Radical+Romantics"><img src="https://lastfm.freetls.fastly.net/i/u/64s/b1961a05a426c464b64532c54794c83b.jpg" title="Fever Ray - Radical Romantics"></a> <a href="https://www.last.fm/music/Novos+Baianos/Acabou+Chorare"><img src="https://lastfm.freetls.fastly.net/i/u/64s/04e10daff3151613e3245811c166b425.jpg" title="Novos Baianos - Acabou Chorare"></a> <a href="https://www.last.fm/music/Lacrimosa/Inferno"><img src="https://lastfm.freetls.fastly.net/i/u/64s/a4facbd97f716e4512ab06b2290f74c4.png" title="Lacrimosa - Inferno"></a> <a href="https://www.last.fm/music/Lacrimosa/Angst"><img src="https://lastfm.freetls.fastly.net/i/u/64s/365aec999a5e4c18a499af5d631e02ae.jpg" title="Lacrimosa - Angst"></a> <a href="https://www.last.fm/music/Lacrimosa/Einsamkeit"><img src="https://lastfm.freetls.fastly.net/i/u/64s/45094854fb3849729d29769f3ea97886.jpg" title="Lacrimosa - Einsamkeit"></a> <a href="https://www.last.fm/music/Lacrimosa/Stille"><img src="https://lastfm.freetls.fastly.net/i/u/64s/acb90877c2b24f0eb723063115f951c0.jpg" title="Lacrimosa - Stille"></a> <a href="https://www.last.fm/music/S%C3%A9rgio+Mendes+&+Brasil+%2766/Equinox"><img src="https://lastfm.freetls.fastly.net/i/u/64s/b87132d8a38b3eae36ec14ebfda30417.jpg" title="Sérgio Mendes & Brasil '66 - Equinox"></a> <a href="https://www.last.fm/music/The+Knife/Deep+Cuts"><img src="https://lastfm.freetls.fastly.net/i/u/64s/6c435df6ae44422c968542ef9d267944.png" title="The Knife - Deep Cuts"></a> <a href="https://www.last.fm/music/The+Knife/Shaking+the+Habitual"><img src="https://lastfm.freetls.fastly.net/i/u/64s/17e442acb6944d90bb4a169b8557f57e.png" title="The Knife - Shaking the Habitual"></a> </p>

          
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
