# coding: utf-8
import pprint
import six
from enum import Enum



class InstallmentPaymentSlice:

    swagger_types = {
    
        'charge_on': 'datetime',
        'created_on': 'datetime',
        'id': 'int',
        'installment_payment': 'InstallmentPayment',
        'line_items': 'list[LineItem]',
        'linked_space_id': 'int',
        'linked_transaction': 'int',
        'planned_purge_date': 'datetime',
        'state': 'InstallmentPaymentSliceState',
        'transaction': 'Transaction',
        'version': 'int',
    }

    attribute_map = {
        'charge_on': 'chargeOn','created_on': 'createdOn','id': 'id','installment_payment': 'installmentPayment','line_items': 'lineItems','linked_space_id': 'linkedSpaceId','linked_transaction': 'linkedTransaction','planned_purge_date': 'plannedPurgeDate','state': 'state','transaction': 'transaction','version': 'version',
    }

    
    _charge_on = None
    _created_on = None
    _id = None
    _installment_payment = None
    _line_items = None
    _linked_space_id = None
    _linked_transaction = None
    _planned_purge_date = None
    _state = None
    _transaction = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.charge_on = kwargs.get('charge_on', None)
        self.created_on = kwargs.get('created_on', None)
        self.id = kwargs.get('id', None)
        self.installment_payment = kwargs.get('installment_payment', None)
        self.line_items = kwargs.get('line_items', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.linked_transaction = kwargs.get('linked_transaction', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.transaction = kwargs.get('transaction', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def charge_on(self):
        """Gets the charge_on of this InstallmentPaymentSlice.

            

        :return: The charge_on of this InstallmentPaymentSlice.
        :rtype: datetime
        """
        return self._charge_on

    @charge_on.setter
    def charge_on(self, charge_on):
        """Sets the charge_on of this InstallmentPaymentSlice.

            

        :param charge_on: The charge_on of this InstallmentPaymentSlice.
        :type: datetime
        """

        self._charge_on = charge_on
    
    @property
    def created_on(self):
        """Gets the created_on of this InstallmentPaymentSlice.

            The date and time when the object was created.

        :return: The created_on of this InstallmentPaymentSlice.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this InstallmentPaymentSlice.

            The date and time when the object was created.

        :param created_on: The created_on of this InstallmentPaymentSlice.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def id(self):
        """Gets the id of this InstallmentPaymentSlice.

            A unique identifier for the object.

        :return: The id of this InstallmentPaymentSlice.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InstallmentPaymentSlice.

            A unique identifier for the object.

        :param id: The id of this InstallmentPaymentSlice.
        :type: int
        """

        self._id = id
    
    @property
    def installment_payment(self):
        """Gets the installment_payment of this InstallmentPaymentSlice.

            

        :return: The installment_payment of this InstallmentPaymentSlice.
        :rtype: InstallmentPayment
        """
        return self._installment_payment

    @installment_payment.setter
    def installment_payment(self, installment_payment):
        """Sets the installment_payment of this InstallmentPaymentSlice.

            

        :param installment_payment: The installment_payment of this InstallmentPaymentSlice.
        :type: InstallmentPayment
        """

        self._installment_payment = installment_payment
    
    @property
    def line_items(self):
        """Gets the line_items of this InstallmentPaymentSlice.

            

        :return: The line_items of this InstallmentPaymentSlice.
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this InstallmentPaymentSlice.

            

        :param line_items: The line_items of this InstallmentPaymentSlice.
        :type: list[LineItem]
        """

        self._line_items = line_items
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this InstallmentPaymentSlice.

            The ID of the space this object belongs to.

        :return: The linked_space_id of this InstallmentPaymentSlice.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this InstallmentPaymentSlice.

            The ID of the space this object belongs to.

        :param linked_space_id: The linked_space_id of this InstallmentPaymentSlice.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def linked_transaction(self):
        """Gets the linked_transaction of this InstallmentPaymentSlice.

            The payment transaction this object is linked to.

        :return: The linked_transaction of this InstallmentPaymentSlice.
        :rtype: int
        """
        return self._linked_transaction

    @linked_transaction.setter
    def linked_transaction(self, linked_transaction):
        """Sets the linked_transaction of this InstallmentPaymentSlice.

            The payment transaction this object is linked to.

        :param linked_transaction: The linked_transaction of this InstallmentPaymentSlice.
        :type: int
        """

        self._linked_transaction = linked_transaction
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this InstallmentPaymentSlice.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :return: The planned_purge_date of this InstallmentPaymentSlice.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this InstallmentPaymentSlice.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :param planned_purge_date: The planned_purge_date of this InstallmentPaymentSlice.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this InstallmentPaymentSlice.

            The object's current state.

        :return: The state of this InstallmentPaymentSlice.
        :rtype: InstallmentPaymentSliceState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InstallmentPaymentSlice.

            The object's current state.

        :param state: The state of this InstallmentPaymentSlice.
        :type: InstallmentPaymentSliceState
        """

        self._state = state
    
    @property
    def transaction(self):
        """Gets the transaction of this InstallmentPaymentSlice.

            

        :return: The transaction of this InstallmentPaymentSlice.
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this InstallmentPaymentSlice.

            

        :param transaction: The transaction of this InstallmentPaymentSlice.
        :type: Transaction
        """

        self._transaction = transaction
    
    @property
    def version(self):
        """Gets the version of this InstallmentPaymentSlice.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :return: The version of this InstallmentPaymentSlice.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InstallmentPaymentSlice.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :param version: The version of this InstallmentPaymentSlice.
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
        if issubclass(InstallmentPaymentSlice, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, InstallmentPaymentSlice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
