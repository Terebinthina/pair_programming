def diceGame(lst):
    score = 0
    for rounds in lst:
        if rounds[0] == rounds[1]:
            score = 0
            break
        else:
            score += rounds[0] + rounds[1]
    print(score)






diceGame([(1, 2), (3, 4), (5, 6)])
diceGame([(1, 2), (3, 3), (5, 6)])