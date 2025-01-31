# 🛠️ **amowrapper** - Python Library for amoCRM OAuth Integration

amowrapper — это библиотека для интеграции с OAuth 2.0 системой amoCRM, предназначенная для упрощения процесса работы с API и аутентификации. С помощью этой библиотеки вы можете легко получить токены, авторизовать пользователей и работать с сервисами AmoCRM.

## 🚀 **Features**

- 🔑 Простая аутентификация с использованием OAuth 2.0
- 🛠️ Логирование всех запросов и ответов и возможность предоставить адекватные логи для поддержки
- 🖧 Обработка исключений для HTTP ошибок
- 🧩 Структура, соответствующая принципам SOLID и чистого кода

## 🛠️ **Installation**

Установить библиотеку можно с помощью pip:

```bash
pip install amowrapper
```

## 📝 Usage Example
Пример использования библиотеки для авторизации и получения токенов:
```python
from amowrapper.core.services.oauth.oauth_client import OAuthClient

# Инициализация клиента OAuth
client = OAuthClient(
    client_id="your_client_id",
    client_secret="your_client_secret",
    redirect_uri="your_redirect_uri",
    subdomain="your_subdomain",
    segment="your_segment"
)

# Получение токенов после callback
payload = {
    "referer": "subdomain",  # Пример значения из payload
    "value": "new_subdomain"
}
token = client.get_token_from_callback(payload)

# Установка субдомена через сеттер
client.subdomain = "new_subdomain"

print(f"Access Token: {token}")

```


⚙️ API Overview

OAuthClient
Класс для работы с OAuth 2.0 для AmoCRM.

Основные методы:
get_token_from_callback(payload: dict) -> dict[str, str]
Получает токен на основе данных из callback (например, из формы или хука).

subdomain
Геттер и сеттер для субдомена.

segment
Геттер и сеттер для сегмента.

🔒 Security
Необходимо внимательно хранить ваш client_id, client_secret, и токены. Рекомендуется использовать переменные окружения или другие безопасные способы хранения этих данных.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

📣 Contributing
We welcome contributions! If you find a bug or want to propose a new feature, please feel free to create an issue or submit a pull request.


