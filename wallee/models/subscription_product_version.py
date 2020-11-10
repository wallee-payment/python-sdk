# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionProductVersion:

    swagger_types = {
    
        'activated_on': 'datetime',
        'billing_cycle': 'str',
        'comment': 'str',
        'created_on': 'datetime',
        'default_currency': 'str',
        'enabled_currencies': 'list[str]',
        'id': 'int',
        'increment_number': 'int',
        'linked_space_id': 'int',
        'minimal_number_of_periods': 'int',
        'name': 'DatabaseTranslatedString',
        'number_of_notice_periods': 'int',
        'obsoleted_on': 'datetime',
        'planned_purge_date': 'datetime',
        'product': 'SubscriptionProduct',
        'reference': 'str',
        'retiring_finished_on': 'datetime',
        'retiring_started_on': 'datetime',
        'state': 'SubscriptionProductVersionState',
        'tax_calculation': 'TaxCalculation',
        'version': 'int',
    }

    attribute_map = {
        'activated_on': 'activatedOn','billing_cycle': 'billingCycle','comment': 'comment','created_on': 'createdOn','default_currency': 'defaultCurrency','enabled_currencies': 'enabledCurrencies','id': 'id','increment_number': 'incrementNumber','linked_space_id': 'linkedSpaceId','minimal_number_of_periods': 'minimalNumberOfPeriods','name': 'name','number_of_notice_periods': 'numberOfNoticePeriods','obsoleted_on': 'obsoletedOn','planned_purge_date': 'plannedPurgeDate','product': 'product','reference': 'reference','retiring_finished_on': 'retiringFinishedOn','retiring_started_on': 'retiringStartedOn','state': 'state','tax_calculation': 'taxCalculation','version': 'version',
    }

    
    _activated_on = None
    _billing_cycle = None
    _comment = None
    _created_on = None
    _default_currency = None
    _enabled_currencies = None
    _id = None
    _increment_number = None
    _linked_space_id = None
    _minimal_number_of_periods = None
    _name = None
    _number_of_notice_periods = None
    _obsoleted_on = None
    _planned_purge_date = None
    _product = None
    _reference = None
    _retiring_finished_on = None
    _retiring_started_on = None
    _state = None
    _tax_calculation = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.activated_on = kwargs.get('activated_on', None)
        self.billing_cycle = kwargs.get('billing_cycle', None)
        self.comment = kwargs.get('comment', None)
        self.created_on = kwargs.get('created_on', None)
        self.default_currency = kwargs.get('default_currency', None)
        self.enabled_currencies = kwargs.get('enabled_currencies', None)
        self.id = kwargs.get('id', None)
        self.increment_number = kwargs.get('increment_number', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.minimal_number_of_periods = kwargs.get('minimal_number_of_periods', None)
        self.name = kwargs.get('name', None)
        self.number_of_notice_periods = kwargs.get('number_of_notice_periods', None)
        self.obsoleted_on = kwargs.get('obsoleted_on', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.product = kwargs.get('product', None)
        self.reference = kwargs.get('reference', None)
        self.retiring_finished_on = kwargs.get('retiring_finished_on', None)
        self.retiring_started_on = kwargs.get('retiring_started_on', None)
        self.state = kwargs.get('state', None)
        self.tax_calculation = kwargs.get('tax_calculation', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def activated_on(self):
        """Gets the activated_on of this SubscriptionProductVersion.

            

        :return: The activated_on of this SubscriptionProductVersion.
        :rtype: datetime
        """
        return self._activated_on

    @activated_on.setter
    def activated_on(self, activated_on):
        """Sets the activated_on of this SubscriptionProductVersion.

            

        :param activated_on: The activated_on of this SubscriptionProductVersion.
        :type: datetime
        """

        self._activated_on = activated_on
    
    @property
    def billing_cycle(self):
        """Gets the billing_cycle of this SubscriptionProductVersion.

            The billing cycle determines the rhythm with which the subscriber is billed. The charging may have different rhythm.

        :return: The billing_cycle of this SubscriptionProductVersion.
        :rtype: str
        """
        return self._billing_cycle

    @billing_cycle.setter
    def billing_cycle(self, billing_cycle):
        """Sets the billing_cycle of this SubscriptionProductVersion.

            The billing cycle determines the rhythm with which the subscriber is billed. The charging may have different rhythm.

        :param billing_cycle: The billing_cycle of this SubscriptionProductVersion.
        :type: str
        """

        self._billing_cycle = billing_cycle
    
    @property
    def comment(self):
        """Gets the comment of this SubscriptionProductVersion.

            The comment allows to provide a internal comment for the version. It helps to document why a product was changed. The comment is not disclosed to the subscriber.

        :return: The comment of this SubscriptionProductVersion.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this SubscriptionProductVersion.

            The comment allows to provide a internal comment for the version. It helps to document why a product was changed. The comment is not disclosed to the subscriber.

        :param comment: The comment of this SubscriptionProductVersion.
        :type: str
        """

        self._comment = comment
    
    @property
    def created_on(self):
        """Gets the created_on of this SubscriptionProductVersion.

            

        :return: The created_on of this SubscriptionProductVersion.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this SubscriptionProductVersion.

            

        :param created_on: The created_on of this SubscriptionProductVersion.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def default_currency(self):
        """Gets the default_currency of this SubscriptionProductVersion.

            The default currency has to be used in all fees.

        :return: The default_currency of this SubscriptionProductVersion.
        :rtype: str
        """
        return self._default_currency

    @default_currency.setter
    def default_currency(self, default_currency):
        """Sets the default_currency of this SubscriptionProductVersion.

            The default currency has to be used in all fees.

        :param default_currency: The default_currency of this SubscriptionProductVersion.
        :type: str
        """

        self._default_currency = default_currency
    
    @property
    def enabled_currencies(self):
        """Gets the enabled_currencies of this SubscriptionProductVersion.

            The currencies which are enabled can be selected to define component fees. Currencies which are not enabled cannot be used to define fees.

        :return: The enabled_currencies of this SubscriptionProductVersion.
        :rtype: list[str]
        """
        return self._enabled_currencies

    @enabled_currencies.setter
    def enabled_currencies(self, enabled_currencies):
        """Sets the enabled_currencies of this SubscriptionProductVersion.

            The currencies which are enabled can be selected to define component fees. Currencies which are not enabled cannot be used to define fees.

        :param enabled_currencies: The enabled_currencies of this SubscriptionProductVersion.
        :type: list[str]
        """

        self._enabled_currencies = enabled_currencies
    
    @property
    def id(self):
        """Gets the id of this SubscriptionProductVersion.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this SubscriptionProductVersion.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionProductVersion.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this SubscriptionProductVersion.
        :type: int
        """

        self._id = id
    
    @property
    def increment_number(self):
        """Gets the increment_number of this SubscriptionProductVersion.

            The increment number represents the version number incremented whenever a new version is activated.

        :return: The increment_number of this SubscriptionProductVersion.
        :rtype: int
        """
        return self._increment_number

    @increment_number.setter
    def increment_number(self, increment_number):
        """Sets the increment_number of this SubscriptionProductVersion.

            The increment number represents the version number incremented whenever a new version is activated.

        :param increment_number: The increment_number of this SubscriptionProductVersion.
        :type: int
        """

        self._increment_number = increment_number
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this SubscriptionProductVersion.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this SubscriptionProductVersion.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this SubscriptionProductVersion.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this SubscriptionProductVersion.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def minimal_number_of_periods(self):
        """Gets the minimal_number_of_periods of this SubscriptionProductVersion.

            The minimal number of periods determines how long the subscription has to run before the subscription can be terminated.

        :return: The minimal_number_of_periods of this SubscriptionProductVersion.
        :rtype: int
        """
        return self._minimal_number_of_periods

    @minimal_number_of_periods.setter
    def minimal_number_of_periods(self, minimal_number_of_periods):
        """Sets the minimal_number_of_periods of this SubscriptionProductVersion.

            The minimal number of periods determines how long the subscription has to run before the subscription can be terminated.

        :param minimal_number_of_periods: The minimal_number_of_periods of this SubscriptionProductVersion.
        :type: int
        """

        self._minimal_number_of_periods = minimal_number_of_periods
    
    @property
    def name(self):
        """Gets the name of this SubscriptionProductVersion.

            The product version name is the name of the product which is shown to the user for the version. When the visible product name should be changed for a particular product a new version has to be created which contains the new name of the product.

        :return: The name of this SubscriptionProductVersion.
        :rtype: DatabaseTranslatedString
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionProductVersion.

            The product version name is the name of the product which is shown to the user for the version. When the visible product name should be changed for a particular product a new version has to be created which contains the new name of the product.

        :param name: The name of this SubscriptionProductVersion.
        :type: DatabaseTranslatedString
        """

        self._name = name
    
    @property
    def number_of_notice_periods(self):
        """Gets the number_of_notice_periods of this SubscriptionProductVersion.

            The number of notice periods determines the number of periods which need to be paid between the request to terminate the subscription and the final period.

        :return: The number_of_notice_periods of this SubscriptionProductVersion.
        :rtype: int
        """
        return self._number_of_notice_periods

    @number_of_notice_periods.setter
    def number_of_notice_periods(self, number_of_notice_periods):
        """Sets the number_of_notice_periods of this SubscriptionProductVersion.

            The number of notice periods determines the number of periods which need to be paid between the request to terminate the subscription and the final period.

        :param number_of_notice_periods: The number_of_notice_periods of this SubscriptionProductVersion.
        :type: int
        """

        self._number_of_notice_periods = number_of_notice_periods
    
    @property
    def obsoleted_on(self):
        """Gets the obsoleted_on of this SubscriptionProductVersion.

            

        :return: The obsoleted_on of this SubscriptionProductVersion.
        :rtype: datetime
        """
        return self._obsoleted_on

    @obsoleted_on.setter
    def obsoleted_on(self, obsoleted_on):
        """Sets the obsoleted_on of this SubscriptionProductVersion.

            

        :param obsoleted_on: The obsoleted_on of this SubscriptionProductVersion.
        :type: datetime
        """

        self._obsoleted_on = obsoleted_on
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this SubscriptionProductVersion.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this SubscriptionProductVersion.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this SubscriptionProductVersion.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this SubscriptionProductVersion.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def product(self):
        """Gets the product of this SubscriptionProductVersion.

            Each product version is linked to a product.

        :return: The product of this SubscriptionProductVersion.
        :rtype: SubscriptionProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this SubscriptionProductVersion.

            Each product version is linked to a product.

        :param product: The product of this SubscriptionProductVersion.
        :type: SubscriptionProduct
        """

        self._product = product
    
    @property
    def reference(self):
        """Gets the reference of this SubscriptionProductVersion.

            The product version reference helps to identify the version. The reference is generated out of the product reference.

        :return: The reference of this SubscriptionProductVersion.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this SubscriptionProductVersion.

            The product version reference helps to identify the version. The reference is generated out of the product reference.

        :param reference: The reference of this SubscriptionProductVersion.
        :type: str
        """
        if reference is not None and len(reference) > 125:
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `125`")

        self._reference = reference
    
    @property
    def retiring_finished_on(self):
        """Gets the retiring_finished_on of this SubscriptionProductVersion.

            

        :return: The retiring_finished_on of this SubscriptionProductVersion.
        :rtype: datetime
        """
        return self._retiring_finished_on

    @retiring_finished_on.setter
    def retiring_finished_on(self, retiring_finished_on):
        """Sets the retiring_finished_on of this SubscriptionProductVersion.

            

        :param retiring_finished_on: The retiring_finished_on of this SubscriptionProductVersion.
        :type: datetime
        """

        self._retiring_finished_on = retiring_finished_on
    
    @property
    def retiring_started_on(self):
        """Gets the retiring_started_on of this SubscriptionProductVersion.

            

        :return: The retiring_started_on of this SubscriptionProductVersion.
        :rtype: datetime
        """
        return self._retiring_started_on

    @retiring_started_on.setter
    def retiring_started_on(self, retiring_started_on):
        """Sets the retiring_started_on of this SubscriptionProductVersion.

            

        :param retiring_started_on: The retiring_started_on of this SubscriptionProductVersion.
        :type: datetime
        """

        self._retiring_started_on = retiring_started_on
    
    @property
    def state(self):
        """Gets the state of this SubscriptionProductVersion.

            

        :return: The state of this SubscriptionProductVersion.
        :rtype: SubscriptionProductVersionState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubscriptionProductVersion.

            

        :param state: The state of this SubscriptionProductVersion.
        :type: SubscriptionProductVersionState
        """

        self._state = state
    
    @property
    def tax_calculation(self):
        """Gets the tax_calculation of this SubscriptionProductVersion.

            Strategy that is used for tax calculation in fees.

        :return: The tax_calculation of this SubscriptionProductVersion.
        :rtype: TaxCalculation
        """
        return self._tax_calculation

    @tax_calculation.setter
    def tax_calculation(self, tax_calculation):
        """Sets the tax_calculation of this SubscriptionProductVersion.

            Strategy that is used for tax calculation in fees.

        :param tax_calculation: The tax_calculation of this SubscriptionProductVersion.
        :type: TaxCalculation
        """

        self._tax_calculation = tax_calculation
    
    @property
    def version(self):
        """Gets the version of this SubscriptionProductVersion.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this SubscriptionProductVersion.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SubscriptionProductVersion.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this SubscriptionProductVersion.
        :type: int
        """

        self._version = version
    

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
        if issubclass(SubscriptionProductVersion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionProductVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
