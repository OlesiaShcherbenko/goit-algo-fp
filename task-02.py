import turtle
import math

# Функція для малювання дерева Піфагора
def draw_pythagoras_tree(branch_length, level):
    if level == 0:
        return
    
    # Малюємо гілку
    turtle.forward(branch_length)
    
    # Повертаємося вліво та малюємо ліву гілку
    turtle.left(45)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, level - 1)
    
    # Повертаємося вправо та малюємо праву гілку
    turtle.right(90)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, level - 1)
    
    # Повертаємося у вихідне положення
    turtle.left(45)
    turtle.backward(branch_length)

# Налаштування параметрів вікна turtle
def setup_turtle():
    turtle.speed(0)
    turtle.left(90)
    turtle.up()
    turtle.backward(300)
    turtle.down()

# Основна функція
def main():
    turtle.title("Дерево Піфагора")
    turtle.bgcolor("white")
    setup_turtle()

    # Введення рівня рекурсії від користувача
    level = int(input("Введіть рівень рекурсії (наприклад, 5-10): "))
    
    # Запуск рекурсивного малювання
    draw_pythagoras_tree(200, level)
    
    # Завершення роботи програми
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()