from abc import ABC, abstractmethod
from typing import Optional, Dict
import requests

class IBaseRequest(ABC):
    """
    Интерфейс для выполнения HTTP-запросов с логированием.
    """

    @classmethod
    @abstractmethod
    def request(self, url: str, method: str, headers: Dict[str, str],
                data: Optional[Dict[str, str]] = None) -> requests.Response:
        """
        Выполнение HTTP запроса.

        :param url: URL для запроса.
        :param method: HTTP метод (например, GET, POST, PUT, DELETE).
        :param headers: Заголовки запроса.
        :param data: Данные для отправки в запросе (опционально).
        :return: Ответ от сервера.
        """
        pass

    @abstractmethod
    def _send_request(self, method: str, url: str, headers: Dict[str, str],
                      data: Optional[Dict[str, str]]) -> requests.Response:
        """
        Отправка HTTP запроса в зависимости от метода.

        :param method: HTTP метод (например, GET, POST, PUT, DELETE).
        :param url: URL для запроса.
        :param headers: Заголовки запроса.
        :param data: Данные для отправки в запросе (опционально).
        :return: Ответ от сервера.
        """
        pass
