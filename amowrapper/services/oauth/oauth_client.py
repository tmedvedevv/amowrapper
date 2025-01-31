from typing import Optional, Dict
from amowrapper.services.oauth.oauth_request import BaseRequest
from amowrapper.services.oauth.interfaces.oauth_client import IOAuthClient


class OAuthClient(IOAuthClient):
    """
    Реализация OAuth клиента для работы с AmoCRM.
    """

    def __init__(self,
                 client_id: str,
                 client_secret: str,
                 redirect_uri: str,
                 subdomain: Optional[str] = None,
                 segment: Optional[str] = None,
                 debug: Optional[bool] = True):  # Добавляем параметр debug
        """
        Конструктор OAuth клиента.

        :param client_id: Идентификатор клиента (client_id).
        :param client_secret: Секрет клиента (client_secret).
        :param redirect_uri: URI для перенаправления после авторизации.
        :param subdomain: Поддомен для работы с AmoCRM.
        :param segment: Сегмент данных для работы.
        :param debug: Включение или отключение режима отладки. По умолчанию True.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

        # Инициализация остальных атрибутов
        self._subdomain = subdomain
        self._segment = segment
        self._debug = debug  # Добавление атрибута debug


    @property
    def subdomain(self) -> Optional[str]:
        """
        Геттер для subdomain.
        :return: Поддомен.
        """
        return self._subdomain

    @subdomain.setter
    def subdomain(self, value: str) -> None:
        """
        Сеттер для subdomain.
        Проверка правильности или валидации значения перед установкой.
        :param value: Новый поддомен.
        """
        if not value:
            raise ValueError("Subdomain cannot be empty.")
        self._subdomain = value

    @property
    def segment(self) -> Optional[str]:
        """
        Геттер для segment.
        :return: Сегмент.
        """
        return self._segment

    @segment.setter
    def segment(self, value: str) -> None:
        """
        Сеттер для segment.
        Проверка правильности или валидации значения перед установкой.
        :param value: Новый сегмент.
        """
        if not value:
            raise ValueError("Segment cannot be empty.")
        self._segment = value

    def webhook_callback(self): # получение токена по коду авторизации
        pass

    def refresh_tokens(self): # получение
        pass

    def request(self,
                method: str = 'GET',
                url: Optional[str] = None,
                data: Optional[Dict] = None,
                content_type: str = 'application/json',
                access_token: Optional[str] = None) -> Dict:
        """
        Выполняет запрос с использованием переданных параметров.

        :param method: HTTP метод, по умолчанию 'GET'.
        :param url: URL для запроса.
        :param data: Данные, которые будут отправлены в теле запроса.
        :param content_type: Тип содержимого для запроса, по умолчанию 'application/json'.
        :param access_token: Токен авторизации.
        :return: Ответ от сервера.
        """
        if not url:
            raise ValueError("URL is required to perform the request.")
        if not access_token:
            raise ValueError("Access token is required.")

        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': content_type
        }

        return BaseRequest._request(url=url, method=method, headers=headers, data=data)
