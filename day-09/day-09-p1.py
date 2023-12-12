def get_extrapolated_value(history):
    dif = []
    for index, item in enumerate(history):
        if index != len(history) - 1:
            dif.append(int(history[index + 1]) - int(item))
    global total_dif, result
    total_dif += dif[-1]
    if len(list(dict.fromkeys(dif))) == 1:
        result += total_dif + int(data[-1])
        total_dif = 0
        return
    else:
        get_extrapolated_value(dif)


with open(".\day-09\input.txt") as f:
    input = f.read()

lines = input.strip().split("\n")
total_dif = 0
result = 0
data = []
for line in lines:
    data = line.strip().split(" ")
    get_extrapolated_value(data)


print(result)
