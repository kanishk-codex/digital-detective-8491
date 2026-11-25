# Mission 0 — Create your GitHub workspace

## 1. Task / objective
The objective of Mission 0 is to set up a clean, structured workspace for the Diwali Independent Learning Assignment (*The Digital Detective*). This includes:
- Verifying the presence and versions of required development tools (Python 3 and Git) on macOS.
- Creating a locally initialized Git repository named `digital-detective-8491` (using the assignment naming convention: `digital-detective-` followed by the last 4 digits of my USN `8491`).
- Setting up the required directory hierarchy and initial placeholder files for all 9 missions (Mission 0 through Mission 8) and an `evidence/` directory.
- Drafting a comprehensive root `README.md` to serve as the navigation index.
- Connecting the local repository to a remote repository on GitHub (`https://github.com/kanishk-codex/digital-detective-8491`) and publishing the initial setup.

---

## 2. Work completed
- Checked the installed version of Python 3 using Terminal: verified `Python 3.14.7`.
- Checked the installed version of Git using Terminal: verified `git version 2.55.0`.
- Created the root project directory `digital-detective-8491` in the designated workspace.
- Initialized a local Git repository on the default branch `main`.
- Configured remote origin: `https://github.com/kanishk-codex/digital-detective-8491.git`.
- Created folders for all nine missions:
  - `mission-00-setup/`
  - `mission-01-computer-basics/`
  - `mission-02-terminal/`
  - `mission-03-operating-system/`
  - `mission-04-programs/`
  - `mission-05-numbers-data/`
  - `mission-06-git-github/`
  - `mission-07-networking/`
  - `mission-08-final-report/`
  - `evidence/`
- Created the root `README.md` containing student identification, project purpose, and a mission index.
- Prepared this Mission 0 documentation detailing setup steps, tool versions, and repository concepts.

---

## 3. Commands / tools used
- `python3 --version`: Checked the installed Python interpreter version.
- `git --version`: Checked the installed Git version control utility.
- `mkdir -p`: Created multiple project directories in one command.
- `git init -b main`: Initialized the Git repository with `main` as the default branch.
- `git status`: Inspected the working tree to verify tracked and untracked files.
- `git add .`: Staged all setup files and directory templates.
- `git commit -m "Set up Digital Detective mission structure"`: Committed the initial project snapshot.

---

## 4. My understanding
- **What a repository is:** A Git repository is a digital storage container that tracks changes to files and folders across a project's timeline. Instead of saving copies of files with names like `file_final_v2.txt`, Git tracks changes incrementally as commits. This enables version history, safe rollback of errors, branching, and team collaboration.
- **Why the folder structure is organised by mission:** Splitting the assignment into numbered mission folders keeps each core subject (basics, terminal commands, OS concepts, Python execution, number representations, Git workflow, and computer networking) isolated and organized. It allows systematic evaluation by faculty, clear milestone tracking, and cleaner documentation.

---

## 5. Difficulties faced
- Ensuring Git initializes directly with the modern default branch name `main` instead of `master` without needing a manual branch rename afterwards.

---

## 6. How I resolved them
- Used the `-b main` flag directly with `git init` (`git init -b main`), which sets the initial branch to `main` immediately upon creation.

---

## 7. Evidence / files
- Root directory files: `README.md`
- Mission documentation: `mission-00-setup/README.md`
- Mission folder structure: `mission-01-computer-basics/`, `mission-02-terminal/`, `mission-03-operating-system/`, `mission-04-programs/`, `mission-05-numbers-data/`, `mission-06-git-github/`, `mission-07-networking/`, `mission-08-final-report/`, `evidence/`
- Tool verification evidence:
  - Python: `Python 3.14.7`
  - Git: `git version 2.55.0`

---

## 8. Commit details
- **Commit message:** `Set up Digital Detective mission structure`
- **Branch:** `main`
- **Status:** Committed locally; ready for remote push once GitHub remote is linked.
