[![Build Status](https://travis-ci.org/wallee-payment/python-sdk.svg?branch=master)](https://travis-ci.org/wallee-payment/python-sdk)

# wallee Python Library

The wallee Python library wraps around the wallee API. This library facilitates your interaction with various services such as transactions, accounts, subscriptions.

## Documentation

[wallee Web Service API](https://app-wallee.com/doc/api/web-service)

## Requirements

- Python 3.4+

## Installation

### pip install (recommended)
```sh
pip install --upgrade wallee
```

### pip install from source via github

```sh
pip install git+http://github.com/wallee-payment/python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+http://github.com/wallee-payment/python-sdk.git` )

### install from source via Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install
```
(or `sudo python setup.py install` to install the package for all users)

## Usage
The library needs to be configured with your account's space id, user id, and secret key which are available in your [wallee
account dashboard](https://app-wallee.com/account/select). Set `space_id`, `user_id`, and `api_secret` to their values:

### Configuring a Client

```python
from wallee import Configuration, ApiClient

space_id = 405

api_client = ApiClient(configuration=Configuration(
    user_id=512,
    api_secret='FKrO76r5VwJtBrqZawBspljbBNOxp5veKQQkOnZxucQ='
))

```

To get stated with sending transactions you can review the example below:

```python
from wallee import Configuration, ApiClient
from wallee.api import TransactionService
from wallee.models import LineItem, LineItemType, TransactionCreate

space_id = 405

api_client = ApiClient(configuration=Configuration(
    user_id=512,
    api_secret='FKrO76r5VwJtBrqZawBspljbBNOxp5veKQQkOnZxucQ='
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

## License

Please see the [license file](LICENSE) for more information.