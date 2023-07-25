# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Natalia+Lafourcade/De+todas+las+flores"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7b66bf560b39c07412c98072958d11d7.jpg" title="Natalia Lafourcade - De todas las flores"></a> <a href="https://www.last.fm/music/Burial/Burial"><img src="https://lastfm.freetls.fastly.net/i/u/64s/aa5aa24f20784946889f7f8ce21ad0a7.png" title="Burial - Burial"></a> <a href="https://www.last.fm/music/Natalia+Lafourcade/Musas:+Un+Homenaje+al+Folclore+Latinoamericano+en+Manos+de+Los+Macorinos,+Vol.+2"><img src="https://lastfm.freetls.fastly.net/i/u/64s/63a1d40dc5708c77260ade567b8d5694.jpg" title="Natalia Lafourcade - Musas: Un Homenaje al Folclore Latinoamericano en Manos de Los Macorinos, Vol. 2"></a> <a href="https://www.last.fm/music/Natalia+Lafourcade/Musas:+Un+homenaje+al+folclore+latinoamericano+en+manos+de+Los+Macorinos,+vol.+1"><img src="https://lastfm.freetls.fastly.net/i/u/64s/625969c8c2ee924502324e78d9156dff.jpg" title="Natalia Lafourcade - Musas: Un homenaje al folclore latinoamericano en manos de Los Macorinos, vol. 1"></a> <a href="https://www.last.fm/music/Kendrick+Lamar/Mr.+Morale+&+the+Big+Steppers"><img src="https://lastfm.freetls.fastly.net/i/u/64s/98050f67524ffee7af6edd314b767ac4.png" title="Kendrick Lamar - Mr. Morale & the Big Steppers"></a> <a href="https://www.last.fm/music/Burial/Untrue"><img src="https://lastfm.freetls.fastly.net/i/u/64s/2c7332bc861d406a80c13f0e69d4ba7f.png" title="Burial - Untrue"></a> <a href="https://www.last.fm/music/Taller+Dejao/El+Brillo+Que+Tiene+Es+lo+Humano+Que+le+Queda"><img src="https://lastfm.freetls.fastly.net/i/u/64s/357a1e7360b32059247aef9be196d435.jpg" title="Taller Dejao - El Brillo Que Tiene Es lo Humano Que le Queda"></a> <a href="https://www.last.fm/music/Inti-Illimani/Imaginacion"><img src="https://lastfm.freetls.fastly.net/i/u/64s/511524241b42421f9be12d52dd1d2028.jpg" title="Inti-Illimani - Imaginacion"></a> <a href="https://www.last.fm/music/Gepe/Folclor+Imaginario+(Canciones+Recopiladas+por+Margot+Loyola+Palacios+y+Algunas+Otras+Que+Parten+Desde+Ah%C3%AD)"><img src="https://lastfm.freetls.fastly.net/i/u/64s/a10777260546cf45aca7f5a2291d74ad.jpg" title="Gepe - Folclor Imaginario (Canciones Recopiladas por Margot Loyola Palacios y Algunas Otras Que Parten Desde Ahí)"></a> <a href="https://www.last.fm/music/System+of+a+Down/Hypnotize"><img src="https://lastfm.freetls.fastly.net/i/u/64s/a96a0ff1cd9b384659b7edac19dc15b6.jpg" title="System of a Down - Hypnotize"></a> </p>

          
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
