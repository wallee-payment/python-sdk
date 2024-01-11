[![Build Status](https://travis-ci.org/wallee-payment/python-sdk.svg?branch=master)](https://travis-ci.org/wallee-payment/python-sdk)

# wallee Python SDK

Python SDK to access wallee web services API.

Library facilitates your interaction with various services such as transactions, accounts, and subscriptions.

## API documentation

[wallee Web Service API](https://app-wallee.com/doc/api/web-service)

## Requirements

- Python 3.7+

## Installation

### pip3 install (recommended)
```sh
pip3 install --upgrade wallee
```

### pip3 install from source via github

```sh
pip3 install git+http://github.com/wallee-payment/python-sdk.git
```
(you may need to run `pip3` with root permission: `sudo pip3 install git+http://github.com/wallee-payment/python-sdk.git` )

### install from source via Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
pip3 install setuptools

python setup.py install
```
(or `sudo python setup.py install` to install the package for all users)

## Usage
The library needs to be configured with your account's space id, user id, and secret key which are available in your [wallee
account dashboard](https://app-wallee.com/account/select). Set `space_id`, `user_id`, and `api_secret` to their values.
You can also optionally set `default_headers` to set some headers that will be sent to all requests

### Configuring a Service

```python
from wallee import Configuration
from wallee.api import TransactionServiceApi, TransactionPaymentPageServiceApi
from wallee.models import LineItem, LineItemType, TransactionCreate

space_id = 405

# default_headers is an optional param, that represents headers sent to all requests
config = Configuration(
    user_id=512,
    api_secret='FKrO76r5VwJtBrqZawBspljbBNOxp5veKQQkOnZxucQ=',
    default_headers={'x-meta-custom-header': 'value-1', 'x-meta-custom-header-2': 'value-2'},
    # set a custom request timeout if needed. (If not set, then the default value is: 25 seconds)
    request_timeout = 30
)

transaction_service = TransactionServiceApi(configuration=config)
transaction_payment_page_service = TransactionPaymentPageServiceApi(configuration=config)

```

To get started with sending transactions, please review the example below:

```python
from wallee import Configuration
from wallee.api import TransactionServiceApi, TransactionPaymentPageServiceApi
from wallee.models import LineItem, LineItemType, TransactionCreate

space_id = 405

config = Configuration(
    user_id=512,
    api_secret='FKrO76r5VwJtBrqZawBspljbBNOxp5veKQQkOnZxucQ=',
    # set a custom request timeout if needed. (If not set, then the default value is: 25 seconds)
    request_timeout = 30
)

transaction_service = TransactionServiceApi(configuration=config)
transaction_payment_page_service = TransactionPaymentPageServiceApi(configuration=config)

# create line item
line_item = LineItem(
    name='Red T-Shirt',
    unique_id='5412',
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

transaction_create = transaction_service.create(space_id=space_id, transaction=transaction)
payment_page_url = transaction_payment_page_service.payment_page_url(space_id=space_id, id=transaction_create.id)
# redirect your customer to this payment_page_url
```


## License

Please see the [license file](https://github.com/wallee-payment/python-sdk/blob/master/LICENSE) for more information.