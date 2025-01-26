from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from qtpy import QtCore, QtGui
from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema


class QAnnotation:
    qtype: type
    schema: core_schema.CoreSchema

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
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
    def validate(cls, value: Any) -> QAnnotation.qtype:
        if isinstance(value, Sequence) and not isinstance(value, str):
            return cls.qtype(*value)
        return cls.qtype(value)

    @staticmethod
    def serialize(value: Any) -> Any: ...


# QtCore


class QSize(QAnnotation):
    qtype = QtCore.QSize
    schema = core_schema.tuple_schema([core_schema.int_schema()] * 2)

    @staticmethod
    def serialize(value: Any) -> Any:
        return value.width(), value.height()


class QSizeF(QSize):
    qtype = QtCore.QSizeF
    schema = core_schema.tuple_schema([core_schema.float_schema()] * 2)


class QPoint(QAnnotation):
    qtype = QtCore.QPoint
    schema = core_schema.tuple_schema([core_schema.int_schema()] * 2)

    @staticmethod
    def serialize(value: Any) -> Any:
        return value.x(), value.y()


class QPointF(QPoint):
    qtype = QtCore.QPointF
    schema = core_schema.tuple_schema([core_schema.float_schema()] * 2)


class QRect(QAnnotation):
    qtype = QtCore.QRect
    schema = core_schema.tuple_schema([core_schema.int_schema()] * 4)

    @staticmethod
    def serialize(value: Any) -> Any:
        return value.x(), value.y(), value.width(), value.height()


class QRectF(QRect):
    qtype = QtCore.QRectF
    schema = core_schema.tuple_schema([core_schema.float_schema()] * 4)


class QDate(QAnnotation):
    qtype = QtCore.QDate
    schema = core_schema.date_schema()

    @classmethod
    def validate(cls, value: Any) -> QAnnotation.qtype:
        return cls.qtype(value.year, value.month, value.day)

    @staticmethod
    def serialize(value: Any) -> Any:
        return value.toString(QtCore.Qt.DateFormat.ISODate)


class QDateTime(QAnnotation):
    qtype = QtCore.QDateTime
    schema = core_schema.datetime_schema()

    @classmethod
    def validate(cls, value: Any) -> QAnnotation.qtype:
        msecs = int(value.timestamp() * 1000)
        return cls.qtype.fromMSecsSinceEpoch(msecs)

    @staticmethod
    def serialize(value: Any) -> Any:
        return value.toString(QtCore.Qt.DateFormat.ISODate)


class QTime(QAnnotation):
    qtype = QtCore.QTime
    schema = core_schema.time_schema()

    @classmethod
    def validate(cls, value: Any) -> QAnnotation.qtype:
        return cls.qtype(
            value.hour, value.minute, value.second, value.microsecond // 1000
        )

    @staticmethod
    def serialize(value: Any) -> Any:
        return value.toString(QtCore.Qt.DateFormat.ISODate)


class QUuid(QAnnotation):
    qtype = QtCore.QUuid
    schema = core_schema.str_schema()

    @staticmethod
    def serialize(value: Any) -> Any:
        return value.toString()


# QColor


class QColor(QAnnotation):
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
    def serialize(value: Any) -> Any:
        return value.getRgb()
