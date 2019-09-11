# coding: utf-8
import pprint
import six
from enum import Enum



class ProductPeriodFee:

    swagger_types = {
    
        'component': 'SubscriptionProductComponent',
        'description': 'DatabaseTranslatedString',
        'id': 'int',
        'ledger_entry_title': 'DatabaseTranslatedString',
        'linked_space_id': 'int',
        'name': 'DatabaseTranslatedString',
        'number_of_free_trial_periods': 'int',
        'period_fee': 'list[PersistableCurrencyAmount]',
        'type': 'ProductFeeType',
        'version': 'int',
    }

    attribute_map = {
        'component': 'component','description': 'description','id': 'id','ledger_entry_title': 'ledgerEntryTitle','linked_space_id': 'linkedSpaceId','name': 'name','number_of_free_trial_periods': 'numberOfFreeTrialPeriods','period_fee': 'periodFee','type': 'type','version': 'version',
    }

    
    _component = None
    _description = None
    _id = None
    _ledger_entry_title = None
    _linked_space_id = None
    _name = None
    _number_of_free_trial_periods = None
    _period_fee = None
    _type = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.component = kwargs.get('component', None)
        self.description = kwargs.get('description', None)
        self.id = kwargs.get('id', None)
        self.ledger_entry_title = kwargs.get('ledger_entry_title', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.number_of_free_trial_periods = kwargs.get('number_of_free_trial_periods', None)
        self.period_fee = kwargs.get('period_fee', None)
        self.type = kwargs.get('type', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def component(self):
        """Gets the component of this ProductPeriodFee.

            

        :return: The component of this ProductPeriodFee.
        :rtype: SubscriptionProductComponent
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this ProductPeriodFee.

            

        :param component: The component of this ProductPeriodFee.
        :type: SubscriptionProductComponent
        """

        self._component = component
    
    @property
    def description(self):
        """Gets the description of this ProductPeriodFee.

            The description of a component fee describes the fee to the subscriber. The description may be shown in documents or on certain user interfaces.

        :return: The description of this ProductPeriodFee.
        :rtype: DatabaseTranslatedString
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProductPeriodFee.

            The description of a component fee describes the fee to the subscriber. The description may be shown in documents or on certain user interfaces.

        :param description: The description of this ProductPeriodFee.
        :type: DatabaseTranslatedString
        """

        self._description = description
    
    @property
    def id(self):
        """Gets the id of this ProductPeriodFee.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this ProductPeriodFee.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProductPeriodFee.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this ProductPeriodFee.
        :type: int
        """

        self._id = id
    
    @property
    def ledger_entry_title(self):
        """Gets the ledger_entry_title of this ProductPeriodFee.

            The ledger entry title will be used for the title in the ledger entry and in the invoice.

        :return: The ledger_entry_title of this ProductPeriodFee.
        :rtype: DatabaseTranslatedString
        """
        return self._ledger_entry_title

    @ledger_entry_title.setter
    def ledger_entry_title(self, ledger_entry_title):
        """Sets the ledger_entry_title of this ProductPeriodFee.

            The ledger entry title will be used for the title in the ledger entry and in the invoice.

        :param ledger_entry_title: The ledger_entry_title of this ProductPeriodFee.
        :type: DatabaseTranslatedString
        """

        self._ledger_entry_title = ledger_entry_title
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this ProductPeriodFee.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this ProductPeriodFee.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this ProductPeriodFee.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this ProductPeriodFee.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this ProductPeriodFee.

            The name of the fee should describe for the subscriber in few words for what the fee is for.

        :return: The name of this ProductPeriodFee.
        :rtype: DatabaseTranslatedString
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductPeriodFee.

            The name of the fee should describe for the subscriber in few words for what the fee is for.

        :param name: The name of this ProductPeriodFee.
        :type: DatabaseTranslatedString
        """

        self._name = name
    
    @property
    def number_of_free_trial_periods(self):
        """Gets the number_of_free_trial_periods of this ProductPeriodFee.

            The number of free trial periods specify how many periods are free of charge at the begining of the subscription.

        :return: The number_of_free_trial_periods of this ProductPeriodFee.
        :rtype: int
        """
        return self._number_of_free_trial_periods

    @number_of_free_trial_periods.setter
    def number_of_free_trial_periods(self, number_of_free_trial_periods):
        """Sets the number_of_free_trial_periods of this ProductPeriodFee.

            The number of free trial periods specify how many periods are free of charge at the begining of the subscription.

        :param number_of_free_trial_periods: The number_of_free_trial_periods of this ProductPeriodFee.
        :type: int
        """

        self._number_of_free_trial_periods = number_of_free_trial_periods
    
    @property
    def period_fee(self):
        """Gets the period_fee of this ProductPeriodFee.

            The period fee is charged for every period of the subscription except for those periods which are trial periods.

        :return: The period_fee of this ProductPeriodFee.
        :rtype: list[PersistableCurrencyAmount]
        """
        return self._period_fee

    @period_fee.setter
    def period_fee(self, period_fee):
        """Sets the period_fee of this ProductPeriodFee.

            The period fee is charged for every period of the subscription except for those periods which are trial periods.

        :param period_fee: The period_fee of this ProductPeriodFee.
        :type: list[PersistableCurrencyAmount]
        """

        self._period_fee = period_fee
    
    @property
    def type(self):
        """Gets the type of this ProductPeriodFee.

            

        :return: The type of this ProductPeriodFee.
        :rtype: ProductFeeType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProductPeriodFee.

            

        :param type: The type of this ProductPeriodFee.
        :type: ProductFeeType
        """

        self._type = type
    
    @property
    def version(self):
        """Gets the version of this ProductPeriodFee.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ProductPeriodFee.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ProductPeriodFee.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ProductPeriodFee.
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
        if issubclass(ProductPeriodFee, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ProductPeriodFee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
