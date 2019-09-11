# coding: utf-8
import pprint
import six
from enum import Enum



class ProductPeriodFeeUpdate:

    swagger_types = {
    
        'id': 'int',
        'version': 'int',
        'component': 'int',
        'description': 'DatabaseTranslatedStringCreate',
        'ledger_entry_title': 'DatabaseTranslatedStringCreate',
        'name': 'DatabaseTranslatedStringCreate',
        'number_of_free_trial_periods': 'int',
        'period_fee': 'list[PersistableCurrencyAmountUpdate]',
    }

    attribute_map = {
        'id': 'id','version': 'version','component': 'component','description': 'description','ledger_entry_title': 'ledgerEntryTitle','name': 'name','number_of_free_trial_periods': 'numberOfFreeTrialPeriods','period_fee': 'periodFee',
    }

    
    _id = None
    _version = None
    _component = None
    _description = None
    _ledger_entry_title = None
    _name = None
    _number_of_free_trial_periods = None
    _period_fee = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id')

        self.version = kwargs.get('version')

        self.component = kwargs.get('component', None)
        self.description = kwargs.get('description', None)
        self.ledger_entry_title = kwargs.get('ledger_entry_title', None)
        self.name = kwargs.get('name', None)
        self.number_of_free_trial_periods = kwargs.get('number_of_free_trial_periods', None)
        self.period_fee = kwargs.get('period_fee', None)
        

    
    @property
    def id(self):
        """Gets the id of this ProductPeriodFeeUpdate.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this ProductPeriodFeeUpdate.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProductPeriodFeeUpdate.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this ProductPeriodFeeUpdate.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id
    
    @property
    def version(self):
        """Gets the version of this ProductPeriodFeeUpdate.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ProductPeriodFeeUpdate.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ProductPeriodFeeUpdate.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ProductPeriodFeeUpdate.
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")

        self._version = version
    
    @property
    def component(self):
        """Gets the component of this ProductPeriodFeeUpdate.

            

        :return: The component of this ProductPeriodFeeUpdate.
        :rtype: int
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this ProductPeriodFeeUpdate.

            

        :param component: The component of this ProductPeriodFeeUpdate.
        :type: int
        """

        self._component = component
    
    @property
    def description(self):
        """Gets the description of this ProductPeriodFeeUpdate.

            The description of a component fee describes the fee to the subscriber. The description may be shown in documents or on certain user interfaces.

        :return: The description of this ProductPeriodFeeUpdate.
        :rtype: DatabaseTranslatedStringCreate
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProductPeriodFeeUpdate.

            The description of a component fee describes the fee to the subscriber. The description may be shown in documents or on certain user interfaces.

        :param description: The description of this ProductPeriodFeeUpdate.
        :type: DatabaseTranslatedStringCreate
        """

        self._description = description
    
    @property
    def ledger_entry_title(self):
        """Gets the ledger_entry_title of this ProductPeriodFeeUpdate.

            The ledger entry title will be used for the title in the ledger entry and in the invoice.

        :return: The ledger_entry_title of this ProductPeriodFeeUpdate.
        :rtype: DatabaseTranslatedStringCreate
        """
        return self._ledger_entry_title

    @ledger_entry_title.setter
    def ledger_entry_title(self, ledger_entry_title):
        """Sets the ledger_entry_title of this ProductPeriodFeeUpdate.

            The ledger entry title will be used for the title in the ledger entry and in the invoice.

        :param ledger_entry_title: The ledger_entry_title of this ProductPeriodFeeUpdate.
        :type: DatabaseTranslatedStringCreate
        """

        self._ledger_entry_title = ledger_entry_title
    
    @property
    def name(self):
        """Gets the name of this ProductPeriodFeeUpdate.

            The name of the fee should describe for the subscriber in few words for what the fee is for.

        :return: The name of this ProductPeriodFeeUpdate.
        :rtype: DatabaseTranslatedStringCreate
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductPeriodFeeUpdate.

            The name of the fee should describe for the subscriber in few words for what the fee is for.

        :param name: The name of this ProductPeriodFeeUpdate.
        :type: DatabaseTranslatedStringCreate
        """

        self._name = name
    
    @property
    def number_of_free_trial_periods(self):
        """Gets the number_of_free_trial_periods of this ProductPeriodFeeUpdate.

            The number of free trial periods specify how many periods are free of charge at the begining of the subscription.

        :return: The number_of_free_trial_periods of this ProductPeriodFeeUpdate.
        :rtype: int
        """
        return self._number_of_free_trial_periods

    @number_of_free_trial_periods.setter
    def number_of_free_trial_periods(self, number_of_free_trial_periods):
        """Sets the number_of_free_trial_periods of this ProductPeriodFeeUpdate.

            The number of free trial periods specify how many periods are free of charge at the begining of the subscription.

        :param number_of_free_trial_periods: The number_of_free_trial_periods of this ProductPeriodFeeUpdate.
        :type: int
        """

        self._number_of_free_trial_periods = number_of_free_trial_periods
    
    @property
    def period_fee(self):
        """Gets the period_fee of this ProductPeriodFeeUpdate.

            The period fee is charged for every period of the subscription except for those periods which are trial periods.

        :return: The period_fee of this ProductPeriodFeeUpdate.
        :rtype: list[PersistableCurrencyAmountUpdate]
        """
        return self._period_fee

    @period_fee.setter
    def period_fee(self, period_fee):
        """Sets the period_fee of this ProductPeriodFeeUpdate.

            The period fee is charged for every period of the subscription except for those periods which are trial periods.

        :param period_fee: The period_fee of this ProductPeriodFeeUpdate.
        :type: list[PersistableCurrencyAmountUpdate]
        """

        self._period_fee = period_fee
    

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
        if issubclass(ProductPeriodFeeUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ProductPeriodFeeUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
