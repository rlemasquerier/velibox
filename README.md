# Velibox

## Raspberry app

### Requirements

- Python 2.7
- pipenv: `pip install --user pipenv`

### Install

#### Install Dependencies
```bash
pipenv install
```
#### Configure project

Get the name of the serial port on which is plugged your Arduino board:
```
ls /dev/tty*
```

Use it to configure the serial used inapp code:
```python
ser = serial.Serial('/dev/tty.<nameOfSerialPort>', 9600, timeout=1)
```

### Run the app

```bash
pipenv run python app.py
```

## Arduino board
