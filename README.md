# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Home/Resting+State"><img src="https://lastfm.freetls.fastly.net/i/u/64s/1f859ae42178aac890aaef4b1bb5e627.jpg" title="Home - Resting State"></a> <a href="https://www.last.fm/music/Hooverphonic/No+More+Sweet+Music"><img src="https://lastfm.freetls.fastly.net/i/u/64s/c84fd8c4cbc6427094d66e31bd05b432.png" title="Hooverphonic - No More Sweet Music"></a> <a href="https://www.last.fm/music/Hooverphonic/Hooverphonic+presents+Jackie+Cane"><img src="https://lastfm.freetls.fastly.net/i/u/64s/4a7197e5571445d1bf847517866aa408.png" title="Hooverphonic - Hooverphonic presents Jackie Cane"></a> <a href="https://www.last.fm/music/Hooverphonic/Blue+Wonder+Power+Milk"><img src="https://lastfm.freetls.fastly.net/i/u/64s/cb08fb9f9a1c4e8a837b1f80b91e4406.png" title="Hooverphonic - Blue Wonder Power Milk"></a> <a href="https://www.last.fm/music/Hooverphonic/A+New+Stereophonic+Sound+Spectacular"><img src="https://lastfm.freetls.fastly.net/i/u/64s/a8e6db9877f9438eab4e833e234cf789.png" title="Hooverphonic - A New Stereophonic Sound Spectacular"></a> <a href="https://www.last.fm/music/Hooverphonic/The+Magnificent+Tree"><img src="https://lastfm.freetls.fastly.net/i/u/64s/b8b9676efa1d4c73b4b48b07026a4683.png" title="Hooverphonic - The Magnificent Tree"></a> <a href="https://www.last.fm/music/Hooverphonic/The+President+Of+The+LSD+Golf+Club"><img src="https://lastfm.freetls.fastly.net/i/u/64s/fb482ea733e42b87ea35c23b56853464.png" title="Hooverphonic - The President Of The LSD Golf Club"></a> <a href="https://www.last.fm/music/Home/Falling+Into+Place"><img src="https://lastfm.freetls.fastly.net/i/u/64s/27cbde7d1381c5d6caae5c601d50d215.jpg" title="Home - Falling Into Place"></a> </p>

          
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
