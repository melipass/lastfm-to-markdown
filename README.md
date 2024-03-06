# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Tegan+and+Sara/Sainthood"><img src="https://lastfm.freetls.fastly.net/i/u/64s/20103f8fcdb5430b8480d6dedfd32eb7.png" title="Tegan and Sara - Sainthood"></a> <a href="https://www.last.fm/music/The+xx/xx"><img src="https://lastfm.freetls.fastly.net/i/u/64s/696d1b64cd9d44bf85aad10df414e959.png" title="The xx - xx"></a> <a href="https://www.last.fm/music/M.I.A./Arular"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7ccd40c10eba466fa5d095600d2945b5.png" title="M.I.A. - Arular"></a> <a href="https://www.last.fm/music/The+Smashing+Pumpkins/Siamese+Dream"><img src="https://lastfm.freetls.fastly.net/i/u/64s/53131f63cde3d29e26930209b91fce57.jpg" title="The Smashing Pumpkins - Siamese Dream"></a> <a href="https://www.last.fm/music/Buena+Vista+Social+Club/Buena+Vista+Social+Club"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7cca22966906be978ef06b1db481bd87.jpg" title="Buena Vista Social Club - Buena Vista Social Club"></a> <a href="https://www.last.fm/music/Rodrigo+y+Gabriela/Rodrigo+y+Gabriela"><img src="https://lastfm.freetls.fastly.net/i/u/64s/4e1db651ac484f00b870ff081ef46290.jpg" title="Rodrigo y Gabriela - Rodrigo y Gabriela"></a> <a href="https://www.last.fm/music/S%C3%A9rgio+Mendes/Brasileiro"><img src="https://lastfm.freetls.fastly.net/i/u/64s/e23927b581c16f6e6b4f9ea35eb815f1.jpg" title="Sérgio Mendes - Brasileiro"></a> <a href="https://www.last.fm/music/Taller+Dejao/El+Brillo+Que+Tiene+Es+lo+Humano+Que+le+Queda"><img src="https://lastfm.freetls.fastly.net/i/u/64s/357a1e7360b32059247aef9be196d435.jpg" title="Taller Dejao - El Brillo Que Tiene Es lo Humano Que le Queda"></a> <a href="https://www.last.fm/music/Tyler,+the+Creator/Flower+Boy"><img src="https://lastfm.freetls.fastly.net/i/u/64s/8598727f88a5b52d53b843a9c4b6f2dd.jpg" title="Tyler, the Creator - Flower Boy"></a> </p>

          
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
