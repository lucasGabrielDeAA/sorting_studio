# ⚡ Sorting Studio

<p align="center">
  <strong>A modern, interactive desktop visualizer and benchmarking suite for 14 sorting algorithms.</strong><br>
  Built with pure Python — featuring a custom canvas-rendered dark GUI and terminal CLI mode with zero third-party dependencies.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+" />
  <img src="https://img.shields.io/badge/GUI-Tkinter%20(Canvas--Rendered)-4B8BBE?style=for-the-badge" alt="Tkinter" />
  <img src="https://img.shields.io/badge/Dependencies-Zero%20(Stdlib)-10B981?style=for-the-badge" alt="Zero Dependencies" />
  <img src="https://img.shields.io/badge/Platform-macOS%20%7C%20Windows%20%7C%20Linux-6366F1?style=for-the-badge" alt="Cross Platform" />
</p>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Algorithms & Theoretical Complexities](#-algorithms--theoretical-complexities)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Usage](#-usage)
  - [1. Launching the GUI](#1-launching-the-gui)
  - [2. Running via Terminal CLI](#2-running-via-terminal-cli)
  - [3. Programmatic Usage in Python](#3-programmatic-usage-in-python)
- [GUI Architecture & Highlights](#-gui-architecture--highlights)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

**Sorting Studio** provides an educational and benchmarking environment to explore, visualize, and compare sorting algorithms. 

Unlike basic Tkinter applications, Sorting Studio features custom canvas-rendered modern UI widgets (smooth rounded buttons, pills, hover animations, responsive canvas bar visualizer, and high-contrast color palettes) ensuring identical, crisp appearance across macOS, Windows, and Linux.

---

## ✨ Key Features

- **14 Sorting Algorithms Implemented**: Covering quadratic $O(n^2)$, log-linear / sub-quadratic $O(n \log n)$, and linear/distribution $O(n + k)$ paradigms.
- **🎨 Custom Modern Dark Theme**: Deep obsidian background (`#0B0F19`) with color-coded complexity columns, smooth hover transitions, and rounded canvas widgets.
- **📊 Interactive Bar Visualizer**: Real-time canvas bar chart dynamically adjusting bar width, gaps, and color cues based on array elements and sort states.
- **⏱ High-Precision Timing**: Microsecond-accurate benchmarking powered by Python's `time.perf_counter()`.
- **🏆 1-Click All-Algorithm Leaderboard**: Benchmark all 14 algorithms concurrently on identical datasets and view a ranked performance leaderboard modal.
- **🎛 Array Presets & Custom Input**: One-click presets (*Default 6, Random 20, Reverse 15, Nearly Sorted 25, Random 100, Clear*) plus support for arbitrary comma- or space-separated integer inputs.
- **📋 Result Copying & Verification**: Automatic sorting verification against Python's ground truth with one-click clipboard copying.
- **💻 Headless CLI Mode**: Fast terminal benchmarking runner without opening the graphical interface.
- **📦 Zero Third-Party Dependencies**: Pure Python standard library (`tkinter`, `argparse`, `time`, `random`).

---

## 🧠 Algorithms & Theoretical Complexities

Algorithms are categorized by their theoretical time complexity:

| Category | Algorithm | Best Time | Average Time | Worst Time | Space Complexity | Stable? | In-Place? |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Quadratic** | **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes | Yes |
| **Quadratic** | **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | No | Yes |
| **Quadratic** | **Insertion Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes | Yes |
| **Quadratic** | **Cocktail Shaker Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes | Yes |
| **Quadratic** | **Gnome Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes | Yes |
| **Log-Linear** | **Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes | No |
| **Log-Linear** | **Quick Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | No | Yes |
| **Log-Linear** | **Heap Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | No | Yes |
| **Log-Linear** | **Tim Sort** | $O(n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes | No |
| **Log-Linear** | **Shell Sort** | $O(n \log n)$ | $O(n^{4/3})$ | $O(n^{3/2})$ | $O(1)$ | No | Yes |
| **Log-Linear** | **Comb Sort** | $O(n \log n)$ | $O(n^2 / 2^p)$ | $O(n^2)$ | $O(1)$ | No | Yes |
| **Linear / Distribution** | **Counting Sort** | $O(n + k)$ | $O(n + k)$ | $O(n + k)$ | $O(k)$ | Yes | No |
| **Linear / Distribution** | **Radix Sort** | $O(n \cdot d)$ | $O(n \cdot d)$ | $O(n \cdot d)$ | $O(n + k)$ | Yes | No |
| **Linear / Distribution** | **Bucket Sort** | $O(n + k)$ | $O(n + k)$ | $O(n^2)$ | $O(n + k)$ | Yes | No |

*Note: $k$ represents range/bucket count, $d$ represents maximum digits, and $p$ represents number of increments.*

---

## 📁 Project Structure

```text
sorting_studio/
├── main.py                     # Primary CLI and GUI application entry point
├── gui.py                      # Modern Tkinter GUI with custom canvas widgets & visualizer
├── helpers.py                  # Benchmarking utility (execution timer)
├── README.md                   # Project documentation & usage guide
└── sorting/                    # Standalone algorithm implementations
    ├── __init__.py             # Module exports for all 14 algorithms
    ├── bubble_sort.py          # Bubble Sort implementation
    ├── selection_sort.py       # Selection Sort implementation
    ├── insertion_sort.py       # Insertion Sort implementation
    ├── cocktail_shaker_sort.py # Bidirectional Cocktail Shaker Sort
    ├── gnome_sort.py           # Gnome Sort implementation
    ├── comb_sort.py            # Comb Sort with shrink factor 1.3
    ├── shell_sort.py           # Shell Sort with diminishing gap intervals
    ├── merge_sort.py           # Divide-and-conquer Merge Sort
    ├── quick_sort.py           # Recursive partition Quick Sort
    ├── heap_sort.py            # Binary Max-Heap Sort
    ├── tim_sort.py             # Hybrid Insertion + Merge Sort
    ├── counting_sort.py        # Non-comparative Counting Sort
    ├── radix_sort.py           # LSD (Least Significant Digit) Radix Sort
    └── bucket_sort.py          # Distribution-based Bucket Sort
```

---

## 🚀 Prerequisites

- **Python 3.8+** installed.
- No external `pip` packages required (uses standard library modules: `tkinter`, `argparse`, `time`, `random`, `sys`).

> **Linux users**: If Tkinter is not bundled with your Python installation, install it via your package manager:
> ```bash
> sudo apt-get install python3-tk    # Debian / Ubuntu
> sudo dnf install python3-tkinter   # Fedora / RHEL
> sudo pacman -S tk                  # Arch Linux
> ```

---

## 💻 Usage

### 1. Launching the GUI

Launch the default desktop interface:
```bash
python3 main.py
```

Launch with a custom initial list:
```bash
python3 main.py --list 84 23 91 12 65 3 47 18
```

#### In-App Controls:
- **Input Field**: Type any space- or comma-separated integers.
- **Preset Buttons**: Quickly load sample datasets (e.g., *Random 20*, *Nearly Sorted 25*, *Random 100*).
- **Complexity Columns**: Click any algorithm button to execute and display sorted output, verification badge, and runtime.
- **⚡ Run Benchmark**: Test all 14 algorithms simultaneously on the current list and open the ranked modal leaderboard.
- **📋 Copy**: Copy sorted values directly to clipboard.

---

### 2. Running via Terminal CLI

Execute all 14 algorithms directly in your terminal without opening a window:

```bash
python3 main.py --cli
```

Provide custom input values to the CLI:
```bash
python3 main.py --cli --list 120 45 68 12 99 3 24 50
```

**Sample CLI Output**:
```text
Initial vector:  [120, 45, 68, 12, 99, 3, 24, 50]

--- Sorting algorithms O(n^2) ---
Bubble sort: 
Execution time: 0.000008 seconds
Selection sort: 
Execution time: 0.000006 seconds
Insertion sort: 
Execution time: 0.000005 seconds
Cocktail Shaker sort: 
Execution time: 0.000006 seconds
Gnome sort: 
Execution time: 0.000005 seconds

--- Sorting algorithms O(n log n) / Sub-Quadratic ---
Merge sort: 
Execution time: 0.000014 seconds
Quick sort: 
Execution time: 0.000007 seconds
Heap sort: 
Execution time: 0.000009 seconds
Tim sort: 
Execution time: 0.000006 seconds
Shell sort: 
Execution time: 0.000005 seconds
Comb sort: 
Execution time: 0.000006 seconds

--- Sorting algorithms O(n + k) (Linear / Distribution) ---
Counting sort: 
Execution time: 0.000008 seconds
Radix sort: 
Execution time: 0.000010 seconds
Bucket sort: 
Execution time: 0.000012 seconds
```

---

### 3. Programmatic Usage in Python

Each algorithm is a pure Python function accepting a list/array of integers and returning a new sorted list:

```python
from sorting import quick_sort, merge_sort, tim_sort, radix_sort
from helpers import calculate_execution_time

data = [42, 17, 93, 8, 55, 23, 61]

# Direct sorting
sorted_data = quick_sort(data)
print("Sorted:", sorted_data)

# Measure execution time
result, elapsed_seconds = calculate_execution_time(tim_sort, data, verbose=True)
print(f"Elapsed: {elapsed_seconds:.6f}s")
```

---

## 🛠 GUI Architecture & Highlights

- **`RoundedCanvasButton`**: Custom `tk.Canvas` subclass generating vector-based anti-aliased polygons with configurable border radii, hover brightness shifts, active states, and optional right-aligned badges.
- **`PillButton`**: Compact micro-action buttons with hover feedback for quick preset switching.
- **`ArrayBarVisualizer`**: Dynamically scaled bar visualizer computing bar width, vertical heights, numerical labels, and dual-tone gradient schemes based on dataset density ($n \le 16$ vs large arrays).
- **Non-Destructive Execution**: All sorting routines copy the input list before sorting, preserving the original input array across multiple benchmarks.

---

## 🤝 Contributing

Contributions, algorithm optimizations, and UI suggestions are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-algorithm`)
3. Commit your changes (`git commit -m 'Add new sorting algorithm'`)
4. Push to the branch (`git push origin feature/new-algorithm`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — feel free to use, modify, and distribute it for educational and personal projects.
