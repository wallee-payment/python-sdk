# coding: utf-8
import pprint
import six
from enum import Enum
from . import TransactionAwareEntity


class TransactionLineItemVersion(TransactionAwareEntity):

    swagger_types = {
    
        'amount': 'float',
        'created_by': 'int',
        'created_on': 'datetime',
        'language': 'str',
        'line_items': 'list[LineItem]',
        'planned_purge_date': 'datetime',
        'space_view_id': 'int',
        'tax_amount': 'float',
        'transaction': 'Transaction',
        'version': 'int',
    }

    attribute_map = {
        'amount': 'amount','created_by': 'createdBy','created_on': 'createdOn','language': 'language','line_items': 'lineItems','planned_purge_date': 'plannedPurgeDate','space_view_id': 'spaceViewId','tax_amount': 'taxAmount','transaction': 'transaction','version': 'version',
    }

    
    _amount = None
    _created_by = None
    _created_on = None
    _language = None
    _line_items = None
    _planned_purge_date = None
    _space_view_id = None
    _tax_amount = None
    _transaction = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.amount = kwargs.get('amount', None)
        self.created_by = kwargs.get('created_by', None)
        self.created_on = kwargs.get('created_on', None)
        self.language = kwargs.get('language', None)
        self.line_items = kwargs.get('line_items', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.space_view_id = kwargs.get('space_view_id', None)
        self.tax_amount = kwargs.get('tax_amount', None)
        self.transaction = kwargs.get('transaction', None)
        self.version = kwargs.get('version', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def amount(self):
        """Gets the amount of this TransactionLineItemVersion.

            

        :return: The amount of this TransactionLineItemVersion.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransactionLineItemVersion.

            

        :param amount: The amount of this TransactionLineItemVersion.
        :type: float
        """

        self._amount = amount
    
    @property
    def created_by(self):
        """Gets the created_by of this TransactionLineItemVersion.

            

        :return: The created_by of this TransactionLineItemVersion.
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this TransactionLineItemVersion.

            

        :param created_by: The created_by of this TransactionLineItemVersion.
        :type: int
        """

        self._created_by = created_by
    
    @property
    def created_on(self):
        """Gets the created_on of this TransactionLineItemVersion.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this TransactionLineItemVersion.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this TransactionLineItemVersion.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this TransactionLineItemVersion.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def language(self):
        """Gets the language of this TransactionLineItemVersion.

            

        :return: The language of this TransactionLineItemVersion.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this TransactionLineItemVersion.

            

        :param language: The language of this TransactionLineItemVersion.
        :type: str
        """

        self._language = language
    
    @property
    def line_items(self):
        """Gets the line_items of this TransactionLineItemVersion.

            

        :return: The line_items of this TransactionLineItemVersion.
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this TransactionLineItemVersion.

            

        :param line_items: The line_items of this TransactionLineItemVersion.
        :type: list[LineItem]
        """

        self._line_items = line_items
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this TransactionLineItemVersion.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this TransactionLineItemVersion.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this TransactionLineItemVersion.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this TransactionLineItemVersion.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def space_view_id(self):
        """Gets the space_view_id of this TransactionLineItemVersion.

            

        :return: The space_view_id of this TransactionLineItemVersion.
        :rtype: int
        """
        return self._space_view_id

    @space_view_id.setter
    def space_view_id(self, space_view_id):
        """Sets the space_view_id of this TransactionLineItemVersion.

            

        :param space_view_id: The space_view_id of this TransactionLineItemVersion.
        :type: int
        """

        self._space_view_id = space_view_id
    
    @property
    def tax_amount(self):
        """Gets the tax_amount of this TransactionLineItemVersion.

            

        :return: The tax_amount of this TransactionLineItemVersion.
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this TransactionLineItemVersion.

            

        :param tax_amount: The tax_amount of this TransactionLineItemVersion.
        :type: float
        """

        self._tax_amount = tax_amount
    
    @property
    def transaction(self):
        """Gets the transaction of this TransactionLineItemVersion.

            

        :return: The transaction of this TransactionLineItemVersion.
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this TransactionLineItemVersion.

            

        :param transaction: The transaction of this TransactionLineItemVersion.
        :type: Transaction
        """

        self._transaction = transaction
    
    @property
    def version(self):
        """Gets the version of this TransactionLineItemVersion.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this TransactionLineItemVersion.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TransactionLineItemVersion.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this TransactionLineItemVersion.
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
        if issubclass(TransactionLineItemVersion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, TransactionLineItemVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
