# coding: utf-8
import pprint
import six
from enum import Enum



class DunningFlowLevel:

    swagger_types = {
    
        'document_text': 'dict(str, str)',
        'flow': 'DunningFlow',
        'id': 'int',
        'linked_space_id': 'int',
        'name': 'str',
        'period': 'str',
        'planned_purge_date': 'datetime',
        'priority': 'int',
        'processor': 'int',
        'reminder_template': 'DocumentTemplate',
        'state': 'CreationEntityState',
        'title': 'dict(str, str)',
        'version': 'int',
    }

    attribute_map = {
        'document_text': 'documentText','flow': 'flow','id': 'id','linked_space_id': 'linkedSpaceId','name': 'name','period': 'period','planned_purge_date': 'plannedPurgeDate','priority': 'priority','processor': 'processor','reminder_template': 'reminderTemplate','state': 'state','title': 'title','version': 'version',
    }

    
    _document_text = None
    _flow = None
    _id = None
    _linked_space_id = None
    _name = None
    _period = None
    _planned_purge_date = None
    _priority = None
    _processor = None
    _reminder_template = None
    _state = None
    _title = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.document_text = kwargs.get('document_text', None)
        self.flow = kwargs.get('flow', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.period = kwargs.get('period', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.priority = kwargs.get('priority', None)
        self.processor = kwargs.get('processor', None)
        self.reminder_template = kwargs.get('reminder_template', None)
        self.state = kwargs.get('state', None)
        self.title = kwargs.get('title', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def document_text(self):
        """Gets the document_text of this DunningFlowLevel.

            This text is put in the reminder document of this dunning flow level.

        :return: The document_text of this DunningFlowLevel.
        :rtype: dict(str, str)
        """
        return self._document_text

    @document_text.setter
    def document_text(self, document_text):
        """Sets the document_text of this DunningFlowLevel.

            This text is put in the reminder document of this dunning flow level.

        :param document_text: The document_text of this DunningFlowLevel.
        :type: dict(str, str)
        """

        self._document_text = document_text
    
    @property
    def flow(self):
        """Gets the flow of this DunningFlowLevel.

            

        :return: The flow of this DunningFlowLevel.
        :rtype: DunningFlow
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this DunningFlowLevel.

            

        :param flow: The flow of this DunningFlowLevel.
        :type: DunningFlow
        """

        self._flow = flow
    
    @property
    def id(self):
        """Gets the id of this DunningFlowLevel.

            A unique identifier for the object.

        :return: The id of this DunningFlowLevel.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DunningFlowLevel.

            A unique identifier for the object.

        :param id: The id of this DunningFlowLevel.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this DunningFlowLevel.

            The ID of the space this object belongs to.

        :return: The linked_space_id of this DunningFlowLevel.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this DunningFlowLevel.

            The ID of the space this object belongs to.

        :param linked_space_id: The linked_space_id of this DunningFlowLevel.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this DunningFlowLevel.

            The dunning flow level name is used internally to identify the dunning flow level. For example the name is used within search fields and hence it should be distinct and descriptive.

        :return: The name of this DunningFlowLevel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DunningFlowLevel.

            The dunning flow level name is used internally to identify the dunning flow level. For example the name is used within search fields and hence it should be distinct and descriptive.

        :param name: The name of this DunningFlowLevel.
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name
    
    @property
    def period(self):
        """Gets the period of this DunningFlowLevel.

            The duration of the level before switching to the next one.

        :return: The period of this DunningFlowLevel.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this DunningFlowLevel.

            The duration of the level before switching to the next one.

        :param period: The period of this DunningFlowLevel.
        :type: str
        """

        self._period = period
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this DunningFlowLevel.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :return: The planned_purge_date of this DunningFlowLevel.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this DunningFlowLevel.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :param planned_purge_date: The planned_purge_date of this DunningFlowLevel.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def priority(self):
        """Gets the priority of this DunningFlowLevel.

            The priority indicates the sort order of the level. A low value indicates that the level is executed before any level with a higher value. Any change to this value affects future level selections. The value has to pe unique per dunning flow.

        :return: The priority of this DunningFlowLevel.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this DunningFlowLevel.

            The priority indicates the sort order of the level. A low value indicates that the level is executed before any level with a higher value. Any change to this value affects future level selections. The value has to pe unique per dunning flow.

        :param priority: The priority of this DunningFlowLevel.
        :type: int
        """

        self._priority = priority
    
    @property
    def processor(self):
        """Gets the processor of this DunningFlowLevel.

            

        :return: The processor of this DunningFlowLevel.
        :rtype: int
        """
        return self._processor

    @processor.setter
    def processor(self, processor):
        """Sets the processor of this DunningFlowLevel.

            

        :param processor: The processor of this DunningFlowLevel.
        :type: int
        """

        self._processor = processor
    
    @property
    def reminder_template(self):
        """Gets the reminder_template of this DunningFlowLevel.

            

        :return: The reminder_template of this DunningFlowLevel.
        :rtype: DocumentTemplate
        """
        return self._reminder_template

    @reminder_template.setter
    def reminder_template(self, reminder_template):
        """Sets the reminder_template of this DunningFlowLevel.

            

        :param reminder_template: The reminder_template of this DunningFlowLevel.
        :type: DocumentTemplate
        """

        self._reminder_template = reminder_template
    
    @property
    def state(self):
        """Gets the state of this DunningFlowLevel.

            The object's current state.

        :return: The state of this DunningFlowLevel.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DunningFlowLevel.

            The object's current state.

        :param state: The state of this DunningFlowLevel.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def title(self):
        """Gets the title of this DunningFlowLevel.

            The title is used to communicate the dunning level to the customer within the reminder.

        :return: The title of this DunningFlowLevel.
        :rtype: dict(str, str)
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DunningFlowLevel.

            The title is used to communicate the dunning level to the customer within the reminder.

        :param title: The title of this DunningFlowLevel.
        :type: dict(str, str)
        """

        self._title = title
    
    @property
    def version(self):
        """Gets the version of this DunningFlowLevel.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :return: The version of this DunningFlowLevel.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DunningFlowLevel.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :param version: The version of this DunningFlowLevel.
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
        if issubclass(DunningFlowLevel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, DunningFlowLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
