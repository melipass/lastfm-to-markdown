# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Kendrick+Lamar/good+kid,+m.A.A.d+city"><img src="https://lastfm.freetls.fastly.net/i/u/64s/48628c6af67db437b0b9ff156b2c1085.jpg" title="Kendrick Lamar - good kid, m.A.A.d city"></a> <a href="https://www.last.fm/music/Kendrick+Lamar/DAMN."><img src="https://lastfm.freetls.fastly.net/i/u/64s/8a59ed3a9c71cb5113325e2026889e4a.png" title="Kendrick Lamar - DAMN."></a> <a href="https://www.last.fm/music/Kendrick+Lamar/To+Pimp+a+Butterfly"><img src="https://lastfm.freetls.fastly.net/i/u/64s/86b35c4eb3c479da49c915d8771bbd1a.png" title="Kendrick Lamar - To Pimp a Butterfly"></a> <a href="https://www.last.fm/music/Death+Grips/Exmilitary"><img src="https://lastfm.freetls.fastly.net/i/u/64s/831e96df3afd4777c7ac562537bdb356.png" title="Death Grips - Exmilitary"></a> <a href="https://www.last.fm/music/OSNO1/REMIXES+2017"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ab38124f0b04a83776479302ad2e5318.jpg" title="OSNO1 - REMIXES 2017"></a> <a href="https://www.last.fm/music/Kanye+West/My+Beautiful+Dark+Twisted+Fantasy"><img src="https://lastfm.freetls.fastly.net/i/u/64s/cbb01b75c20f48dfb7d86f46367dbbdb.png" title="Kanye West - My Beautiful Dark Twisted Fantasy"></a> <a href="https://www.last.fm/music/Makiza/Aerolineas+Makiza"><img src="https://lastfm.freetls.fastly.net/i/u/64s/1a34f6bb47144c409f7862eafe6f5654.jpg" title="Makiza - Aerolineas Makiza"></a> <a href="https://www.last.fm/music/Omar+Souleyman/Wenu+Wenu"><img src="https://lastfm.freetls.fastly.net/i/u/64s/d56aeb3cd96d402ea4552dfebcd61a0c.png" title="Omar Souleyman - Wenu Wenu"></a> <a href="https://www.last.fm/music/Pet+Shop+Boys/Please"><img src="https://lastfm.freetls.fastly.net/i/u/64s/443d58d1211fae46acdde809931ca5d5.jpg" title="Pet Shop Boys - Please"></a> <a href="https://www.last.fm/music/King+Gizzard+&+The+Lizard+Wizard/Nonagon+Infinity"><img src="https://lastfm.freetls.fastly.net/i/u/64s/45d2570199853ec87e5da6dd8c1ea1a3.jpg" title="King Gizzard & The Lizard Wizard - Nonagon Infinity"></a> </p>

          
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
