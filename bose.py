from string import ascii_lowercase as letters

while True:
    text = input("text: ").lower()
    num = 0
    result = ""

    for i in text:
        if num == 27:
            num = 1
        result += letters[letters.index(i) + num]
        num += 1