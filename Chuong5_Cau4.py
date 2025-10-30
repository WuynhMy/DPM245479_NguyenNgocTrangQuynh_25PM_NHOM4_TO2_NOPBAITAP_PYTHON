'''Các hàm quan trọng trong xử lý chuỗi của Python'''
s = "  Hello, Python!  "
print(s.strip())         # "Hello, Python!"
print(s.lower())         # "  hello, python!  "
print(s.find("Python"))  # 8
print(s.replace("Python", "World"))  # "  Hello, World!  "
print(s.split(","))      # ['  Hello', ' Python!  ']
print(" ".join(["I", "love", "Python"]))  # "I love Python"