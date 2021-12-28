# ДЗ№ 2 (б)

"""К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""

def sum_list_1(dataset: list) -> int:
    answer = []
    list_1 = [i for i in range(number) if i % 2 != 0]

    for n in list_1:
        x = n**3
        z = [int(i) for i in str(x) + "17"]
        if sum(z) % 7 == 0:
            answer.append(sum(z))

    return sum(answer)

number = int(input("dataset: "))

my_list = []

result_1 = sum_list_1(my_list)
print(result_1)
