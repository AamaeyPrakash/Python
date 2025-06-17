N = int(input("Number of Product Codes: "))

for _ in range(N):
    code = input("Enter Product Code: ").strip()
    uppercase = ''
    total = 0
    i = 0
    while i < len(code):
        ch = code[i]
        if ch.isupper():
            uppercase += ch
            i += 1
        elif ch == '-' or ch.isdigit():
            num_str = ''
            if ch == '-':
                num_str += '-'
                i += 1
            while i < len(code) and code[i].isdigit():
                num_str += code[i]
                i += 1
            total += int(num_str)        
        else:
            i += 1

    print(uppercase + str(total))
