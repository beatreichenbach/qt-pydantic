from PySide6 import QtCore, QtGui
from pydantic import BaseModel
from qt_pydantic import (
    QSize,
    QSizeF,
    QPoint,
    QPointF,
    QRect,
    QRectF,
    QDate,
    QDateTime,
    QTime,
    QUuid,
    QColor,
)


class Settings(BaseModel):
    size: QSize
    sizef: QSizeF
    point: QPoint
    pointf: QPointF
    rect: QRect
    rectf: QRectF
    date: QDate
    date_time: QDateTime
    time: QTime
    uuid: QUuid
    color: QColor


def test_model() -> None:
    settings = Settings(
        size=QtCore.QSize(720, 480),
        sizef=QtCore.QSizeF(-2.34, 3),
        point=QtCore.QPoint(-2, 3),
        pointf=QtCore.QPointF(-2.34, 3),
        rect=QtCore.QRect(-2, 3, -1, -4),
        rectf=QtCore.QRectF(-2.34, 3, -1.2, -3.4),
        date=QtCore.QDate(2021, 1, 1),
        date_time=QtCore.QDateTime(QtCore.QDate(2032, 4, 23), QtCore.QTime(10, 20, 30)),
        time=QtCore.QTime(4, 8, 16),
        uuid=QtCore.QUuid('{9a619ea5-038c-42db-8845-3a33ea55887d}'),
        color=QtGui.QColor(255, 95, 135),
    )
    json_data = settings.model_dump_json(indent=2)

    expected = Settings.model_validate_json(json_data)
    assert settings == expected
