# # Alternative input method - String splitting
# birthday = input("Nhap ngay thang sinh: ").split("/")
# day = int(birthday[0])
# month = int(birthday[1])

day = int(input("Nhap ngay sinh: "))
month = int(input("Nhap thang sinh: "))

date_var = month * 100 + day

if (date_var >= 1222) or (date_var <= 119):
    print("Ban la cung Ma Ket (Capricorn)!")
elif date_var <= 218:
    print("Ban la cung Bao Binh (Aquarius)!")
elif date_var <= 320:
    print("Ban la cung Song Ngu (Pisces)!")
elif date_var <= 419:
    print("Ban la cung Bach Duong (Aries)!")
elif date_var <= 520:
    print("Ban la cung Kim Nguu (Taurus)!")
elif date_var <= 620:
    print("Ban la cung Song Tu (Gemini)!")
elif date_var <= 722:
    print("Ban la cung Cu Giai (Cancer)!")
elif date_var <= 822:
    print("Ban la cung Su Tu (Leo)!")
elif date_var <= 922:
    print("Ban la cung Xu Nu (Virgo)!")
elif date_var <= 1022:
    print("Ban la cung Thien Binh (Libra)!")
elif date_var <= 1121:
    print("Ban la cung Ho Cap (Scorpio)!")
elif date_var <= 1221:
    print("Ban la cung Nhan Ma (Sagittarius)!")
