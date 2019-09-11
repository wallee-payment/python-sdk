# coding: utf-8
import pprint
import six
from enum import Enum
from . import TransactionAwareEntity


class ConnectorInvocation(TransactionAwareEntity):

    swagger_types = {
    
        'created_on': 'datetime',
        'planned_purge_date': 'datetime',
        'stage': 'ConnectorInvocationStage',
        'time_took_in_milliseconds': 'int',
        'transaction': 'int',
        'version': 'int',
    }

    attribute_map = {
        'created_on': 'createdOn','planned_purge_date': 'plannedPurgeDate','stage': 'stage','time_took_in_milliseconds': 'timeTookInMilliseconds','transaction': 'transaction','version': 'version',
    }

    
    _created_on = None
    _planned_purge_date = None
    _stage = None
    _time_took_in_milliseconds = None
    _transaction = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.created_on = kwargs.get('created_on', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.stage = kwargs.get('stage', None)
        self.time_took_in_milliseconds = kwargs.get('time_took_in_milliseconds', None)
        self.transaction = kwargs.get('transaction', None)
        self.version = kwargs.get('version', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def created_on(self):
        """Gets the created_on of this ConnectorInvocation.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this ConnectorInvocation.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this ConnectorInvocation.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this ConnectorInvocation.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this ConnectorInvocation.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this ConnectorInvocation.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this ConnectorInvocation.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this ConnectorInvocation.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def stage(self):
        """Gets the stage of this ConnectorInvocation.

            

        :return: The stage of this ConnectorInvocation.
        :rtype: ConnectorInvocationStage
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this ConnectorInvocation.

            

        :param stage: The stage of this ConnectorInvocation.
        :type: ConnectorInvocationStage
        """

        self._stage = stage
    
    @property
    def time_took_in_milliseconds(self):
        """Gets the time_took_in_milliseconds of this ConnectorInvocation.

            

        :return: The time_took_in_milliseconds of this ConnectorInvocation.
        :rtype: int
        """
        return self._time_took_in_milliseconds

    @time_took_in_milliseconds.setter
    def time_took_in_milliseconds(self, time_took_in_milliseconds):
        """Sets the time_took_in_milliseconds of this ConnectorInvocation.

            

        :param time_took_in_milliseconds: The time_took_in_milliseconds of this ConnectorInvocation.
        :type: int
        """

        self._time_took_in_milliseconds = time_took_in_milliseconds
    
    @property
    def transaction(self):
        """Gets the transaction of this ConnectorInvocation.

            

        :return: The transaction of this ConnectorInvocation.
        :rtype: int
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this ConnectorInvocation.

            

        :param transaction: The transaction of this ConnectorInvocation.
        :type: int
        """

        self._transaction = transaction
    
    @property
    def version(self):
        """Gets the version of this ConnectorInvocation.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ConnectorInvocation.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ConnectorInvocation.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ConnectorInvocation.
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
        if issubclass(ConnectorInvocation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ConnectorInvocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
