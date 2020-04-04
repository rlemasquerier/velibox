# Velibox

## Raspberry app

### Requirements

- Python 2.7
- pipenv: 
  ```bash
  pip install --user pipenv
  ```

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

### Install

#### Requirements

- Arduino board ATmega2560. Would work with other boards, but it may require some changes on the configuration
- Platformio
  ```bash
  curl -fsSL https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py -o get-platformio.py
  python3 get-platformio.py
  ```

### Electrical setup

TODO

### Flash the board

Test that the code compile with:

```bash
platformio run
```

Upload the code to Arduino board with:

```bash
platformio run --target upload
```
