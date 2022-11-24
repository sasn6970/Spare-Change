while True:
    owed = float(input("How much change are you owed? "))
    if owed > 0:
        break

coins = 0 #  Possible USD coins: 25¢, 10¢, 5¢, 1¢
cents = int(owed * 100)
print(cents)

while cents > 0:
    if cents >= 25:
        cents -= 25
        coins += 1

    elif cents >= 10:
        cents -= 10
        coins += 1

    elif cents >= 5:
        cents -= 5
        coins += 1

    else:
        cents -= 1
        coins += 1

print(f"{coins}")
