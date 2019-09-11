# coding: utf-8
import pprint
import six
from enum import Enum
from . import TransactionAwareEntity


class InstallmentPaymentSlice(TransactionAwareEntity):

    swagger_types = {
    
        'charge_on': 'datetime',
        'created_on': 'datetime',
        'installment_payment': 'InstallmentPayment',
        'line_items': 'list[LineItem]',
        'planned_purge_date': 'datetime',
        'state': 'InstallmentPaymentSliceState',
        'transaction': 'Transaction',
        'version': 'int',
    }

    attribute_map = {
        'charge_on': 'chargeOn','created_on': 'createdOn','installment_payment': 'installmentPayment','line_items': 'lineItems','planned_purge_date': 'plannedPurgeDate','state': 'state','transaction': 'transaction','version': 'version',
    }

    
    _charge_on = None
    _created_on = None
    _installment_payment = None
    _line_items = None
    _planned_purge_date = None
    _state = None
    _transaction = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.charge_on = kwargs.get('charge_on', None)
        self.created_on = kwargs.get('created_on', None)
        self.installment_payment = kwargs.get('installment_payment', None)
        self.line_items = kwargs.get('line_items', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.transaction = kwargs.get('transaction', None)
        self.version = kwargs.get('version', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
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

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this InstallmentPaymentSlice.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this InstallmentPaymentSlice.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this InstallmentPaymentSlice.
        :type: datetime
        """

        self._created_on = created_on
    
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
    def planned_purge_date(self):
        """Gets the planned_purge_date of this InstallmentPaymentSlice.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this InstallmentPaymentSlice.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this InstallmentPaymentSlice.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this InstallmentPaymentSlice.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this InstallmentPaymentSlice.

            

        :return: The state of this InstallmentPaymentSlice.
        :rtype: InstallmentPaymentSliceState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InstallmentPaymentSlice.

            

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

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this InstallmentPaymentSlice.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InstallmentPaymentSlice.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

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
