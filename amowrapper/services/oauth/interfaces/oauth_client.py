from abc import ABC, abstractmethod
from typing import Optional, Dict


class IOAuthClient(ABC):
    """
    Интерфейс для OAuth клиента, который предоставляет методы для работы с AmoCRM.
    """

    @abstractmethod
    def __init__(self,
                 client_id: str,
                 client_secret: str,
                 redirect_uri: str,
                 subdomain: Optional[str] = None,
                 segment: Optional[str] = None,
                 debug: Optional[bool] = True):
        """
        Конструктор OAuth клиента.

        :param client_id: Идентификатор клиента (client_id).
        :param client_secret: Секрет клиента (client_secret).
        :param redirect_uri: URI для перенаправления после авторизации.
        :param subdomain: Поддомен для работы с AmoCRM.
        :param segment: Сегмент данных для работы.
        :param debug: Включение или отключение режима отладки. По умолчанию True.
        """
        pass

    @property
    @abstractmethod
    def subdomain(self) -> Optional[str]:
        """
        Геттер для subdomain.
        :return: Поддомен.
        """
        pass

    @subdomain.setter
    @abstractmethod
    def subdomain(self, value: str) -> None:
        """
        Сеттер для subdomain.
        :param value: Новый поддомен.
        """
        pass

    @property
    @abstractmethod
    def segment(self) -> Optional[str]:
        """
        Геттер для segment.
        :return: Сегмент.
        """
        pass

    @segment.setter
    @abstractmethod
    def segment(self, value: str) -> None:
        """
        Сеттер для segment.
        :param value: Новый сегмент.
        """
        pass


    @abstractmethod
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
        pass
