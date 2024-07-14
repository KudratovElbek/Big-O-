import random
import timeit


# Bubble Sort funksiyasi
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Merge Sort funksiyasi
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Ro'yxat yaratish uchun funksiya
def create_random_list(size):
    return [random.randint(0, size) for _ in range(size)]


# Saralash vaqtini o'lchash uchun funksiya
def time_sorting_algorithm(algorithm, lst):
    start_time = timeit.default_timer()
    algorithm(lst)
    end_time = timeit.default_timer()
    return end_time - start_time


# Ro'yxat hajmlari
sizes = [100, 1000, 5000, 10000]

# Saralash vaqtlarini saqlash uchun lug'atlar
bubble_sort_times = {}
merge_sort_times = {}

# Har bir hajm uchun saralash vaqtlarini o'lchash
for size in sizes:
    random_list = create_random_list(size)

    # Bubble Sort
    bubble_sort_list = random_list.copy()
    bubble_sort_time = time_sorting_algorithm(bubble_sort, bubble_sort_list)
    bubble_sort_times[size] = bubble_sort_time

    # Merge Sort
    merge_sort_list = random_list.copy()
    merge_sort_time = time_sorting_algorithm(merge_sort, merge_sort_list)
    merge_sort_times[size] = merge_sort_time

# Natijalarni chop etish
print("Bubble Sort Vaqtlari:")
for size, time in bubble_sort_times.items():
    print(f"Ro'yxat hajmi: {size} - Vaqt: {time:.6f} sekund")

print("\nMerge Sort Vaqtlari:")
for size, time in merge_sort_times.items():
    print(f"Ro'yxat hajmi: {size} - Vaqt: {time:.6f} sekund")