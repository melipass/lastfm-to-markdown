# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/CHAI/WINK"><img src="https://lastfm.freetls.fastly.net/i/u/64s/816daec225081d809056930eaff2beac.png" title="CHAI - WINK"></a> <a href="https://www.last.fm/music/Home/Before+The+Night"><img src="https://lastfm.freetls.fastly.net/i/u/64s/9ddbf80049214a75ca3aaf15e4abe872.jpg" title="Home - Before The Night"></a> <a href="https://www.last.fm/music/Holy+Ghost!/Holy+Ghost!"><img src="https://lastfm.freetls.fastly.net/i/u/64s/e6d6fe7b5ae341fc8446894b4422d9d3.png" title="Holy Ghost! - Holy Ghost!"></a> <a href="https://www.last.fm/music/Home/Odyssey"><img src="https://lastfm.freetls.fastly.net/i/u/64s/41e1ed74a64f41c7c14a94439b422a04.jpg" title="Home - Odyssey"></a> <a href="https://www.last.fm/music/My+Chemical+Romance/The+Foundations+of+Decay+-+Single"><img src="https://lastfm.freetls.fastly.net/i/u/64s/269349eef88cb86a2c55407b3e77e710.jpg" title="My Chemical Romance - The Foundations of Decay - Single"></a> </p>

          
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
