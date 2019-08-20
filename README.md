[![Build Status](https://travis-ci.org/wallee-payment/python-sdk.svg?branch=master)](https://travis-ci.org/wallee-payment/python-sdk)

# wallee
Python SDK

## Requirements.

Python 3.2+

## Documentation

[https://app-wallee.com/doc/api/web-service](https://app-wallee.com/doc/api/web-service)

## Installation & Usage
### pip install

You can install directly from Github

```sh
pip install git@github.com:wallee-payment/python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git@github.com:wallee-payment/python-sdk.git` )

Then import the package:
```python
import wallee 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
cd to/package/directory
python setup.py install
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wallee
```

## Getting Started

Please follow the installation procedure and then run the following:

```python
from wallee import Configuration, ApiClient
from wallee.api import TransactionService
from wallee.models import LineItem, LineItemType, TransactionCreate

# Configure the client
space_id = 405
api_client = ApiClient(configuration=Configuration(
    user_id=512, # change this to your application, user's user_id
    api_secret='FKrO76r5VwJtBrqZawBspljbBNOxp5veKQQkOnZxucQ=' # change this to your application user's key
))

transaction_service = TransactionService(api_client=api_client)

# create line item
line_item = LineItem(
    name='Red T-Shirt',
    unique_id=5412,
    sku='red-t-shirt-123',
    quantity=1,
    amount_including_tax=29.95,
    type=LineItemType.PRODUCT
)

# create transaction model
transaction = TransactionCreate(
    line_items=[line_item],
    auto_confirmation_enabled=True,
    currency='EUR',
)

# send transaction to our API
transaction_create = transaction_service.create(space_id=space_id, transaction=transaction)

# redirect your customer to this url
redirect_url = transaction_service.build_payment_page_url(space_id=space_id, id=transaction_create.id)
print(redirect_url)

# get the state of the transaction
transaction_read = transaction_service.read(space_id=space_id, id=transaction_create.id)
print(transaction_read.state)
```