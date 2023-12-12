def get_extrapolated_value(history):
    dif = []
    for index, item in enumerate(history):
        if index != len(history) - 1:
            dif.append(int(item) - int(history[index + 1]))
    global total_dif, result, step
    total_dif = -total_dif - dif[-1]
    step += 1
    if len(list(dict.fromkeys(dif))) == 1:
        if step % 2 == 0:
            result -= total_dif
        else:
            result += total_dif
        return
    else:
        get_extrapolated_value(dif)


with open(".\day-09\input.txt") as f:
    input = f.read()

lines = input.strip().split("\n")
total_dif = 0
result = 0
step = 0
data = []
for line in lines:
    data = line.strip().split(" ")
    data.reverse()
    total_dif = -int(data[-1])
    step = 0
    get_extrapolated_value(data)

print(result)
