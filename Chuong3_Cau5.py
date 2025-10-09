'''Hãy cho biết kết quả xuất ra màn hình'''
"(a) i = 3, j = 5," and "k = 7"
"(b) i = 3, j = 7," and "k = 5"
"(c) i = 5, j = 3," and "k = 7"
"(d) i = 5, j = 7," and "k =3"
"(e) i = 7, j = 3," and "k = 5"
"(f) i =7, j = 5," and "k = 3"

# Các trường hợp khác nhau của i, j, k
test_cases = [
    (3, 5, 7),  # (a) i = 3, j = 5, k = 7
    (3, 7, 5),  # (b) i = 3, j = 7, k = 5
    (5, 3, 7),  # (c) i = 5, j = 3, k = 7
    (5, 7, 3),  # (d) i = 5, j = 7, k = 3
    (7, 3, 5),  # (e) i = 7, j = 3, k = 5
    (7, 5, 3),  # (f) i = 7, j = 5, k = 3
]

# Lặp qua từng bộ giá trị của i, j, k
for case in test_cases:
    i, j, k = case
    # Logic theo yêu cầu
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    
    # In kết quả cho từng trường hợp
    print(f"i={i}, j={j}, k={k}")
