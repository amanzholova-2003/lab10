def knapsack(weights, values, max_weight):
    n = len(weights) # количество предметов
    table = [[0 for x in range(max_weight+1)] for x in range(n+1)]

    for i in range(n+1):
        for w in range(max_weight+1):
            if i==0 or w==0:
                table[i][w] = 0
            elif weights[i-1] <= w:
                table[i][w] = max(values[i-1] + table[i-1][w-weights[i-1]], table[i-1][w])
            else:
               table[i][w] = table[i-1][w]

    return table[n][max_weight]

max_weight = 6
weights = [1, 2, 3, 4]
values = [1, 2, 3, 5]
result = knapsack(weights, values, max_weight)
print(result)
