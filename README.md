# Kodi Repo Generator

**Host your own Kodi add-on repository for free using GitHub — no coding or servers required.**

This project lets you create a personal Kodi add-on repository (the kind you add as a "source" in Kodi) and host it online at no cost. GitHub handles the building and hosting automatically. You just need to upload your add-on folders and click a few buttons.

---

## What You'll Need Before Starting

- A **GitHub account** (free) — sign up at [github.com](https://github.com/signup) if you don't have one.
- Your **Kodi add-on folders** — each one should contain an `addon.xml` file inside it. If you're developing your own add-ons, you probably already have these.
- A **web browser** — everything is done through the GitHub website. No special software to install.

---

## What This Actually Does

When you're finished, you'll have a web address (URL) like:

```
https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/
```

You can add that URL as a source in Kodi, and Kodi will be able to install and update your add-ons from it — just like any other Kodi repository.

---

## Step-by-Step Setup

### Step 1 — Create Your Own Copy of This Project

You need to make your own copy of this project on GitHub. This is called "using a template" — it gives you a fresh copy under your own account that you fully control.

1. Make sure you are **signed in** to GitHub.
2. Go to [this project's page](https://github.com/Forking-Help/Kodi-repo-gen).
3. Near the top of the page, click the green **"Use this template"** button.
4. Choose **"Create a new repository"**.
5. Give it a name (for example, `my-kodi-repo`). This name will be part of your URL, so pick something simple.
6. Make sure **Public** is selected (Kodi needs to be able to reach it).
7. Click **"Create repository"**.

You now have your own copy of the project. GitHub will take you to its page automatically.

> **Why "Use this template" instead of "Fork"?** Forking on GitHub comes with extra restrictions that can cause problems with the automated build process. The template approach avoids all of that.

---

### Step 2 — Turn On GitHub Pages

GitHub Pages is a free feature that turns your repository into a website. This is what Kodi will connect to.

1. On your new repository's page, click the **"Settings"** tab (near the top, next to "Insights").
2. In the left sidebar, scroll down and click **"Pages"**.
3. Under **"Build and deployment"**, find the dropdown labeled **"Source"**.
4. Change it to **"GitHub Actions"**.
5. The page saves automatically — you're done here.

---

### Step 3 — Turn On GitHub Actions (if asked)

GitHub Actions is the tool that automatically builds your repository files. It might already be enabled, but if not:

1. Click the **"Actions"** tab at the top of your repository page.
2. If GitHub shows a message asking you to enable workflows, click the button to **enable** them.
3. If you don't see any message and you see a list of workflows, you're all set — it's already enabled.

---

### Step 4 — Customize the Repository Name and Author

You'll want to change a few settings so your Kodi repository has your name on it instead of the defaults.

1. On your repository page, open the `.github` folder by clicking on it.
2. Then open the `workflows` folder inside it.
3. Click on the file named **`build-kodi-repo.yml`**.
4. Click the **pencil icon** (✏️) in the upper right of the file to edit it.
5. Find the section that looks like this:

```
env:
  KODI_REPO_ID: repository.myrepo
  KODI_REPO_NAME: MyRepo
  KODI_REPO_VERSION: 1.0.${{ github.run_number }}
  KODI_REPO_AUTHOR: MyRepo
  KODI_REPO_OUTPUT_PATH: _zips/
```

6. Change the values to match your preferences:
   - **KODI_REPO_ID** — A unique ID for your repo. Use the format `repository.yourname` (for example, `repository.johns_addons`). No spaces allowed.
   - **KODI_REPO_NAME** — The display name users will see in Kodi (for example, `John's Add-ons`).
   - **KODI_REPO_AUTHOR** — Your name or username.
   - Leave **KODI_REPO_VERSION** and **KODI_REPO_OUTPUT_PATH** as they are unless you have a reason to change them.

7. Scroll to the bottom and click the green **"Commit changes"** button. You can leave the default commit message.

---

### Step 5 — Add Your Kodi Add-ons

Now you need to upload the add-on folders you want in your repository.

1. Go back to the main page of your repository (click the repository name at the top).
2. Click the **"Add file"** button and choose **"Upload files"**.
3. Drag and drop your add-on folders into the upload area. Each add-on should be its own folder containing an `addon.xml` file.
4. Scroll down and click **"Commit changes"**.

Your repository should now look something like this:

```
my-kodi-repo/
├── plugin.video.myvideos/       ← your add-on
│   ├── addon.xml
│   └── (other files)
├── script.module.mylib/         ← another add-on (optional)
│   ├── addon.xml
│   └── (other files)
├── repository.myrepo/           ← already here from the template
│   ├── icon.png
│   └── fanart.jpg
├── tools/                       ← already here, don't touch
├── .github/                     ← already here, don't touch
└── README.md
```

> **Tip:** You can customize the `icon.png` and `fanart.jpg` inside the `repository.myrepo` folder. The icon shows up in Kodi's add-on browser, and the fanart is the background image. Replace them with your own images if you'd like — just keep the same filenames.

---

### Step 6 — Build and Publish

The build does **not** happen automatically when you upload files. This is on purpose — it gives you time to get everything set up before going live.

When you're ready to publish:

1. Click the **"Actions"** tab at the top of your repository.
2. On the left side, click **"Build Kodi Repo"**.
3. On the right side, click the **"Run workflow"** button.
4. A small dropdown will appear — leave the branch set to `main`.
5. Click the green **"Run workflow"** button inside the dropdown.

A yellow dot will appear showing the build is in progress. Wait a minute or two for it to finish — it will turn into a green checkmark when done.

Your repository is now live at:

```
https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/
```

(Replace `YOUR_USERNAME` with your GitHub username and `YOUR_REPO_NAME` with whatever you named your repository in Step 1.)

---

## How to Install Your Repository in Kodi

Once the build finishes, you can add your new repository to Kodi:

1. Open a web browser on any device and go to your Pages URL (the address from Step 6 above). You should see a page listing your repository zip file. This confirms everything is working.
2. Open **Kodi**.
3. Go to **Settings** (the gear icon).
4. Open **File Manager**.
5. Click **"Add source"**.
6. Click `<None>`, type in your Pages URL, and click **OK**.
7. Give the source a name (anything you'll recognize) and click **OK**.
8. Go back to the Kodi home screen.
9. Go to **Add-ons**.
10. Click the **open box icon** (top left) to open the add-on browser.
11. Choose **"Install from zip file"**.
12. Select the source you just added.
13. Select the `_zips` folder, then select the `repository.yourname-X.X.X.zip` file.
14. Wait for the notification that the repository installed successfully.
15. Now choose **"Install from repository"** and pick your repository to browse and install your add-ons.

---

## Updating Your Add-ons Later

When you want to push an update to one of your add-ons:

1. Update the **version number** inside that add-on's `addon.xml` file (for example, change `version="1.0.0"` to `version="1.0.1"`). This is required — Kodi uses the version number to detect updates.
2. Upload the updated add-on folder to your repository (the same way you did in Step 5 — uploading will replace the old files).
3. Go to the **Actions** tab and run the **Build Kodi Repo** workflow again (Step 6).
4. Kodi will automatically detect the update the next time it checks for updates.

---

## Troubleshooting

**"I ran the workflow but my Pages URL shows a 404 error."**
Go to **Settings → Pages** and make sure the Source is set to **GitHub Actions**. It can take a minute or two after the first build for the page to appear.

**"The workflow won't run or I don't see it."**
Click the **Actions** tab. If GitHub shows a banner asking you to enable workflows, click the button to enable them. Also make sure the file `.github/workflows/build-kodi-repo.yml` exists in your repository.

**"My add-on doesn't show up in Kodi after installing the repository."**
Make sure the add-on folder is at the top level of your repository (not inside another folder) and that it contains a valid `addon.xml` file. Then run the build workflow again.

**"Kodi says there are no updates even though I uploaded new files."**
You must increase the version number in the add-on's `addon.xml` before rebuilding. Kodi ignores changes if the version number hasn't changed.

---

## License

This project is provided as-is for personal use. Kodi is a registered trademark of the Kodi Foundation. This project is not affiliated with or endorsed by the Kodi Foundation.
