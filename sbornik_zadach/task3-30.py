def is_multiple_of_two_or_three(A):
    return A % 2 == 0 or A % 3 == 0

def is_not_multiple_of_three_and_ends_with_zero(A):
    return A % 3 != 0 and A % 10 == 0

test_values = [0, 1, 2, 3, 4, 5, 6, 10, 12, 15, 20]

print("Проверка кратности двум или трем:")
for value in test_values:
    if is_multiple_of_two_or_three(value):
        print(f"{value} кратно двум или трем.")
    else:
        print(f"{value} не кратно ни двум, ни трем.")

print("\nПроверка на не кратность трем и окончание на ноль:")
for value in test_values:
    if is_not_multiple_of_three_and_ends_with_zero(value):
        print(f"{value} не кратно трем и оканчивается на ноль.")
    else:
        print(f"{value} либо кратно трем, либо не оканчивается на ноль.")