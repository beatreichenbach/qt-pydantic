from pydantic import BaseModel
from PySide6 import QtCore, QtGui

from qt_pydantic import QColor, QDate, QSize


class Settings(BaseModel):
    size: QSize
    date: QDate
    color: QColor


def main() -> None:
    json_data = '{"size": [720, 480], "date": "2021-01-01", "color": [255, 95, 135]}'
    settings = Settings.model_validate_json(json_data)

    assert isinstance(settings.size, QtCore.QSize)
    assert isinstance(settings.date, QtCore.QDate)
    assert isinstance(settings.color, QtGui.QColor)

    print(settings.model_dump_json(indent=2))


if __name__ == '__main__':
    main()
