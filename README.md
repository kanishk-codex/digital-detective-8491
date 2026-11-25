# The Digital Detective — Diwali Independent Learning Assignment

Explore Your Computer • Build a Mini System Report

## Student Information
- **Name:** Kanishk Patel
- **USN:** 2392608491
- **GitHub Username:** [kanishk-codex](https://github.com/kanishk-codex)
- **Repository Name:** `digital-detective-8491`
- **Repository URL:** [https://github.com/kanishk-codex/digital-detective-8491](https://github.com/kanishk-codex/digital-detective-8491)

---

## Project Overview
This repository contains my complete submission for the SnAI Diwali Independent Learning Assignment: *The Digital Detective*. The project investigates how modern computer systems function beneath graphical interfaces—exploring computer architecture, operating system internals, command-line operations, programming language execution, data representation in binary and hexadecimal, Git/GitHub collaboration workflows, and computer networking.

Every activity was conducted directly on my macOS computer, recorded with genuine terminal outputs and code tests, and systematically committed across isolated missions.

---

## Topics Explored
1. **Workspace and Version Control Setup:** Creating structured workspaces, initializing Git repositories, and linking local projects to GitHub.
2. **Computer Fundamentals & IPOS:** Tracing the Input-Processing-Output-Storage cycle across hardware and software classifications, and analyzing embedded real-world computer systems.
3. **Terminal and Command-Line Interface:** Navigating directory hierarchies, performing non-destructive file operations, utilizing command flags (`-l`, `-a`, `-h`), and chaining programs using Unix pipes (`|`).
4. **Operating System Internals:** Inspecting macOS system details, monitoring running processes with Process IDs (PIDs), understanding disk storage, distinguishing between absolute and relative paths, and auditing file permissions (`rwx`).
5. **Program Translation & Execution:** Executing Python scripts from the terminal and analyzing the architectural differences between compilers and interpreters.
6. **Number Systems & Data Encoding:** Performing manual base conversions (decimal, binary, hexadecimal) with mathematical working, verifying results with Python, building a modular CLI number converter, and investigating ASCII and UTF-8 encoding standards.
7. **Git Collaboration & Workflows:** Managing feature branches (`update-about`), practicing staging vs. committing, understanding Pull Requests, and compiling a practical Git command glossary.
8. **Computer Networking & Protocols:** Examining network scales (LAN, MAN, WAN), executing network diagnostics (`ping`, `nslookup`), and tracing the complete 7-step lifecycle of a web request.

---

## Mission Index

| Mission | Focus Area | Status | Documentation Link |
| :--- | :--- | :--- | :--- |
| **Mission 0** | Repository and workspace setup | Completed | [mission-00-setup/README.md](mission-00-setup/README.md) |
| **Mission 1** | Computer fundamentals and IPOS | Completed | [mission-01-computer-basics/README.md](mission-01-computer-basics/README.md) |
| **Mission 2** | Terminal and file management | Completed | [mission-02-terminal/README.md](mission-02-terminal/README.md) |
| **Mission 3** | Operating system, processes and permissions | Completed | [mission-03-operating-system/README.md](mission-03-operating-system/README.md) |
| **Mission 4** | How programs run | Completed | [mission-04-programs/README.md](mission-04-programs/README.md) |
| **Mission 5** | Number systems, Python and text encoding | Completed | [mission-05-numbers-data/README.md](mission-05-numbers-data/README.md) |
| **Mission 6** | Git, GitHub, branches and Pull Requests | Completed | [mission-06-git-github/README.md](mission-06-git-github/README.md) |
| **Mission 7** | Computer networks | Completed | [mission-07-networking/README.md](mission-07-networking/README.md) |
| **Mission 8** | Final review and submission | Completed | [mission-08-final-report/README.md](mission-08-final-report/README.md) |

---

## Instructions for Running the Number Converter
The Python number converter program is located in `mission-05-numbers-data/number_converter.py`. It accepts a decimal integer and prints both its binary and hexadecimal equivalents.

### How to run:
1. Open your Terminal and navigate to the repository directory:
   ```bash
   cd digital-detective-8491
   ```
2. Navigate into the Mission 5 folder:
   ```bash
   cd mission-05-numbers-data
   ```
3. Run the script using Python 3:
   ```bash
   python3 number_converter.py
   ```
4. Enter any positive decimal integer when prompted (for example: `42`, `156`, or `255`).
5. The program will display the converted binary (prefixed with `0b`) and hexadecimal (prefixed with `0x`) outputs.

Alternatively, run it directly from the repository root:
```bash
python3 mission-05-numbers-data/number_converter.py
```

---

## My Learning
During this assignment, I developed foundational skills across computing systems:
1. **Understanding Computer Internals:** Tracing the IPOS cycle revealed how keyboard interrupts, memory buffers in RAM, the CPU scheduler, and non-volatile SSD blocks collaborate seamlessly when creating and executing software.
2. **Command-Line Confidence:** Navigating the macOS filesystem using Terminal commands (`pwd`, `ls -lah`, `cp`, `mv`, and Unix pipes like `| head`) proved that complex file management and diagnostics can be performed faster and more reliably without relying on a graphical user interface.
3. **Data Representation Mastery:** Converting numbers by hand between decimal, binary, and hexadecimal gave me a solid grasp of positional value notation, why hexadecimal is essential for representing raw byte values, and how character standards like ASCII and UTF-8 enable global digital communication.
4. **Professional Version Control:** Moving from simple file saves to structured Git commits, feature branches, and Pull Requests taught me how professional software engineering teams safely collaborate and preserve project history.

---

## Workflow and Commit Strategy
Every mission in this repository was completed sequentially, verified through practical command-line activities or code execution, documented following the required uniform 8-section structure, and saved using an independent Git commit with clear, descriptive commit messages.

*Note: In compliance with privacy guidelines, sensitive personal network addresses, local account names, and hardware identifiers have been redacted throughout this repository.*
