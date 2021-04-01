# coding: utf-8
import pprint
import six
from enum import Enum



class InternalTransferBankTransaction:

    swagger_types = {
    
        'id': 'int',
        'linked_space_id': 'int',
        'source_bank_transaction': 'BankTransaction',
        'target_bank_transaction': 'BankTransaction',
        'version': 'int',
    }

    attribute_map = {
        'id': 'id','linked_space_id': 'linkedSpaceId','source_bank_transaction': 'sourceBankTransaction','target_bank_transaction': 'targetBankTransaction','version': 'version',
    }

    
    _id = None
    _linked_space_id = None
    _source_bank_transaction = None
    _target_bank_transaction = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.source_bank_transaction = kwargs.get('source_bank_transaction', None)
        self.target_bank_transaction = kwargs.get('target_bank_transaction', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def id(self):
        """Gets the id of this InternalTransferBankTransaction.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this InternalTransferBankTransaction.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InternalTransferBankTransaction.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this InternalTransferBankTransaction.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this InternalTransferBankTransaction.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this InternalTransferBankTransaction.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this InternalTransferBankTransaction.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this InternalTransferBankTransaction.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def source_bank_transaction(self):
        """Gets the source_bank_transaction of this InternalTransferBankTransaction.

            

        :return: The source_bank_transaction of this InternalTransferBankTransaction.
        :rtype: BankTransaction
        """
        return self._source_bank_transaction

    @source_bank_transaction.setter
    def source_bank_transaction(self, source_bank_transaction):
        """Sets the source_bank_transaction of this InternalTransferBankTransaction.

            

        :param source_bank_transaction: The source_bank_transaction of this InternalTransferBankTransaction.
        :type: BankTransaction
        """

        self._source_bank_transaction = source_bank_transaction
    
    @property
    def target_bank_transaction(self):
        """Gets the target_bank_transaction of this InternalTransferBankTransaction.

            

        :return: The target_bank_transaction of this InternalTransferBankTransaction.
        :rtype: BankTransaction
        """
        return self._target_bank_transaction

    @target_bank_transaction.setter
    def target_bank_transaction(self, target_bank_transaction):
        """Sets the target_bank_transaction of this InternalTransferBankTransaction.

            

        :param target_bank_transaction: The target_bank_transaction of this InternalTransferBankTransaction.
        :type: BankTransaction
        """

        self._target_bank_transaction = target_bank_transaction
    
    @property
    def version(self):
        """Gets the version of this InternalTransferBankTransaction.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this InternalTransferBankTransaction.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InternalTransferBankTransaction.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this InternalTransferBankTransaction.
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
        if issubclass(InternalTransferBankTransaction, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, InternalTransferBankTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
