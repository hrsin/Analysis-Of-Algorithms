def fractionalKnapsack(weights, values, capacity):
    n = len(weights)
    items = [(values[i]/weights[i], weights[i], values[i]) for i in range(n)]
    print(items)
    items.sort(reverse=True)
    total_value = 0.0
    for ratio, weight, value in items:
        if capacity > weight:
            capacity -= weight
            total_value += value
            sel_weights.append(weight)
        else:
            total_value += ratio * capacity
            break
    return total_value
sel_weights = []
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
max_value = fractionalKnapsack(weights, values, capacity)
print("Greedy Knapsack (Fractional) -> Max value:", max_value)
print(sel_weights)