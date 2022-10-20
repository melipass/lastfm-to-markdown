# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Pixies/Surfer+Rosa"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7a0af4bf09044557ac7bbb916eee1fc0.png" title="Pixies - Surfer Rosa"></a> <a href="https://www.last.fm/music/Isobel+Campbell+&+Mark+Lanegan/Ballad+of+the+Broken+Seas"><img src="https://lastfm.freetls.fastly.net/i/u/64s/bb1d9a39586d4b1985052e4b57b947fe.png" title="Isobel Campbell & Mark Lanegan - Ballad of the Broken Seas"></a> <a href="https://www.last.fm/music/Pixies/Doolittle"><img src="https://lastfm.freetls.fastly.net/i/u/64s/baafa02626d54475c412e80c6b121193.jpg" title="Pixies - Doolittle"></a> <a href="https://www.last.fm/music/Iron+Maiden/En+Vivo!"><img src="https://lastfm.freetls.fastly.net/i/u/64s/b799592a1d1642c29596b518b8aaae40.jpg" title="Iron Maiden - En Vivo!"></a> <a href="https://www.last.fm/music/Iron+Maiden/The+Number+of+the+Beast"><img src="https://lastfm.freetls.fastly.net/i/u/64s/4848a0ce2f98376b71c932e409e9afb4.jpg" title="Iron Maiden - The Number of the Beast"></a> <a href="https://www.last.fm/music/Cat+Power/Myra+Lee"><img src="https://lastfm.freetls.fastly.net/i/u/64s/f04295b594d54f9c982e3e84878c7067.png" title="Cat Power - Myra Lee"></a> <a href="https://www.last.fm/music/Isabel+y+%C3%81ngel+Parra/De+Violeta+Parra"><img src="https://lastfm.freetls.fastly.net/i/u/64s/874f0129762546f5c6a0a429f275bcd5.jpg" title="Isabel y Ángel Parra - De Violeta Parra"></a> </p>

          
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
