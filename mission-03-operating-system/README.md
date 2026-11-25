# Mission 3 — Understand the operating system

## 1. Task / objective
The objective of Mission 3 is to examine how the operating system (macOS) manages hardware, software, and data:
- Gather live, privacy-safe operating system details, user identity, disk storage, and process activity.
- Investigate running processes, Process Identifiers (PIDs), and task scheduling.
- Differentiate between absolute and relative filesystem paths and analyze Unix file permissions (`r`, `w`, `x`).
- Document the six primary responsibilities of a modern operating system.

---

## 2. Work completed

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Identifies the OS name, version number, build, and underlying kernel architecture. | `macOS` (Darwin Kernel Version 27.2.0, ARM64 architecture for Apple Silicon). |
| **Current account identity** | Reveals the active user account executing the terminal session. | `[redacted]` (Non-root user account belonging to the primary student profile). |
| **Available and used storage** | Shows storage drive partition size, currently consumed capacity, and free space. | Root filesystem (`/dev/disk3s1s1`) total capacity: `460 GiB`, Used: `13 GiB`, Available: `270 GiB` (~5% used). |
| **System activity snapshot** | Displays active processes, CPU utilization, memory distribution, and background tasks. | Background daemons active: PID 1 (`/sbin/launchd`), `logd`, `fseventsd`, and interactive terminal shells. |

---

### Task 3.2 — Understand processes
- **What is a process?**
  A process is an active, executing instance of a computer program loaded into memory (RAM). While a program stored on disk is passive code, a process has an allocated address space, registers, program counter, and assigned system resources.
- **What does the PID column represent?**
  PID stands for **Process Identifier**. It is a unique positive integer assigned by the operating system kernel to identify and track every active process throughout its lifecycle.
- **Two examples of processes running on my computer:**
  1. `/sbin/launchd` (PID 1) — The primary root init process in macOS that boots the system, launches system daemons, and manages all other processes.
  2. `Terminal` / `zsh` — The interactive command-line shell process interpreting user keystrokes and executing CLI commands.

---

### Task 3.3 — Understand paths and permissions
- **Absolute path:** The complete, unambiguous location of a file or directory starting from the root directory (`/`). It is valid regardless of the user's current working directory.
  - *Example from repository:* `/Users/[redacted]/.../digital-detective-8491/terminal-practice/notes.txt`
- **Relative path:** The location of a file or directory relative to the current working directory where the shell is active.
  - *Example from repository root:* `terminal-practice/notes.txt` (or `../README.md` from inside `terminal-practice/`).

#### File permissions examination:
Inspecting `notes.txt` with `ls -l` displayed:
`-rw-r--r--  1 [redacted]  staff  100  notes.txt`

| Permission | Meaning | Example / Observed Status on `notes.txt` |
| :--- | :--- | :--- |
| **r — Read** | Allows viewing/reading the file's contents. | Enabled for owner (`r`), group (`r`), and others (`r`). |
| **w — Write** | Allows editing, modifying, or deleting the file's contents. | Enabled for owner (`w`); disabled for group (`-`) and others (`-`). |
| **x — Execute** | Allows running the file as a program or script (or traversing a directory). | Disabled (`-`) because `notes.txt` is a text document, not an executable binary or script. |

**Owner Permission Summary:** The owner (`[redacted]`) possesses **Read and Write** permissions (`rw-`), meaning the owner can view and modify the file, but cannot run it as a program.

---

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Controls program execution by scheduling CPU time, tracking process states (running, waiting, ready), and handling context switching. | The macOS scheduler allocates CPU cycles between an active code editor and background system sync tasks. |
| **Memory management** | Tracks physical RAM allocations, ensures processes have isolated address spaces, and reclaims memory when programs terminate. | Assigns 200 MB of RAM when opening Python or VS Code and prevents programs from overwriting each other's memory. |
| **Device management** | Manages hardware peripherals and internal chips via specialized device drivers and handles hardware interrupts. | Translates physical key presses from the keyboard and manages graphics rendering to the Retina display. |
| **File management** | Organizes data into hierarchical files and directories on disk, tracks metadata, and manages storage access permissions. | The APFS (Apple File System) organizes assignment folders, tracks file sizes, and handles saving `notes.txt`. |
| **User interface / shell** | Provides an interface for humans to interact with system hardware and run software, either graphically or via commands. | The macOS Aqua Graphical User Interface (Finder/Dock) and the zsh Terminal command-line shell. |
| **Security and permissions** | Authenticates users, isolates processes in secure memory spaces, and restricts unauthorized read/write access to files. | Enforcing `-rw-r--r--` permissions so other system accounts cannot modify assignment files without authorization. |

---

## 3. Commands / tools used
- `sw_vers`: Displayed macOS version and build numbers.
- `uname -a`: Displayed Darwin kernel release, architecture, and date.
- `whoami`: Checked the currently active user account (redacted in report for privacy).
- `df -h /`: Inspected mounted storage space, total capacity, and available disk space.
- `ps -eo pid,user,%cpu,%mem,comm`: Viewed active system processes and PIDs.
- `ls -l`: Inspected file permission strings (`rwx`) and ownership.

---

## 4. My understanding
- The operating system is the master coordinator of the entire computer. Without it, software programs would have to communicate directly with raw transistor circuitry, memory controllers, and display buses.
- Multitasking is made possible by the OS kernel rapidly switching CPU time slices across hundreds of concurrent processes, each tracked by a unique PID.
- Permissions protect both system stability and user privacy by explicitly defining who can read, modify, or execute any given file or directory.

---

## 5. Difficulties faced
- Filtering through the vast list of macOS background daemons returned by `ps` to find human-understandable processes without revealing private username paths.

---

## 6. How I resolved them
- Used formatted columns (`ps -eo pid,user,%cpu,%mem,comm | head -n 12`) to clearly observe system init daemons (such as `launchd` PID 1) while redacting local account names and specific path tokens.

---

## 7. Evidence / files
- `mission-03-operating-system/README.md`: Contains complete OS inspection records, process analysis, path/permission breakdown, and OS responsibilities table.

---

## 8. Commit details
- **Commit message:** `Document operating system and file management`
- **Branch:** `main`
- **Status:** Ready to stage and commit.
