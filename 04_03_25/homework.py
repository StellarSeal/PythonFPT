def capitalize_name(s: str) -> str:
    words = s.lower().split(" ")
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    return ' '.join(words)

def to_fpt_email(s: str) -> str:
    words = s.lower().split(" ")
    for i in range(len(words) - 1):
        words[i] = (words[i])[0]
    return ''.join(words)

def reverse_string(s: str) -> str:
    words = s.lower().split(" ")
    for i in range(len(words)):
        words[i] = (words[i])[::-1]
    return ' '.join(words)

def fill_password(p: str) -> str:
    return str(p).zfill(6)

def main(prompt: callable):
    string = input("Input = ")
    print(prompt(string))

if __name__ == "__main__":
    main(capitalize_name)
    main(to_fpt_email)
    main(reverse_string)
    main(fill_password)
