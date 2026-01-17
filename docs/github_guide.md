# 🐙 Getting Started with GitHub

A beginner's guide to using GitHub for accessing course materials.

---

## What is GitHub?

GitHub is a website that hosts code and files. Think of it as Google Drive for code — you can view, download, and collaborate on projects.

For this course, you'll use GitHub to:
- ✅ Download course notebooks and demos
- ✅ Access the latest updates
- ✅ (Optional) Track your own experiments

---

## Option 1: Download Files (Easiest)

If you just want to get the files and don't need to track changes:

### Download the Entire Repository

1. Go to the repository: [github.com/dlwhyte/GenAI_foundry](https://github.com/dlwhyte/GenAI_foundry)

2. Click the green **Code** button

3. Select **Download ZIP**

4. Extract the ZIP file on your computer

5. Done! You now have all the files

---

## Option 2: Clone with Git (Recommended)

Cloning creates a local copy that's easy to update when new content is added.

### Step 1: Install Git

| Operating System | Instructions |
|-----------------|--------------|
| **Mac** | Open Terminal and type `git --version`. If not installed, you'll be prompted to install it. |
| **Windows** | Download from [git-scm.com/download/win](https://git-scm.com/download/win) |
| **Linux** | Run `sudo apt install git` (Ubuntu/Debian) or `sudo yum install git` (Fedora) |

### Step 2: Clone the Repository

Open Terminal (Mac/Linux) or Command Prompt (Windows):

```bash
git clone https://github.com/dlwhyte/GenAI_foundry.git
```

This creates a folder called `GenAI_foundry` with all the files.

### Step 3: Navigate into the Folder

```bash
cd GenAI_foundry
```

### Step 4: Get Updates Later

When new content is added to the course:

```bash
cd GenAI_foundry
git pull
```

This downloads any new or changed files.

---

## Option 3: Open Directly in Google Colab

For notebooks, you don't need to download anything:

1. Find the notebook in the repository
2. Click on it to view
3. Click the **Open in Colab** badge, or
4. Go to [colab.research.google.com](https://colab.research.google.com/)
5. Select **GitHub** tab
6. Enter: `dlwhyte/GenAI_foundry`
7. Choose the notebook you want

---

## Understanding the Repository Structure

```
GenAI_foundry/
├── README.md           ← Main page (what you see on GitHub)
├── notebooks/          ← Jupyter notebooks for tutorials
├── docker-demos/       ← Interactive demo applications
├── docs/               ← Documentation and guides
└── images/             ← Images used in docs
```

---

## Common Tasks

### View a File
Click on any file name to see its contents.

### Download a Single File
1. Click on the file
2. Click the **Raw** button
3. Right-click → **Save As**

Or: Click the download icon (↓) if available.

### Check When Files Were Updated
Each file shows when it was last modified. Look for "2 days ago" or similar text next to file names.

### See What Changed
Click on **Commits** to see the history of changes.

---

## Glossary

| Term | Meaning |
|------|---------|
| **Repository (Repo)** | A project folder hosted on GitHub |
| **Clone** | Download a copy of a repository |
| **Pull** | Update your local copy with new changes |
| **Commit** | A saved change (like a checkpoint) |
| **Branch** | A separate version of the code (we use `main`) |
| **Fork** | Your own copy of someone else's repo |

---

## Troubleshooting

### "git: command not found"
Git isn't installed. See Step 1 above.

### "Repository not found"
Check the URL for typos. Make sure it's:
```
https://github.com/dlwhyte/GenAI_foundry.git
```

### "Permission denied"
You're trying to push changes to a repo you don't own. For this course, you only need to `clone` and `pull`.

### Files look outdated
Run `git pull` to get the latest version.

---

## Want to Learn More?

- [GitHub's Official Guide](https://docs.github.com/en/get-started/quickstart/hello-world)
- [Git Basics Video (10 min)](https://www.youtube.com/watch?v=HVsySz-h9r4)
- [Interactive Git Tutorial](https://learngitbranching.js.org/)

---

*MIT Professional Education — Applied Generative AI for Digital Transformation*
