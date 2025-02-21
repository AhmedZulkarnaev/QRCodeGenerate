# Генератор QR-кодов

Это простой генератор QR-кодов, созданный с использованием **Flet** и **Python**.

## Возможности
- Генерация QR-кодов по указанной ссылке
- Настройка версии, размера, границы
- Мгновенный предпросмотр QR-кода
- Скачивание сгенерированного QR-кода

## Установка
1. Клонируйте этот репозиторий:
   ```bash
   git clone https://github.com/your-username/qr-code-generator.git
   cd QRCodeGenerate
   ```
2. Создайте виртуальное окружение и установите зависимости:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Использование
Запустите приложение:
```bash
flet run app.py
```
Для веб-версии:
```bash
flet run app.py --web
```
