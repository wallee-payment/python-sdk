# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionLedgerEntryCreate:

    swagger_types = {
    
        'amount_including_tax': 'float',
        'component_reference_name': 'str',
        'external_id': 'str',
        'quantity': 'float',
        'subscription_metric_id': 'int',
        'subscription_version': 'int',
        'taxes': 'list[TaxCreate]',
        'title': 'str',
    }

    attribute_map = {
        'amount_including_tax': 'amountIncludingTax','component_reference_name': 'componentReferenceName','external_id': 'externalId','quantity': 'quantity','subscription_metric_id': 'subscriptionMetricId','subscription_version': 'subscriptionVersion','taxes': 'taxes','title': 'title',
    }

    
    _amount_including_tax = None
    _component_reference_name = None
    _external_id = None
    _quantity = None
    _subscription_metric_id = None
    _subscription_version = None
    _taxes = None
    _title = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.amount_including_tax = kwargs.get('amount_including_tax')

        self.component_reference_name = kwargs.get('component_reference_name', None)
        self.external_id = kwargs.get('external_id')

        self.quantity = kwargs.get('quantity')

        self.subscription_metric_id = kwargs.get('subscription_metric_id', None)
        self.subscription_version = kwargs.get('subscription_version')

        self.taxes = kwargs.get('taxes', None)
        self.title = kwargs.get('title')

        

    
    @property
    def amount_including_tax(self):
        """Gets the amount_including_tax of this SubscriptionLedgerEntryCreate.

            The leger entry's amount with discounts applied, including taxes.

        :return: The amount_including_tax of this SubscriptionLedgerEntryCreate.
        :rtype: float
        """
        return self._amount_including_tax

    @amount_including_tax.setter
    def amount_including_tax(self, amount_including_tax):
        """Sets the amount_including_tax of this SubscriptionLedgerEntryCreate.

            The leger entry's amount with discounts applied, including taxes.

        :param amount_including_tax: The amount_including_tax of this SubscriptionLedgerEntryCreate.
        :type: float
        """
        if amount_including_tax is None:
            raise ValueError("Invalid value for `amount_including_tax`, must not be `None`")

        self._amount_including_tax = amount_including_tax
    
    @property
    def component_reference_name(self):
        """Gets the component_reference_name of this SubscriptionLedgerEntryCreate.

            

        :return: The component_reference_name of this SubscriptionLedgerEntryCreate.
        :rtype: str
        """
        return self._component_reference_name

    @component_reference_name.setter
    def component_reference_name(self, component_reference_name):
        """Sets the component_reference_name of this SubscriptionLedgerEntryCreate.

            

        :param component_reference_name: The component_reference_name of this SubscriptionLedgerEntryCreate.
        :type: str
        """

        self._component_reference_name = component_reference_name
    
    @property
    def external_id(self):
        """Gets the external_id of this SubscriptionLedgerEntryCreate.

            A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.

        :return: The external_id of this SubscriptionLedgerEntryCreate.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this SubscriptionLedgerEntryCreate.

            A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.

        :param external_id: The external_id of this SubscriptionLedgerEntryCreate.
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")

        self._external_id = external_id
    
    @property
    def quantity(self):
        """Gets the quantity of this SubscriptionLedgerEntryCreate.

            The number of items that were consumed.

        :return: The quantity of this SubscriptionLedgerEntryCreate.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this SubscriptionLedgerEntryCreate.

            The number of items that were consumed.

        :param quantity: The quantity of this SubscriptionLedgerEntryCreate.
        :type: float
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")

        self._quantity = quantity
    
    @property
    def subscription_metric_id(self):
        """Gets the subscription_metric_id of this SubscriptionLedgerEntryCreate.

            

        :return: The subscription_metric_id of this SubscriptionLedgerEntryCreate.
        :rtype: int
        """
        return self._subscription_metric_id

    @subscription_metric_id.setter
    def subscription_metric_id(self, subscription_metric_id):
        """Sets the subscription_metric_id of this SubscriptionLedgerEntryCreate.

            

        :param subscription_metric_id: The subscription_metric_id of this SubscriptionLedgerEntryCreate.
        :type: int
        """

        self._subscription_metric_id = subscription_metric_id
    
    @property
    def subscription_version(self):
        """Gets the subscription_version of this SubscriptionLedgerEntryCreate.

            The subscription version that the ledger entry belongs to.

        :return: The subscription_version of this SubscriptionLedgerEntryCreate.
        :rtype: int
        """
        return self._subscription_version

    @subscription_version.setter
    def subscription_version(self, subscription_version):
        """Sets the subscription_version of this SubscriptionLedgerEntryCreate.

            The subscription version that the ledger entry belongs to.

        :param subscription_version: The subscription_version of this SubscriptionLedgerEntryCreate.
        :type: int
        """
        if subscription_version is None:
            raise ValueError("Invalid value for `subscription_version`, must not be `None`")

        self._subscription_version = subscription_version
    
    @property
    def taxes(self):
        """Gets the taxes of this SubscriptionLedgerEntryCreate.

            A set of tax lines, each of which specifies a tax applied to the ledger entry.

        :return: The taxes of this SubscriptionLedgerEntryCreate.
        :rtype: list[TaxCreate]
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """Sets the taxes of this SubscriptionLedgerEntryCreate.

            A set of tax lines, each of which specifies a tax applied to the ledger entry.

        :param taxes: The taxes of this SubscriptionLedgerEntryCreate.
        :type: list[TaxCreate]
        """

        self._taxes = taxes
    
    @property
    def title(self):
        """Gets the title of this SubscriptionLedgerEntryCreate.

            The title that indicates what the ledger entry is about.

        :return: The title of this SubscriptionLedgerEntryCreate.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SubscriptionLedgerEntryCreate.

            The title that indicates what the ledger entry is about.

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
