# coding: utf-8
import pprint
import six
from enum import Enum



class CurrencyBankAccount:

    swagger_types = {
    
        'bank_account': 'BankAccount',
        'currency': 'str',
        'environment': 'BankAccountEnvironment',
        'id': 'int',
        'linked_space_id': 'int',
        'version': 'int',
    }

    attribute_map = {
        'bank_account': 'bankAccount','currency': 'currency','environment': 'environment','id': 'id','linked_space_id': 'linkedSpaceId','version': 'version',
    }

    
    _bank_account = None
    _currency = None
    _environment = None
    _id = None
    _linked_space_id = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.bank_account = kwargs.get('bank_account', None)
        self.currency = kwargs.get('currency', None)
        self.environment = kwargs.get('environment', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def bank_account(self):
        """Gets the bank_account of this CurrencyBankAccount.

            

        :return: The bank_account of this CurrencyBankAccount.
        :rtype: BankAccount
        """
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        """Sets the bank_account of this CurrencyBankAccount.

            

        :param bank_account: The bank_account of this CurrencyBankAccount.
        :type: BankAccount
        """

        self._bank_account = bank_account
    
    @property
    def currency(self):
        """Gets the currency of this CurrencyBankAccount.

            

        :return: The currency of this CurrencyBankAccount.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CurrencyBankAccount.

            

        :param currency: The currency of this CurrencyBankAccount.
        :type: str
        """

        self._currency = currency
    
    @property
    def environment(self):
        """Gets the environment of this CurrencyBankAccount.

            

        :return: The environment of this CurrencyBankAccount.
        :rtype: BankAccountEnvironment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this CurrencyBankAccount.

            

        :param environment: The environment of this CurrencyBankAccount.
        :type: BankAccountEnvironment
        """

        self._environment = environment
    
    @property
    def id(self):
        """Gets the id of this CurrencyBankAccount.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this CurrencyBankAccount.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CurrencyBankAccount.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this CurrencyBankAccount.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this CurrencyBankAccount.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this CurrencyBankAccount.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this CurrencyBankAccount.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this CurrencyBankAccount.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def version(self):
        """Gets the version of this CurrencyBankAccount.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this CurrencyBankAccount.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CurrencyBankAccount.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this CurrencyBankAccount.
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
        if issubclass(CurrencyBankAccount, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, CurrencyBankAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
