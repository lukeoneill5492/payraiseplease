def calculatepay(hours, rate):
    if type(hours) is not type(int()):
        return "Enter a number in number format"
    if type(rate) is not type(int()):
        return "Enter a number in number format"
    x = int(hours) * int(rate)
    while x < 3000:
        print(x, "is not enough")
        x = x + 100
    if x >= 3000:
        print(x, "is enough for now")
    return ""

x = calculatepay(40, 20)
print(x)
