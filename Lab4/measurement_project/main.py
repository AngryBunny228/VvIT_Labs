import json
import logging
from pathlib import Path
from utils.reader import read_numbers, validate_numbers
from utils.statistics import calculate_average, find_min, find_max

def main():
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    log_path = Path(config["log_file"])
    log_path.parent.mkdir(exist_ok=True)
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )
    logging.info("Программа запущена")
    file_path = Path(config["input_file"])
    try:
        numbers = read_numbers(file_path)
        validate_numbers(numbers)
        logging.info(f"Файл прочитан: {file_path}")
        logging.info(f"Прочитано значений: {len(numbers)}") 
        print("Количество значений:", len(numbers))
        print("Среднее арифметическое:", calculate_average(numbers))
        print("Минимальное значение:", find_min(numbers))
        print("Максимальное значение:", find_max(numbers))
    except FileNotFoundError:
        logging.error(f"Файл не найден: {file_path}")
        print("Ошибка: файл не найден!")
    except ValueError as error:
        logging.error(f"Ошибка данных: {error}")
        print(f"Ошибка в данных: {error}")
    finally:
        logging.info("Программа завершена")

if __name__ == "__main__":
    main()