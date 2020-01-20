def fizz_buzz(num):
    result = ""
    if num % 3 == 0:
        result += "Fizz"
    if num % 5 == 0:
        result += "Buzz"
    if result == "":
        result += str(num)
    print(result)

fizz_buzz(int(input("Integer: ")))