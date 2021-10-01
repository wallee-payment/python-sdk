# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentContract:

    swagger_types = {
    
        'account': 'Account',
        'activated_on': 'datetime',
        'contract_identifier': 'str',
        'contract_type': 'PaymentContractType',
        'created_by': 'User',
        'created_on': 'datetime',
        'external_id': 'str',
        'id': 'int',
        'rejected_on': 'datetime',
        'rejection_reason': 'FailureReason',
        'start_terminating_on': 'datetime',
        'state': 'PaymentContractState',
        'terminated_by': 'User',
        'terminated_on': 'datetime',
        'version': 'int',
    }

    attribute_map = {
        'account': 'account','activated_on': 'activatedOn','contract_identifier': 'contractIdentifier','contract_type': 'contractType','created_by': 'createdBy','created_on': 'createdOn','external_id': 'externalId','id': 'id','rejected_on': 'rejectedOn','rejection_reason': 'rejectionReason','start_terminating_on': 'startTerminatingOn','state': 'state','terminated_by': 'terminatedBy','terminated_on': 'terminatedOn','version': 'version',
    }

    
    _account = None
    _activated_on = None
    _contract_identifier = None
    _contract_type = None
    _created_by = None
    _created_on = None
    _external_id = None
    _id = None
    _rejected_on = None
    _rejection_reason = None
    _start_terminating_on = None
    _state = None
    _terminated_by = None
    _terminated_on = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.account = kwargs.get('account', None)
        self.activated_on = kwargs.get('activated_on', None)
        self.contract_identifier = kwargs.get('contract_identifier', None)
        self.contract_type = kwargs.get('contract_type', None)
        self.created_by = kwargs.get('created_by', None)
        self.created_on = kwargs.get('created_on', None)
        self.external_id = kwargs.get('external_id', None)
        self.id = kwargs.get('id', None)
        self.rejected_on = kwargs.get('rejected_on', None)
        self.rejection_reason = kwargs.get('rejection_reason', None)
        self.start_terminating_on = kwargs.get('start_terminating_on', None)
        self.state = kwargs.get('state', None)
        self.terminated_by = kwargs.get('terminated_by', None)
        self.terminated_on = kwargs.get('terminated_on', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def account(self):
        """Gets the account of this PaymentContract.

            

        :return: The account of this PaymentContract.
        :rtype: Account
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this PaymentContract.

            

        :param account: The account of this PaymentContract.
        :type: Account
        """

        self._account = account
    
    @property
    def activated_on(self):
        """Gets the activated_on of this PaymentContract.

            

        :return: The activated_on of this PaymentContract.
        :rtype: datetime
        """
        return self._activated_on

    @activated_on.setter
    def activated_on(self, activated_on):
        """Sets the activated_on of this PaymentContract.

            

        :param activated_on: The activated_on of this PaymentContract.
        :type: datetime
        """

        self._activated_on = activated_on
    
    @property
    def contract_identifier(self):
        """Gets the contract_identifier of this PaymentContract.

            

        :return: The contract_identifier of this PaymentContract.
        :rtype: str
        """
        return self._contract_identifier

    @contract_identifier.setter
    def contract_identifier(self, contract_identifier):
        """Sets the contract_identifier of this PaymentContract.

            

        :param contract_identifier: The contract_identifier of this PaymentContract.
        :type: str
        """

        self._contract_identifier = contract_identifier
    
    @property
    def contract_type(self):
        """Gets the contract_type of this PaymentContract.

            

        :return: The contract_type of this PaymentContract.
        :rtype: PaymentContractType
        """
        return self._contract_type

    @contract_type.setter
    def contract_type(self, contract_type):
        """Sets the contract_type of this PaymentContract.

            

        :param contract_type: The contract_type of this PaymentContract.
        :type: PaymentContractType
        """

        self._contract_type = contract_type
    
    @property
    def created_by(self):
        """Gets the created_by of this PaymentContract.

            

        :return: The created_by of this PaymentContract.
        :rtype: User
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this PaymentContract.

            

        :param created_by: The created_by of this PaymentContract.
        :type: User
        """

        self._created_by = created_by
    
    @property
    def created_on(self):
        """Gets the created_on of this PaymentContract.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this PaymentContract.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this PaymentContract.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this PaymentContract.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def external_id(self):
        """Gets the external_id of this PaymentContract.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :return: The external_id of this PaymentContract.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this PaymentContract.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :param external_id: The external_id of this PaymentContract.
        :type: str
        """

        self._external_id = external_id
    
    @property
    def id(self):
        """Gets the id of this PaymentContract.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentContract.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentContract.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentContract.
        :type: int
        """

        self._id = id
    
    @property
    def rejected_on(self):
        """Gets the rejected_on of this PaymentContract.

            

        :return: The rejected_on of this PaymentContract.
        :rtype: datetime
        """
        return self._rejected_on

    @rejected_on.setter
    def rejected_on(self, rejected_on):
        """Sets the rejected_on of this PaymentContract.

            

        :param rejected_on: The rejected_on of this PaymentContract.
        :type: datetime
        """

        self._rejected_on = rejected_on
    
    @property
    def rejection_reason(self):
        """Gets the rejection_reason of this PaymentContract.

            

        :return: The rejection_reason of this PaymentContract.
        :rtype: FailureReason
        """
        return self._rejection_reason

    @rejection_reason.setter
    def rejection_reason(self, rejection_reason):
        """Sets the rejection_reason of this PaymentContract.

            

        :param rejection_reason: The rejection_reason of this PaymentContract.
        :type: FailureReason
        """

        self._rejection_reason = rejection_reason
    
    @property
    def start_terminating_on(self):
        """Gets the start_terminating_on of this PaymentContract.

            

        :return: The start_terminating_on of this PaymentContract.
        :rtype: datetime
        """
        return self._start_terminating_on

    @start_terminating_on.setter
    def start_terminating_on(self, start_terminating_on):
        """Sets the start_terminating_on of this PaymentContract.

            

        :param start_terminating_on: The start_terminating_on of this PaymentContract.
        :type: datetime
        """

        self._start_terminating_on = start_terminating_on
    
    @property
    def state(self):
        """Gets the state of this PaymentContract.

            

        :return: The state of this PaymentContract.
        :rtype: PaymentContractState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentContract.

            

        :param state: The state of this PaymentContract.
        :type: PaymentContractState
        """

        self._state = state
    
    @property
    def terminated_by(self):
        """Gets the terminated_by of this PaymentContract.

            

        :return: The terminated_by of this PaymentContract.
        :rtype: User
        """
        return self._terminated_by

    @terminated_by.setter
    def terminated_by(self, terminated_by):
        """Sets the terminated_by of this PaymentContract.

            

        :param terminated_by: The terminated_by of this PaymentContract.
        :type: User
        """

        self._terminated_by = terminated_by
    
    @property
    def terminated_on(self):
        """Gets the terminated_on of this PaymentContract.

            

        :return: The terminated_on of this PaymentContract.
        :rtype: datetime
        """
        return self._terminated_on

    @terminated_on.setter
    def terminated_on(self, terminated_on):
        """Sets the terminated_on of this PaymentContract.

            

        :param terminated_on: The terminated_on of this PaymentContract.
        :type: datetime
        """

        self._terminated_on = terminated_on
    
    @property
    def version(self):
        """Gets the version of this PaymentContract.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this PaymentContract.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PaymentContract.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this PaymentContract.
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
        if issubclass(PaymentContract, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentContract):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
