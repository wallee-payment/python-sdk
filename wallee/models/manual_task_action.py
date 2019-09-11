# coding: utf-8
import pprint
import six
from enum import Enum



class ManualTaskAction:

    swagger_types = {
    
        'id': 'int',
        'label': 'dict(str, str)',
        'style': 'ManualTaskActionStyle',
        'task_type': 'int',
    }

    attribute_map = {
        'id': 'id','label': 'label','style': 'style','task_type': 'taskType',
    }

    
    _id = None
    _label = None
    _style = None
    _task_type = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id', None)
        self.label = kwargs.get('label', None)
        self.style = kwargs.get('style', None)
        self.task_type = kwargs.get('task_type', None)
        

    
    @property
    def id(self):
        """Gets the id of this ManualTaskAction.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this ManualTaskAction.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ManualTaskAction.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this ManualTaskAction.
        :type: int
        """

        self._id = id
    
    @property
    def label(self):
        """Gets the label of this ManualTaskAction.

            

        :return: The label of this ManualTaskAction.
        :rtype: dict(str, str)
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ManualTaskAction.

            

        :param label: The label of this ManualTaskAction.
        :type: dict(str, str)
        """

        self._label = label
    
    @property
    def style(self):
        """Gets the style of this ManualTaskAction.

            

        :return: The style of this ManualTaskAction.
        :rtype: ManualTaskActionStyle
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this ManualTaskAction.

            

        :param style: The style of this ManualTaskAction.
        :type: ManualTaskActionStyle
        """

        self._style = style
    
    @property
    def task_type(self):
        """Gets the task_type of this ManualTaskAction.

            

        :return: The task_type of this ManualTaskAction.
        :rtype: int
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this ManualTaskAction.

            

        :param task_type: The task_type of this ManualTaskAction.
        :type: int
        """

        self._task_type = task_type
    

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
        if issubclass(ManualTaskAction, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ManualTaskAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
