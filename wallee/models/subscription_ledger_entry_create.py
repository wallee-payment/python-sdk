# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionLedgerEntryCreate:

    swagger_types = {
    
        'amount_including_tax': 'float',
        'external_id': 'str',
        'quantity': 'float',
        'subscription_version': 'int',
        'taxes': 'list[TaxCreate]',
        'title': 'str',
    }

    attribute_map = {
        'amount_including_tax': 'amountIncludingTax','external_id': 'externalId','quantity': 'quantity','subscription_version': 'subscriptionVersion','taxes': 'taxes','title': 'title',
    }

    
    _amount_including_tax = None
    _external_id = None
    _quantity = None
    _subscription_version = None
    _taxes = None
    _title = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.amount_including_tax = kwargs.get('amount_including_tax')

        self.external_id = kwargs.get('external_id')

        self.quantity = kwargs.get('quantity')

        self.subscription_version = kwargs.get('subscription_version')

        self.taxes = kwargs.get('taxes', None)
        self.title = kwargs.get('title')

        

    
    @property
    def amount_including_tax(self):
        """Gets the amount_including_tax of this SubscriptionLedgerEntryCreate.

            

        :return: The amount_including_tax of this SubscriptionLedgerEntryCreate.
        :rtype: float
        """
        return self._amount_including_tax

    @amount_including_tax.setter
    def amount_including_tax(self, amount_including_tax):
        """Sets the amount_including_tax of this SubscriptionLedgerEntryCreate.

            

        :param amount_including_tax: The amount_including_tax of this SubscriptionLedgerEntryCreate.
        :type: float
        """
        if amount_including_tax is None:
            raise ValueError("Invalid value for `amount_including_tax`, must not be `None`")

        self._amount_including_tax = amount_including_tax
    
    @property
    def external_id(self):
        """Gets the external_id of this SubscriptionLedgerEntryCreate.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :return: The external_id of this SubscriptionLedgerEntryCreate.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this SubscriptionLedgerEntryCreate.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :param external_id: The external_id of this SubscriptionLedgerEntryCreate.
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")

        self._external_id = external_id
    
    @property
    def quantity(self):
        """Gets the quantity of this SubscriptionLedgerEntryCreate.

            

        :return: The quantity of this SubscriptionLedgerEntryCreate.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this SubscriptionLedgerEntryCreate.

            

        :param quantity: The quantity of this SubscriptionLedgerEntryCreate.
        :type: float
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")

        self._quantity = quantity
    
    @property
    def subscription_version(self):
        """Gets the subscription_version of this SubscriptionLedgerEntryCreate.

            

        :return: The subscription_version of this SubscriptionLedgerEntryCreate.
        :rtype: int
        """
        return self._subscription_version

    @subscription_version.setter
    def subscription_version(self, subscription_version):
        """Sets the subscription_version of this SubscriptionLedgerEntryCreate.

            

        :param subscription_version: The subscription_version of this SubscriptionLedgerEntryCreate.
        :type: int
        """
        if subscription_version is None:
            raise ValueError("Invalid value for `subscription_version`, must not be `None`")

        self._subscription_version = subscription_version
    
    @property
    def taxes(self):
        """Gets the taxes of this SubscriptionLedgerEntryCreate.

            

        :return: The taxes of this SubscriptionLedgerEntryCreate.
        :rtype: list[TaxCreate]
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """Sets the taxes of this SubscriptionLedgerEntryCreate.

            

        :param taxes: The taxes of this SubscriptionLedgerEntryCreate.
        :type: list[TaxCreate]
        """

        self._taxes = taxes
    
    @property
    def title(self):
        """Gets the title of this SubscriptionLedgerEntryCreate.

            

        :return: The title of this SubscriptionLedgerEntryCreate.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SubscriptionLedgerEntryCreate.

            

        :param title: The title of this SubscriptionLedgerEntryCreate.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")
        if title is not None and len(title) > 150:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `150`")
        if title is not None and len(title) < 1:
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")

        self._title = title
    

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            elif isinstance(value, Enum):
                result[attr] = value.value
            else:
                result[attr] = value
        if issubclass(SubscriptionLedgerEntryCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionLedgerEntryCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
