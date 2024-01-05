# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Ashnikko/DEMIDEVIL"><img src="https://lastfm.freetls.fastly.net/i/u/64s/9196a46c5993ae2bf86ec10487dcdb90.jpg" title="Ashnikko - DEMIDEVIL"></a> <a href="https://www.last.fm/music/Doja+Cat/Amala"><img src="https://lastfm.freetls.fastly.net/i/u/64s/3d8c6b5ea4a34c222a9a8069687c12e9.jpg" title="Doja Cat - Amala"></a> <a href="https://www.last.fm/music/Kim+Petras/TURN+OFF+THE+LIGHT"><img src="https://lastfm.freetls.fastly.net/i/u/64s/3b74a779c7b6e5163689e68f5d2d8df6.jpg" title="Kim Petras - TURN OFF THE LIGHT"></a> <a href="https://www.last.fm/music/Pescado+Rabioso/Artaud"><img src="https://lastfm.freetls.fastly.net/i/u/64s/04036a3638615c001c9438aabb2d3c20.jpg" title="Pescado Rabioso - Artaud"></a> <a href="https://www.last.fm/music/The+2+Bears/Be+Strong"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ff1a1a662f5d4a309d9161197a003fcf.jpg" title="The 2 Bears - Be Strong"></a> <a href="https://www.last.fm/music/Doja+Cat/Hot+Pink"><img src="https://lastfm.freetls.fastly.net/i/u/64s/be2aca67c96a044ec6e2726d7de50d94.jpg" title="Doja Cat - Hot Pink"></a> <a href="https://www.last.fm/music/Groove+Armada/Goodbye+Country+(Hello+Nightclub)"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ee96e6a12a7f454998d3b320aeb2ecc3.png" title="Groove Armada - Goodbye Country (Hello Nightclub)"></a> <a href="https://www.last.fm/music/Alice+Glass/Alice+Glass"><img src="https://lastfm.freetls.fastly.net/i/u/64s/4b47c02fc11f04ec7056e2b6854ec2d2.jpg" title="Alice Glass - Alice Glass"></a> <a href="https://www.last.fm/music/Billie+Eilish/Happier+Than+Ever"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7ebd8b6f8ac6766fb26303245a265a2e.jpg" title="Billie Eilish - Happier Than Ever"></a> <a href="https://www.last.fm/music/Billie+Eilish/WHEN+WE+ALL+FALL+ASLEEP,+WHERE+DO+WE+GO%3F"><img src="https://lastfm.freetls.fastly.net/i/u/64s/c2652de4809e5b4349565518b34b85ca.jpg" title="Billie Eilish - WHEN WE ALL FALL ASLEEP, WHERE DO WE GO?"></a> </p>

          
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
