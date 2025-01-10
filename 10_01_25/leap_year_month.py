month = int(input("Nhap vao thang muon kiem tra: "))
year = int(input("NNhap vao nam muon kiem tra: "))

if year < 1000:
    print("Vui long nhap vao 1 nam lon hon hoac bang 1000!")

days = 0
if month == 2:
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        days = 29
    else:
        days = 28
elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
    days = 30
else:
    days = 31

print("Thang ", month, "/", year, " co ", days, " ngay", sep = "")
