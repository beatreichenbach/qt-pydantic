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
        ((0, 1), QtCore.QSize(0, 1)),
        ((-2, 3), QtCore.QSize(-2, 3)),
        ([5, 0], QtCore.QSize(5, 0)),
        ((0.8, 2.3), None),
        ((1, 2, 3), None),
    ],
)
def test_qsize(data: Any, expected: QtCore.QSize | None) -> None:

    class Model(BaseModel):
        data: QSize

    if expected:
        assert Model(data=data).data == expected
    else:
        with pytest.raises(ValidationError):
            assert Model(data=data).data == expected


# QSizeF
@pytest.mark.parametrize(
    'data,expected',
    [
        ((0.0, 1.2), QtCore.QSizeF(0, 1.2)),
        ((-2.34, 3), QtCore.QSizeF(-2.34, 3)),
        ([5.1, 0.1], QtCore.QSizeF(5.1, 0.1)),
        ((1.1, 2.1, 3.1), None),
    ],
)
def test_qsizef(data: Any, expected: QtCore.QSizeF | None) -> None:

    class Model(BaseModel):
        data: QSizeF

    if expected:
        assert Model(data=data).data == expected
    else:
        with pytest.raises(ValidationError):
            assert Model(data=data).data == expected


# QPoint
@pytest.mark.parametrize(
    'data,expected',
    [
        ((0, 1), QtCore.QPoint(0, 1)),
        ((-2, 3), QtCore.QPoint(-2, 3)),
        ([5, 0], QtCore.QPoint(5, 0)),
        ((0.8, 2.3), None),
        ((1, 2, 3), None),
    ],
)
def test_qpoint(data: Any, expected: QtCore.QPoint | None) -> None:

    class Model(BaseModel):
        data: QPoint

    if expected:
        assert Model(data=data).data == expected
    else:
        with pytest.raises(ValidationError):
            assert Model(data=data).data == expected


# QPointF
@pytest.mark.parametrize(
    'data,expected',
    [
        ((0.0, 1.2), QtCore.QPointF(0, 1.2)),
        ((-2.34, 3), QtCore.QPointF(-2.34, 3)),
        ([5.1, 0.1], QtCore.QPointF(5.1, 0.1)),
        ((1.1, 2.1, 3.1), None),
    ],
)
def test_qpointf(data: Any, expected: QtCore.QPointF | None) -> None:

    class Model(BaseModel):
        data: QPointF

    if expected:
        assert Model(data=data).data == expected
    else:
        with pytest.raises(ValidationError):
            assert Model(data=data).data == expected


# QRect
@pytest.mark.parametrize(
    'data,expected',
    [
        ((0, 1, 2, 3), QtCore.QRect(0, 1, 2, 3)),
        ((-2, 3, -1, -4), QtCore.QRect(-2, 3, -1, -4)),
        ([5, 0, 2, 3], QtCore.QRect(5, 0, 2, 3)),
        ((0.8, 2.3, 1.2, 3.4), None),
        ((1, 2, 3, 4, 5), None),
    ],
)
def test_qrect(data: Any, expected: QtCore.QRect | None) -> None:

    class Model(BaseModel):
        data: QRect

    if expected:
        assert Model(data=data).data == expected
    else:
        with pytest.raises(ValidationError):
            assert Model(data=data).data == expected


# QRectF
@pytest.mark.parametrize(
    'data,expected',
    [
        ((0.0, 1.2, 2.3, 3.4), QtCore.QRectF(0, 1.2, 2.3, 3.4)),
        ((-2.34, 3, -1.2, -3.4), QtCore.QRectF(-2.34, 3, -1.2, -3.4)),
        ([5.1, 0.1, 0.0, -1.2], QtCore.QRectF(5.1, 0.1, 0.0, -1.2)),
        ((1.1, 2.1, 3.1, 4.1, 5.1), None),
    ],
)
def test_qrectf(data: Any, expected: QtCore.QRectF | None) -> None:

    class Model(BaseModel):
        data: QRectF

    if expected:
        assert Model(data=data).data == expected
    else:
        with pytest.raises(ValidationError):
            assert Model(data=data).data == expected


# QDate
@pytest.mark.parametrize(
    'data,expected',
    [
        ('2000-01-05', QtCore.QDate(2000, 1, 5)),
        (1679616000.0, QtCore.QDate(2023, 3, 24)),
        ('2000-jan-05', None),
        ('2000-1-5', None),
    ],
)
def test_qdate(data: Any, expected: QtCore.QDate | None) -> None:

    class Model(BaseModel):
        data: QDate

    if expected:
        assert Model(data=data).data == expected
    else:
        with pytest.raises(ValidationError):
            assert Model(data=data).data == expected


# QDateTime
@pytest.mark.parametrize(
    'data,expected',
    [
        (
            '2032-04-23T10:20:30.400+02:30',
            QtCore.QDateTime(
                QtCore.QDate(2032, 4, 23),
                QtCore.QTime(10, 20, 30, 400),
                QtCore.QTimeZone((2 * 3600) + (30 * 60)),
            ),
        ),
        (
            '2032-04-23 10:20:30',
            QtCore.QDateTime(QtCore.QDate(2032, 4, 23), QtCore.QTime(10, 20, 30)),
        ),
        (
            '2032-04-23 10:20:30 UTC',
            None,
        ),
    ],
)
def test_qdatetime(data: Any, expected: QtCore.QDateTime | None) -> None:

    class Model(BaseModel):
        data: QDateTime

    if expected:
        assert Model(data=data).data == expected
    else:
        with pytest.raises(ValidationError):
            assert Model(data=data).data == expected


# QTime
@pytest.mark.parametrize(
    'data,expected',
    [
        ('04:08:16', QtCore.QTime(4, 8, 16)),
        ([4, 8, 16], None),
        ('4:8:16', None),
    ],
)
def test_qtime(data: Any, expected: QtCore.QTime | None) -> None:

    class Model(BaseModel):
        data: QTime

    if expected:
        assert Model(data=data).data == expected
    else:
        with pytest.raises(ValidationError):
            assert Model(data=data).data == expected


# QUuid
@pytest.mark.parametrize(
    'data,expected',
    [
        (
            '{9a619ea5-038c-42db-8845-3a33ea55887d}',
            QtCore.QUuid('{9a619ea5-038c-42db-8845-3a33ea55887d}'),
        ),
        (
            '9a619ea5-038c-42db-8845-3a33ea55887d',
            QtCore.QUuid('{9a619ea5-038c-42db-8845-3a33ea55887d}'),
        ),
        (
            '9a619ea5038c42db88453a33ea55887d',
            QtCore.QUuid('{00000000-0000-0000-0000-000000000000}'),
        ),
    ],
)
def test_quuid(data: Any, expected: QtCore.QUuid | None) -> None:

    class Model(BaseModel):
        data: QUuid

    if expected is None:
        with pytest.raises(ValidationError):
            assert Model(data=data).data == expected
    else:
        assert Model(data=data).data == expected


# QColor
@pytest.mark.parametrize(
    'data,expected',
    [
        ([12, 55, 255], QtGui.QColor(12, 55, 255)),
        ([0, 0, 0], QtGui.QColor(0, 0, 0)),
        ([12, 55, 255, 23], QtGui.QColor(12, 55, 255, 23)),
        ('red', QtGui.QColor('red')),
        ([-120, 55, 127], None),
        ([12, 55], None),
    ],
)
def test_qcolor(data: Any, expected: QtGui.QColor | None) -> None:

    class Model(BaseModel):
        data: QColor

    if expected:
        assert Model(data=data).data == expected
    else:
        with pytest.raises(ValidationError):
            assert Model(data=data).data == expected
