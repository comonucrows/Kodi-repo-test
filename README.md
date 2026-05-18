# Kodi Repo Generator

Generate and host a personal Kodi add-on repository with GitHub Actions and GitHub Pages.

This repository is designed to be used as a GitHub template. Click **Use this template**, create a new repository under your own account, add your Kodi add-ons, and GitHub Actions will publish the generated Kodi repository to GitHub Pages.

## Why Use A Template Instead Of A Fork?

GitHub adds extra workflow restrictions and approval prompts around forks. A template repository gives each user a clean repo that belongs to them from the start, which makes Actions and Pages easier to enable and reason about.

## Getting Started

### 1. Create Your Repository

1. Open this repository on GitHub.
2. Click **Use this template**.
3. Create a new public repository under your GitHub account or organization.
4. Clone your new repository.

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Enable GitHub Pages

1. Open your new repository on GitHub.
2. Go to **Settings**.
3. Open **Pages**.
4. Under **Build and deployment**, set **Source** to **GitHub Actions**.
5. Save the setting.

Your repository URL will be:

```text
https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/
```

### 3. Enable GitHub Actions If Prompted

If GitHub shows a prompt on the **Actions** tab, choose the option to enable workflows for your repository.

The workflow only needs:

- `contents: read` to read your add-on source files
- `pages: write` to create the Pages deployment
- `id-token: write` to authenticate the Pages deployment

It does not commit generated files back to your repository.

### 4. Configure Your Repository Add-on

Edit `.github/workflows/build-kodi-repo.yml`:

```yaml
env:
  KODI_REPO_ID: repository.myrepo
  KODI_REPO_NAME: MyRepo
  KODI_REPO_VERSION: 1.0.${{ github.run_number }}
  KODI_REPO_AUTHOR: MyRepo
  KODI_REPO_OUTPUT_PATH: _zips/
```

Use a unique `KODI_REPO_ID`, usually in the form `repository.yourname`.

The workflow sets `KODI_REPO_URL` automatically from your GitHub owner and repository name:

```text
https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/
```

If you use a custom Pages URL, add or replace this workflow environment value:

```yaml
KODI_REPO_URL: https://example.com/kodi/
```

### 5. Add Your Kodi Add-ons

Place each add-on folder in the repository root. Each add-on folder must contain an `addon.xml` file.

```text
YOUR_REPO_NAME/
├── plugin.video.example/
│   ├── addon.xml
│   └── ...
├── script.module.example/
│   ├── addon.xml
│   └── ...
├── repository.myrepo/
│   ├── icon.png
│   └── fanart.jpg
├── tools/
│   ├── generate_repo.py
│   └── template.xml
└── .github/
    └── workflows/
        └── build-kodi-repo.yml
```

The `repository.*` folder only needs `icon.png` and `fanart.jpg` at first. The workflow generates its `addon.xml` file during the build.

### 6. Build And Deploy

Push your changes to `main`:

```bash
git add .
git commit -m "Configure my Kodi repository"
git push origin main
```

GitHub Actions will:

1. Generate the repository add-on metadata.
2. Build versioned zip files.
3. Generate `addons.xml` and `addons.xml.md5`.
4. Publish the generated site to GitHub Pages.

You can also run the workflow manually from the **Actions** tab.

## Installing In Kodi

After the workflow deploys, open your Pages URL in a browser:

```text
https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/
```

Install the repository zip shown on that page in Kodi:

1. Open Kodi.
2. Go to **Settings** > **File Manager**.
3. Add your Pages URL as a source.
4. Go to **Add-ons** > **Install from zip file**.
5. Select the repository zip.
6. After it installs, use **Install from repository** to browse your add-ons.

## Local Build

You can test the generator locally if Python 3 is installed:

```bash
KODI_REPO_ID=repository.myrepo \
KODI_REPO_NAME=MyRepo \
KODI_REPO_VERSION=1.0.0 \
KODI_REPO_AUTHOR=MyRepo \
KODI_REPO_URL=https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/ \
python tools/generate_repo.py
```

On Windows PowerShell:

```powershell
$env:KODI_REPO_ID = "repository.myrepo"
$env:KODI_REPO_NAME = "MyRepo"
$env:KODI_REPO_VERSION = "1.0.0"
$env:KODI_REPO_AUTHOR = "MyRepo"
$env:KODI_REPO_URL = "https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/"
python tools/generate_repo.py
```

## Troubleshooting

### The Workflow Does Not Run

Open the **Actions** tab and enable workflows if GitHub asks. Also confirm your workflow file exists at `.github/workflows/build-kodi-repo.yml`.

### Pages Does Not Deploy

Open **Settings** > **Pages** and set **Source** to **GitHub Actions**.

### Kodi Cannot Find Updates

Check the generated `repository.*-VERSION.zip` and make sure the repository add-on points to your actual Pages URL. The generated `addon.xml` should contain:

```xml
<info compressed="false">https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/_zips/addons.xml</info>
<checksum>https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/_zips/addons.xml.md5</checksum>
<datadir zip="true">https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/_zips/</datadir>
```

### Add-on Does Not Appear

Make sure the add-on folder is at the repository root and contains a valid `addon.xml`. If you update an add-on, bump its version in `addon.xml` before pushing.

## Project Structure

```text
YOUR_REPO_NAME/
├── .github/workflows/build-kodi-repo.yml
├── repository.myrepo/
│   ├── fanart.jpg
│   └── icon.png
├── tools/
│   ├── generate_repo.py
│   └── template.xml
└── README.md
```

Generated files are published to GitHub Pages as a workflow artifact. They are not committed back to your repository.

## License

This project is provided as-is for personal use. Kodi is a registered trademark of the Kodi Foundation. This project is not affiliated with or endorsed by the Kodi Foundation.
