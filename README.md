# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Bring+Me+the+Horizon/Suicide+Season"><img src="https://lastfm.freetls.fastly.net/i/u/64s/594142ef2a94491fe45bc96598bf8005.jpg" title="Bring Me the Horizon - Suicide Season"></a> <a href="https://www.last.fm/music/Bring+Me+the+Horizon/Live+at+Wembley"><img src="https://lastfm.freetls.fastly.net/i/u/64s/fa5098c2fafbd11858eddc52d25dd5b1.jpg" title="Bring Me the Horizon - Live at Wembley"></a> <a href="https://www.last.fm/music/Bring+Me+the+Horizon/Sempiternal"><img src="https://lastfm.freetls.fastly.net/i/u/64s/b665c029fbe8489f8e6a45dde56215d4.png" title="Bring Me the Horizon - Sempiternal"></a> <a href="https://www.last.fm/music/Bring+Me+the+Horizon/There+Is+a+Hell,+Believe+Me+I%27ve+Seen+It.+There+Is+a+Heaven,+Let%27s+Keep+It+a+Secret"><img src="https://lastfm.freetls.fastly.net/i/u/64s/278d843ca23c37a3f64dbbfea052e6b4.jpg" title="Bring Me the Horizon - There Is a Hell, Believe Me I've Seen It. There Is a Heaven, Let's Keep It a Secret"></a> <a href="https://www.last.fm/music/Deafheaven/Sunbather"><img src="https://lastfm.freetls.fastly.net/i/u/64s/8a6a1123bb124e4890f20c956a63e734.png" title="Deafheaven - Sunbather"></a> <a href="https://www.last.fm/music/The+Mamas+&+the+Papas/If+You+Can+Believe+Your+Eyes+And+Ears"><img src="https://lastfm.freetls.fastly.net/i/u/64s/4ddf4b3f9d1f4db883ac7644c2b7db05.png" title="The Mamas & the Papas - If You Can Believe Your Eyes And Ears"></a> </p>

          
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
