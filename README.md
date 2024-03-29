# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Fiskales+Ad-Hok/Traga!"><img src="https://lastfm.freetls.fastly.net/i/u/64s/95ab7f6a4ff640b6c08d1fd090f04db3.png" title="Fiskales Ad-Hok - Traga!"></a> <a href="https://www.last.fm/music/Neutral+Milk+Hotel/In+the+Aeroplane+Over+the+Sea"><img src="https://lastfm.freetls.fastly.net/i/u/64s/d95051e07a714889c8f7fbbccf61bf8b.jpg" title="Neutral Milk Hotel - In the Aeroplane Over the Sea"></a> <a href="https://www.last.fm/music/Kendrick+Lamar/good+kid,+m.A.A.d+city"><img src="https://lastfm.freetls.fastly.net/i/u/64s/48628c6af67db437b0b9ff156b2c1085.jpg" title="Kendrick Lamar - good kid, m.A.A.d city"></a> <a href="https://www.last.fm/music/Juana+Molina/Wed+21"><img src="https://lastfm.freetls.fastly.net/i/u/64s/0b07079aa807473f9a9f4dde61e98e9b.png" title="Juana Molina - Wed 21"></a> <a href="https://www.last.fm/music/System+of+a+Down/Toxicity"><img src="https://lastfm.freetls.fastly.net/i/u/64s/faa79372c53139010902e67938ccf78e.jpg" title="System of a Down - Toxicity"></a> <a href="https://www.last.fm/music/System+of+a+Down/Mezmerize"><img src="https://lastfm.freetls.fastly.net/i/u/64s/6af731c307585bb1e496f80f7dbad566.jpg" title="System of a Down - Mezmerize"></a> <a href="https://www.last.fm/music/Asamblea+Internacional+del+Fuego/Dial%C3%A9ctica+Negativa"><img src="https://lastfm.freetls.fastly.net/i/u/64s/d6f0fc84b072f074615e37f63cc86510.jpg" title="Asamblea Internacional del Fuego - Dialéctica Negativa"></a> <a href="https://www.last.fm/music/De+Kiruza/De+Kiruza"><img src="https://lastfm.freetls.fastly.net/i/u/64s/8086ea28889117b4ea263cdfb43b2d97.jpg" title="De Kiruza - De Kiruza"></a> <a href="https://www.last.fm/music/JAY-Z/The+Black+Album"><img src="https://lastfm.freetls.fastly.net/i/u/64s/03ae3101a390cc3596c25337520f0473.jpg" title="JAY-Z - The Black Album"></a> <a href="https://www.last.fm/music/Los+Ex/Ca%C3%ADda+Libre"><img src="https://lastfm.freetls.fastly.net/i/u/64s/0d5d4a2657834196a87d7e2e90adb8b9.jpg" title="Los Ex - Caída Libre"></a> </p>

          
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
