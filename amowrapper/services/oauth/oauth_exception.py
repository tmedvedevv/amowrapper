from typing import Optional, Dict, Any


class OAuthError(Exception):
    """Основная ошибка при взаимодействии с OAuth 2.0."""
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.details = details or {}


class OAuthTokenNotFoundError(OAuthError):
    """Ошибка при отсутствии токена."""


class OAuthAccessTokenExpired(OAuthError):
    """Ошибка при истечении срока действия токена."""


class OAuthInvalidRequestError(OAuthError):
    """Ошибка, возникающая при неправильном запросе к OAuth серверу."""
