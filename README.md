# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Hooverphonic/No+More+Sweet+Music"><img src="https://lastfm.freetls.fastly.net/i/u/64s/c84fd8c4cbc6427094d66e31bd05b432.png" title="Hooverphonic - No More Sweet Music"></a> <a href="https://www.last.fm/music/Hope+Sandoval+&+The+Warm+Inventions/Bavarian+Fruit+Bread"><img src="https://lastfm.freetls.fastly.net/i/u/64s/c8e7f393513a66ec90630fd88163fb8d.jpg" title="Hope Sandoval & The Warm Inventions - Bavarian Fruit Bread"></a> <a href="https://www.last.fm/music/Hope+Sandoval+&+The+Warm+Inventions/Through+The+Devil+Softly"><img src="https://lastfm.freetls.fastly.net/i/u/64s/be125796a3c548ceb581d8db2b9dd95b.png" title="Hope Sandoval & The Warm Inventions - Through The Devil Softly"></a> <a href="https://www.last.fm/music/Hope+Sandoval+&+The+Warm+Inventions/Until+the+Hunter"><img src="https://lastfm.freetls.fastly.net/i/u/64s/0bb18b2250fa527a3a7dfb78dbf97e91.jpg" title="Hope Sandoval & The Warm Inventions - Until the Hunter"></a> <a href="https://www.last.fm/music/The+Horrors/Primary+Colours"><img src="https://lastfm.freetls.fastly.net/i/u/64s/f492573478814e8c82d1302bfcda3138.png" title="The Horrors - Primary Colours"></a> <a href="https://www.last.fm/music/Hooverphonic/Hidden+Stories"><img src="https://lastfm.freetls.fastly.net/i/u/64s/f7e279d0f0d2b2454e7e217b3abc2d3c.jpg" title="Hooverphonic - Hidden Stories"></a> <a href="https://www.last.fm/music/Hooverphonic/The+President+Of+The+LSD+Golf+Club"><img src="https://lastfm.freetls.fastly.net/i/u/64s/fb482ea733e42b87ea35c23b56853464.png" title="Hooverphonic - The President Of The LSD Golf Club"></a> <a href="https://www.last.fm/music/Iron+Maiden/The+Number+of+the+Beast"><img src="https://lastfm.freetls.fastly.net/i/u/64s/0b05ebbc6af93b2c88a5c9fa476974ca.jpg" title="Iron Maiden - The Number of the Beast"></a> <a href="https://www.last.fm/music/The+Horrors/Strange+House"><img src="https://lastfm.freetls.fastly.net/i/u/64s/79d7f5d9e656452badd53b46ca48e1ad.png" title="The Horrors - Strange House"></a> <a href="https://www.last.fm/music/Metallica/Master+of+Puppets"><img src="https://lastfm.freetls.fastly.net/i/u/64s/07f492a00c904cc6ccf868010be4d5a6.png" title="Metallica - Master of Puppets"></a> </p>

          
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
