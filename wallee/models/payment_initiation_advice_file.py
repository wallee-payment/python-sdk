# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentInitiationAdviceFile:

    swagger_types = {
    
        'created_on': 'datetime',
        'file_generated_on': 'datetime',
        'id': 'int',
        'linked_space_id': 'int',
        'name': 'str',
        'processed_on': 'datetime',
        'processor': 'PaymentProcessor',
        'state': 'PaymentInitiationAdviceFileState',
    }

    attribute_map = {
        'created_on': 'createdOn','file_generated_on': 'fileGeneratedOn','id': 'id','linked_space_id': 'linkedSpaceId','name': 'name','processed_on': 'processedOn','processor': 'processor','state': 'state',
    }

    
    _created_on = None
    _file_generated_on = None
    _id = None
    _linked_space_id = None
    _name = None
    _processed_on = None
    _processor = None
    _state = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.created_on = kwargs.get('created_on', None)
        self.file_generated_on = kwargs.get('file_generated_on', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.processed_on = kwargs.get('processed_on', None)
        self.processor = kwargs.get('processor', None)
        self.state = kwargs.get('state', None)
        

    
    @property
    def created_on(self):
        """Gets the created_on of this PaymentInitiationAdviceFile.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this PaymentInitiationAdviceFile.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this PaymentInitiationAdviceFile.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this PaymentInitiationAdviceFile.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def file_generated_on(self):
        """Gets the file_generated_on of this PaymentInitiationAdviceFile.

            

        :return: The file_generated_on of this PaymentInitiationAdviceFile.
        :rtype: datetime
        """
        return self._file_generated_on

    @file_generated_on.setter
    def file_generated_on(self, file_generated_on):
        """Sets the file_generated_on of this PaymentInitiationAdviceFile.

            

        :param file_generated_on: The file_generated_on of this PaymentInitiationAdviceFile.
        :type: datetime
        """

        self._file_generated_on = file_generated_on
    
    @property
    def id(self):
        """Gets the id of this PaymentInitiationAdviceFile.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentInitiationAdviceFile.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentInitiationAdviceFile.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentInitiationAdviceFile.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this PaymentInitiationAdviceFile.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this PaymentInitiationAdviceFile.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this PaymentInitiationAdviceFile.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this PaymentInitiationAdviceFile.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this PaymentInitiationAdviceFile.

            

        :return: The name of this PaymentInitiationAdviceFile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentInitiationAdviceFile.

            

        :param name: The name of this PaymentInitiationAdviceFile.
        :type: str
        """

        self._name = name
    
    @property
    def processed_on(self):
        """Gets the processed_on of this PaymentInitiationAdviceFile.

            

        :return: The processed_on of this PaymentInitiationAdviceFile.
        :rtype: datetime
        """
        return self._processed_on

    @processed_on.setter
    def processed_on(self, processed_on):
        """Sets the processed_on of this PaymentInitiationAdviceFile.

            

        :param processed_on: The processed_on of this PaymentInitiationAdviceFile.
        :type: datetime
        """

        self._processed_on = processed_on
    
    @property
    def processor(self):
        """Gets the processor of this PaymentInitiationAdviceFile.

            

        :return: The processor of this PaymentInitiationAdviceFile.
        :rtype: PaymentProcessor
        """
        return self._processor

    @processor.setter
    def processor(self, processor):
        """Sets the processor of this PaymentInitiationAdviceFile.

            

        :param processor: The processor of this PaymentInitiationAdviceFile.
        :type: PaymentProcessor
        """

        self._processor = processor
    
    @property
    def state(self):
        """Gets the state of this PaymentInitiationAdviceFile.

            

        :return: The state of this PaymentInitiationAdviceFile.
        :rtype: PaymentInitiationAdviceFileState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentInitiationAdviceFile.

            

        :param state: The state of this PaymentInitiationAdviceFile.
        :type: PaymentInitiationAdviceFileState
        """

        self._state = state
    

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
        if issubclass(PaymentInitiationAdviceFile, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentInitiationAdviceFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
