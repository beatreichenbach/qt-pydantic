from typing import Annotated

from qtpy import QtCore, QtGui

from . import annotations

# QtCore

QSize = Annotated[QtCore.QSize, annotations.QSize]
QSizeF = Annotated[QtCore.QSizeF, annotations.QSizeF]
QPoint = Annotated[QtCore.QPoint, annotations.QPoint]
QPointF = Annotated[QtCore.QPointF, annotations.QPointF]
QRect = Annotated[QtCore.QRect, annotations.QRect]
QRectF = Annotated[QtCore.QRectF, annotations.QRectF]
QDate = Annotated[QtCore.QDate, annotations.QDate]
QDateTime = Annotated[QtCore.QDateTime, annotations.QDateTime]
QTime = Annotated[QtCore.QTime, annotations.QTime]
QUuid = Annotated[QtCore.QUuid, annotations.QUuid]

# QtGui

QColor = Annotated[QtGui.QColor, annotations.QColor]
