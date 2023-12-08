time = [40, 81, 77, 72]
distance = [219, 1012, 1365, 1089]
result = 1

for i in range(len(time)):
    win = 0
    for j in range(0, time[i] + 1):
        if (j * (time[i] - j)) > distance[i]:
            win += 1
    result *= win


print(result)
