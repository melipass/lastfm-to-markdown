# last.fm to markdown

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need extra privileges to modify the README.md file if it's in the same repo. If you come from the GitHub Marketplace, I'm still learning about making it usable from other repositories (any help appreciated!), but the code at the lastfmweekly.yml is enough to run things as long as you have the following requirements in place:

## 👩🏽‍💻 What you need
* A README.md file.
* Last.fm API key
  * Fill [this form](https://www.last.fm/api/account/create) to instantly get one. Requires a last.fm account.
* Set up a GitHub Secret called ```LASTFM_API_KEY``` with the value given by last.fm.
* Also set up a ```LASTFM_USER``` GitHub Secret with the user you'll get the weekly charts for.
* Add a ```<!-- lastfm -->``` tag in your README.md file, with two blank lines below it. The album covers will be placed here.

## 🚧 To do
* Fix the workflow to make it usable from other repositories, especially for those who come from the GitHub Marketplace.
* Allow users to choose the image size and image count for the album covers.
* Feel free to send a PR for anything you believe would be useful.

## 🎵 My weekly last.fm chart (example)

<!-- lastfm -->
![Fishmans - 98.12.28 男達の別れ](https://lastfm.freetls.fastly.net/i/u/64s/f473049c0d8b4dc5cdf70ca773c32ee1.png) ![Fishmans - 宇宙 日本 世田谷](https://lastfm.freetls.fastly.net/i/u/64s/42f09145a2c040959ffe6bbf1a82034c.png) ![Fishmans - 空中キャンプ](https://lastfm.freetls.fastly.net/i/u/64s/534891a8e26aa44f17936987a82f597b.png) ![Fishmans - Long Season](https://lastfm.freetls.fastly.net/i/u/64s/bff21f34908aa59773d0c3621cb373b0.png) ![The Flaming Lips - Clouds Taste Metallic](https://lastfm.freetls.fastly.net/i/u/64s/3d5fe77ecd5b4863a61cf63cc16392d2.png) 
