class UrlPatterns:
    """Класс с константами для работы с API Kommo."""

    @staticmethod
    def V4_BASE_URL() -> str:
        """Генерация базового URL для Kommo API."""
        return f'https://kommo.com'

    @staticmethod
    def MAKE_V4_ENDPOINT(base_url: str, endpoint: str) -> str:
        return f'{base_url}/{endpoint}'

    @staticmethod
    def MAKE_AMOJO_ENDPOINT(base_url: str, endpoint: str) -> str:
        """Генерация URL для API Amojo (пока не реализовано)."""
        return f'{base_url}/amojo/{endpoint}'  # Пример реализации, зависит от дальнейших деталей

    @staticmethod
    def MAKE_DRIVE_ENDPOINT(base_url: str, endpoint: str) -> str:
        """Генерация URL для API Drive (пока не реализовано)."""
        return f'{base_url}/drive/{endpoint}'  # Пример реализации, зависит от дальнейших деталей
