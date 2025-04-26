import pytest
import asyncio
from bot import (
    load_user_states,
    save_user_states,
    check_email_settings,
    send_email,
    get_deadlines,
    check_deadline,
    check_new_email,
    check_candidates_status
)

# Тесты для работы с состояниями пользователей
@pytest.mark.asyncio
async def test_user_states():
    """Тестирование загрузки и сохранения состояний пользователей"""
    test_states = {
        "123": {
            "access": True,
            "email": "test@example.com",
            "email_password": "password",
            "smtp_server": "smtp.example.com",
            "smtp_port": 587,
            "last_reminders": {}
        }
    }
    
    # Сохраняем тестовые данные
    save_user_states(test_states)
    
    # Загружаем и проверяем
    loaded_states = load_user_states()
    assert loaded_states == test_states

# Тесты для проверки настроек почты
@pytest.mark.asyncio
async def test_email_settings():
    """Тестирование проверки настроек почты"""
    user_id = "123"
    success, message = await check_email_settings(user_id)
    assert isinstance(success, bool)
    assert isinstance(message, str)

# Тесты для работы с API TrueTabs
@pytest.mark.asyncio
async def test_get_deadlines():
    """Тестирование получения дедлайнов из TrueTabs"""
    deadlines = await get_deadlines()
    assert isinstance(deadlines, list)

# Тесты для проверки дедлайнов
@pytest.mark.asyncio
async def test_check_deadline():
    """Тестирование проверки дедлайнов"""
    await check_deadline()
    # Проверяем, что функция выполнилась без ошибок

# Тесты для проверки новых писем
@pytest.mark.asyncio
async def test_check_new_email():
    """Тестирование проверки новых писем"""
    await check_new_email()
    # Проверяем, что функция выполнилась без ошибок

# Тесты для проверки статуса кандидатов
@pytest.mark.asyncio
async def test_check_candidates_status():
    """Тестирование проверки статуса кандидатов"""
    await check_candidates_status()
    # Проверяем, что функция выполнилась без ошибок

# Тесты для отправки email
@pytest.mark.asyncio
async def test_send_email():
    """Тестирование отправки email"""
    result = await send_email(
        to_email="test@example.com",
        subject="Test",
        body="Test message",
        user_id="123"
    )
    assert isinstance(result, bool)

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
