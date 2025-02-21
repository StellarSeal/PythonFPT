def input_function():
    #return [int(input()) for i in range(int(input('Nhap vao so n: ')))]
    n = int(input("Nhap vao so n: "))
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    return numbers

def max_occurence(target):
    marked = []
    max_num = None
    max_count = None
    for number in target:
        if (max_num == None) or (max_count == None):
            max_num = number
            max_count = target.count(number)
            marked.append(number)
            continue
        # Sửa điều kiện, phải đảo ngược để skip cache :P
        if not (number in marked):
            marked.append(number)
            occurence = target.count(number)
            if occurence > max_count:
                max_count = occurence
                max_num = number
            elif occurence == max_count:
                if number < max_num:
                    max_count = occurence
                    max_num = number
    return max_num

def main():
    input_list = input_function()
    print("Most appeared number:", max_occurence(input_list))

if __name__ == "__main__":
    main()
