# Mission 1 — Know your computer

## 1. Task / objective
The objective of Mission 1 is to investigate and understand fundamental computer architecture and operations:
- Trace an everyday computer activity through the four core stages of computing: Input, Processing, Output, and Storage (IPOS).
- Identify and classify hardware and software components, distinguishing between operating systems, application software, and utility software.
- Examine real-world computer systems embedded in everyday life beyond traditional laptops and mobile phones.

---

## 2. Work completed

### Task 1.1 — Trace one activity using IPOS
- **Chosen Activity:** Writing, saving, and executing a Python script (`hello.py`) on my computer.

| Stage | What happens in your example? | Possible hardware / component |
| :--- | :--- | :--- |
| **Input** | I type Python statements like `print("Hello from Python")` using the keyboard and press `Cmd + S` or click the save button. | Keyboard, Trackpad / Mouse, USB/Bluetooth controller |
| **Processing** | The CPU interprets keystroke interrupts, the text editor buffer in RAM is updated, and the operating system processes the file-write command. Later, the Python interpreter compiles source code into bytecode and evaluates instructions. | CPU (Apple Silicon / Central Processing Unit), RAM (Random Access Memory), System Bus |
| **Output** | The text editor displays the characters on the screen in real-time, and running the script in Terminal outputs the message text `Hello from Python`. | Monitor / Built-in Retina Display, GPU (Graphics Processing Unit) |
| **Storage** | When saved, the code residing in temporary RAM is transferred to non-volatile flash blocks on the drive so that it persists after closing the program or powering off. | Solid State Drive (SSD), NVMe Storage Controller |

#### How the activity moves from input to output and storage:
1. Physical key presses send electrical signals through the keyboard controller to the CPU via hardware interrupts.
2. The operating system kernel receives the keystrokes and places the characters into an active memory buffer allocated to the editor in RAM.
3. The display subsystem (GPU and screen buffer) continuously reads from memory to refresh the pixels, rendering the characters on screen (Output).
4. When issuing the save command, the OS filesystem driver transfers the memory buffer from volatile RAM to non-volatile storage blocks on the SSD (Storage).
5. When executed from Terminal, the CPU reads the saved file from the SSD back into RAM, interprets the code, and sends text output to the screen.

---

### Task 1.2 — Identify hardware and software

| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| **Keyboard** | Hardware | Not applicable | Captures physical keypresses to input characters, shortcuts, and terminal commands. |
| **Retina Display / Monitor** | Hardware | Not applicable | Visually displays graphical user interfaces, text windows, and command outputs. |
| **CPU (Central Processing Unit)** | Hardware | Not applicable | Executes machine code instructions, manages logic, and controls system arithmetic operations. |
| **Solid State Drive (SSD)** | Hardware | Not applicable | Provides non-volatile long-term storage for system files, applications, and user projects. |
| **RAM (System Memory)** | Hardware | Not applicable | High-speed temporary workspace that holds active programs, kernel routines, and open data. |
| **macOS (Darwin Kernel)** | Software | Operating System software | Manages hardware access, schedules CPU tasks, handles memory management, and enforces file security. |
| **Visual Studio Code** | Software | Application software | Integrated code editor providing syntax highlighting, file browsing, and script debugging. |
| **Google Chrome / Safari** | Software | Application software | Web browser used for accessing course material, online documentation, and web services. |
| **Terminal (zsh shell)** | Software | Utility software | Command-line interface allowing direct execution of system tools, scripts, and file commands. |
| **Activity Monitor** | Software | Utility software | System diagnostics utility displaying live CPU load, memory usage, and process identifiers (PIDs). |

---

### Task 1.3 — Computer systems around you

| System | Main purpose | One input | One output |
| :--- | :--- | :--- | :--- |
| **Automated Teller Machine (ATM)** | Enables self-service banking transactions such as cash withdrawals, deposits, and balance inquiries. | Pin-pad keypad / Touchscreen selection / Card reader sensor | Physical cash dispenser / Thermal paper receipt printer / Screen prompt |
| **Smart Traffic Signal Controller** | Coordinates traffic flow dynamically at road intersections to minimize congestion and ensure pedestrian safety. | Inductive road loop sensors (detecting vehicle weight/metal) or pedestrian push-button | Red/Yellow/Green signal lamp arrays / Digital countdown timer display |
| **Metro Ticket Vending Machine (TVM)** | Automates the issuance of passenger tokens and smart card recharges at transit stations. | Touchscreen destination selector / Banknote & coin acceptor slot | Dispensed RFID transit token / Recharge confirmation on screen / Printed receipt |

---

## 3. Commands / tools used
- Text Editor / VS Code: Used to draft and structure Markdown tables.
- System Profiler / About This Mac: Used to verify local hardware components (CPU, unified RAM, display resolution, and SSD capacity).
- Terminal (`zsh`): Used for running and checking initial concepts.

---

## 4. My understanding
- **The IPOS Cycle:** Every computing system, regardless of scale, relies on the Input-Processing-Output-Storage cycle. Input brings external signals into digital data; processing manipulates or transforms that data in RAM using the CPU; output translates processed digital information into human-understandable or mechanical results; and storage ensures that information is preserved across power cycles.
- **Hardware vs Software hierarchy:** Hardware represents the tangible, electronic circuitry (processors, memory chips, buses, and storage media). Software represents the instructions executed by the hardware. Operating systems act as the bridge between hardware and application software, while utility software assists in maintenance, management, and diagnostics.
- **Embedded computer systems:** Dedicated computers exist everywhere around us (ATMs, traffic controllers, automated transit machines). Unlike general-purpose laptops, embedded systems often run dedicated firmware or specialized operating systems designed for a singular, reliable task.

---

## 5. Difficulties faced
- Differentiating between application software and utility software for command-line tools like Terminal, because Terminal is used daily like an application but fundamentally acts as a system utility interface.

---

## 6. How I resolved them
- Reviewed the definitions provided in the assignment document: application software helps users perform end-user tasks (such as writing documents or browsing the web), whereas utility software helps maintain, inspect, protect, or manage the computer. Since the Terminal interface provides administrative control, filesystem management, and system inspection, it is accurately classified as utility software.

---

## 7. Evidence / files
- `mission-01-computer-basics/README.md`: Contains completed IPOS trace, hardware/software classification table, and embedded everyday systems table.

---

## 8. Commit details
- **Commit message:** `Complete computer basics and IPOS mission`
- **Branch:** `main`
- **Status:** Ready to stage and commit.
