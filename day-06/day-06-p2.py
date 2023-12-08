time = 40817772
distance = 219101213651089

win = 0
for j in range(0, time + 1):
    if (j * (time - j)) > distance:
        win += 1


print(win)
