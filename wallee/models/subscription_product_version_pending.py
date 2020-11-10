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
        'name': 'DatabaseTranslatedStringCreate',
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

            The billing cycle determines the rhythm with which the subscriber is billed. The charging may have different rhythm.

        :return: The billing_cycle of this SubscriptionProductVersionPending.
        :rtype: str
        """
        return self._billing_cycle

    @billing_cycle.setter
    def billing_cycle(self, billing_cycle):
        """Sets the billing_cycle of this SubscriptionProductVersionPending.

            The billing cycle determines the rhythm with which the subscriber is billed. The charging may have different rhythm.

        :param billing_cycle: The billing_cycle of this SubscriptionProductVersionPending.
        :type: str
        """

        self._billing_cycle = billing_cycle
    
    @property
    def comment(self):
        """Gets the comment of this SubscriptionProductVersionPending.

            The comment allows to provide a internal comment for the version. It helps to document why a product was changed. The comment is not disclosed to the subscriber.

        :return: The comment of this SubscriptionProductVersionPending.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this SubscriptionProductVersionPending.

            The comment allows to provide a internal comment for the version. It helps to document why a product was changed. The comment is not disclosed to the subscriber.

        :param comment: The comment of this SubscriptionProductVersionPending.
        :type: str
        """

        self._comment = comment
    
    @property
    def default_currency(self):
        """Gets the default_currency of this SubscriptionProductVersionPending.

            The default currency has to be used in all fees.

        :return: The default_currency of this SubscriptionProductVersionPending.
        :rtype: str
        """
        return self._default_currency

    @default_currency.setter
    def default_currency(self, default_currency):
        """Sets the default_currency of this SubscriptionProductVersionPending.

            The default currency has to be used in all fees.

        :param default_currency: The default_currency of this SubscriptionProductVersionPending.
        :type: str
        """

        self._default_currency = default_currency
    
    @property
    def enabled_currencies(self):
        """Gets the enabled_currencies of this SubscriptionProductVersionPending.

            The currencies which are enabled can be selected to define component fees. Currencies which are not enabled cannot be used to define fees.

        :return: The enabled_currencies of this SubscriptionProductVersionPending.
        :rtype: list[str]
        """
        return self._enabled_currencies

    @enabled_currencies.setter
    def enabled_currencies(self, enabled_currencies):
        """Sets the enabled_currencies of this SubscriptionProductVersionPending.

            The currencies which are enabled can be selected to define component fees. Currencies which are not enabled cannot be used to define fees.

        :param enabled_currencies: The enabled_currencies of this SubscriptionProductVersionPending.
        :type: list[str]
        """

        self._enabled_currencies = enabled_currencies
    
    @property
    def minimal_number_of_periods(self):
        """Gets the minimal_number_of_periods of this SubscriptionProductVersionPending.

            The minimal number of periods determines how long the subscription has to run before the subscription can be terminated.

        :return: The minimal_number_of_periods of this SubscriptionProductVersionPending.
        :rtype: int
        """
        return self._minimal_number_of_periods

    @minimal_number_of_periods.setter
    def minimal_number_of_periods(self, minimal_number_of_periods):
        """Sets the minimal_number_of_periods of this SubscriptionProductVersionPending.

            The minimal number of periods determines how long the subscription has to run before the subscription can be terminated.

        :param minimal_number_of_periods: The minimal_number_of_periods of this SubscriptionProductVersionPending.
        :type: int
        """

        self._minimal_number_of_periods = minimal_number_of_periods
    
    @property
    def name(self):
        """Gets the name of this SubscriptionProductVersionPending.

            The product version name is the name of the product which is shown to the user for the version. When the visible product name should be changed for a particular product a new version has to be created which contains the new name of the product.

        :return: The name of this SubscriptionProductVersionPending.
        :rtype: DatabaseTranslatedStringCreate
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionProductVersionPending.

            The product version name is the name of the product which is shown to the user for the version. When the visible product name should be changed for a particular product a new version has to be created which contains the new name of the product.

        :param name: The name of this SubscriptionProductVersionPending.
        :type: DatabaseTranslatedStringCreate
        """

        self._name = name
    
    @property
    def number_of_notice_periods(self):
        """Gets the number_of_notice_periods of this SubscriptionProductVersionPending.

            The number of notice periods determines the number of periods which need to be paid between the request to terminate the subscription and the final period.

        :return: The number_of_notice_periods of this SubscriptionProductVersionPending.
        :rtype: int
        """
        return self._number_of_notice_periods

    @number_of_notice_periods.setter
    def number_of_notice_periods(self, number_of_notice_periods):
        """Sets the number_of_notice_periods of this SubscriptionProductVersionPending.

            The number of notice periods determines the number of periods which need to be paid between the request to terminate the subscription and the final period.

        :param number_of_notice_periods: The number_of_notice_periods of this SubscriptionProductVersionPending.
        :type: int
        """

        self._number_of_notice_periods = number_of_notice_periods
    
    @property
    def product(self):
        """Gets the product of this SubscriptionProductVersionPending.

            Each product version is linked to a product.

        :return: The product of this SubscriptionProductVersionPending.
        :rtype: int
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this SubscriptionProductVersionPending.

            Each product version is linked to a product.

        :param product: The product of this SubscriptionProductVersionPending.
        :type: int
        """

        self._product = product
    
    @property
    def state(self):
        """Gets the state of this SubscriptionProductVersionPending.

            

        :return: The state of this SubscriptionProductVersionPending.
        :rtype: SubscriptionProductVersionState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubscriptionProductVersionPending.

            

        :param state: The state of this SubscriptionProductVersionPending.
        :type: SubscriptionProductVersionState
        """

        self._state = state
    
    @property
    def tax_calculation(self):
        """Gets the tax_calculation of this SubscriptionProductVersionPending.

            Strategy that is used for tax calculation in fees.

        :return: The tax_calculation of this SubscriptionProductVersionPending.
        :rtype: TaxCalculation
        """
        return self._tax_calculation

    @tax_calculation.setter
    def tax_calculation(self, tax_calculation):
        """Sets the tax_calculation of this SubscriptionProductVersionPending.

            Strategy that is used for tax calculation in fees.

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
