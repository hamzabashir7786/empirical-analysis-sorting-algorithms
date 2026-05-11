# Empirical Analysis of Sorting Algorithms

**Course:** Analysis of Algorithms  
**Implementations in Python**

## 📖 Overview

This project empirically compares four classic sorting algorithms – **Selection Sort**, **Bubble Sort**, **Quick Sort**, and **Merge Sort** – by measuring their execution time, number of comparisons, swaps/moves, and memory behaviour on different input sizes and orders.

The implementation is done from scratch without using any built-in sorting functions. The test cases include:

- Size 5: already sorted array
- Size 5: reverse sorted array
- Size 100: already sorted array
- Size 100: reverse sorted array

Each test is repeated 3 times and the average results are recorded.

## 🧠 Algorithms Implemented

| Algorithm      | Best Time  | Average Time | Worst Time | Space (aux.) | Stable | In-place |
|----------------|------------|--------------|------------|--------------|--------|----------|
| Selection Sort | O(n²)      | O(n²)        | O(n²)      | O(1)         | No     | Yes      |
| Bubble Sort    | O(n)       | O(n²)        | O(n²)      | O(1)         | Yes    | Yes      |
| Quick Sort     | O(n log n) | O(n log n)   | O(n²)      | O(log n) avg | No     | Yes      |
| Merge Sort     | O(n log n) | O(n log n)   | O(n log n) | O(n)         | Yes    | No       |

## 📂 Files

- `sorting_analysis.py` – Python source code containing all four sorting algorithms and the test harness.
- `Analysis_of_Sorting_Algorithms_Report.pdf` (optional) – Full academic report with theory, results, and analysis.

## 🚀 How to Run

1. Make sure you have **Python 3.6+** installed.
2. Download `sorting_analysis.py` or clone the repository:
   ```bash
   git clone https://github.com/<your-username>/empirical-analysis-sorting-algorithms.git
   cd empirical-analysis-sorting-algorithms
