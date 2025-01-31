import requests
from typing import Optional, Dict
from loguru import logger
from amowrapper.services.oauth.interfaces.oauth_request import IBaseRequest
from amowrapper import __version__


class BaseRequest(IBaseRequest):
    """
    Базовый класс для выполнения HTTP-запросов с логированием.
    """

    __IDENTIFIER = f'API Chats Library v{__version__} by Timur Medvedev (git@github.com:tmedvedevv/amowrapper.git)'

    @classmethod
    def _request(cls, url: str, method: str, headers: Dict[str, str], data: Optional[Dict[str, str]] = None) -> requests.Response:
        """
        Выполняет HTTP-запрос с логированием.

        :param url: URL для запроса.
        :param method: HTTP метод (например, GET, POST, PUT, DELETE).
        :param headers: Заголовки запроса.
        :param data: Данные для отправки в запросе (опционально).
        :return: Ответ от сервера.
        """
        logger.debug(f'Trying request: {method} {url}')
        headers.update({'User-Agent': cls.__IDENTIFIER})

        try:
            response = cls._send_request(method=method, url=url, headers=headers, data=data)
            if response.status_code != requests.codes.ok:
                logger.critical(f'{response.reason}: {method} {url} {response.status_code}\nPayload: {data}\nResponse: {response.content}')
            else:
                logger.debug(f'{response.reason}')
                return response.json()
        except Exception as e:
            raise Exception(f"Critical Error: {e}")

    @classmethod
    def _send_request(cls, method: str, url: str, headers: Dict[str, str], data: Optional[Dict[str, str]]) -> requests.Response:
        """
        Отправка HTTP запроса в зависимости от метода.

        :param method: HTTP метод (например, GET, POST, PUT, DELETE).
        :param url: URL для запроса.
        :param headers: Заголовки запроса.
        :param data: Данные для отправки в запросе (опционально).
        :return: Ответ от сервера.
        """
        method_map = {
            "GET": requests.get,
            "POST": requests.post,
            "PATCH": requests.patch,
            "PUT": requests.put,
            "DELETE": requests.delete
        }

        if method not in method_map:
            raise ValueError(f"Unsupported HTTP method: {method}")

        return method_map[method](url, headers=headers, json=data)