# coding: utf-8
import pprint
import six
from enum import Enum
from . import AbstractAccountUpdate


class AccountCreate(AbstractAccountUpdate):

    swagger_types = {
    
        'parent_account': 'int',
        'scope': 'int',
    }

    attribute_map = {
        'parent_account': 'parentAccount','scope': 'scope',
    }

    
    _parent_account = None
    _scope = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.parent_account = kwargs.get('parent_account', None)
        self.scope = kwargs.get('scope')

        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def parent_account(self):
        """Gets the parent_account of this AccountCreate.

            The account which is responsible for administering the account.

        :return: The parent_account of this AccountCreate.
        :rtype: int
        """
        return self._parent_account

    @parent_account.setter
    def parent_account(self, parent_account):
        """Sets the parent_account of this AccountCreate.

            The account which is responsible for administering the account.

        :param parent_account: The parent_account of this AccountCreate.
        :type: int
        """

        self._parent_account = parent_account
    
    @property
    def scope(self):
        """Gets the scope of this AccountCreate.

            This is the scope to which the account belongs to.

        :return: The scope of this AccountCreate.
        :rtype: int
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this AccountCreate.

            This is the scope to which the account belongs to.

        :param scope: The scope of this AccountCreate.
        :type: int
        """
        if scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")

        self._scope = scope
    

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
        if issubclass(AccountCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AccountCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
