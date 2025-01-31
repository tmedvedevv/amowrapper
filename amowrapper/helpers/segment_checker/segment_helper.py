from typing import Dict
from .const import KOMMO_V4_CONST, AMOCRM_V4_CONST
from .exceptions import UnknownSegmentError  # Предположим, что исключение находится в exceptions.py

class OAuthV4SegmentHelper:
    """Обработчик сегментов, отвечающий за выбор правильных константных классов для различных сегментов."""

    # Хранение констант в верхнем регистре
    SEGMENTS: Dict[str, object] = {
        'kommo': KOMMO_V4_CONST,
        'amocrm': AMOCRM_V4_CONST
    }

    @staticmethod
    def handle_from_hook(segment: str):
        """
        Получение константного класса для соответствующего сегмента.

        :param segment: строка, представляющая сегмент (например, 'kommo' или 'amocrm').
        :return: класс констант для соответствующего сегмента.
        :raises UnknownSegmentError: если сегмент не найден.
        """
        segment_constants = OAuthV4SegmentHelper.SEGMENTS.get(segment)

        if not segment_constants:
            raise UnknownSegmentError(message=f'Segment {segment} not found.')

        return segment_constants
