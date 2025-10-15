# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionProductVersionPending:

    swagger_types = {
    
        'id': 'int',
        'version': 'int',
        'billing_cycle': 'str',
        'comment': 'str',
        'default_currency': 'str',
        'enabled_currencies': 'list[str]',
        'minimal_number_of_periods': 'int',
        'name': 'dict(str, str)',
        'number_of_notice_periods': 'int',
        'product': 'int',
        'state': 'SubscriptionProductVersionState',
        'tax_calculation': 'TaxCalculation',
    }

    attribute_map = {
        'id': 'id','version': 'version','billing_cycle': 'billingCycle','comment': 'comment','default_currency': 'defaultCurrency','enabled_currencies': 'enabledCurrencies','minimal_number_of_periods': 'minimalNumberOfPeriods','name': 'name','number_of_notice_periods': 'numberOfNoticePeriods','product': 'product','state': 'state','tax_calculation': 'taxCalculation',
    }

    
    _id = None
    _version = None
    _billing_cycle = None
    _comment = None
    _default_currency = None
    _enabled_currencies = None
    _minimal_number_of_periods = None
    _name = None
    _number_of_notice_periods = None
    _product = None
    _state = None
    _tax_calculation = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id')

        self.version = kwargs.get('version')

        self.billing_cycle = kwargs.get('billing_cycle', None)
        self.comment = kwargs.get('comment', None)
        self.default_currency = kwargs.get('default_currency', None)
        self.enabled_currencies = kwargs.get('enabled_currencies', None)
        self.minimal_number_of_periods = kwargs.get('minimal_number_of_periods', None)
        self.name = kwargs.get('name', None)
        self.number_of_notice_periods = kwargs.get('number_of_notice_periods', None)
        self.product = kwargs.get('product', None)
        self.state = kwargs.get('state', None)
        self.tax_calculation = kwargs.get('tax_calculation', None)
        

    
    @property
    def id(self):
        """Gets the id of this SubscriptionProductVersionPending.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this SubscriptionProductVersionPending.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionProductVersionPending.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this SubscriptionProductVersionPending.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id
    
    @property
    def version(self):
        """Gets the version of this SubscriptionProductVersionPending.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this SubscriptionProductVersionPending.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SubscriptionProductVersionPending.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this SubscriptionProductVersionPending.
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")

        self._version = version
    
    @property
    def billing_cycle(self):
        """Gets the billing_cycle of this SubscriptionProductVersionPending.

            The recurring period of time, typically monthly or annually, for which a subscriber is charged.

        :return: The billing_cycle of this SubscriptionProductVersionPending.
        :rtype: str
        """
        return self._billing_cycle

    @billing_cycle.setter
    def billing_cycle(self, billing_cycle):
        """Sets the billing_cycle of this SubscriptionProductVersionPending.

            The recurring period of time, typically monthly or annually, for which a subscriber is charged.

        :param billing_cycle: The billing_cycle of this SubscriptionProductVersionPending.
        :type: str
        """

        self._billing_cycle = billing_cycle
    
    @property
    def comment(self):
        """Gets the comment of this SubscriptionProductVersionPending.

            A comment that describes the product version and why it was created. It is not disclosed to the subscriber.

        :return: The comment of this SubscriptionProductVersionPending.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this SubscriptionProductVersionPending.

            A comment that describes the product version and why it was created. It is not disclosed to the subscriber.

        :param comment: The comment of this SubscriptionProductVersionPending.
        :type: str
        """

        self._comment = comment
    
    @property
    def default_currency(self):
        """Gets the default_currency of this SubscriptionProductVersionPending.

            The three-letter code (ISO 4217 format) of the product version's default currency.

        :return: The default_currency of this SubscriptionProductVersionPending.
        :rtype: str
        """
        return self._default_currency

    @default_currency.setter
    def default_currency(self, default_currency):
        """Sets the default_currency of this SubscriptionProductVersionPending.

            The three-letter code (ISO 4217 format) of the product version's default currency.

        :param default_currency: The default_currency of this SubscriptionProductVersionPending.
        :type: str
        """

        self._default_currency = default_currency
    
    @property
    def enabled_currencies(self):
        """Gets the enabled_currencies of this SubscriptionProductVersionPending.

            The three-letter codes (ISO 4217 format) of the currencies that the product version supports.

        :return: The enabled_currencies of this SubscriptionProductVersionPending.
        :rtype: list[str]
        """
        return self._enabled_currencies

    @enabled_currencies.setter
    def enabled_currencies(self, enabled_currencies):
        """Sets the enabled_currencies of this SubscriptionProductVersionPending.

            The three-letter codes (ISO 4217 format) of the currencies that the product version supports.

        :param enabled_currencies: The enabled_currencies of this SubscriptionProductVersionPending.
        :type: list[str]
        """

        self._enabled_currencies = enabled_currencies
    
    @property
    def minimal_number_of_periods(self):
        """Gets the minimal_number_of_periods of this SubscriptionProductVersionPending.

            The minimum number of periods the subscription will run before it can be terminated.

        :return: The minimal_number_of_periods of this SubscriptionProductVersionPending.
        :rtype: int
        """
        return self._minimal_number_of_periods

    @minimal_number_of_periods.setter
    def minimal_number_of_periods(self, minimal_number_of_periods):
        """Sets the minimal_number_of_periods of this SubscriptionProductVersionPending.

            The minimum number of periods the subscription will run before it can be terminated.

        :param minimal_number_of_periods: The minimal_number_of_periods of this SubscriptionProductVersionPending.
        :type: int
        """

        self._minimal_number_of_periods = minimal_number_of_periods
    
    @property
    def name(self):
        """Gets the name of this SubscriptionProductVersionPending.

            The localized name of the product that is displayed to the customer.

        :return: The name of this SubscriptionProductVersionPending.
        :rtype: dict(str, str)
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionProductVersionPending.

            The localized name of the product that is displayed to the customer.

        :param name: The name of this SubscriptionProductVersionPending.
        :type: dict(str, str)
        """

        self._name = name
    
    @property
    def number_of_notice_periods(self):
        """Gets the number_of_notice_periods of this SubscriptionProductVersionPending.

            The number of periods the subscription will keep running after its termination was requested.

        :return: The number_of_notice_periods of this SubscriptionProductVersionPending.
        :rtype: int
        """
        return self._number_of_notice_periods

    @number_of_notice_periods.setter
    def number_of_notice_periods(self, number_of_notice_periods):
        """Sets the number_of_notice_periods of this SubscriptionProductVersionPending.

            The number of periods the subscription will keep running after its termination was requested.

        :param number_of_notice_periods: The number_of_notice_periods of this SubscriptionProductVersionPending.
        :type: int
        """

        self._number_of_notice_periods = number_of_notice_periods
    
    @property
    def product(self):
        """Gets the product of this SubscriptionProductVersionPending.

            The product that the version belongs to.

        :return: The product of this SubscriptionProductVersionPending.
        :rtype: int
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this SubscriptionProductVersionPending.

            The product that the version belongs to.

        :param product: The product of this SubscriptionProductVersionPending.
        :type: int
        """

        self._product = product
    
    @property
    def state(self):
        """Gets the state of this SubscriptionProductVersionPending.

            The object's current state.

        :return: The state of this SubscriptionProductVersionPending.
        :rtype: SubscriptionProductVersionState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubscriptionProductVersionPending.

            The object's current state.

        :param state: The state of this SubscriptionProductVersionPending.
        :type: SubscriptionProductVersionState
        """

        self._state = state
    
    @property
    def tax_calculation(self):
        """Gets the tax_calculation of this SubscriptionProductVersionPending.

            The way taxes are calculated for fees.

        :return: The tax_calculation of this SubscriptionProductVersionPending.
        :rtype: TaxCalculation
        """
        return self._tax_calculation

    @tax_calculation.setter
    def tax_calculation(self, tax_calculation):
        """Sets the tax_calculation of this SubscriptionProductVersionPending.

            The way taxes are calculated for fees.

        :param tax_calculation: The tax_calculation of this SubscriptionProductVersionPending.
        :type: TaxCalculation
        """

        self._tax_calculation = tax_calculation
    

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
        if issubclass(SubscriptionProductVersionPending, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionProductVersionPending):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
