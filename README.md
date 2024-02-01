# Юнит-тесты (Диплом.Часть 1).

Юнит-тесты для Stellar Burgers (https://stellarburgers.nomoreparties.site/).

## Установка

1. Склонируйте репозиторий на локальную машину:

git clone https://github.com/your_username/your_project.git

2. Перейдите в каталог проекта:

cd your_project

3. Создайте виртуальное окружение и активируйте его:

python -m venv venv
venv\Scripts\activate (Windows)
source venv/bin/activate (Linux/Mac)

4. Установите зависимости:

pip install -r requirements.txt

## Запуск тестов

1. Перейдите в каталог с тестами:

cd tests

2. Запустите тесты с помощью pytest:

pytest


## Структура проекта

Проект имеет следующую структуру:

## Структура проекта

Проект имеет следующую структуру:

- mocks/ - Содержит модули для мокирования
  - mock_bun.py - Модуль для мокирования булочки
  - mock_ingredient.py - Модуль для мокирования ингредиента

- services/ - Содержит вспомогательные модули для генерации данных
  - gen_float_number.py - Модуль для генерации случайного числа с плавающей запятой
  - gen_string.py - Модуль для генерации случайной строки

- tests/ - Содержит файлы тестов для различных функциональностей
  - test_bun.py - Тест для булочки
  - test_burger.py - Тест для бургера
  - test_ingredient.py - Тест для ингредиента
  
- bun.py - Модуль для работы с булочкой
- burger.py - Модуль для работы с бургером
- conftest.py - Файл конфигурации для pytest
- database.py - Модуль для работы с базой данных
- ingredient.py - Модуль для работы с ингредиентом
- ingredient_types.py - Модуль, определяющий типы ингредиентов