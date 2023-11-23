# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

num = int(input("Введите трехзначное число: "))
firstNum : int = num % 10
print(firstNum)
secondNum : int = num // 10 % 10
print(secondNum)
thirdNum : int = num // 100  % 10
print(thirdNum)
sum = firstNum + secondNum + thirdNum
print(f"Сумма цифр этого трехзначного числа = {sum}")