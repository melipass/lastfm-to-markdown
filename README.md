# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/100+gecs/1000+gecs+and+The+Tree+of+Clues"><img src="https://lastfm.freetls.fastly.net/i/u/64s/f503389fd56d946a27c94358985188b7.jpg" title="100 gecs - 1000 gecs and The Tree of Clues"></a> <a href="https://www.last.fm/music/Kendrick+Lamar/Mr.+Morale+&+the+Big+Steppers"><img src="https://lastfm.freetls.fastly.net/i/u/64s/98050f67524ffee7af6edd314b767ac4.png" title="Kendrick Lamar - Mr. Morale & the Big Steppers"></a> <a href="https://www.last.fm/music/Jack+White/Blunderbuss"><img src="https://lastfm.freetls.fastly.net/i/u/64s/9dbff5e7be08d5d1e364c0e501be866b.jpg" title="Jack White - Blunderbuss"></a> <a href="https://www.last.fm/music/My+Chemical+Romance/The+Black+Parade"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7675defb2787ce67cd030081eb8ff77c.png" title="My Chemical Romance - The Black Parade"></a> <a href="https://www.last.fm/music/Pixies/Trompe+le+Monde"><img src="https://lastfm.freetls.fastly.net/i/u/64s/5c8a109c4216e6f08d02ea03260ffc24.jpg" title="Pixies - Trompe le Monde"></a> <a href="https://www.last.fm/music/Pixies/Bossanova"><img src="https://lastfm.freetls.fastly.net/i/u/64s/6d729a661ee0278e2777546113f9b61d.jpg" title="Pixies - Bossanova"></a> <a href="https://www.last.fm/music/Pixies/Doolittle"><img src="https://lastfm.freetls.fastly.net/i/u/64s/baafa02626d54475c412e80c6b121193.jpg" title="Pixies - Doolittle"></a> <a href="https://www.last.fm/music/Dirty+on+Purpose/Hallelujah+Sirens"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7b12e29b30cb453584a6e20499a9ac73.png" title="Dirty on Purpose - Hallelujah Sirens"></a> <a href="https://www.last.fm/music/My+Chemical+Romance/Conventional+Weapons"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7e8357aa314d29903ab7b835f55039b9.png" title="My Chemical Romance - Conventional Weapons"></a> <a href="https://www.last.fm/music/Como+Asesinar+a+Felipes/Luz,+figura+y+sombra"><img src="https://lastfm.freetls.fastly.net/i/u/64s/f8b760d4069bc14607cf838ecd3a0b74.jpg" title="Como Asesinar a Felipes - Luz, figura y sombra"></a> </p>

          
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
