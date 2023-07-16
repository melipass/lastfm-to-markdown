# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Thundercat/Drunk"><img src="https://lastfm.freetls.fastly.net/i/u/64s/17311ac4702bbc6245e9ee2958630c8f.jpg" title="Thundercat - Drunk"></a> <a href="https://www.last.fm/music/Thundercat/The+Golden+Age+of+Apocalypse"><img src="https://lastfm.freetls.fastly.net/i/u/64s/5ba4646467174a5ebd74ad9db752d63d.png" title="Thundercat - The Golden Age of Apocalypse"></a> <a href="https://www.last.fm/music/Thundercat/Apocalypse"><img src="https://lastfm.freetls.fastly.net/i/u/64s/a6b1ec6724b24a3892a0f27311f272e7.png" title="Thundercat - Apocalypse"></a> <a href="https://www.last.fm/music/Kendrick+Lamar/DAMN."><img src="https://lastfm.freetls.fastly.net/i/u/64s/8a59ed3a9c71cb5113325e2026889e4a.png" title="Kendrick Lamar - DAMN."></a> <a href="https://www.last.fm/music/TesseracT/Altered+State"><img src="https://lastfm.freetls.fastly.net/i/u/64s/f9423553d24546d88bb55c1fc93e9d6f.png" title="TesseracT - Altered State"></a> <a href="https://www.last.fm/music/black+midi/Schlagenheim"><img src="https://lastfm.freetls.fastly.net/i/u/64s/9903bae260baaa04c6177ebcac4b74bc.jpg" title="black midi - Schlagenheim"></a> <a href="https://www.last.fm/music/Blur/Blur"><img src="https://lastfm.freetls.fastly.net/i/u/64s/0d6b7482b12c4f7786ce17eb7b3cf589.png" title="Blur - Blur"></a> <a href="https://www.last.fm/music/Green+Day/BBC+Sessions"><img src="https://lastfm.freetls.fastly.net/i/u/64s/71ec3db6f887348e1b98bdfe1fb49018.jpg" title="Green Day - BBC Sessions"></a> <a href="https://www.last.fm/music/black+midi/Cavalcade"><img src="https://lastfm.freetls.fastly.net/i/u/64s/67a4d6e9f3425753c90e0eb0e2d19c7c.jpg" title="black midi - Cavalcade"></a> <a href="https://www.last.fm/music/Thundercat/The+Beyond+%2F+Where+the+Giants+Roam"><img src="https://lastfm.freetls.fastly.net/i/u/64s/00607a78fc745ae8382b6c9225b50b83.png" title="Thundercat - The Beyond / Where the Giants Roam"></a> </p>

          
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
