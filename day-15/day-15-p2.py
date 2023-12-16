def hashmap(label):
    value = 0
    for char in label:
        value = (value + ord(char)) * 17 % 256
    return value


with open(".\day-15\input.txt") as f:
    input_data = f.read()

strings = input_data.strip().split(",")

result = 0
boxes = {}
for string in strings:
    if string[-1] == "-":
        if boxes.get(string[0:-1]):
            boxes.pop(string[0:-1])
    else:
        hashmap(string.strip().split("=")[0])
        boxes.update({string.strip().split("=")[
                     0]: string.strip().split("=")[1]})

boxes_map = {}
for item in boxes:
    hash = hashmap(item)
    if boxes_map.get(hash):
        boxes_map.update({hash: boxes_map.get(hash) + 1})
        result += (hash + 1) * boxes_map.get(hash) * int(boxes[item])
    else:
        boxes_map.update({hash: 1})
        result += (hash + 1) * 1 * int(boxes[item])

print(result)
