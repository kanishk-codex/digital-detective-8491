# Mission 5 — Numbers and data

## 1. Task / objective
The objective of Mission 5 is to understand how numbers and text are represented at the machine level:
- Manually calculate step-by-step conversions between decimal, binary, and hexadecimal number systems using the positional-value and repeated division methods.
- Verify all manual conversion results using Python's interactive functions (`bin()`, `hex()`, `int()`).
- Write and test an interactive Python program (`number_converter.py`) that converts decimal inputs into binary and hexadecimal representations.
- Investigate character encoding schemes (ASCII and UTF-8), including the binary codes of characters and why international standards are required.

---

## 2. Work completed

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
| :--- | :--- |
| **Convert decimal 13 to binary** | Repeated division by 2:<br>• $13 \div 2 = 6$ with remainder **1** (LSB)<br>• $6 \div 2 = 3$ with remainder **0**<br>• $3 \div 2 = 1$ with remainder **1**<br>• $1 \div 2 = 0$ with remainder **1** (MSB)<br>Reading remainders from bottom to top (MSB to LSB): **$1101_2$** |
| **Convert decimal 25 to binary** | Repeated division by 2:<br>• $25 \div 2 = 12$ with remainder **1** (LSB)<br>• $12 \div 2 = 6$ with remainder **0**<br>• $6 \div 2 = 3$ with remainder **0**<br>• $3 \div 2 = 1$ with remainder **1**<br>• $1 \div 2 = 0$ with remainder **1** (MSB)<br>Reading remainders from bottom to top: **$11001_2$** |
| **Convert binary 1010 to decimal** | Positional expansion in base 2:<br>• $(1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0)$<br>• $= (1 \times 8) + (0 \times 4) + (1 \times 2) + (0 \times 1)$<br>• $= 8 + 0 + 2 + 0 = \mathbf{10_{10}}$ |
| **Convert binary 1101 to decimal** | Positional expansion in base 2:<br>• $(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)$<br>• $= (1 \times 8) + (1 \times 4) + (0 \times 2) + (1 \times 1)$<br>• $= 8 + 4 + 0 + 1 = \mathbf{13_{10}}$ |
| **Convert hexadecimal A to decimal** | In base 16, symbol $\text{A}$ represents value 10:<br>• Positional calculation: $10 \times 16^0 = \mathbf{10_{10}}$ |
| **Convert hexadecimal 1F to decimal** | Positional expansion in base 16 (where $\text{F} = 15$):<br>• $(1 \times 16^1) + (15 \times 16^0)$<br>• $= 16 + 15 = \mathbf{31_{10}}$ |
| **Convert binary 1111 to hexadecimal** | Evaluate 4-bit nibble value in decimal:<br>• $(1 \times 8) + (1 \times 4) + (1 \times 2) + (1 \times 1) = 8 + 4 + 2 + 1 = 15_{10}$<br>In base 16, value 15 corresponds to the symbol **$\text{F}_{16}$** (or `0xF`). |

---

### Task 5.2 — Verify using Python

| Conversion Task | Python Expression Tested | Interactive Result | Matches Manual Working? |
| :--- | :--- | :--- | :--- |
| Decimal 13 to binary | `bin(13)` | `'0b1101'` | Yes, matches $1101_2$ |
| Decimal 25 to binary | `bin(25)` | `'0b11001'` | Yes, matches $11001_2$ |
| Binary 1010 to decimal | `int('1010', 2)` | `10` | Yes, matches $10_{10}$ |
| Binary 1101 to decimal | `int('1101', 2)` | `13` | Yes, matches $13_{10}$ |
| Hexadecimal A to decimal | `int('A', 16)` | `10` | Yes, matches $10_{10}$ |
| Hexadecimal 1F to decimal | `int('1F', 16)` | `31` | Yes, matches $31_{10}$ |
| Binary 1111 to hexadecimal | `hex(0b1111)` | `'0xf'` | Yes, matches $\text{F}_{16}$ |

---

### Task 5.3 — Build a small number converter
Created `mission-05-numbers-data/number_converter.py` using standard beginner-friendly Python constructs.

#### Program Test Runs:

| Test number | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| **42** | `0b101010` | `0x2a` |
| **156** | `0b10011100` | `0x9c` |
| **255** | `0b11111111` | `0xff` |

#### Explanation of built-in functions used:
- `input()`: Pauses program execution and reads a line of text entered by the user as a string.
- `int()`: Parses the string input and converts it into a numerical integer base 10 (or another specified base).
- `bin()`: Takes an integer value and returns its binary representation as a string prefixed with `0b`.
- `hex()`: Takes an integer value and returns its lowercase hexadecimal representation as a string prefixed with `0x`.

---

### Task 5.4 — How is text stored?
- **ASCII decimal codes:**
  - Uppercase letter **A**: `65` (binary: `01000001`)
  - Lowercase letter **a**: `97` (binary: `01100001`)
  *(Notice: The difference between uppercase and lowercase is exactly 32, which corresponds to setting the 6th bit).*
- **Why a computer needs an encoding standard:**
  Computer hardware and memory exclusively store binary switches (0s and 1s). A character encoding standard defines an agreed-upon dictionary that maps every letter, digit, and symbol to a distinct numerical value, ensuring that text written on one machine is stored, transmitted across networks, and rendered identically on any other device without corruption.
- **Example of a character not in basic ASCII:**
  The Indian Rupee sign **`₹`** (Unicode code point `U+20B9`). Basic 7-bit ASCII only covers English letters, digits, and control characters from 0 to 127. Characters from international languages and modern symbols require modern multi-byte encodings like **UTF-8**, where `₹` is represented by three bytes (`0xE2 0x82 0xB9`).

---

## 3. Commands / tools used
- Python 3 interactive shell / CLI: Ran verification expressions `bin()`, `hex()`, `int()`, and `ord()`.
- Text Editor: Created `mission-05-numbers-data/number_converter.py`.
- `python3 mission-05-numbers-data/number_converter.py`: Ran the converter script against multiple test cases.

---

## 4. My understanding
- All computer data—numbers, characters, images, and audio—is fundamentally encoded as binary digits (bits) grouped into bytes.
- Hexadecimal is used extensively by programmers because it is human-readable shorthand for binary: exactly 4 binary bits (a nibble) correspond to 1 hexadecimal digit.
- ASCII was an early 7-bit standard that worked well for English, but global communication necessitated UTF-8, which can represent over a million characters from all world alphabets and emojis while remaining backward compatible with ASCII.

---

## 5. Difficulties faced
- Understanding the prefixes `0b` and `0x` returned by Python's `bin()` and `hex()` functions.

---

## 6. How I resolved them
- Discovered that Python uses `0b` to denote binary literals and `0x` to denote hexadecimal literals so the interpreter does not confuse them with regular base-10 integers.

---

## 7. Evidence / files
- `mission-05-numbers-data/number_converter.py`: Python number converter script.
- `mission-05-numbers-data/README.md`: Complete manual conversion working, Python verification table, test run table, and encoding explanations.

---

## 8. Commit details
- **Commit message:** `Build number converter and practise data representation`
- **Branch:** `main`
- **Status:** Ready to stage and commit.
