# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The objective of Mission 2 is to develop practical fluency in the command-line interface (CLI) on macOS:
- Execute and document standard Terminal navigation and file management commands (`pwd`, `ls`, `ls -l`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`).
- Safely perform non-destructive file operations in an isolated practice folder (`terminal-practice`).
- Understand command options (flags such as `-l`, `-a`, `-h`) and Unix pipelines (`|`).
- Examine the role of package managers on macOS (Homebrew).

---

## 2. Work completed

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Prints the full absolute path of the current working directory. | Displayed `/Users/[redacted]/.../digital-detective-8491`, confirming I am located at the root of my assignment repository. |
| **Directory listing (`ls`)** | Lists visible files and directories in the active folder in columnar format. | Displayed all mission folders (`mission-00-setup`, `mission-01-computer-basics`, etc.) and `README.md`. |
| **Detailed listing (`ls -l`)** | Displays a long-format listing with permissions, owner, group, byte size, modification timestamp, and filename. | Output showed lines like `-rw-r--r-- [redacted] staff 2730 README.md`, showing metadata for each item. |
| **Change directory (`cd ..` / `cd`)** | Moves the working directory to the parent directory or a specified folder. | Navigated up one level (`..`) and confirmed path changed, then returned into `digital-detective-8491`. |
| **Create directory (`mkdir`)** | Creates a new subdirectory at the specified path. | Created the folder `terminal-practice` inside the repository. |
| **Create empty file (`touch`)** | Creates an empty file or updates the access/modification timestamps of an existing file. | Created `notes.txt` with an initial size of 0 bytes inside `terminal-practice/`. |
| **Copy file (`cp`)** | Creates an independent duplicate of a file at a new destination path. | Copied `notes.txt` to `notes_backup.txt`; both files existed simultaneously with identical content. |
| **Move / rename file (`mv`)** | Moves a file to another path or renames it in place without duplicating data. | Renamed `notes_backup.txt` to `notes_archive.txt`. The original backup name was replaced. |
| **Display file contents (`cat`)** | Concatenates and displays the text contents of a file to standard output. | Output printed the two practice lines of text written into `notes.txt`. |

---

### Task 2.2 — Practise file changes safely
Inside the isolated folder `terminal-practice/`, I executed:
1. `echo "Learning basic terminal commands in macOS." > notes.txt` (overwriting/creating the file).
2. `echo "Appending a second line to verify non-destructive edits." >> notes.txt` (appending).
3. `cat notes.txt` to verify both lines were intact.
4. `cp notes.txt notes_backup.txt` and `mv notes_backup.txt notes_archive.txt`.

#### Answers to required conceptual questions:
- **Replacing vs Adding text (`>` vs `>>`):**
  - Replacing using `>` overwrites the destination file completely from the beginning, erasing all prior content.
  - Adding using `>>` appends new text at the end of the file, preserving all previously existing data.
- **Copying vs Moving (`cp` vs `mv`):**
  - Copying creates a separate, second file on storage with its own inode and content; modifications to one do not alter the other.
  - Moving changes the file's path or name within the directory index without creating a second copy on disk.
- **What information does the current-directory display provide?**
  - `pwd` (print working directory) reveals the absolute filesystem hierarchy from the root `/` to where the shell is currently positioned. This prevents running accidental commands in the wrong directory.
- **Why is a directory-listing operation useful?**
  - `ls` lets you quickly verify file existence, inspect directory organization, and review metadata (sizes, permissions, timestamps, and hidden files) without needing a graphical file browser.

---

### Task 2.3 — Understand flags and pipes
- **Comparing listing flags:**
  - `ls`: Bare filenames only.
  - `ls -l`: Detailed list showing permissions, ownership, size in raw bytes, and timestamp.
  - `ls -lah`: Incorporates `-a` (showing hidden files/dotfiles like `.git`, `.`, `..`) and `-h` (human-readable file sizes in KB, MB instead of raw bytes, e.g., `2.7K` instead of `2730`).
- **Pipeline demonstration (`ls -lah | head -n 5`):**
  - The pipe operator (`|`) redirects the standard output (`stdout`) of the command on the left into the standard input (`stdin`) of the command on the right.
  - In `ls -lah | head -n 5`, `ls -lah` generates a complete detailed directory listing, and `head -n 5` reads that incoming text stream and outputs only the first 5 lines to the screen.

---

### Task 2.4 — Understand package managers
- **Homebrew Check:**
  - Checked version: `Homebrew 7.0.7`
  - Sample installed packages listed: `git`, `python@3.14`, `gh`, `jq`, `htop`, `tree`, `sqlite`, `wget`.
- **Why package managers are useful:**
  - A package manager automates finding, installing, upgrading, and configuring software tools and programming libraries from central, verified repositories.
  - It resolves complex dependency chains automatically (for example, installing required libraries before compiling or running a main program).
  - It prevents broken configurations by tracking every installed file, making software updates and uninstalls clean and reliable.

---

## 3. Commands / tools used
- `pwd`: Printed current working directory.
- `ls`, `ls -l`, `ls -lah`: Listed directory contents with various detail flags.
- `cd`: Navigated directories.
- `mkdir -p terminal-practice`: Created practice directory.
- `touch`: Created initial empty practice file.
- `echo "..." >` and `echo "..." >>`: Performed write and append file operations.
- `cat`: Displayed file text.
- `cp`: Copied file.
- `mv`: Renamed backup file.
- `|` (pipe) with `head -n 5`: Piped output stream to display first 5 lines.
- `brew --version` & `brew list`: Inspected macOS package manager status and packages.

---

## 4. My understanding
- The command line gives direct, precise control over the operating system without the overhead of a graphical interface.
- Commands accept flags (prefixed with `-` or `--`) that modify their default behavior, allowing customized output formats.
- Streams and pipes (`|`) are one of the most powerful paradigms of Unix-like operating systems: small, modular tools that do one thing well can be connected together to accomplish complex workflows.

---

## 5. Difficulties faced
- Remembering the exact difference between `>` and `>>` when redirecting output in the shell.

---

## 6. How I resolved them
- Tested both operators directly inside `terminal-practice/`: `>` created/overwrote the file, while `>>` appended the second line below the first without wiping it. Inspected the output using `cat` to confirm both lines were present.

---

## 7. Evidence / files
- `mission-02-terminal/README.md`: Contains complete command reference, practical answers, flags/pipes explanation, and package manager review.
- `terminal-practice/notes.txt`: Practice text file created with appended lines.
- `terminal-practice/notes_archive.txt`: Renamed backup practice file.

---

## 8. Commit details
- **Commit message:** `Complete Terminal and file management mission`
- **Branch:** `main`
- **Status:** Ready to stage and commit.
