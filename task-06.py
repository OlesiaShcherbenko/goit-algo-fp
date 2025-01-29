def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = {}
    
    for item, values in sorted_items:
        if budget >= values['cost']:
            selected_items[item] = budget // values['cost']
            total_calories += selected_items[item] * values['calories']
            budget -= selected_items[item] * values['cost']
    
    return selected_items, total_calories


def dynamic_programming(items, budget):
    item_list = list(items.keys())
    costs = [items[item]['cost'] for item in item_list]
    calories = [items[item]['calories'] for item in item_list]
    n = len(items)
    
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    total_calories = dp[n][budget]
    selected_items = {}
    w = budget
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item = item_list[i - 1]
            selected_items[item] = selected_items.get(item, 0) + 1
            w -= costs[i - 1]
    
    return selected_items, total_calories


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

print("Greedy Algorithm:", greedy_result)
print("Dynamic Programming:", dp_result)