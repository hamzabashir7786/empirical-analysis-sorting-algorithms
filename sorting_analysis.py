import time
import copy

# ========== SELECTION SORT ==========
def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return comparisons, swaps

# ========== BUBBLE SORT (optimised) ==========
def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return comparisons, swaps

# ========== QUICK SORT (Lomuto partition, first element pivot) ==========
def quick_sort(arr):
    comparisons = 0
    swaps = 0

    def partition(low, high):
        nonlocal comparisons, swaps
        pivot = arr[low]
        i = low
        for j in range(low + 1, high + 1):
            comparisons += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        arr[low], arr[i] = arr[i], arr[low]
        swaps += 1
        return i

    def _quick_sort(low, high):
        if low < high:
            pi = partition(low, high)
            _quick_sort(low, pi - 1)
            _quick_sort(pi + 1, high)

    _quick_sort(0, len(arr) - 1)
    return comparisons, swaps

# ========== MERGE SORT ==========
def merge_sort(arr):
    comparisons = 0
    moves = 0          # we count element writes during merge as "moves"

    def merge(left, right):
        nonlocal comparisons, moves
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
            moves += 1
        while i < len(left):
            merged.append(left[i])
            i += 1
            moves += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
            moves += 1
        return merged

    def _merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = _merge_sort(arr[:mid])
        right = _merge_sort(arr[mid:])
        return merge(left, right)

    sorted_arr = _merge_sort(arr)
    # Copy sorted values back to original array (in-place effect)
    for i in range(len(arr)):
        arr[i] = sorted_arr[i]
    return comparisons, moves   # treating moves as swap-equivalent for reporting

# ========== TEST HARNESS ==========
def run_test(sort_fn, name, test_cases):
    print(f"\n{'='*60}")
    print(f"Algorithm: {name}")
    print(f"{'Input Size':<12}{'Order':<18}{'Avg Time (ms)':<15}{'Comparisons':<15}{'Swaps/Moves':<15}")
    print("-" * 75)

    for size_label, arr in test_cases:
        times = []
        total_comps = 0
        total_swaps = 0
        for _ in range(3):      # run 3 times
            arr_copy = copy.deepcopy(arr)
            start = time.time()
            comps, swps = sort_fn(arr_copy)
            end = time.time()
            times.append(end - start)
            total_comps += comps
            total_swaps += swps
        avg_time_ms = (sum(times) / 3) * 1000   # convert to milliseconds
        avg_comps = int(total_comps / 3)
        avg_swaps = int(total_swaps / 3)
        # Determine order description
        if arr == sorted(arr):
            order = "Sorted"
        elif arr == sorted(arr, reverse=True):
            order = "Reverse Sorted"
        else:
            order = "Random"
        print(f"{size_label:<12}{order:<18}{avg_time_ms:<15.6f}{avg_comps:<15}{avg_swaps:<15}")

# ========== DEFINE TEST CASES ==========
test_cases = [
    ("5", [1, 2, 3, 4, 5]),
    ("5", [5, 4, 3, 2, 1]),
    ("100", list(range(1, 101))),
    ("100", list(range(100, 0, -1)))
]

# Run all algorithms
run_test(selection_sort, "Selection Sort", test_cases)
run_test(bubble_sort,   "Bubble Sort",   test_cases)
run_test(quick_sort,    "Quick Sort",    test_cases)
run_test(merge_sort,    "Merge Sort",    test_cases)