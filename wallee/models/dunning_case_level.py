# coding: utf-8
import pprint
import six
from enum import Enum



class DunningCaseLevel:

    swagger_types = {
    
        'canceled_on': 'datetime',
        'created_on': 'datetime',
        'dunning_case': 'DunningCase',
        'environment': 'Environment',
        'failed_on': 'datetime',
        'flow_level': 'int',
        'id': 'int',
        'invoice': 'int',
        'language': 'str',
        'linked_space_id': 'int',
        'linked_transaction': 'int',
        'most_recent_level': 'bool',
        'planned_purge_date': 'datetime',
        'state': 'DunningCaseLevelState',
        'succeeded_on': 'datetime',
        'timeout_on': 'datetime',
        'version': 'int',
    }

    attribute_map = {
        'canceled_on': 'canceledOn','created_on': 'createdOn','dunning_case': 'dunningCase','environment': 'environment','failed_on': 'failedOn','flow_level': 'flowLevel','id': 'id','invoice': 'invoice','language': 'language','linked_space_id': 'linkedSpaceId','linked_transaction': 'linkedTransaction','most_recent_level': 'mostRecentLevel','planned_purge_date': 'plannedPurgeDate','state': 'state','succeeded_on': 'succeededOn','timeout_on': 'timeoutOn','version': 'version',
    }

    
    _canceled_on = None
    _created_on = None
    _dunning_case = None
    _environment = None
    _failed_on = None
    _flow_level = None
    _id = None
    _invoice = None
    _language = None
    _linked_space_id = None
    _linked_transaction = None
    _most_recent_level = None
    _planned_purge_date = None
    _state = None
    _succeeded_on = None
    _timeout_on = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.canceled_on = kwargs.get('canceled_on', None)
        self.created_on = kwargs.get('created_on', None)
        self.dunning_case = kwargs.get('dunning_case', None)
        self.environment = kwargs.get('environment', None)
        self.failed_on = kwargs.get('failed_on', None)
        self.flow_level = kwargs.get('flow_level', None)
        self.id = kwargs.get('id', None)
        self.invoice = kwargs.get('invoice', None)
        self.language = kwargs.get('language', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.linked_transaction = kwargs.get('linked_transaction', None)
        self.most_recent_level = kwargs.get('most_recent_level', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.succeeded_on = kwargs.get('succeeded_on', None)
        self.timeout_on = kwargs.get('timeout_on', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def canceled_on(self):
        """Gets the canceled_on of this DunningCaseLevel.

            

        :return: The canceled_on of this DunningCaseLevel.
        :rtype: datetime
        """
        return self._canceled_on

    @canceled_on.setter
    def canceled_on(self, canceled_on):
        """Sets the canceled_on of this DunningCaseLevel.

            

        :param canceled_on: The canceled_on of this DunningCaseLevel.
        :type: datetime
        """

        self._canceled_on = canceled_on
    
    @property
    def created_on(self):
        """Gets the created_on of this DunningCaseLevel.

            The date and time when the object was created.

        :return: The created_on of this DunningCaseLevel.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this DunningCaseLevel.

            The date and time when the object was created.

        :param created_on: The created_on of this DunningCaseLevel.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def dunning_case(self):
        """Gets the dunning_case of this DunningCaseLevel.

            

        :return: The dunning_case of this DunningCaseLevel.
        :rtype: DunningCase
        """
        return self._dunning_case

    @dunning_case.setter
    def dunning_case(self, dunning_case):
        """Sets the dunning_case of this DunningCaseLevel.

            

        :param dunning_case: The dunning_case of this DunningCaseLevel.
        :type: DunningCase
        """

        self._dunning_case = dunning_case
    
    @property
    def environment(self):
        """Gets the environment of this DunningCaseLevel.

            The environment used when rendering resources.

        :return: The environment of this DunningCaseLevel.
        :rtype: Environment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this DunningCaseLevel.

            The environment used when rendering resources.

        :param environment: The environment of this DunningCaseLevel.
        :type: Environment
        """

        self._environment = environment
    
    @property
    def failed_on(self):
        """Gets the failed_on of this DunningCaseLevel.

            

        :return: The failed_on of this DunningCaseLevel.
        :rtype: datetime
        """
        return self._failed_on

    @failed_on.setter
    def failed_on(self, failed_on):
        """Sets the failed_on of this DunningCaseLevel.

            

        :param failed_on: The failed_on of this DunningCaseLevel.
        :type: datetime
        """

        self._failed_on = failed_on
    
    @property
    def flow_level(self):
        """Gets the flow_level of this DunningCaseLevel.

            

        :return: The flow_level of this DunningCaseLevel.
        :rtype: int
        """
        return self._flow_level

    @flow_level.setter
    def flow_level(self, flow_level):
        """Sets the flow_level of this DunningCaseLevel.

            

        :param flow_level: The flow_level of this DunningCaseLevel.
        :type: int
        """

        self._flow_level = flow_level
    
    @property
    def id(self):
        """Gets the id of this DunningCaseLevel.

            A unique identifier for the object.

        :return: The id of this DunningCaseLevel.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DunningCaseLevel.

            A unique identifier for the object.

        :param id: The id of this DunningCaseLevel.
        :type: int
        """

        self._id = id
    
    @property
    def invoice(self):
        """Gets the invoice of this DunningCaseLevel.

            

        :return: The invoice of this DunningCaseLevel.
        :rtype: int
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this DunningCaseLevel.

            

        :param invoice: The invoice of this DunningCaseLevel.
        :type: int
        """

        self._invoice = invoice
    
    @property
    def language(self):
        """Gets the language of this DunningCaseLevel.

            The language that is linked to the object.

        :return: The language of this DunningCaseLevel.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this DunningCaseLevel.

            The language that is linked to the object.

        :param language: The language of this DunningCaseLevel.
        :type: str
        """

        self._language = language
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this DunningCaseLevel.

            The ID of the space this object belongs to.

        :return: The linked_space_id of this DunningCaseLevel.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this DunningCaseLevel.

            The ID of the space this object belongs to.

        :param linked_space_id: The linked_space_id of this DunningCaseLevel.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def linked_transaction(self):
        """Gets the linked_transaction of this DunningCaseLevel.

            The payment transaction this object is linked to.

        :return: The linked_transaction of this DunningCaseLevel.
        :rtype: int
        """
        return self._linked_transaction

    @linked_transaction.setter
    def linked_transaction(self, linked_transaction):
        """Sets the linked_transaction of this DunningCaseLevel.

            The payment transaction this object is linked to.

        :param linked_transaction: The linked_transaction of this DunningCaseLevel.
        :type: int
        """

        self._linked_transaction = linked_transaction
    
    @property
    def most_recent_level(self):
        """Gets the most_recent_level of this DunningCaseLevel.

            

        :return: The most_recent_level of this DunningCaseLevel.
        :rtype: bool
        """
        return self._most_recent_level

    @most_recent_level.setter
    def most_recent_level(self, most_recent_level):
        """Sets the most_recent_level of this DunningCaseLevel.

            

        :param most_recent_level: The most_recent_level of this DunningCaseLevel.
        :type: bool
        """

        self._most_recent_level = most_recent_level
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this DunningCaseLevel.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :return: The planned_purge_date of this DunningCaseLevel.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this DunningCaseLevel.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :param planned_purge_date: The planned_purge_date of this DunningCaseLevel.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this DunningCaseLevel.

            The object's current state.

        :return: The state of this DunningCaseLevel.
        :rtype: DunningCaseLevelState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DunningCaseLevel.

            The object's current state.

        :param state: The state of this DunningCaseLevel.
        :type: DunningCaseLevelState
        """

        self._state = state
    
    @property
    def succeeded_on(self):
        """Gets the succeeded_on of this DunningCaseLevel.

            

        :return: The succeeded_on of this DunningCaseLevel.
        :rtype: datetime
        """
        return self._succeeded_on

    @succeeded_on.setter
    def succeeded_on(self, succeeded_on):
        """Sets the succeeded_on of this DunningCaseLevel.

            

        :param succeeded_on: The succeeded_on of this DunningCaseLevel.
        :type: datetime
        """

        self._succeeded_on = succeeded_on
    
    @property
    def timeout_on(self):
        """Gets the timeout_on of this DunningCaseLevel.

            

        :return: The timeout_on of this DunningCaseLevel.
        :rtype: datetime
        """
        return self._timeout_on

    @timeout_on.setter
    def timeout_on(self, timeout_on):
        """Sets the timeout_on of this DunningCaseLevel.

            

        :param timeout_on: The timeout_on of this DunningCaseLevel.
        :type: datetime
        """

        self._timeout_on = timeout_on
    
    @property
    def version(self):
        """Gets the version of this DunningCaseLevel.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :return: The version of this DunningCaseLevel.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DunningCaseLevel.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :param version: The version of this DunningCaseLevel.
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
        if issubclass(DunningCaseLevel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, DunningCaseLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
