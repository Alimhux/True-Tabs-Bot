# Документация по структуре user_states.json

Файл `user_states.json` хранит состояния пользователей бота. Каждый пользователь идентифицируется по своему Telegram ID.

## Структура данных

```json
{
  "USER_ID": {
    "access": boolean,      // Флаг доступа к функциям бота
    "email": string,        // Email пользователя
    "email_password": string, // Пароль от email
    "smtp_server": string,  // SMTP сервер для отправки писем
    "smtp_port": number,    // Порт SMTP сервера
    "last_reminders": {     // История напоминаний
      "project_name": "timestamp" // Временная метка последнего напоминания
    }
  }
}
```

## Пример использования

```json
{
	"724312444": {
		"access": true,
		"email": "user@example.com",
		"email_password": "password123",
		"smtp_server": "smtp.example.com",
		"smtp_port": 587,
		"last_reminders": {
			"project1": "2024-03-20T12:00:00",
			"project2": "2024-03-21T15:30:00"
		}
	}
}
```

## Описание полей

- `access`: Булево значение, определяющее доступ пользователя к функциям бота
- `email`: Email адрес пользователя для отправки и получения писем
- `email_password`: Пароль от email (рекомендуется использовать пароль приложения)
- `smtp_server`: Адрес SMTP сервера для отправки писем
- `smtp_port`: Порт SMTP сервера (587 для TLS, 465 для SSL)
- `last_reminders`: Словарь с историей напоминаний по проектам
