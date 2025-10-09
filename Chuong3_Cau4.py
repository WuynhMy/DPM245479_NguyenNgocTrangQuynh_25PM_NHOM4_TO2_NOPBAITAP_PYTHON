'''Hãy cho biết kết quả của Boolean Expression'''
'''Cho x, y, z = 3, 5, 7. Hãy cho biết kết quả của Boolean Expression
(a) x == 3
(b) x < y
(c) x >= y
(d) x <= y
(e) x != y - 2
(f) x < 10
(g) x >= 0 and x < 10
(h) x < 0 and x < 10
(i) x >= 0 and x < 2
(j) x < 0 or x < 10
(k) x > 0 or x < 10
(l) x < 0 or x > 10'''
x, y, z = 3, 5, 7

# Evaluate the boolean expressions
results = {
    "(a) x == 3": (x == 3),
    "(b) x < y": (x < y),
    "(c) x >= y": (x >= y),
    "(d) x <= y": (x <= y),
    "(e) x != y - 2": (x != (y - 2)),
    "(f) x < 10": (x < 10),
    "(g) x >= 0 and x < 10": (x >= 0 and x < 10),
    "(h) x < 0 and x < 10": (x < 0 and x < 10),
    "(i) x >= 0 and x < 2": (x >= 0 and x < 2),
    "(j) x < 0 or x < 10": (x < 0 or x < 10),
    "(k) x > 0 or x < 10": (x > 0 or x < 10),
    "(l) x < 0 or x > 10": (x < 0 or x > 10)
}

# Print the results
for key, value in results.items():
    print(f"{key}: {value}")