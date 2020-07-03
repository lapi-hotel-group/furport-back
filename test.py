for i in range(1, 10):
    text = ""
    if i % 3 == 0:
        text += "Fizz"
    if i % 5 == 0:
        text += "Buzz"
    print(text or i)
