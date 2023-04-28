# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Apocalyptica/Inquisition+Symphony"><img src="https://lastfm.freetls.fastly.net/i/u/64s/66e7744db7d98d7e218f0269f7f90b94.jpg" title="Apocalyptica - Inquisition Symphony"></a> <a href="https://www.last.fm/music/Testament/The+Gathering"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ad478efd592aa22adb621dce6f5bfee6.png" title="Testament - The Gathering"></a> <a href="https://www.last.fm/music/Accept/Balls+to+the+Wall"><img src="https://lastfm.freetls.fastly.net/i/u/64s/9e732529e2f063d6c934bfb0d24d9c5e.png" title="Accept - Balls to the Wall"></a> <a href="https://www.last.fm/music/Accept/Restless+and+Wild"><img src="https://lastfm.freetls.fastly.net/i/u/64s/0915bf8e6c90df8c2c9110b16b493271.jpg" title="Accept - Restless and Wild"></a> <a href="https://www.last.fm/music/Apocalyptica/7th+Symphony"><img src="https://lastfm.freetls.fastly.net/i/u/64s/f6163add16ca4e89a3149ab82f391949.png" title="Apocalyptica - 7th Symphony"></a> <a href="https://www.last.fm/music/Lady+Gaga/Born+This+Way"><img src="https://lastfm.freetls.fastly.net/i/u/64s/44900f2f1a4f5a9500a329ba8e075b32.jpg" title="Lady Gaga - Born This Way"></a> <a href="https://www.last.fm/music/Stratovarius/Visions"><img src="https://lastfm.freetls.fastly.net/i/u/64s/4640011f936a0a429d7d9b430ff0893c.jpg" title="Stratovarius - Visions"></a> <a href="https://www.last.fm/music/Accept/Metal+Heart"><img src="https://lastfm.freetls.fastly.net/i/u/64s/9a7a239c9e8e422098fb702886fbc91c.png" title="Accept - Metal Heart"></a> <a href="https://www.last.fm/music/Stratovarius/Episode"><img src="https://lastfm.freetls.fastly.net/i/u/64s/71f89b29b378b4daf1545eda33d6ead5.jpg" title="Stratovarius - Episode"></a> <a href="https://www.last.fm/music/Apocalyptica/Shadowmaker"><img src="https://lastfm.freetls.fastly.net/i/u/64s/0115b79ff5844230c24db5a7ab46757f.jpg" title="Apocalyptica - Shadowmaker"></a> </p>

          
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
