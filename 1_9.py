spisok = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]


def filt(x):
    return x % 2


def square(x):
    return x**2


result = filter(filt, spisok)
result_final = map(square, list(result))
print(list(result_final), 'С помощью def, map и filter')

print('---------------------------------------------------------')

spisok_1 = [x**2 for x in spisok if x % 2]
print(spisok_1, 'С помощью филтра в списке')