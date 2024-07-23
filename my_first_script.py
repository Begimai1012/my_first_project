import json
import math
from time import sleep

# Строка для красоты
from time import sleep

pict_list = ['MY FIRST SKRIPT\n\n',
              '    *********',
              '   *       **',
              '  *       * *',
              ' *********  *',
              ' *       *  *',
              ' *       *  *',
              ' *       * *',
              ' *********',
             '\n\nI LOVE PYTHON']
for i in pict_list:
  sleep(.4)
  print(i)
  
import json
import math
import webbrowser
import os

# Функция для вычисления характеристик параллелепипеда
def calculate_characteristics(a, b, c):
    diag = math.sqrt(a**2 + b**2 + c**2)
    volume = a * b * c
    surface_area = 2 * (a*b + a*c + b*c)
    alpha = math.degrees(math.acos(a / diag))
    beta = math.degrees(math.acos(b / diag))
    gamma = math.degrees(math.acos(c / diag))
    radius_described_sphere = diag / 2
    volume_described_sphere = (4/3) * math.pi * radius_described_sphere**3

    characteristics = {
        "diag": str(diag),
        "volume": str(volume),
        "surface_area": str(surface_area),
        "alpha": str(alpha),
        "beta": str(beta),
        "gamma": str(gamma),
        "radius_described_sphere": str(radius_described_sphere),
        "volume_described_sphere": str(volume_described_sphere)
    }

    return characteristics

# Определение путей к файлам
input_file = 'parallelepipeds.json'
output_file = 'characteristics.json'
statistics_file = 'statistics.json'
html_template_file = 'template.html'  # ваш шаблон HTML

try:
    # Чтение исходного файла parallelepipeds.json
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Создание нового словаря для хранения вычисленных характеристик
    calculated_data = {}

    # Вычисление характеристик для каждого параллелепипеда в исходных данных
    for key, values in data.items():
        a = float(values['a'])
        b = float(values['b'])
        c = float(values['c'])

        # Вызов функции для вычисления характеристик
        characteristics = calculate_characteristics(a, b, c)

        # Добавление характеристик в новый словарь
        calculated_data[key] = characteristics

    # Сохранение вычисленных характеристик в файл characteristics.json
    with open(output_file, 'w') as outfile:
        json.dump(calculated_data, outfile, indent=4)

    # Вычисление усредненных значений
    avg_diag = sum(float(item['diag']) for item in calculated_data.values()) / len(calculated_data)
    avg_volume = sum(float(item['volume']) for item in calculated_data.values()) / len(calculated_data)
    avg_surface_area = sum(float(item['surface_area']) for item in calculated_data.values()) / len(calculated_data)
    avg_alpha = sum(float(item['alpha']) for item in calculated_data.values()) / len(calculated_data)
    avg_beta = sum(float(item['beta']) for item in calculated_data.values()) / len(calculated_data)
    avg_gamma = sum(float(item['gamma']) for item in calculated_data.values()) / len(calculated_data)
    avg_radius_described_sphere = sum(float(item['radius_described_sphere']) for item in calculated_data.values()) / len(calculated_data)
    avg_volume_described_sphere = sum(float(item['volume_described_sphere']) for item in calculated_data.values()) / len(calculated_data)

    # Формирование словаря со средними значениями
    statistics_data = {
        "avg_diag": str(avg_diag),
        "avg_volume": str(avg_volume),
        "avg_surface_area": str(avg_surface_area),
        "avg_alpha": str(avg_alpha),
        "avg_beta": str(avg_beta),
        "avg_gamma": str(avg_gamma),
        "avg_radius_described_sphere": str(avg_radius_described_sphere),
        "avg_volume_described_sphere": str(avg_volume_described_sphere)
    }

    # Сохранение средних значений в файл statistics.json
    with open(statistics_file, 'w') as statsfile:
        json.dump(statistics_data, statsfile, indent=4)

    # Вывод сообщения о количестве фигур
    print(f"Total number of figures: {len(calculated_data)}")

    # Вывод усредненных значений
    print("\nAverage characteristics:")
    for key, value in statistics_data.items():
        print(f"{key}: {value}")

    # Создание HTML страницы на основе шаблона
    with open(html_template_file, 'r') as template_file:
        template_content = template_file.read()

    # Замена меток в шаблоне на вычисленные значения
    for key, value in statistics_data.items():
        template_content = template_content.replace(f'<span id="{key}"></span>', value)

    # Сохранение сгенерированного HTML файла
    generated_html_file = 'generated_statistics.html'
    with open(generated_html_file, 'w') as html_file:
        html_file.write(template_content)

    # Открытие HTML страницы в браузере
    webbrowser.open(f"file://{os.path.abspath(generated_html_file)}")

except FileNotFoundError:
    print(f"File '{input_file}' not found.")
except Exception as e:
    print(f"Error: {e}")





