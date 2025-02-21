def input_function():
    return int(input("Nhap vao so n: "))

def fibonacci_a(n):
    base = [1, 1]
    for i in range(2, n):
        base.append(base[i-1] + base[i-2])
    return base

def fibonacci_b(n):
    base = [1, 1]
    e = 2
    while True:
        next_element = base[e - 2] + base[e - 1]
        if next_element == n:
            return True
        if next_element > n:
            break
        base.append(next_element)
        e += 1
    return False

def main():
    print("3a. Print out fibonacci sequence")
    nA = input_function()
    print("Sequence with", nA, "elements:", fibonacci_a(nA))
    print("3b. Check if target belongs to the fibonacci sequence")
    nB = input_function()
    print("Is", nB, "in the fibonacci sequence ?",fibonacci_b(nB))

if __name__ == "__main__":
    main()
