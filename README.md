# Kodi Repo Generator !!!

A GitHub-based tool that automatically generates and hosts a personal Kodi add-on repository. Push your add-on source code, and GitHub Actions will build the repository artifacts (zipped add-ons, `addons.xml`, checksums) and publish them to GitHub Pages — giving you a fully hosted Kodi repo with zero manual steps.

---

## How It Works

This project uses **GitHub Actions** to automate the entire Kodi repository build-and-deploy pipeline:

1. You place your Kodi add-on source folders in the repo.
2. On every push to the main branch, a GitHub Actions workflow runs automatically.
3. The workflow executes a Python script that:
   - Scans for add-on folders (each containing an `addon.xml`).
   - Zips each add-on into a versioned archive.
   - Generates the `addons.xml` manifest and its MD5 checksum (`addons.xml.md5`).
   - Builds a repository add-on zip so Kodi users can install your repo as a source.
4. The generated output is deployed to **GitHub Pages**, making your Kodi repository publicly accessible at `https://YOUR_USERNAME.github.io/Kodi-repo-gen/`.

No local build tools are required — everything runs in the cloud.

---

## Getting Started

### 1. Fork This Repository

Click the **Fork** button at the top-right of this page to create your own copy under your GitHub account. This is required because:

- GitHub Pages publishes from **your** fork, giving you a unique URL.
- GitHub Actions workflows run under **your** account's free Actions minutes.
- You'll be pushing your own add-on source code to your fork.

After forking, you'll have a repo at:
```
https://github.com/YOUR_USERNAME/Kodi-repo-gen
```

### 2. Clone Your Fork Locally

```bash
git clone https://github.com/YOUR_USERNAME/Kodi-repo-gen.git
cd Kodi-repo-gen
```

### 3. Enable GitHub Pages

1. Go to your forked repo's **Settings** tab.
2. In the left sidebar, click **Pages**.
3. Under **Build and deployment**, set the **Source** to `GitHub Actions` (or `Deploy from a branch` if the workflow pushes to a `gh-pages` branch — check the workflow file for specifics).
4. Click **Save**.

Your repository will be live at:
```
https://YOUR_USERNAME.github.io/Kodi-repo-gen/
```

### 4. Add Your Add-ons

Place each add-on's source folder in the root of the repository (or in a designated `src/` directory if the project uses one). Each add-on folder must contain a valid `addon.xml` at its root. For example:

```
Kodi-repo-gen/
├── plugin.video.example/
│   ├── addon.xml
│   ├── __init__.py
│   └── ...
├── script.module.mylib/
│   ├── addon.xml
│   └── lib/
├── repository.YOUR_REPO_NAME/
│   ├── addon.xml
│   └── ...
├── .github/
│   └── workflows/
│       └── repo-gen.yml
├── _repo_xml_generator.py
└── README.md
```

### 5. Configure the Repository Add-on

If the project includes a `repository.*` folder, update its `addon.xml` to point to your GitHub Pages URL:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<addon id="repository.YOUR_REPO_NAME"
       name="Your Repo Name"
       version="1.0.0"
       provider-name="Your Name">
    <extension point="xbmc.addon.repository" name="Your Repo Name">
        <info compressed="false">https://YOUR_USERNAME.github.io/Kodi-repo-gen/zips/addons.xml</info>
        <checksum>https://YOUR_USERNAME.github.io/Kodi-repo-gen/zips/addons.xml.md5</checksum>
        <datadir zip="true">https://YOUR_USERNAME.github.io/Kodi-repo-gen/zips/</datadir>
    </extension>
    <extension point="xbmc.addon.metadata">
        <summary>Your personal Kodi add-on repository</summary>
        <description>Install and update add-ons from this repository.</description>
        <platform>all</platform>
    </extension>
</addon>
```

### 6. Push and Let GitHub Actions Build

```bash
git add .
git commit -m "Add my add-ons"
git push origin main
```

That's it. The GitHub Actions workflow will trigger automatically, build the zips, generate the manifest, and deploy everything to GitHub Pages.

---

## GitHub Actions Workflow Explained

The workflow file lives at `.github/workflows/repo-gen.yml` and is the engine behind this project. Here's what it does step by step:

### Trigger

```yaml
on:
  push:
    branches: [ main ]
```

The workflow runs every time you push commits to the `main` branch. This means any time you add a new add-on, update an existing one, or change any file, the repo is automatically rebuilt and redeployed.

### Job Steps (typical flow)

1. **Checkout** — Pulls your latest code from the repository.
2. **Set up Python** — Installs Python so the generator script can run.
3. **Run the generator script** — Executes the Python script (e.g., `_repo_xml_generator.py`) which:
   - Finds all directories containing an `addon.xml`.
   - Creates a zip archive for each add-on, named `ADDON_ID-VERSION.zip`.
   - Generates `addons.xml` (the master manifest listing all add-ons and their metadata).
   - Generates `addons.xml.md5` (the checksum Kodi uses to detect updates).
   - Places all output in a `zips/` directory.
4. **Deploy to GitHub Pages** — Publishes the `zips/` directory (and optionally a `repo/` directory with the installable repository zip) to GitHub Pages so it's publicly accessible.

### Permissions

The workflow needs write access to deploy to Pages. This is typically configured with:

```yaml
permissions:
  contents: read
  pages: write
  id-token: write
```

If the workflow pushes to a `gh-pages` branch instead, it will use `GITHUB_TOKEN` with write permissions to that branch.

### Viewing Workflow Runs

You can monitor the build status at any time:

1. Go to your fork on GitHub.
2. Click the **Actions** tab.
3. You'll see a list of workflow runs. Click any run to see logs, including which add-ons were zipped and whether the deployment succeeded.

A green checkmark means everything built and deployed successfully. A red X means something went wrong — click into the run to see the error logs.

---

## Installing in Kodi

Once your GitHub Pages site is live, you can install your repository in Kodi:

1. Open Kodi and go to **Settings** → **File Manager**.
2. Click **Add source**.
3. Enter your GitHub Pages URL as the source:
   ```
   https://YOUR_USERNAME.github.io/Kodi-repo-gen/
   ```
4. Give it a name (e.g., "My Kodi Repo") and click **OK**.
5. Go back to the home screen → **Add-ons** → **Install from zip file**.
6. Select your source and navigate to the repository zip file (e.g., `repository.YOUR_REPO_NAME-1.0.0.zip`).
7. Once installed, go to **Install from repository** → select your repository → browse and install add-ons.

Kodi will now check your GitHub Pages URL for updates automatically.

---

## Updating Add-ons

To publish an update to any add-on:

1. Update the add-on's source code in your local clone.
2. **Bump the version number** in the add-on's `addon.xml`.
3. Commit and push:
   ```bash
   git add .
   git commit -m "Update plugin.video.example to v1.2.0"
   git push origin main
   ```
4. GitHub Actions will automatically rebuild and redeploy. Kodi will detect the new version on its next update check.

---

## Troubleshooting

**GitHub Pages not working?**
Make sure Pages is enabled in your repo settings and the source is configured to match the workflow's deployment method (either `GitHub Actions` or the `gh-pages` branch).

**Workflow not running?**
Check that the workflow file exists at `.github/workflows/repo-gen.yml` and that you're pushing to the correct branch (`main`).

**Kodi not finding add-ons?**
Verify that the URLs in your repository add-on's `addon.xml` match your actual GitHub Pages URL. The `<info>`, `<checksum>`, and `<datadir>` paths must be correct.

**Add-on not appearing after push?**
Make sure the add-on folder has a valid `addon.xml` at its root and that the version number was incremented from the previous release.

---

## Project Structure

```
Kodi-repo-gen/
├── .github/
│   └── workflows/
│       └── repo-gen.yml          # GitHub Actions workflow
├── repository.example/           # Repository add-on (rename to yours)
│   └── addon.xml
├── plugin.video.example/         # Example add-on (replace with yours)
│   └── addon.xml
├── _repo_xml_generator.py        # Script that builds zips and addons.xml
├── zips/                         # (generated) Output directory for artifacts
│   ├── addons.xml
│   ├── addons.xml.md5
│   ├── plugin.video.example/
│   │   └── plugin.video.example-1.0.0.zip
│   └── repository.example/
│       └── repository.example-1.0.0.zip
└── README.md
```

---

## License

This project is provided as-is for personal use. Kodi is a registered trademark of the Kodi Foundation. This project is not affiliated with or endorsed by the Kodi Foundation.
