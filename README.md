# Affirmpy

A Python client lib for the Affirm API. Inspired by the project [affirm-ruby](https://github.com/reverbdotcom/affirm-ruby).

Developed on Python 2.7. <b>Should</b> work on Python 3 as well.

## Install

Add to your requirements.txt

```
Affirmpy
```
and pip install -r requirements.txt

Alternatively, install directly:

```
pip install Affirmpy
```

## Initialize

Set an initial client with credentials:

```python
from affirmpy.api import API

API.public_key = "WHEE"
API.secret_key = "WOOO"
API.api_url    = "https://www.idontknowwhatimdoing.com/"
```

## Charges

All API requests raise an ```
Error``` or subtype on failure.

Start with:
```python
from affirmpy.charge import Charge
```

### Creating Charges

```python
charge = Charge.create('token')
```

### Retrieving a Charge

```python
charge = Charge.retrieve('macklemore')
```

Raises `ResourceNotFoundError` if nonexistent charge.

### Capturing charges
