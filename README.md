# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Daddy+Yankee/Talento+De+Barrio"><img src="https://lastfm.freetls.fastly.net/i/u/64s/5f0b9a7890508ac26e61a27490ae5c84.jpg" title="Daddy Yankee - Talento De Barrio"></a> <a href="https://www.last.fm/music/%E6%96%B0%E3%81%97%E3%81%84%E5%AD%A6%E6%A0%A1%E3%81%AE%E3%83%AA%E3%83%BC%E3%83%80%E3%83%BC%E3%82%BA/%E3%83%9E%E3%82%A8%E3%83%8A%E3%83%A9%E3%83%AF%E3%83%8A%E3%82%A4"><img src="https://lastfm.freetls.fastly.net/i/u/64s/b9c2bc28d8d6d8226039a73008a848f1.jpg" title="新しい学校のリーダーズ - マエナラワナイ"></a> <a href="https://www.last.fm/music/ATARASHII+GAKKO!/%E8%8B%A5%E6%B0%97%E3%82%AC%E3%82%A4%E3%82%BF%E3%83%AB"><img src="https://lastfm.freetls.fastly.net/i/u/64s/82c08a2acd477c97ade4581653b6e4a1.jpg" title="ATARASHII GAKKO! - 若気ガイタル"></a> <a href="https://www.last.fm/music/Beck/Odelay"><img src="https://lastfm.freetls.fastly.net/i/u/64s/8381e54db1d4b669bb6baedc68180503.jpg" title="Beck - Odelay"></a> <a href="https://www.last.fm/music/%E6%96%B0%E3%81%97%E3%81%84%E5%AD%A6%E6%A0%A1%E3%81%AE%E3%83%AA%E3%83%BC%E3%83%80%E3%83%BC%E3%82%BA/%E8%8B%A5%E6%B0%97%E3%82%AC%E3%82%A4%E3%82%BF%E3%83%AB"><img src="https://lastfm.freetls.fastly.net/i/u/64s/b12d7304b51c6012f955b0a25e88e2c3.jpg" title="新しい学校のリーダーズ - 若気ガイタル"></a> <a href="https://www.last.fm/music/BABYMETAL/METAL+RESISTANCE"><img src="https://lastfm.freetls.fastly.net/i/u/64s/42ae0f5a57257113176059500e55ddce.jpg" title="BABYMETAL - METAL RESISTANCE"></a> <a href="https://www.last.fm/music/BABYMETAL/BABYMETAL"><img src="https://lastfm.freetls.fastly.net/i/u/64s/70045af203785b0b4c21c7ea1f63b10c.jpg" title="BABYMETAL - BABYMETAL"></a> <a href="https://www.last.fm/music/Crystal+Castles/Crystal+Castles"><img src="https://lastfm.freetls.fastly.net/i/u/64s/7096b4c2d2d9cc84bd3d919c552ca47d.jpg" title="Crystal Castles - Crystal Castles"></a> <a href="https://www.last.fm/music/Fiskales+Ad-Hok/Traga!"><img src="https://lastfm.freetls.fastly.net/i/u/64s/95ab7f6a4ff640b6c08d1fd090f04db3.png" title="Fiskales Ad-Hok - Traga!"></a> <a href="https://www.last.fm/music/Perfume/COSMIC+EXPLORER"><img src="https://lastfm.freetls.fastly.net/i/u/64s/bc9a47273fc93d5dd45dbac102c3b616.jpg" title="Perfume - COSMIC EXPLORER"></a> </p>

          
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
