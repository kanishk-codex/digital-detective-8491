# Mission 4 — How programs run

## 1. Task / objective
The objective of Mission 4 is to understand how computer programs are translated from human-readable code into instructions the CPU can execute:
- Write and execute a simple Python program (`hello.py`) using Python 3 from the macOS Terminal.
- Compare compilers and interpreters across execution models, typical outputs, examples, and advantages.
- Explain the key differences between compilation and interpretation in simple, accurate terms.

---

## 2. Work completed

### Task 4.1 — Create and run a Python program
- Created the file `mission-04-programs/hello.py` containing:
  ```python
  print("Hello from Python")
  ```
- Executed the program from the terminal using Python 3:
  ```bash
  python3 mission-04-programs/hello.py
  ```
- **Observed output:**
  ```text
  Hello from Python
  ```

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translates the entire source code file into machine code all at once before the program runs. | Translates and executes code line-by-line (or statement-by-statement) on the fly during runtime. |
| **Typical output** | A standalone executable binary file (e.g., Mach-O on macOS, ELF on Linux, or `.exe` on Windows) or intermediate object files. | Immediate program output / results on screen without generating a separate standalone binary executable. |
| **One example** | C, C++, Rust, Go | Python, JavaScript, Ruby |
| **One advantage** | Much faster execution speed because machine instructions are pre-translated and hardware-optimized prior to execution. | Quicker development workflow and easier debugging since code can be tested immediately without waiting for compilation. |

#### Explanation of differences:
A compiler translates an entire source code file into native machine instructions in a separate compilation step before anything runs, producing a standalone binary file that the CPU executes directly. An interpreter, by contrast, reads and executes code line by line at runtime without creating a separate machine code file first. This makes compiled languages like C or Rust faster during execution, while interpreted languages like Python allow for rapid testing and simpler cross-platform portability. In real-world software, modern language implementations frequently combine both models: for example, Python compiles source code into intermediate bytecode (`.pyc`) before running it on the Python Virtual Machine (PVM).

---

## 3. Commands / tools used
- Text Editor: Created `mission-04-programs/hello.py`.
- `python3 mission-04-programs/hello.py`: Ran the script using Python interpreter version `3.14.7`.

---

## 4. My understanding
- High-level programming code (like Python or C) cannot be directly processed by the CPU, which only understands binary machine instructions (0s and 1s).
- Translators bridge this gap: compilers convert the whole program beforehand for execution speed, whereas interpreters evaluate instructions at runtime for flexibility.
- Python gives immediate feedback when testing programs, making it beginner-friendly and great for iterative coding.

---

## 5. Difficulties faced
- Understanding why Python is called an interpreted language even though it creates `.pyc` bytecode files under the hood.

---

## 6. How I resolved them
- Learned that Python uses a hybrid approach: the interpreter first compiles human-readable code into intermediate bytecode, and then the Python Virtual Machine (PVM) interprets that bytecode instruction-by-instruction. It is still classified primarily as an interpreted language because users execute the source script directly without manually invoking a linker or compiler build tool.

---

## 7. Evidence / files
- `mission-04-programs/hello.py`: Working one-line Python script.
- Terminal execution output: `Hello from Python`.
- `mission-04-programs/README.md`: Completed comparison table and conceptual explanation.

---

## 8. Commit details
- **Commit message:** `Compare compilers and interpreters`
- **Branch:** `main`
- **Status:** Ready to stage and commit.
