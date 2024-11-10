# 01 – Các lát cắt
s = input().strip()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

# 02 – Số lượng từ
s = input().strip()
print(len(s.split()))

# 03 – Xâu mới
s = input().strip()
mid = (len(s) + 1) // 2
s1, s2 = s[:mid], s[mid:]
print(s2 + s1)

# 04 – Vị trí ký tự
s = input().strip()
c = input().strip()
if s.count(c) == 1:
    print(s.index(c))
elif s.count(c) > 1:
    print(s.index(c), s.rindex(c))
else:
    print(-1)

# 05 – Lần thứ 2
s = input().strip()
c = input().strip()
if s.count(c) > 1:
    print(s.index(c, s.index(c) + 1))
elif s.count(c) == 1:
    print(-1)
else:
    print(-2)

# 06 – Xóa xâu con
s = input().strip()
c = input().strip()
if s.count(c) > 1:
    start = s.index(c)
    end = s.rindex(c)
    print(s[:start] + s[end + 1:])
else:
    print(s)

# 07 – Đảo ngược xâu con
s = input().strip()
c = input().strip()
start = s.index(c)
end = s.rindex(c)
print(s[:start] + s[start:end + 1][::-1] + s[end + 1:])

# 08 – Thay thế
s = input().strip()
print(s.replace('1', 'one'))

# 09 – Xóa ký tự
s = input().strip()
c = input().strip()
print(s.replace(c, ''))

# 10 – Thay thế ký tự
s = input().strip()
c = input().strip()
cnew = input().strip()
first = s.index(c)
last = s.rindex(c)
print(s[:first + 1] + s[first + 1:last].replace(c, cnew) + s[last:])

# 11 – Rút ngắn xâu
s = input().strip()
print(''.join([s[i] for i in range(len(s)) if i % 3 != 0]))

# 12 – Tìm và thay thế xâu con
t = input().strip()
w_old = input().strip()
w_new = input().strip()
while w_old in t:
    t = t.replace(w_old, w_new)
print(t)

# 13 – Chữ số lớn nhất
import random
a = round(random.uniform(0, 1), 6)
b = round(random.uniform(0, 1), 6)
product = a * b
print(a, b, product, max(str(product)))

# 14 – Từ dài nhất
s = input().strip()
words = s.split()
longest_word = max(words, key=len)
print(longest_word, len(longest_word))

# 15 – Xâu Palindrome
s = input().strip()
print("Yes" if s == s[::-1] else "No")

# 16 – Đổi cơ số
n = int(input().strip())
b = int(input().strip())
result = ""
while n > 0:
    remainder = n % b
    if remainder >= 10:
        result = chr(remainder - 10 + ord('A')) + result
    else:
        result = str(remainder) + result
    n //= b
print(result)

# 17 – Số Palindrome
n = int(input().strip())
while str(n) != str(n)[::-1]:
    n += int(str(n)[::-1])
print(n)

# 18 – Nhiệt độ Fahrenheit và Celsius
s = input().strip()
if s[-1].lower() == 'c':
    tf = (9 / 5) * int(s[:-1]) + 32
    print(f"{tf:.2f}F")
else:
    tc = (5 / 9) * (int(s[:-1]) - 32)
    print(f"{tc:.2f}C")