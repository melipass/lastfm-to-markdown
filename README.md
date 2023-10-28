# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/TOKiMONSTA/Midnight+Menu"><img src="https://lastfm.freetls.fastly.net/i/u/64s/6258d1feead248b48fea8c9f58feed3e.png" title="TOKiMONSTA - Midnight Menu"></a> <a href="https://www.last.fm/music/TOKiMONSTA/Creature+Dreams"><img src="https://lastfm.freetls.fastly.net/i/u/64s/d4a2e35b5c13445aad5c4251e23a3d15.png" title="TOKiMONSTA - Creature Dreams"></a> <a href="https://www.last.fm/music/TOKiMONSTA/Half+Shadows"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ac0e9928b7c44d69b53714e84a932947.png" title="TOKiMONSTA - Half Shadows"></a> <a href="https://www.last.fm/music/Los+Tres/La+Espada+&+la+Pared"><img src="https://lastfm.freetls.fastly.net/i/u/64s/318a8943455039ebe1ca9ec0da6ade3b.jpg" title="Los Tres - La Espada & la Pared"></a> <a href="https://www.last.fm/music/Los+Tres/Los+Tres"><img src="https://lastfm.freetls.fastly.net/i/u/64s/b36ef0b75542919c650c8bdefbc1a6d6.jpg" title="Los Tres - Los Tres"></a> <a href="https://www.last.fm/music/The+Rasmus/Dead+Letters"><img src="https://lastfm.freetls.fastly.net/i/u/64s/9f0714a59508d27c0ca151b05fa3cdce.jpg" title="The Rasmus - Dead Letters"></a> <a href="https://www.last.fm/music/Beck/Odelay"><img src="https://lastfm.freetls.fastly.net/i/u/64s/8381e54db1d4b669bb6baedc68180503.jpg" title="Beck - Odelay"></a> <a href="https://www.last.fm/music/Red+Hot+Chili+Peppers/Stadium+Arcadium"><img src="https://lastfm.freetls.fastly.net/i/u/64s/fb7d1a6c6e5240c48159d08b17ea022b.png" title="Red Hot Chili Peppers - Stadium Arcadium"></a> <a href="https://www.last.fm/music/Soda+Stereo/Dynamo"><img src="https://lastfm.freetls.fastly.net/i/u/64s/d5fe5d1ba9da5b60600aaf883a84b633.jpg" title="Soda Stereo - Dynamo"></a> <a href="https://www.last.fm/music/The+Rasmus/Hide+from+the+Sun"><img src="https://lastfm.freetls.fastly.net/i/u/64s/2624ca521fc7420c8047c12b3b2eec0b.png" title="The Rasmus - Hide from the Sun"></a> </p>

          
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
