# coding: utf-8
import pprint
import six
from enum import Enum
from . import AbstractSpaceUpdate


class SpaceCreate(AbstractSpaceUpdate):

    swagger_types = {
    
        'account': 'int',
        'database': 'int',
    }

    attribute_map = {
        'account': 'account','database': 'database',
    }

    
    _account = None
    _database = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.account = kwargs.get('account')

        self.database = kwargs.get('database', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def account(self):
        """Gets the account of this SpaceCreate.

            The account that the space belongs to.

        :return: The account of this SpaceCreate.
        :rtype: int
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this SpaceCreate.

            The account that the space belongs to.

        :param account: The account of this SpaceCreate.
        :type: int
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")

        self._account = account
    
    @property
    def database(self):
        """Gets the database of this SpaceCreate.

            The database the space is connected to and that holds the space's data.

        :return: The database of this SpaceCreate.
        :rtype: int
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this SpaceCreate.

            The database the space is connected to and that holds the space's data.

        :param database: The database of this SpaceCreate.
        :type: int
        """

        self._database = database
    

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
        if issubclass(SpaceCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SpaceCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
