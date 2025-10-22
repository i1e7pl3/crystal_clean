# crystal_clean
Установка рабочего окружения

Следуйте этим шагам, чтобы настроить и запустить проект локально.

1. Клонирование репозитория

Склонируйте репозиторий проекта с помощью Git:

git clone https://github.com/kiruha211/crystal_clean
cd crystalclean

Замените https://github.com/kiruha211/crystal_clean на URL вашего репозитория.

2. Создание виртуального окружения

Создайте и активируйте виртуальное окружение для изоляции зависимостей проекта:

# Для Linux/MacOS
python3 -m venv venv
source venv/bin/activate

# Для Windows
python -m venv venv
venv\Scripts\activate

После активации вы увидите (venv) в командной строке.

3. Установка зависимостей

Установите необходимые Python-пакеты, указанные в requirements.txt:

pip install -r requirements.txt

4. Запуск проекта

Перейдите в папку crystal_clean, и в терминале Bash запустите локальный сервер командой:

python manage.py runserver
