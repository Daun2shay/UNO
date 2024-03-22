while True:
    line = input("Enter a line of text: ")
    if line.lower() == "done" or line.lower() == "d":
        break
    else:
        reversed_line = line[::-1]
        print(reversed_line)