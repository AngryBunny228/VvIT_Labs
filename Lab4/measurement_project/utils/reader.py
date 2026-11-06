def read_numbers(file_path):
    numbers = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            numbers.append(float(line))
    return numbers
def validate_numbers(numbers):
    if len(numbers) == 0:
        raise ValueError("Список измерений пуст")