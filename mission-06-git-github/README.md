# Mission 6 — Git and GitHub

## 1. Task / objective
The objective of Mission 6 is to master collaborative version control workflows using Git and GitHub:
- Inspect repository status, stage targeted changes, commit with concise messages, and review commit history.
- Explain the fundamental distinction between staging changes and committing them.
- Create an independent feature branch named `update-about`, update the root `README.md` with a "My Learning" reflection, and practice the branch workflow.
- Understand the purpose of branches and Pull Requests (PRs) in software teams.
- Build a clear, one-line Git command glossary covering essential version-control operations.

---

## 2. Work completed

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status (`git status`)** | Displays the current branch, files that have been modified or staged, and any untracked files in the working directory. |
| **Stage selected changes (`git add <file>`)** | Moves specific file changes into the staging area (index) to prepare them for inclusion in the next commit snapshot. |
| **Create a commit (`git commit -m "..."`)** | Permanently records all staged changes as an immutable, hashed snapshot in the repository's history along with a descriptive message. |
| **View commit history (`git log`)** | Displays a chronological list of prior commits, including their unique SHA hashes, author names, timestamps, and commit messages. |

#### Difference between staging and committing:
- **Staging (`git add`):** Acts as a draft preparation table (the index). Staging allows a developer to carefully choose which specific files or changes belong together in the next logical update, without altering repository history yet.
- **Committing (`git commit`):** Takes everything currently on the staging table and locks it into the repository's permanent history database as a versioned snapshot. Once committed, the state can be referenced, reviewed, or restored at any point in the future.

---

### Task 6.2 — Create and use a branch
1. Created and switched to a new branch named `update-about`:
   ```bash
   git switch -c update-about
   ```
2. Opened root `README.md` and added the `## My Learning` section describing three key takeaways:
   - Understanding computer internals and the IPOS cycle.
   - Command-line confidence in macOS Terminal.
   - Data representation mastery across binary, hexadecimal, ASCII, and UTF-8.
3. Inspected `git status` to verify `README.md` was detected as modified.
4. Staged the file (`git add README.md`) and committed:
   ```bash
   git commit -m "Add My Learning section to root README"
   ```
5. Verified the commit on the `update-about` branch (`commit 677ef78`).

---

### Task 6.3 — Create a Pull Request workflow
- **What is a branch?**
  A branch is an independent, lightweight movable pointer to a commit in the repository. It enables developers to work on new features, documentation, or bug fixes in complete isolation without risking damage to the stable, tested code on the `main` branch.
- **What is a Pull Request (PR)?**
  A Pull Request is a collaborative feature hosted on GitHub that notifies team members that a feature branch is ready for review. It provides a visual line-by-line diff of all changes, allows team members to comment and request adjustments, and facilitates automated testing before code is merged into `main`.
- **Why branches and PRs are useful in team projects:**
  They prevent team members from overwriting each other's work or introducing breaking changes directly into production. By isolating changes on feature branches and vetting them through PR reviews, teams maintain high code quality and clear accountability.
- **Pull Request Status:**
  - Branch created: `update-about`
  - Target branch: `main`
  - Local state: Merged into `main` after verification; `update-about` branch retained in Git history.
  - Remote state: Ready to be published to `kanishk-codex/digital-detective-8491` on GitHub.

---

### Task 6.4 — Git command glossary

| Git Operation | One-line explanation in my own words |
| :--- | :--- |
| **Initialise a repository** | `git init` creates a new Git version-control database inside the current folder. |
| **Check status** | `git status` displays which files are modified, untracked, or staged for the next commit. |
| **Stage changes** | `git add` places modified or new files into the staging area ready to be committed. |
| **Commit changes** | `git commit` records staged changes permanently into the repository's history timeline. |
| **View history** | `git log` displays a chronological record of all previous commits, authors, and messages. |
| **Create or list branches** | `git branch` displays all existing local branches or creates a new branch pointer. |
| **Switch branches** | `git switch` changes the active working branch to another existing branch. |
| **Publish changes** | `git push` uploads local commits from your computer to a remote repository on GitHub. |
| **Retrieve remote changes** | `git pull` downloads and merges the latest commits from the remote repository into your local branch. |

---

## 3. Commands / tools used
- `git switch -c update-about`: Created and switched to the feature branch.
- `git status`: Verified working directory and staging status.
- `git add README.md`: Staged modified root README.
- `git commit -m "..."`: Created commit on the branch.
- `git switch main`: Switched back to the main branch.
- `git merge update-about`: Merged the verified feature branch changes into `main`.
- `git branch -v`: Listed local branches and verified commit heads.

---

## 4. My understanding
- Version control is essential for software development. Rather than saving chaotic versions like `report_final_v2_reallyfinal.txt`, Git tracks exact line-level differences across time.
- Branches provide safe sandbox environments: even if an experiment fails completely, the `main` branch remains untouched and functional.
- Pull Requests turn version control into an active peer-review communication platform.

---

## 5. Difficulties faced
- Understanding the difference between `git branch` and `git switch` (or older `git checkout`).

---

## 6. How I resolved them
- Learned that modern Git introduced `git switch` specifically for moving between branches and `git restore` for files, simplifying older overloaded `git checkout` syntax.

---

## 7. Evidence / files
- Branch `update-about` created with dedicated commit `677ef78`.
- Updated root `README.md` containing `## My Learning`.
- `mission-06-git-github/README.md`: Completed workflow table, PR explanation, and Git glossary.

---

## 8. Commit details
- **Commit message:** `Complete Git and GitHub collaboration mission`
- **Branch:** `main`
- **Status:** Ready to stage and commit.
