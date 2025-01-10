# # Alternative input method using an array
#
# input = [float(input("Nhap diem trung binh hoc ki 1: ")), float(input("Nhap diem trung binh hoc ki 2: "))]
# average_first_semester = input[0]
# average_second_semester = input[1]

average_first_semester = float(input("Nhap diem trung binh hoc ki 1: "))
average_second_semester = float(input("Nhap diem trung binh hoc ki 2: "))

average_year = (average_first_semester + average_first_semester*2) / 3

print("Diem trung binh ca nam: %.2f" % average_year, end=" | ")

if average_year >= 8:
    print("Xep loai: Gioi")
elif average_year >= 6.5:
    print("Xep loai: Kha")
elif average_year >= 5:
    print("Xep loai: Trung binh")
elif average_year >= 3.5:
    print("Xep loai: Yeu")
else:
    print("Xep loai: Kem")
