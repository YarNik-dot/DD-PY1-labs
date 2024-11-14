numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers_without_None = numbers[:4] + numbers[5:]
correct_number = round(sum(numbers_without_None)/(len(numbers_without_None) + 1), 2)
numbers[4] = correct_number

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
