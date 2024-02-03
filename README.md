# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Panico/Pornostar"><img src="https://lastfm.freetls.fastly.net/i/u/64s/d8df451046624f85cf69e9d7e16b509b.jpg" title="Panico - Pornostar"></a> <a href="https://www.last.fm/music/Kendrick+Lamar/DAMN."><img src="https://lastfm.freetls.fastly.net/i/u/64s/8a59ed3a9c71cb5113325e2026889e4a.png" title="Kendrick Lamar - DAMN."></a> <a href="https://www.last.fm/music/Fiskales+Ad-Hok/Traga!"><img src="https://lastfm.freetls.fastly.net/i/u/64s/95ab7f6a4ff640b6c08d1fd090f04db3.png" title="Fiskales Ad-Hok - Traga!"></a> <a href="https://www.last.fm/music/Kendrick+Lamar/To+Pimp+a+Butterfly"><img src="https://lastfm.freetls.fastly.net/i/u/64s/86b35c4eb3c479da49c915d8771bbd1a.png" title="Kendrick Lamar - To Pimp a Butterfly"></a> <a href="https://www.last.fm/music/Death+Grips/Exmilitary"><img src="https://lastfm.freetls.fastly.net/i/u/64s/831e96df3afd4777c7ac562537bdb356.png" title="Death Grips - Exmilitary"></a> <a href="https://www.last.fm/music/OSNO1/REMIXES+2017"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ab38124f0b04a83776479302ad2e5318.jpg" title="OSNO1 - REMIXES 2017"></a> <a href="https://www.last.fm/music/Prissa/Ni+tu+ni+yo"><img src="https://lastfm.freetls.fastly.net/i/u/64s/99397ca9898b4d9e831e8541f014809a.jpg" title="Prissa - Ni tu ni yo"></a> <a href="https://www.last.fm/music/Linkin+Park/Hybrid+Theory"><img src="https://lastfm.freetls.fastly.net/i/u/64s/c21b3923a4d3ff5629996f3f8e178140.jpg" title="Linkin Park - Hybrid Theory"></a> <a href="https://www.last.fm/music/M.I.A./MAYA"><img src="https://lastfm.freetls.fastly.net/i/u/64s/60137c1c3f0aa60d9e3ab9c195bee2fe.jpg" title="M.I.A. - MAYA"></a> <a href="https://www.last.fm/music/Kanye+West/My+Beautiful+Dark+Twisted+Fantasy"><img src="https://lastfm.freetls.fastly.net/i/u/64s/f5afd8fe052b452c999b657664cae99f.png" title="Kanye West - My Beautiful Dark Twisted Fantasy"></a> </p>

          
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
