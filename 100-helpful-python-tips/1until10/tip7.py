# Você pode fazer um loop sobre elementos em uma lista em uma simples linha de uma maneira compreensivel.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Com dicionários isso também é possível.
dictionary = {'first_element': 1, 'second_element': 2, 'third_element': 3, 'fourth_element': 4}
odd_value_elements = { key: num for (key, num) in dictionary.items() if num % 2 == 1}
