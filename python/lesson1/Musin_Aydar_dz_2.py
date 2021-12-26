# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число `19 ^ 3 = 6859` будем включать в сумму, так как `6 + 8 + 5 + 9 = 28` – делится нацело на `7`.



def sum_list_1(dataset: list) -> int:
    answer = []

    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    for n in list_1:
        x = n**3
        z = [int(i) for i in str(x)]
        if sum(z) % 7 == 0:
            answer.append(sum(z))

    return answer

number = 1000
list_1 = [i for i in range(number) if i % 2 != 0]
my_list = []

result_1 = sum_list_1(my_list)
print(result_1)








