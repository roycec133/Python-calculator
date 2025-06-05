# Python CLI Calculator

This project is a command-line calculator application written entirely in Python. It supports multiple arithmetic operations, handles user input interactively, and manages edge cases such as division by zero. The tool is designed to run in any terminal environment.

## Features

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Floor Division (`//`)
- Exponentiation (`**`)
- Handles division by zero
- Supports float and integer input
- Runs in a loop until the user chooses to quit
- Clean and readable function-based code structure

## Requirements

- Python version **3.6 or higher**

Python must be installed and accessible from your system's PATH. The script uses features such as f-strings introduced in Python 3.6.

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
