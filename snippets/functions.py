def list_adder(ls):
    for i in range(len(ls) - 1):
        ls[i + 1] += ls[i]

list_1 = [0, 1, 2, 3, 0]
list_2 = [-1, 1, -2, 1, 4, 8, -5, -3, 0]

list_adder(list_1)
list_adder(list_2)

print(list_1)
print(list_2)
