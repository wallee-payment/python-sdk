# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentTerminalDevice:

    swagger_types = {
    
        'account': 'Account',
        'created_on': 'datetime',
        'id': 'int',
        'model': 'PaymentTerminalDeviceModel',
        'name': 'str',
        'serial_number': 'str',
        'state': 'PaymentTerminalDeviceState',
        'terminal': 'PaymentTerminalReference',
        'version': 'int',
    }

    attribute_map = {
        'account': 'account','created_on': 'createdOn','id': 'id','model': 'model','name': 'name','serial_number': 'serialNumber','state': 'state','terminal': 'terminal','version': 'version',
    }

    
    _account = None
    _created_on = None
    _id = None
    _model = None
    _name = None
    _serial_number = None
    _state = None
    _terminal = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.account = kwargs.get('account', None)
        self.created_on = kwargs.get('created_on', None)
        self.id = kwargs.get('id', None)
        self.model = kwargs.get('model', None)
        self.name = kwargs.get('name', None)
        self.serial_number = kwargs.get('serial_number', None)
        self.state = kwargs.get('state', None)
        self.terminal = kwargs.get('terminal', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def account(self):
        """Gets the account of this PaymentTerminalDevice.

            

        :return: The account of this PaymentTerminalDevice.
        :rtype: Account
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this PaymentTerminalDevice.

            

        :param account: The account of this PaymentTerminalDevice.
        :type: Account
        """

        self._account = account
    
    @property
    def created_on(self):
        """Gets the created_on of this PaymentTerminalDevice.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this PaymentTerminalDevice.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this PaymentTerminalDevice.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this PaymentTerminalDevice.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def id(self):
        """Gets the id of this PaymentTerminalDevice.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentTerminalDevice.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentTerminalDevice.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentTerminalDevice.
        :type: int
        """

        self._id = id
    
    @property
    def model(self):
        """Gets the model of this PaymentTerminalDevice.

            

        :return: The model of this PaymentTerminalDevice.
        :rtype: PaymentTerminalDeviceModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this PaymentTerminalDevice.

            

        :param model: The model of this PaymentTerminalDevice.
        :type: PaymentTerminalDeviceModel
        """

        self._model = model
    
    @property
    def name(self):
        """Gets the name of this PaymentTerminalDevice.

            

        :return: The name of this PaymentTerminalDevice.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentTerminalDevice.

            

        :param name: The name of this PaymentTerminalDevice.
        :type: str
        """

        self._name = name
    
    @property
    def serial_number(self):
        """Gets the serial_number of this PaymentTerminalDevice.

            

        :return: The serial_number of this PaymentTerminalDevice.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this PaymentTerminalDevice.

            

        :param serial_number: The serial_number of this PaymentTerminalDevice.
        :type: str
        """

        self._serial_number = serial_number
    
    @property
    def state(self):
        """Gets the state of this PaymentTerminalDevice.

            

        :return: The state of this PaymentTerminalDevice.
        :rtype: PaymentTerminalDeviceState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentTerminalDevice.

            

        :param state: The state of this PaymentTerminalDevice.
        :type: PaymentTerminalDeviceState
        """

        self._state = state
    
    @property
    def terminal(self):
        """Gets the terminal of this PaymentTerminalDevice.

            

        :return: The terminal of this PaymentTerminalDevice.
        :rtype: PaymentTerminalReference
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this PaymentTerminalDevice.

            

        :param terminal: The terminal of this PaymentTerminalDevice.
        :type: PaymentTerminalReference
        """

        self._terminal = terminal
    
    @property
    def version(self):
        """Gets the version of this PaymentTerminalDevice.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this PaymentTerminalDevice.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PaymentTerminalDevice.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this PaymentTerminalDevice.
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
        if issubclass(PaymentTerminalDevice, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentTerminalDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
