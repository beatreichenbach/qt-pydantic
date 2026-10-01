import datetime
from collections.abc import Sequence
from typing import Any, Generic, TypeVar, cast

from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema
from qtpy import QtCore, QtGui

QType = TypeVar('QType')


class QAnnotation(Generic[QType]):
    qtype: type[Any]
    schema: core_schema.CoreSchema

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: object,
        _handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        chain_schema = core_schema.chain_schema(
            [cls.schema, core_schema.no_info_plain_validator_function(cls.validate)]
        )
        python_schema = core_schema.union_schema(
            [core_schema.is_instance_schema(cls.qtype), chain_schema]
        )
        serialization = core_schema.plain_serializer_function_ser_schema(cls.serialize)
        return core_schema.json_or_python_schema(
            json_schema=chain_schema,
            python_schema=python_schema,
            serialization=serialization,
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls, _core_schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        return handler(cls.schema)

    @classmethod
    def validate(cls, value: Any) -> QType:  # noqa: ANN401
        if isinstance(value, Sequence) and not isinstance(value, str):
            return cls.qtype(*value)
        return cls.qtype(value)

    @staticmethod
    def serialize(value: QType) -> object:
        raise NotImplementedError


# QtCore


class QSize(QAnnotation[QtCore.QSize]):
    qtype = QtCore.QSize
    schema = core_schema.tuple_schema([core_schema.int_schema()] * 2)

    @staticmethod
    def serialize(value: QtCore.QSize) -> tuple[int, int]:
        return value.width(), value.height()


class QSizeF(QAnnotation[QtCore.QSizeF]):
    qtype = QtCore.QSizeF
    schema = core_schema.tuple_schema([core_schema.float_schema()] * 2)

    @staticmethod
    def serialize(value: QtCore.QSizeF) -> tuple[float, float]:
        return value.width(), value.height()


class QPoint(QAnnotation[QtCore.QPoint]):
    qtype = QtCore.QPoint
    schema = core_schema.tuple_schema([core_schema.int_schema()] * 2)

    @staticmethod
    def serialize(value: QtCore.QPoint) -> tuple[int, int]:
        return value.x(), value.y()


class QPointF(QAnnotation[QtCore.QPointF]):
    qtype = QtCore.QPointF
    schema = core_schema.tuple_schema([core_schema.float_schema()] * 2)

    @staticmethod
    def serialize(value: QtCore.QPointF) -> tuple[float, float]:
        return value.x(), value.y()


class QRect(QAnnotation[QtCore.QRect]):
    qtype = QtCore.QRect
    schema = core_schema.tuple_schema([core_schema.int_schema()] * 4)

    @staticmethod
    def serialize(value: QtCore.QRect) -> tuple[int, int, int, int]:
        return value.x(), value.y(), value.width(), value.height()


class QRectF(QAnnotation[QtCore.QRectF]):
    qtype = QtCore.QRectF
    schema = core_schema.tuple_schema([core_schema.float_schema()] * 4)

    @staticmethod
    def serialize(value: QtCore.QRectF) -> tuple[float, float, float, float]:
        return value.x(), value.y(), value.width(), value.height()


class QDate(QAnnotation[QtCore.QDate]):
    qtype = QtCore.QDate
    schema = core_schema.date_schema()

    @classmethod
    def validate(cls, value: datetime.date) -> QtCore.QDate:
        return cls.qtype(value.year, value.month, value.day)

    @staticmethod
    def serialize(value: QtCore.QDate) -> str:
        return value.toString(QtCore.Qt.DateFormat.ISODate)


class QDateTime(QAnnotation[QtCore.QDateTime]):
    qtype = QtCore.QDateTime
    schema = core_schema.datetime_schema()

    @classmethod
    def validate(cls, value: datetime.datetime) -> QtCore.QDateTime:
        msecs = int(value.timestamp() * 1000)
        return cls.qtype.fromMSecsSinceEpoch(msecs)

    @staticmethod
    def serialize(value: QtCore.QDateTime) -> str:
        return value.toString(QtCore.Qt.DateFormat.ISODate)


class QTime(QAnnotation[QtCore.QTime]):
    qtype = QtCore.QTime
    schema = core_schema.time_schema()

    @classmethod
    def validate(cls, value: datetime.time) -> QtCore.QTime:
        return cls.qtype(
            value.hour, value.minute, value.second, value.microsecond // 1000
        )

    @staticmethod
    def serialize(value: QtCore.QTime) -> str:
        return value.toString(QtCore.Qt.DateFormat.ISODate)


class QUuid(QAnnotation[QtCore.QUuid]):
    qtype = QtCore.QUuid
    schema = core_schema.str_schema()

    @staticmethod
    def serialize(value: QtCore.QUuid) -> str:
        return value.toString()


# QColor


class QColor(QAnnotation[QtGui.QColor]):
    qtype = QtGui.QColor
    schema = core_schema.union_schema(
        [
            # name
            core_schema.str_schema(),
            # rgb(a)
            core_schema.tuple_schema(
                [core_schema.int_schema(ge=0, le=255)],
                variadic_item_index=0,
                min_length=3,
                max_length=4,
            ),
        ]
    )

    @staticmethod
    def serialize(value: QtGui.QColor) -> tuple[int, int, int, int]:
        return cast(tuple[int, int, int, int], value.getRgb())
