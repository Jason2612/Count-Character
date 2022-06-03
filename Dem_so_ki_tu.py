# Viet chuong trinh cho nguoi dung nhap vao chuoi
# hien thi so ky tu trong chuoi vua nhap vao

from itertools import count


txt = input("Nhap 1 chuoi bat ki vao day: ")

def count_char(txt):
    result = 0
    for char in txt:
        result += 1
    return result

print("Length: ", count_char(txt))