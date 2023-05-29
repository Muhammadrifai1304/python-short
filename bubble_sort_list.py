def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

angka = [42, 19, 33, 8, 55]
bubble_sort(angka)
print("Hasil pengurutan:", angka)
