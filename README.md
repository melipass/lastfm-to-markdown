# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/64s/88633cbec943a54faf0c35449d3c10a6.jpg" title="Gepe - Gepinto"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/211429dd46cb419a9ff737d573419680.png" title="Generation X - Generation X"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/ce5547a6847f4453b6ec2d8018132333.png" title="Gepe - Audiovisión"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/4e533595e0754af28d19ac24d6f52376.png" title="Gepe - Hungría"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/6b1305ee4381e8635390055585b5b9df.png" title="Lady Gaga - The Fame Monster"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/71870e901187424aa1a28b424fe1db76.png" title="Genesis - Foxtrot"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/3ffd54b049a13d8d1b9ecc9a125d9aa2.jpg" title="Lady Gaga - Born This Way"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/c4fa57048cf94ebf8e26b1c20cb11f14.png" title="Gepe - 5x5"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/4f72ff93a5425b2fa2f086e5cb5bef32.jpg" title="Gepe - Las Piedras EP"> <img src="https://lastfm.freetls.fastly.net/i/u/64s/46a995942fa9fb32426cc6c80d010346.jpg" title="Lady Gaga - The Fame (Special Edition)"> </p>

          
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
        uses: melipass/lastfm-to-markdown@v1.3
        with:
          LASTFM_API_KEY: ${{ secrets.LASTFM_API_KEY }}
          LASTFM_USER: ${{ secrets.LASTFM_USER }}
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
