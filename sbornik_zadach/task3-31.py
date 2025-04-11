def is_multiple_of_five_or_seven(N):

    return N % 5 == 0 or N % 7 == 0

def is_multiple_of_four_and_not_ending_with_zero(N):
    return N % 4 == 0 and N % 10 != 0

test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
               12, 14, 15, 16, 20, 21, 24]
print("Проверка кратности пяти или семи:")
for value in test_values:
    if is_multiple_of_five_or_seven(value):
        print(f"{value} кратно пяти или семи.")
    else:
        print(f"{value} не кратно ни пяти, ни семи.")

print("\nПроверка на кратность четырем и отсутствие окончания на ноль:")
for value in test_values:
    if is_multiple_of_four_and_not_ending_with_zero(value):
        print(f"{value} кратно четырем и не оканчивается на ноль.")
    else:
        print(f"{value} либо не кратно четырем, либо оканчивается на ноль.")
        