# qt-pydantic

[![PyPI version](https://img.shields.io/pypi/v/qt-pydantic.svg)](https://pypi.org/project/qt-pydantic/)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://pypi.org/project/qt-pydantic/)
[![License](https://img.shields.io/pypi/l/qt-pydantic.svg)](https://github.com/beatreichenbach/qt-pydantic/blob/main/LICENSE)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![ty](https://img.shields.io/badge/type%20checked-ty-261230.svg)](https://github.com/astral-sh/ty)

The `qt-pydantic` package adds support for Qt types in Pydantic BaseModels.
Using these annotations allows for easy serialization and deserialization of Qt types.

## Installation

Install using pip:

```shell
pip install qt-pydantic
```

## Usage

```python
from PySide6 import QtCore, QtGui
from pydantic import BaseModel
from qt_pydantic import QSize, QColor, QDate


# Define a model with Qt types
class Settings(BaseModel):
    size: QSize
    date: QDate
    color: QColor


# Parse json string into model
json_data = '{"size": [720, 480], "date": "2021-01-01", "color": [255, 95, 135]}'
settings = Settings.model_validate_json(json_data)

# Model types are actual Qt types
assert isinstance(settings.size, QtCore.QSize)
assert isinstance(settings.date, QtCore.QDate)
assert isinstance(settings.color, QtGui.QColor)

# Turn model into json string
data = settings.model_dump_json(indent=2)
```

## Contributing

To contribute please refer to the [Contributing Guide](CONTRIBUTING.md).

## License

MIT License. Copyright 2026 - Beat Reichenbach. Seef the [License file](LICENSE) for details.
