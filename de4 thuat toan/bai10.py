c = int(input())
d = int(input())

a = str(c)
b = str(d)

# Đảm bảo 2 chuỗi có cùng độ dài (thêm số 0 ở đầu nếu cần)
max_len = max(len(a), len(b))
a = a.zfill(max_len)
b = b.zfill(max_len)

result = ""

for i in range(max_len - 1, -1, -1):
    digit_sum = int(a[i]) + int(b[i])
    result = str(digit_sum % 10) + result  # chỉ lấy chữ số hàng đơn vị

print(result)
