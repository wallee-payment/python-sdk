# coding: utf-8
import pprint
import six
from enum import Enum



class InstallmentPayment:

    swagger_types = {
    
        'created_on': 'datetime',
        'id': 'int',
        'initial_transaction': 'Transaction',
        'line_items': 'list[LineItem]',
        'linked_space_id': 'int',
        'plan_configuration': 'int',
        'planned_purge_date': 'datetime',
        'state': 'InstallmentPaymentState',
        'version': 'int',
    }

    attribute_map = {
        'created_on': 'createdOn','id': 'id','initial_transaction': 'initialTransaction','line_items': 'lineItems','linked_space_id': 'linkedSpaceId','plan_configuration': 'planConfiguration','planned_purge_date': 'plannedPurgeDate','state': 'state','version': 'version',
    }

    
    _created_on = None
    _id = None
    _initial_transaction = None
    _line_items = None
    _linked_space_id = None
    _plan_configuration = None
    _planned_purge_date = None
    _state = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.created_on = kwargs.get('created_on', None)
        self.id = kwargs.get('id', None)
        self.initial_transaction = kwargs.get('initial_transaction', None)
        self.line_items = kwargs.get('line_items', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.plan_configuration = kwargs.get('plan_configuration', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def created_on(self):
        """Gets the created_on of this InstallmentPayment.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this InstallmentPayment.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this InstallmentPayment.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this InstallmentPayment.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def id(self):
        """Gets the id of this InstallmentPayment.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this InstallmentPayment.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InstallmentPayment.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this InstallmentPayment.
        :type: int
        """

        self._id = id
    
    @property
    def initial_transaction(self):
        """Gets the initial_transaction of this InstallmentPayment.

            

        :return: The initial_transaction of this InstallmentPayment.
        :rtype: Transaction
        """
        return self._initial_transaction

    @initial_transaction.setter
    def initial_transaction(self, initial_transaction):
        """Sets the initial_transaction of this InstallmentPayment.

            

        :param initial_transaction: The initial_transaction of this InstallmentPayment.
        :type: Transaction
        """

        self._initial_transaction = initial_transaction
    
    @property
    def line_items(self):
        """Gets the line_items of this InstallmentPayment.

            

        :return: The line_items of this InstallmentPayment.
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this InstallmentPayment.

            

        :param line_items: The line_items of this InstallmentPayment.
        :type: list[LineItem]
        """

        self._line_items = line_items
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this InstallmentPayment.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this InstallmentPayment.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this InstallmentPayment.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this InstallmentPayment.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def plan_configuration(self):
        """Gets the plan_configuration of this InstallmentPayment.

            

        :return: The plan_configuration of this InstallmentPayment.
        :rtype: int
        """
        return self._plan_configuration

    @plan_configuration.setter
    def plan_configuration(self, plan_configuration):
        """Sets the plan_configuration of this InstallmentPayment.

            

        :param plan_configuration: The plan_configuration of this InstallmentPayment.
        :type: int
        """

        self._plan_configuration = plan_configuration
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this InstallmentPayment.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this InstallmentPayment.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this InstallmentPayment.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this InstallmentPayment.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this InstallmentPayment.

            

        :return: The state of this InstallmentPayment.
        :rtype: InstallmentPaymentState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InstallmentPayment.

            

        :param state: The state of this InstallmentPayment.
        :type: InstallmentPaymentState
        """

        self._state = state
    
    @property
    def version(self):
        """Gets the version of this InstallmentPayment.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this InstallmentPayment.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InstallmentPayment.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this InstallmentPayment.
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
        if issubclass(InstallmentPayment, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, InstallmentPayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
