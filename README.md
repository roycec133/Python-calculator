# Python CLI + GUI Scientific Calculator

This project is a fully functional scientific calculator written in Python. It started as a simple command-line calculator and has evolved into a modern calculator with both command-line (CLI) and graphical user interface (GUI) versions. The GUI is built using CustomTkinter and features a custom math parser and calculation engine, allowing it to parse and evaluate mathematical expressions without relying on Python’s eval() function.

## Features

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Floor Division (`//`)
- Exponentiation (`**`)
- Square root operation: `sqrt <number>`
- Handles division by zero
- Supports float and integer input
- Runs in a loop until the user chooses to quit
- Clean and readable function-based code structure
- Trigonometric operations:
  - Sine: `sin <angle in degrees>`
  - Cosine: `cos <angle in degrees>`
  - Tangent: `tan <angle in degrees>`
- Continuous loop until user exits with `q`
- Modern GUI with CustomTkinter
- Custom math parser — parses expressions like 5 + 3 * 2 with correct operator precedence
- Dedicated calculation engine (no eval())
-  Multiple GUI themes: Dark, Light, and Pastel
- Handles negative numbers correctly (e.g., -5 + 3)

## Requirements

- Python version **3.9 or higher**

While it may work on 3.6+, certain versions of tkinter bundled with older Python versions can cause GUI rendering issues, style bugs, or missing widget features.

CLI version remains compatible with Python 3.6+

## Installation

1. Clone this repository or download the project files:

```bash
git clone https://github.com/roycec133/Python-calculator.git
```

2. Navigate into the project directory:

```bash
cd python-calculator
```

3. (Optional for Linux/macOS) Make the script executable:

```bash
chmod +x calculator.py
```

## How to Run

### On Windows

Use Command Prompt or PowerShell:

```bash
python calculator.py
```

### On Linux / macOS

Option 1 – Run directly with Python:

```bash
python3 calculator.py
```

Option 2 – If made executable:

```bash
./calculator.py
```

## Usage Example

```
input an operation (ex. 5 + 2) or press q to quit anytime: 8 * 3
24.0
input an operation (ex. 5 + 2) or press q to quit anytime: 10 / 0
infinity (divided by zero)
input an operation (ex. 5 + 2) or press q to quit anytime: q
exiting calculator
```

## Changelog

See [`changelog.txt`](changelog.txt) for version history and updates.

## Author

**Terry Royce**  
[GitHub Profile](https://github.com/roycec133)
