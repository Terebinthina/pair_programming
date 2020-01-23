def is_untouchable(number):
    if number >= 2:
        lst = []
        x = 2
        for _ in range(int(number ** 2 - 1)):
            num_sum = 0
            y = 1
            for _ in range(x - 1):
                if x % y == 0:
                    num_sum += y
                y += 1
            if num_sum == number:
                lst.append(x)
            x += 1
        if len(lst) == 0:
            print(True)
        else:
            print(lst)
    else:
        print("Invalid Input")
is_untouchable(6)