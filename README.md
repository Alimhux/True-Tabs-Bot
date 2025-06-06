# MTS TrueTabs Automation Bot

**Tech Stack:** Python, aiogram, IMAP/SMTP, API Integration  

Многофункциональный Telegram-бот для автоматизации работы с корпоративной системой TrueTabs (аналог Excel Online от MTS).

## Основные функции
- Интеграция с TrueTabs API: сбор данных о проектах, сотрудниках и кандидатах.
- Мониторинг дедлайнов с интеллектуальными уведомлениями.
- Работа с почтой: парсинг входящих писем через IMAP, отправка через SMTP.
- Генерация комплексных отчетов в Word.
- HR-автоматизация: обработка кандидатов, отправка приглашений.

## Технические особенности
- Асинхронная архитектура на `asyncio`.
- Шифрование данных и двухэтапная верификация.
- Самовосстановление при ошибках соединения.
- Многопользовательский режим с индивидуальными настройками.

## Используемые технологии
- Python 3.10+, aiogram 3.x
- IMAP4 SSL / SMTP с TLS
- python-docx для отчетов
- Requests для API TrueTabs
- Логгирование и уведомления об ошибках
