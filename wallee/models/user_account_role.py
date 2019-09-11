# coding: utf-8
import pprint
import six
from enum import Enum



class UserAccountRole:

    swagger_types = {
    
        'account': 'int',
        'applies_on_sub_account': 'bool',
        'id': 'int',
        'role': 'int',
        'user': 'int',
        'version': 'int',
    }

    attribute_map = {
        'account': 'account','applies_on_sub_account': 'appliesOnSubAccount','id': 'id','role': 'role','user': 'user','version': 'version',
    }

    
    _account = None
    _applies_on_sub_account = None
    _id = None
    _role = None
    _user = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.account = kwargs.get('account', None)
        self.applies_on_sub_account = kwargs.get('applies_on_sub_account', None)
        self.id = kwargs.get('id', None)
        self.role = kwargs.get('role', None)
        self.user = kwargs.get('user', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def account(self):
        """Gets the account of this UserAccountRole.

            

        :return: The account of this UserAccountRole.
        :rtype: int
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this UserAccountRole.

            

        :param account: The account of this UserAccountRole.
        :type: int
        """

        self._account = account
    
    @property
    def applies_on_sub_account(self):
        """Gets the applies_on_sub_account of this UserAccountRole.

            

        :return: The applies_on_sub_account of this UserAccountRole.
        :rtype: bool
        """
        return self._applies_on_sub_account

    @applies_on_sub_account.setter
    def applies_on_sub_account(self, applies_on_sub_account):
        """Sets the applies_on_sub_account of this UserAccountRole.

            

        :param applies_on_sub_account: The applies_on_sub_account of this UserAccountRole.
        :type: bool
        """

        self._applies_on_sub_account = applies_on_sub_account
    
    @property
    def id(self):
        """Gets the id of this UserAccountRole.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this UserAccountRole.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserAccountRole.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this UserAccountRole.
        :type: int
        """

        self._id = id
    
    @property
    def role(self):
        """Gets the role of this UserAccountRole.

            

        :return: The role of this UserAccountRole.
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UserAccountRole.

            

        :param role: The role of this UserAccountRole.
        :type: int
        """

        self._role = role
    
    @property
    def user(self):
        """Gets the user of this UserAccountRole.

            

        :return: The user of this UserAccountRole.
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserAccountRole.

            

        :param user: The user of this UserAccountRole.
        :type: int
        """

        self._user = user
    
    @property
    def version(self):
        """Gets the version of this UserAccountRole.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this UserAccountRole.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UserAccountRole.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this UserAccountRole.
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
        if issubclass(UserAccountRole, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, UserAccountRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
