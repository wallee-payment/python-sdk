# coding: utf-8
import pprint
import six
from enum import Enum



class DebtCollectionReceipt:

    swagger_types = {
    
        'amount': 'float',
        'created_by': 'int',
        'created_on': 'datetime',
        'debt_collection_case': 'int',
        'external_id': 'str',
        'id': 'int',
        'linked_space_id': 'int',
        'planned_purge_date': 'datetime',
        'source': 'int',
        'version': 'int',
    }

    attribute_map = {
        'amount': 'amount','created_by': 'createdBy','created_on': 'createdOn','debt_collection_case': 'debtCollectionCase','external_id': 'externalId','id': 'id','linked_space_id': 'linkedSpaceId','planned_purge_date': 'plannedPurgeDate','source': 'source','version': 'version',
    }

    
    _amount = None
    _created_by = None
    _created_on = None
    _debt_collection_case = None
    _external_id = None
    _id = None
    _linked_space_id = None
    _planned_purge_date = None
    _source = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.amount = kwargs.get('amount', None)
        self.created_by = kwargs.get('created_by', None)
        self.created_on = kwargs.get('created_on', None)
        self.debt_collection_case = kwargs.get('debt_collection_case', None)
        self.external_id = kwargs.get('external_id', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.source = kwargs.get('source', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def amount(self):
        """Gets the amount of this DebtCollectionReceipt.

            

        :return: The amount of this DebtCollectionReceipt.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this DebtCollectionReceipt.

            

        :param amount: The amount of this DebtCollectionReceipt.
        :type: float
        """

        self._amount = amount
    
    @property
    def created_by(self):
        """Gets the created_by of this DebtCollectionReceipt.

            The created by field indicates the user which has created the receipt.

        :return: The created_by of this DebtCollectionReceipt.
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this DebtCollectionReceipt.

            The created by field indicates the user which has created the receipt.

        :param created_by: The created_by of this DebtCollectionReceipt.
        :type: int
        """

        self._created_by = created_by
    
    @property
    def created_on(self):
        """Gets the created_on of this DebtCollectionReceipt.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this DebtCollectionReceipt.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this DebtCollectionReceipt.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this DebtCollectionReceipt.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def debt_collection_case(self):
        """Gets the debt_collection_case of this DebtCollectionReceipt.

            

        :return: The debt_collection_case of this DebtCollectionReceipt.
        :rtype: int
        """
        return self._debt_collection_case

    @debt_collection_case.setter
    def debt_collection_case(self, debt_collection_case):
        """Sets the debt_collection_case of this DebtCollectionReceipt.

            

        :param debt_collection_case: The debt_collection_case of this DebtCollectionReceipt.
        :type: int
        """

        self._debt_collection_case = debt_collection_case
    
    @property
    def external_id(self):
        """Gets the external_id of this DebtCollectionReceipt.

            The external id is a unique identifier for the receipt. The external id has to be unique in combination with the debt collection case. When a receipt is sent with an existing external id the existing one is returned rather than a new one is created.

        :return: The external_id of this DebtCollectionReceipt.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this DebtCollectionReceipt.

            The external id is a unique identifier for the receipt. The external id has to be unique in combination with the debt collection case. When a receipt is sent with an existing external id the existing one is returned rather than a new one is created.

        :param external_id: The external_id of this DebtCollectionReceipt.
        :type: str
        """
        if external_id is not None and len(external_id) > 100:
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `100`")
        if external_id is not None and len(external_id) < 1:
            raise ValueError("Invalid value for `external_id`, length must be greater than or equal to `1`")

        self._external_id = external_id
    
    @property
    def id(self):
        """Gets the id of this DebtCollectionReceipt.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this DebtCollectionReceipt.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DebtCollectionReceipt.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this DebtCollectionReceipt.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this DebtCollectionReceipt.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this DebtCollectionReceipt.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this DebtCollectionReceipt.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this DebtCollectionReceipt.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this DebtCollectionReceipt.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this DebtCollectionReceipt.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this DebtCollectionReceipt.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this DebtCollectionReceipt.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def source(self):
        """Gets the source of this DebtCollectionReceipt.

            

        :return: The source of this DebtCollectionReceipt.
        :rtype: int
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DebtCollectionReceipt.

            

        :param source: The source of this DebtCollectionReceipt.
        :type: int
        """

        self._source = source
    
    @property
    def version(self):
        """Gets the version of this DebtCollectionReceipt.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this DebtCollectionReceipt.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DebtCollectionReceipt.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this DebtCollectionReceipt.
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
        if issubclass(DebtCollectionReceipt, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, DebtCollectionReceipt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
