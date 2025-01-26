from typing import Any
from pydantic import BaseModel, ValidationError
import pytest
from qtpy import QtCore, QtGui
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


# QSize
@pytest.mark.parametrize(
    'data,expected',
    [
        (QtCore.QSize(0, 1), '[0,1]'),
        (QtCore.QSize(-2, 3), '[-2,3]'),
        (QtCore.QSize(5, 0), '[5,0]'),
    ],
)
def test_qsize(data: Any, expected: QtCore.QSize | None) -> None:

    class Model(BaseModel):
        data: QSize

    model = Model(data=data)
    expected_string = f'{{"data":{expected}}}'
    assert model.model_dump_json() == expected_string


# QSizeF
@pytest.mark.parametrize(
    'data,expected',
    [
        (QtCore.QSizeF(0, 1.2), '[0.0,1.2]'),
        (QtCore.QSizeF(-2.34, 3), '[-2.34,3.0]'),
        (QtCore.QSizeF(5.1, 0.1), '[5.1,0.1]'),
    ],
)
def test_qsize(data: Any, expected: QtCore.QSizeF | None) -> None:

    class Model(BaseModel):
        data: QSizeF

    model = Model(data=data)
    expected_string = f'{{"data":{expected}}}'
    assert model.model_dump_json() == expected_string


# QPoint
@pytest.mark.parametrize(
    'data,expected',
    [
        (QtCore.QPoint(0, 1), '[0,1]'),
        (QtCore.QPoint(-2, 3), '[-2,3]'),
        (QtCore.QPoint(5, 0), '[5,0]'),
    ],
)
def test_qpoint(data: Any, expected: QtCore.QPoint | None) -> None:

    class Model(BaseModel):
        data: QPoint

    model = Model(data=data)
    expected_string = f'{{"data":{expected}}}'
    assert model.model_dump_json() == expected_string


# QPointF
@pytest.mark.parametrize(
    'data,expected',
    [
        (QtCore.QPointF(0, 1.2), '[0.0,1.2]'),
        (QtCore.QPointF(-2.34, 3), '[-2.34,3.0]'),
        (QtCore.QPointF(5.1, 0.1), '[5.1,0.1]'),
    ],
)
def test_qpointf(data: Any, expected: QtCore.QPointF | None) -> None:

    class Model(BaseModel):
        data: QPointF

    model = Model(data=data)
    expected_string = f'{{"data":{expected}}}'
    assert model.model_dump_json() == expected_string


# QRect
@pytest.mark.parametrize(
    'data,expected',
    [
        (QtCore.QRect(0, 1, 2, 3), '[0,1,2,3]'),
        (QtCore.QRect(-2, 3, -1, -4), '[-2,3,-1,-4]'),
        (QtCore.QRect(5, 0, 2, 3), '[5,0,2,3]'),
    ],
)
def test_qrect(data: Any, expected: QtCore.QRect | None) -> None:

    class Model(BaseModel):
        data: QRect

    model = Model(data=data)
    expected_string = f'{{"data":{expected}}}'
    assert model.model_dump_json() == expected_string


# QRectF
@pytest.mark.parametrize(
    'data,expected',
    [
        (QtCore.QRectF(0, 1.2, 2.3, 3.4), '[0.0,1.2,2.3,3.4]'),
        (QtCore.QRectF(-2.34, 3, -1.2, -3.4), '[-2.34,3.0,-1.2,-3.4]'),
        (QtCore.QRectF(5.1, 0.1, 0.0, -1.2), '[5.1,0.1,0.0,-1.2]'),
    ],
)
def test_qrectf(data: Any, expected: QtCore.QRectF | None) -> None:

    class Model(BaseModel):
        data: QRectF

    model = Model(data=data)
    expected_string = f'{{"data":{expected}}}'
    assert model.model_dump_json() == expected_string


# QDate
@pytest.mark.parametrize(
    'data,expected',
    [
        (QtCore.QDate(2000, 1, 5), '"2000-01-05"'),
        (QtCore.QDate(2023, 3, 24), '"2023-03-24"'),
    ],
)
def test_qdate(data: Any, expected: QtCore.QDate | None) -> None:

    class Model(BaseModel):
        data: QDate

    model = Model(data=data)
    expected_string = f'{{"data":{expected}}}'
    assert model.model_dump_json() == expected_string


# QDateTime
@pytest.mark.parametrize(
    'data,expected',
    [
        (
            QtCore.QDateTime(QtCore.QDate(2032, 4, 23), QtCore.QTime(10, 20, 30)),
            '"2032-04-23T10:20:30"',
        ),
        (
            QtCore.QDateTime(
                QtCore.QDate(2032, 4, 23),
                QtCore.QTime(10, 20, 30, 400),
                QtCore.QTimeZone((2 * 3600) + (30 * 60)),
            ),
            '"2032-04-23T10:20:30+02:30"',
        ),
    ],
)
def test_qdatetime(data: Any, expected: QtCore.QDateTime | None) -> None:

    class Model(BaseModel):
        data: QDateTime

    model = Model(data=data)
    expected_string = f'{{"data":{expected}}}'
    assert model.model_dump_json() == expected_string


# QTime
@pytest.mark.parametrize(
    'data,expected',
    [
        (QtCore.QTime(4, 8, 16), '"04:08:16"'),
    ],
)
def test_qtime(data: Any, expected: QtCore.QTime | None) -> None:

    class Model(BaseModel):
        data: QTime

    model = Model(data=data)
    expected_string = f'{{"data":{expected}}}'
    assert model.model_dump_json() == expected_string


# QUuid
@pytest.mark.parametrize(
    'data,expected',
    [
        (
            QtCore.QUuid('{9a619ea5-038c-42db-8845-3a33ea55887d}'),
            '"{9a619ea5-038c-42db-8845-3a33ea55887d}"',
        ),
    ],
)
def test_quuid(data: Any, expected: QtCore.QUuid | None) -> None:

    class Model(BaseModel):
        data: QUuid

    model = Model(data=data)
    expected_string = f'{{"data":{expected}}}'
    assert model.model_dump_json() == expected_string


# QColor
@pytest.mark.parametrize(
    'data,expected',
    [
        (QtGui.QColor('red'), '[255,0,0,255]'),
        (QtGui.QColor(12, 55, 127), '[12,55,127,255]'),
        (QtGui.QColor(12, 55, 127, 23), '[12,55,127,23]'),
    ],
)
def test_qcolor(data: Any, expected: QtGui.QColor | None) -> None:

    class Model(BaseModel):
        data: QColor

    model = Model(data=data)
    expected_string = f'{{"data":{expected}}}'
    assert model.model_dump_json() == expected_string
