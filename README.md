# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Turnstile/GLOW+ON"><img src="https://lastfm.freetls.fastly.net/i/u/64s/9bbf56b7df22d8044b0102c3ef12183a.jpg" title="Turnstile - GLOW ON"></a> <a href="https://www.last.fm/music/IC3PEAK/%D0%94%D0%BE+%D1%81%D0%B2%D0%B8%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ab72603510789b5288f0260dcbaaf1da.jpg" title="IC3PEAK - До свидания"></a> <a href="https://www.last.fm/music/Turnstile/Time+&+Space"><img src="https://lastfm.freetls.fastly.net/i/u/64s/db9e3924dee420e998fd88d837929124.jpg" title="Turnstile - Time & Space"></a> <a href="https://www.last.fm/music/Turnstile/Nonstop+Feeling"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7eb4264103714209c2f0ea5d39a68a55.jpg" title="Turnstile - Nonstop Feeling"></a> <a href="https://www.last.fm/music/Lebanon+Hanover/The+World+Is+Getting+Colder"><img src="https://lastfm.freetls.fastly.net/i/u/64s/dce5be26a45443c0c3a71fc0ba55e9af.png" title="Lebanon Hanover - The World Is Getting Colder"></a> <a href="https://www.last.fm/music/Lebanon+Hanover/Why+Not+Just+Be+Solo"><img src="https://lastfm.freetls.fastly.net/i/u/64s/71b77eb86f8e4d38cdd6b8f38ee2d115.jpg" title="Lebanon Hanover - Why Not Just Be Solo"></a> <a href="https://www.last.fm/music/IC3PEAK/Kiss+Of+Death"><img src="https://lastfm.freetls.fastly.net/i/u/64s/2106d421f164bb5f94d28bdacf97c394.jpg" title="IC3PEAK - Kiss Of Death"></a> <a href="https://www.last.fm/music/Lebanon+Hanover/Tomb+for+Two"><img src="https://lastfm.freetls.fastly.net/i/u/64s/8d9a1319348a4917c9714e0d311ffec9.png" title="Lebanon Hanover - Tomb for Two"></a> </p>

          
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
