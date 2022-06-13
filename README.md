# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Doja+Cat/Amala"><img src="https://lastfm.freetls.fastly.net/i/u/64s/25b42a40b3e21733c284c9ea4a1d6b1a.jpg" title="Doja Cat - Amala"></a> <a href="https://www.last.fm/music/Marilyn+Manson/Portrait+of+an+American+Family"><img src="https://lastfm.freetls.fastly.net/i/u/64s/2944b130d99410e072f56e8adacb77a8.png" title="Marilyn Manson - Portrait of an American Family"></a> <a href="https://www.last.fm/music/Doja+Cat/Purrr!"><img src="https://lastfm.freetls.fastly.net/i/u/64s/464aebb8aaba4399c3f0e22efaa9cab7.png" title="Doja Cat - Purrr!"></a> <a href="https://www.last.fm/music/Sonny+Sharrock/Ask+The+Ages"><img src="https://lastfm.freetls.fastly.net/i/u/64s/fdaaaee3cddc47d18d23ca63ef158394.png" title="Sonny Sharrock - Ask The Ages"></a> <a href="https://www.last.fm/music/John+Coltrane/My+Favorite+Things"><img src="https://lastfm.freetls.fastly.net/i/u/64s/70456da468c048d0856f414c86e61374.png" title="John Coltrane - My Favorite Things"></a> <a href="https://www.last.fm/music/Doja+Cat/Hot+Pink"><img src="https://lastfm.freetls.fastly.net/i/u/64s/6a520a662b0d30646781d03ade00625a.jpg" title="Doja Cat - Hot Pink"></a> <a href="https://www.last.fm/music/Hildur+Gu%C3%B0nad%C3%B3ttir/Mount+A"><img src="https://lastfm.freetls.fastly.net/i/u/64s/77aa9e4785558d5c6111063fa06ab98c.jpg" title="Hildur Guðnadóttir - Mount A"></a> </p>

          
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
name: lastfmweekly

on:
  schedule:
    - cron: '2 0 * * *'
  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

jobs:
  # This workflow contains a single job called "build"
  build:
    runs-on: ubuntu-latest
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - name: repo checkout
        uses: actions/checkout@v2

      - name: python setup
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: python packages installation
        run: |
          python -m pip install --upgrade pip
          pip install -r dependencies.txt
      - name: use lastfm api
        env:
          LASTFM_API_KEY: ${{ secrets.LASTFM_API_KEY }}
          LASTFM_USER: ${{ secrets.LASTFM_USER }}
          IMAGE_COUNT: 8 # Optional. Defaults to 10. Feel free to remove this line if you want.
          IMAGE_SIZE: 2 # "0" for small image. "1" for medium image. "2" for large image. "3" for extralarge image.
        run: python lastfm.py

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
