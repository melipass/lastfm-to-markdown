# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/100+gecs/100+gecs+&+the+chamber+of+secrets"><img src="https://lastfm.freetls.fastly.net/i/u/64s/97660c50f2c711a9bbb9f30d13358f73.jpg" title="100 gecs - 100 gecs & the chamber of secrets"></a> <a href="https://www.last.fm/music/Big+Thief/Dragon+New+Warm+Mountain+I+Believe+in+You"><img src="https://lastfm.freetls.fastly.net/i/u/64s/2564874af4af9498e7227367968adad3.jpg" title="Big Thief - Dragon New Warm Mountain I Believe in You"></a> <a href="https://www.last.fm/music/Mitski/Be+the+Cowboy"><img src="https://lastfm.freetls.fastly.net/i/u/64s/a9b9c68a6ecb979e1ac95e28bb28e06b.png" title="Mitski - Be the Cowboy"></a> <a href="https://www.last.fm/music/Alvvays/Blue+Rev"><img src="https://lastfm.freetls.fastly.net/i/u/64s/e41b308ca8a94f72e26a79320a3bf313.jpg" title="Alvvays - Blue Rev"></a> <a href="https://www.last.fm/music/Death+Grips/Exmilitary"><img src="https://lastfm.freetls.fastly.net/i/u/64s/831e96df3afd4777c7ac562537bdb356.png" title="Death Grips - Exmilitary"></a> <a href="https://www.last.fm/music/Lizzo/Lizzobangers"><img src="https://lastfm.freetls.fastly.net/i/u/64s/fe9aadadb1434dcb8441820b1a3c6b28.jpg" title="Lizzo - Lizzobangers"></a> <a href="https://www.last.fm/music/The+2+Bears/Be+Strong"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ff1a1a662f5d4a309d9161197a003fcf.jpg" title="The 2 Bears - Be Strong"></a> <a href="https://www.last.fm/music/Charli+XCX/how+i%27m+feeling+now"><img src="https://lastfm.freetls.fastly.net/i/u/64s/f18b8f5ca083f7f9e86ceed75304e2e5.jpg" title="Charli XCX - how i'm feeling now"></a> <a href="https://www.last.fm/music/Fimber+Bravo/Lunar+Tredd"><img src="https://lastfm.freetls.fastly.net/i/u/64s/993ba2549ffc22b4f25df935c024a851.jpg" title="Fimber Bravo - Lunar Tredd"></a> <a href="https://www.last.fm/music/Black+Country,+New+Road/Ants+From+Up+There"><img src="https://lastfm.freetls.fastly.net/i/u/64s/3332b3cee5de8598dbd080f8e2783f93.jpg" title="Black Country, New Road - Ants From Up There"></a> </p>

          
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
