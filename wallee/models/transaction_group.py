# coding: utf-8
import pprint
import six
from enum import Enum



class TransactionGroup:

    swagger_types = {
    
        'begin_date': 'datetime',
        'customer_id': 'str',
        'end_date': 'datetime',
        'id': 'int',
        'linked_space_id': 'int',
        'planned_purge_date': 'datetime',
        'state': 'TransactionGroupState',
        'version': 'int',
    }

    attribute_map = {
        'begin_date': 'beginDate','customer_id': 'customerId','end_date': 'endDate','id': 'id','linked_space_id': 'linkedSpaceId','planned_purge_date': 'plannedPurgeDate','state': 'state','version': 'version',
    }

    
    _begin_date = None
    _customer_id = None
    _end_date = None
    _id = None
    _linked_space_id = None
    _planned_purge_date = None
    _state = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.begin_date = kwargs.get('begin_date', None)
        self.customer_id = kwargs.get('customer_id', None)
        self.end_date = kwargs.get('end_date', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def begin_date(self):
        """Gets the begin_date of this TransactionGroup.

            

        :return: The begin_date of this TransactionGroup.
        :rtype: datetime
        """
        return self._begin_date

    @begin_date.setter
    def begin_date(self, begin_date):
        """Sets the begin_date of this TransactionGroup.

            

        :param begin_date: The begin_date of this TransactionGroup.
        :type: datetime
        """

        self._begin_date = begin_date
    
    @property
    def customer_id(self):
        """Gets the customer_id of this TransactionGroup.

            

        :return: The customer_id of this TransactionGroup.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this TransactionGroup.

            

        :param customer_id: The customer_id of this TransactionGroup.
        :type: str
        """
        if customer_id is not None and len(customer_id) > 100:
            raise ValueError("Invalid value for `customer_id`, length must be less than or equal to `100`")

        self._customer_id = customer_id
    
    @property
    def end_date(self):
        """Gets the end_date of this TransactionGroup.

            

        :return: The end_date of this TransactionGroup.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TransactionGroup.

            

        :param end_date: The end_date of this TransactionGroup.
        :type: datetime
        """

        self._end_date = end_date
    
    @property
    def id(self):
        """Gets the id of this TransactionGroup.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this TransactionGroup.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransactionGroup.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this TransactionGroup.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this TransactionGroup.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this TransactionGroup.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this TransactionGroup.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this TransactionGroup.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this TransactionGroup.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this TransactionGroup.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this TransactionGroup.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this TransactionGroup.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this TransactionGroup.

            

        :return: The state of this TransactionGroup.
        :rtype: TransactionGroupState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TransactionGroup.

            

        :param state: The state of this TransactionGroup.
        :type: TransactionGroupState
        """

        self._state = state
    
    @property
    def version(self):
        """Gets the version of this TransactionGroup.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this TransactionGroup.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TransactionGroup.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this TransactionGroup.
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
        if issubclass(TransactionGroup, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, TransactionGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
