def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if arr[j][2] > arr[max_index][2]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

pemain = [
    ["Kylian Mbappe", "Paris Saint Germain", 40],
    ["Victor Osimhen", "Napoli", 28],
    ["Robert Lewandowski", "Barcelona", 33],
    ["Erling Haaland", "Manchester City", 52],
    ["Christopher Nkunku", "RB Leipzig", 22]
]

selection_sort(pemain)

print("Daftar pemain berdasarkan jumlah gol secara descending:")
for i, player in enumerate(pemain):
    print(f"{i+1}. {player[0]} ({player[1]}): {player[2]} gol")
