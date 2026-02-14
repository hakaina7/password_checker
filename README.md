# 🔐 Password Security Tool

CLI-инструмент на Python для генерации и анализа надёжности паролей с возможностью сохранения отчётов в TXT и PDF формате.

Проект демонстрирует практические навыки разработки CLI-приложений, работы с безопасностью и генерации документов.

---

## 🚀 Возможности

- Генерация криптографически стойких паролей произвольной длины  
- Проверка сложности существующего пароля  
- Цветной вывод уровня надёжности в терминале  
- Скрытый ввод пароля (без отображения в консоли)  
- Маскирование пароля в отчётах  
- Генерация SHA-256 хеша  
- Сохранение отчётов в формате:
  - TXT
  - PDF  
- Автоматическое создание папки `reports/`

---

## 📦 Установка

Клонировать репозиторий:

```bash
git clone https://github.com/yourusername/password-security-tool.git
cd password-security-tool
```

---

### Создать виртуальное окружение (рекомендуется):

```bash
python -m venv venv
```

### Активировать:

Linux / macOS
```bash
source venv/bin/activate
```
Windows
```bash
venv\Scripts\activate
```
### Установить зависимости:
```bash
pip install -r requirements.txt
```

---

## 📁 Структура проекта
```
password-security-tool/
│
├── main.py              # Точка входа
├── checker.py           # Проверка сложности пароля
├── generator.py         # Генерация паролей
├── pdf_report.py        # Создание PDF-отчёта
├── requirements.txt     # Зависимости
├── .gitignore
└── reports/             # Сохраняемые отчёты
```

---

## 🖥 Использование

### Проверка пароля
```
python main.py --check "RNtndpl$ST2w3b<=|ug9/_DJ/v"
```

### Скрытый ввод пароля
```
python main.py
```
или
```
python main.py --hidden
```

### Генерация безопасного пароля
```
python main.py --generate 26
```

### Сохранение TXT отчёта
```
python main.py --check "RNtndpl$ST2w3b<=|ug9/_DJ/v" --save
```

### Сохранение PDF отчёта
```
python main.py --generate 20 --pdf
```

---

## 📊 Пример отчёта

```
PASSWORD SECURITY REPORT
========================================
Password (masked): RN***********************/v
SHA-256: 3b7e1c9e2a6b...
Generated at: 2026-02-14 14:32:10
----------------------------------------
length: 14
uppercase: True
lowercase: True
digits: True
special_chars: True
strength: Strong
```

---

## 🔐 Безопасность

- Пароль не сохраняется в открытом виде

- В отчётах используется маскирование

- Генерируется SHA-256 хеш

- Используется безопасный ввод через getpass

- Генерация основана на модуле secrets (криптографически стойкий генератор)


---

## 🛠 Используемые технологии

- Python 3.10+

- argparse

- colorama

- reportlab

- hashlib

- secrets

- getpass


---

## 🎯 Цель проекта

Проект создан для демонстрации навыков:

- разработки CLI-приложений

- безопасной работы с пользовательскими данными

- генерации PDF-документов

- организации структуры Python-проекта

- соблюдения best practices в области безопасности


---

📄 Лицензия

**MIT License**
