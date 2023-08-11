# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Pet+Shop+Boys/Bilingual"><img src="https://lastfm.freetls.fastly.net/i/u/64s/f05b1bdc21a3133fc74a00300ed76502.jpg" title="Pet Shop Boys - Bilingual"></a> <a href="https://www.last.fm/music/Pet+Shop+Boys/Very"><img src="https://lastfm.freetls.fastly.net/i/u/64s/28f808934a0040d5877b57b499c67847.jpg" title="Pet Shop Boys - Very"></a> <a href="https://www.last.fm/music/Pet+Shop+Boys/Actually"><img src="https://lastfm.freetls.fastly.net/i/u/64s/2253901fbb8391cc8e09e7008c19bee0.png" title="Pet Shop Boys - Actually"></a> <a href="https://www.last.fm/music/Pet+Shop+Boys/Behaviour"><img src="https://lastfm.freetls.fastly.net/i/u/64s/99988f9b3fdd7a0dd973f2ad6f10baff.png" title="Pet Shop Boys - Behaviour"></a> <a href="https://www.last.fm/music/Pet+Shop+Boys/Nightlife"><img src="https://lastfm.freetls.fastly.net/i/u/64s/1ce7253ec0ec4f47a126ec2d14aa310d.png" title="Pet Shop Boys - Nightlife"></a> <a href="https://www.last.fm/music/Pet+Shop+Boys/Introspective"><img src="https://lastfm.freetls.fastly.net/i/u/64s/9adc7f58de87808926e3baec7f5c8ce9.png" title="Pet Shop Boys - Introspective"></a> <a href="https://www.last.fm/music/Pet+Shop+Boys/Please"><img src="https://lastfm.freetls.fastly.net/i/u/64s/858bb688810a4cc39f6f14389072ee0c.png" title="Pet Shop Boys - Please"></a> <a href="https://www.last.fm/music/Gerard+Way/Hesitant+Alien"><img src="https://lastfm.freetls.fastly.net/i/u/64s/a111fb4807c64d81cdb3995a7f9a1d4f.png" title="Gerard Way - Hesitant Alien"></a> <a href="https://www.last.fm/music/The+Knife/Deep+Cuts"><img src="https://lastfm.freetls.fastly.net/i/u/64s/6c435df6ae44422c968542ef9d267944.png" title="The Knife - Deep Cuts"></a> <a href="https://www.last.fm/music/Gerard+Way/Pinkish+%2F+Don%27t+Try"><img src="https://lastfm.freetls.fastly.net/i/u/64s/1aa58b3dc0cb50b90a506faa23105bb6.png" title="Gerard Way - Pinkish / Don't Try"></a> </p>

          
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
