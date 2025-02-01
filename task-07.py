import random
import matplotlib.pyplot as plt

# Кількість ітерацій (кількість кидків кубиків)
N = 1_000_000

# Можливі суми від 2 до 12
sum_counts = {i: 0 for i in range(2, 13)}

# Симуляція кидків двох кубиків
for _ in range(N):
    dice_sum = random.randint(1, 6) + random.randint(1, 6)
    sum_counts[dice_sum] += 1

# Обчислення ймовірностей
simulated_probabilities = {key: (value / N) * 100 for key, value in sum_counts.items()}

# Теоретичні ймовірності (аналітичні)
theoretical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

# Вивід результатів у вигляді таблиці
print(f"{'Сума':<5} {'Монте-Карло':<15} {'Теоретична':<15}")
for key in range(2, 13):
    print(f"{key:<5} {simulated_probabilities[key]:<15.2f} {theoretical_probabilities[key]:<15.2f}")

# Побудова графіку
plt.figure(figsize=(10, 5))
plt.bar(simulated_probabilities.keys(), simulated_probabilities.values(), color='blue', alpha=0.6, label="Монте-Карло")
plt.plot(theoretical_probabilities.keys(), theoretical_probabilities.values(), color='red', marker='o', linestyle='dashed', label="Теоретична")
plt.xlabel("Сума на кубиках")
plt.ylabel("Ймовірність (%)")
plt.title("Ймовірності сум чисел при киданні двох кубиків")
plt.legend()
plt.xticks(range(2, 13))
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()