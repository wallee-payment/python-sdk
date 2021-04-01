# coding: utf-8
import pprint
import six
from enum import Enum



class ExternalTransferBankTransaction:

    swagger_types = {
    
        'bank_transaction': 'BankTransaction',
        'external_account_identifier': 'str',
        'external_account_type': 'str',
        'external_bank_name': 'str',
        'id': 'int',
        'linked_space_id': 'int',
        'version': 'int',
    }

    attribute_map = {
        'bank_transaction': 'bankTransaction','external_account_identifier': 'externalAccountIdentifier','external_account_type': 'externalAccountType','external_bank_name': 'externalBankName','id': 'id','linked_space_id': 'linkedSpaceId','version': 'version',
    }

    
    _bank_transaction = None
    _external_account_identifier = None
    _external_account_type = None
    _external_bank_name = None
    _id = None
    _linked_space_id = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.bank_transaction = kwargs.get('bank_transaction', None)
        self.external_account_identifier = kwargs.get('external_account_identifier', None)
        self.external_account_type = kwargs.get('external_account_type', None)
        self.external_bank_name = kwargs.get('external_bank_name', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def bank_transaction(self):
        """Gets the bank_transaction of this ExternalTransferBankTransaction.

            

        :return: The bank_transaction of this ExternalTransferBankTransaction.
        :rtype: BankTransaction
        """
        return self._bank_transaction

    @bank_transaction.setter
    def bank_transaction(self, bank_transaction):
        """Sets the bank_transaction of this ExternalTransferBankTransaction.

            

        :param bank_transaction: The bank_transaction of this ExternalTransferBankTransaction.
        :type: BankTransaction
        """

        self._bank_transaction = bank_transaction
    
    @property
    def external_account_identifier(self):
        """Gets the external_account_identifier of this ExternalTransferBankTransaction.

            

        :return: The external_account_identifier of this ExternalTransferBankTransaction.
        :rtype: str
        """
        return self._external_account_identifier

    @external_account_identifier.setter
    def external_account_identifier(self, external_account_identifier):
        """Sets the external_account_identifier of this ExternalTransferBankTransaction.

            

        :param external_account_identifier: The external_account_identifier of this ExternalTransferBankTransaction.
        :type: str
        """

        self._external_account_identifier = external_account_identifier
    
    @property
    def external_account_type(self):
        """Gets the external_account_type of this ExternalTransferBankTransaction.

            

        :return: The external_account_type of this ExternalTransferBankTransaction.
        :rtype: str
        """
        return self._external_account_type

    @external_account_type.setter
    def external_account_type(self, external_account_type):
        """Sets the external_account_type of this ExternalTransferBankTransaction.

            

        :param external_account_type: The external_account_type of this ExternalTransferBankTransaction.
        :type: str
        """

        self._external_account_type = external_account_type
    
    @property
    def external_bank_name(self):
        """Gets the external_bank_name of this ExternalTransferBankTransaction.

            

        :return: The external_bank_name of this ExternalTransferBankTransaction.
        :rtype: str
        """
        return self._external_bank_name

    @external_bank_name.setter
    def external_bank_name(self, external_bank_name):
        """Sets the external_bank_name of this ExternalTransferBankTransaction.

            

        :param external_bank_name: The external_bank_name of this ExternalTransferBankTransaction.
        :type: str
        """

        self._external_bank_name = external_bank_name
    
    @property
    def id(self):
        """Gets the id of this ExternalTransferBankTransaction.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this ExternalTransferBankTransaction.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExternalTransferBankTransaction.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this ExternalTransferBankTransaction.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this ExternalTransferBankTransaction.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this ExternalTransferBankTransaction.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this ExternalTransferBankTransaction.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this ExternalTransferBankTransaction.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def version(self):
        """Gets the version of this ExternalTransferBankTransaction.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ExternalTransferBankTransaction.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ExternalTransferBankTransaction.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ExternalTransferBankTransaction.
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
        if issubclass(ExternalTransferBankTransaction, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ExternalTransferBankTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
