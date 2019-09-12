# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentTerminalDeviceModel:

    swagger_types = {
    
        'description': 'DatabaseTranslatedString',
        'id': 'int',
        'image': 'list[str]',
        'image_type': 'str',
        'manufacturer': 'PaymentTerminalDeviceManufacturer',
        'name': 'str',
        'planned_purge_date': 'datetime',
        'state': 'CreationEntityState',
        'title': 'DatabaseTranslatedString',
        'version': 'int',
    }

    attribute_map = {
        'description': 'description','id': 'id','image': 'image','image_type': 'imageType','manufacturer': 'manufacturer','name': 'name','planned_purge_date': 'plannedPurgeDate','state': 'state','title': 'title','version': 'version',
    }

    
    _description = None
    _id = None
    _image = None
    _image_type = None
    _manufacturer = None
    _name = None
    _planned_purge_date = None
    _state = None
    _title = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.description = kwargs.get('description', None)
        self.id = kwargs.get('id', None)
        self.image = kwargs.get('image', None)
        self.image_type = kwargs.get('image_type', None)
        self.manufacturer = kwargs.get('manufacturer', None)
        self.name = kwargs.get('name', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.title = kwargs.get('title', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def description(self):
        """Gets the description of this PaymentTerminalDeviceModel.

            

        :return: The description of this PaymentTerminalDeviceModel.
        :rtype: DatabaseTranslatedString
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PaymentTerminalDeviceModel.

            

        :param description: The description of this PaymentTerminalDeviceModel.
        :type: DatabaseTranslatedString
        """

        self._description = description
    
    @property
    def id(self):
        """Gets the id of this PaymentTerminalDeviceModel.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentTerminalDeviceModel.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentTerminalDeviceModel.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentTerminalDeviceModel.
        :type: int
        """

        self._id = id
    
    @property
    def image(self):
        """Gets the image of this PaymentTerminalDeviceModel.

            

        :return: The image of this PaymentTerminalDeviceModel.
        :rtype: list[str]
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this PaymentTerminalDeviceModel.

            

        :param image: The image of this PaymentTerminalDeviceModel.
        :type: list[str]
        """

        self._image = image
    
    @property
    def image_type(self):
        """Gets the image_type of this PaymentTerminalDeviceModel.

            

        :return: The image_type of this PaymentTerminalDeviceModel.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this PaymentTerminalDeviceModel.

            

        :param image_type: The image_type of this PaymentTerminalDeviceModel.
        :type: str
        """

        self._image_type = image_type
    
    @property
    def manufacturer(self):
        """Gets the manufacturer of this PaymentTerminalDeviceModel.

            

        :return: The manufacturer of this PaymentTerminalDeviceModel.
        :rtype: PaymentTerminalDeviceManufacturer
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this PaymentTerminalDeviceModel.

            

        :param manufacturer: The manufacturer of this PaymentTerminalDeviceModel.
        :type: PaymentTerminalDeviceManufacturer
        """

        self._manufacturer = manufacturer
    
    @property
    def name(self):
        """Gets the name of this PaymentTerminalDeviceModel.

            

        :return: The name of this PaymentTerminalDeviceModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentTerminalDeviceModel.

            

        :param name: The name of this PaymentTerminalDeviceModel.
        :type: str
        """

        self._name = name
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this PaymentTerminalDeviceModel.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this PaymentTerminalDeviceModel.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this PaymentTerminalDeviceModel.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this PaymentTerminalDeviceModel.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this PaymentTerminalDeviceModel.

            

        :return: The state of this PaymentTerminalDeviceModel.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentTerminalDeviceModel.

            

        :param state: The state of this PaymentTerminalDeviceModel.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def title(self):
        """Gets the title of this PaymentTerminalDeviceModel.

            

        :return: The title of this PaymentTerminalDeviceModel.
        :rtype: DatabaseTranslatedString
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PaymentTerminalDeviceModel.

            

        :param title: The title of this PaymentTerminalDeviceModel.
        :type: DatabaseTranslatedString
        """

        self._title = title
    
    @property
    def version(self):
        """Gets the version of this PaymentTerminalDeviceModel.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this PaymentTerminalDeviceModel.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PaymentTerminalDeviceModel.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this PaymentTerminalDeviceModel.
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
        if issubclass(PaymentTerminalDeviceModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentTerminalDeviceModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
