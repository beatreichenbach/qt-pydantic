# qt-pydantic

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

MIT License. Copyright 2024 - Beat Reichenbach.
See the [License file](LICENSE) for details.
