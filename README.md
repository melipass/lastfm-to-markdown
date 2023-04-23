# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Testament/The+Gathering"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ad478efd592aa22adb621dce6f5bfee6.png" title="Testament - The Gathering"></a> <a href="https://www.last.fm/music/Stratovarius/Visions"><img src="https://lastfm.freetls.fastly.net/i/u/64s/4640011f936a0a429d7d9b430ff0893c.jpg" title="Stratovarius - Visions"></a> <a href="https://www.last.fm/music/Testament/The+New+Order"><img src="https://lastfm.freetls.fastly.net/i/u/64s/f15467dee28005fe2169317d6c5973be.jpg" title="Testament - The New Order"></a> <a href="https://www.last.fm/music/Apocalyptica/Cell-0"><img src="https://lastfm.freetls.fastly.net/i/u/64s/34ec98069632859e49a2f9d8492f6d79.jpg" title="Apocalyptica - Cell-0"></a> <a href="https://www.last.fm/music/Stratovarius/Episode"><img src="https://lastfm.freetls.fastly.net/i/u/64s/71f89b29b378b4daf1545eda33d6ead5.jpg" title="Stratovarius - Episode"></a> <a href="https://www.last.fm/music/Tyler,+the+Creator/Flower+Boy"><img src="https://lastfm.freetls.fastly.net/i/u/64s/52a7f32bdc99238080b0f17e859b3b4d.jpg" title="Tyler, the Creator - Flower Boy"></a> <a href="https://www.last.fm/music/The+Jimi+Hendrix+Experience/Are+You+Experienced"><img src="https://lastfm.freetls.fastly.net/i/u/64s/50e9c81e046775be2287b9fb53a788e7.jpg" title="The Jimi Hendrix Experience - Are You Experienced"></a> <a href="https://www.last.fm/music/Testament/The+Legacy"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ab2d3de3da75bb0758c06fa69a734fd1.jpg" title="Testament - The Legacy"></a> <a href="https://www.last.fm/music/The+Rasmus/Dead+Letters"><img src="https://lastfm.freetls.fastly.net/i/u/64s/9f0714a59508d27c0ca151b05fa3cdce.jpg" title="The Rasmus - Dead Letters"></a> </p>

          
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
