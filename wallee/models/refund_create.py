# coding: utf-8
import pprint
import six
from enum import Enum



class RefundCreate:

    swagger_types = {
    
        'amount': 'float',
        'completion': 'int',
        'external_id': 'str',
        'merchant_reference': 'str',
        'reductions': 'list[LineItemReductionCreate]',
        'transaction': 'int',
        'type': 'RefundType',
    }

    attribute_map = {
        'amount': 'amount','completion': 'completion','external_id': 'externalId','merchant_reference': 'merchantReference','reductions': 'reductions','transaction': 'transaction','type': 'type',
    }

    
    _amount = None
    _completion = None
    _external_id = None
    _merchant_reference = None
    _reductions = None
    _transaction = None
    _type = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.amount = kwargs.get('amount', None)
        self.completion = kwargs.get('completion', None)
        self.external_id = kwargs.get('external_id')

        self.merchant_reference = kwargs.get('merchant_reference', None)
        self.reductions = kwargs.get('reductions', None)
        self.transaction = kwargs.get('transaction', None)
        self.type = kwargs.get('type')

        

    
    @property
    def amount(self):
        """Gets the amount of this RefundCreate.

            

        :return: The amount of this RefundCreate.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this RefundCreate.

            

        :param amount: The amount of this RefundCreate.
        :type: float
        """

        self._amount = amount
    
    @property
    def completion(self):
        """Gets the completion of this RefundCreate.

            

        :return: The completion of this RefundCreate.
        :rtype: int
        """
        return self._completion

    @completion.setter
    def completion(self, completion):
        """Sets the completion of this RefundCreate.

            

        :param completion: The completion of this RefundCreate.
        :type: int
        """

        self._completion = completion
    
    @property
    def external_id(self):
        """Gets the external_id of this RefundCreate.

            The external id helps to identify duplicate calls to the refund service. As such the external ID has to be unique per transaction.

        :return: The external_id of this RefundCreate.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this RefundCreate.

            The external id helps to identify duplicate calls to the refund service. As such the external ID has to be unique per transaction.

        :param external_id: The external_id of this RefundCreate.
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")
        if external_id is not None and len(external_id) > 100:
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `100`")
        if external_id is not None and len(external_id) < 1:
            raise ValueError("Invalid value for `external_id`, length must be greater than or equal to `1`")

        self._external_id = external_id
    
    @property
    def merchant_reference(self):
        """Gets the merchant_reference of this RefundCreate.

            

        :return: The merchant_reference of this RefundCreate.
        :rtype: str
        """
        return self._merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, merchant_reference):
        """Sets the merchant_reference of this RefundCreate.

            

        :param merchant_reference: The merchant_reference of this RefundCreate.
        :type: str
        """
        if merchant_reference is not None and len(merchant_reference) > 100:
            raise ValueError("Invalid value for `merchant_reference`, length must be less than or equal to `100`")

        self._merchant_reference = merchant_reference
    
    @property
    def reductions(self):
        """Gets the reductions of this RefundCreate.

            

        :return: The reductions of this RefundCreate.
        :rtype: list[LineItemReductionCreate]
        """
        return self._reductions

    @reductions.setter
    def reductions(self, reductions):
        """Sets the reductions of this RefundCreate.

            

        :param reductions: The reductions of this RefundCreate.
        :type: list[LineItemReductionCreate]
        """

        self._reductions = reductions
    
    @property
    def transaction(self):
        """Gets the transaction of this RefundCreate.

            

        :return: The transaction of this RefundCreate.
        :rtype: int
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this RefundCreate.

            

        :param transaction: The transaction of this RefundCreate.
        :type: int
        """

        self._transaction = transaction
    
    @property
    def type(self):
        """Gets the type of this RefundCreate.

            

        :return: The type of this RefundCreate.
        :rtype: RefundType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RefundCreate.

            

        :param type: The type of this RefundCreate.
        :type: RefundType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
    

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
        if issubclass(RefundCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, RefundCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
