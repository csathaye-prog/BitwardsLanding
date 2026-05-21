# BitwardsLanding

Static landing page for Bitwards. This repo is configured to deploy to GitHub Pages automatically when you push to `main` using the included GitHub Actions workflow.

## Quick deploy

1. Ensure your local branch is `main` and commit all files.
2. Add the GitHub remote and push:

```bash
git remote add origin https://github.com/csathaye-prog/BitwardsLanding.git
git branch -M main
git push -u origin main
```

3. GitHub Actions will run the `deploy-pages.yml` workflow and publish the site.

## Public URL

Once deployed, the site will be available at:

```
https://csathaye-prog.github.io/BitwardsLanding/
```

## Generating a QR code

This repo includes `make_qr.py`. By default it creates a QR for the Pages URL above. To generate or override the URL:

```bash
python make_qr.py              # creates qr-code.png for the default Pages URL
python make_qr.py https://example.com/path  # creates qr-code.png for custom URL
```

Scan `qr-code.png` with your phone to open the deployed site.

If you prefer a temporary test URL, run a local server and use `ngrok` to expose it, then pass the `ngrok` URL to `make_qr.py`.
