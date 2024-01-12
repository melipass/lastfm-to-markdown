# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/My+Chemical+Romance/Three+Cheers+for+Sweet+Revenge"><img src="https://lastfm.freetls.fastly.net/i/u/64s/09cb27a9f908354fd210a07830951791.png" title="My Chemical Romance - Three Cheers for Sweet Revenge"></a> <a href="https://www.last.fm/music/Green+Day/American+Idiot"><img src="https://lastfm.freetls.fastly.net/i/u/64s/5bcb675866706c229ad9f77188b8ac44.jpg" title="Green Day - American Idiot"></a> <a href="https://www.last.fm/music/Green+Day/21st+Century+Breakdown"><img src="https://lastfm.freetls.fastly.net/i/u/64s/72a314e1e9064a0418159b144fe1ad72.jpg" title="Green Day - 21st Century Breakdown"></a> <a href="https://www.last.fm/music/Green+Day/Bullet+in+a+Bible"><img src="https://lastfm.freetls.fastly.net/i/u/64s/19ac07537e21e1bad10947ea53878f1c.jpg" title="Green Day - Bullet in a Bible"></a> <a href="https://www.last.fm/music/Garbage/Garbage"><img src="https://lastfm.freetls.fastly.net/i/u/64s/e1ee4a6e9e1e40c28ed510e0272b8ceb.png" title="Garbage - Garbage"></a> <a href="https://www.last.fm/music/Garbage/Version+2.0"><img src="https://lastfm.freetls.fastly.net/i/u/64s/8d80ecd72b1e8571edd326ba1c163551.png" title="Garbage - Version 2.0"></a> <a href="https://www.last.fm/music/Bring+Me+the+Horizon/Suicide+Season"><img src="https://lastfm.freetls.fastly.net/i/u/64s/594142ef2a94491fe45bc96598bf8005.jpg" title="Bring Me the Horizon - Suicide Season"></a> <a href="https://www.last.fm/music/Foo+Fighters/The+Colour+and+the+Shape"><img src="https://lastfm.freetls.fastly.net/i/u/64s/c2ecd547171fc923b5b32718a8e8780a.jpg" title="Foo Fighters - The Colour and the Shape"></a> <a href="https://www.last.fm/music/Green+Day/Dookie"><img src="https://lastfm.freetls.fastly.net/i/u/64s/2248e72411992639ffa8ab94ba97a631.jpg" title="Green Day - Dookie"></a> <a href="https://www.last.fm/music/Paramore/RIOT!"><img src="https://lastfm.freetls.fastly.net/i/u/64s/b7a4b3000d0c431fbce299986ac51c48.png" title="Paramore - RIOT!"></a> </p>

          
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
