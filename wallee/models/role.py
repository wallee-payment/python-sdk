# coding: utf-8
import pprint
import six
from enum import Enum



class Role:

    swagger_types = {
    
        'account': 'Account',
        'id': 'int',
        'name': 'dict(str, str)',
        'permissions': 'list[Permission]',
        'planned_purge_date': 'datetime',
        'state': 'RoleState',
        'two_factor_required': 'bool',
        'version': 'int',
    }

    attribute_map = {
        'account': 'account','id': 'id','name': 'name','permissions': 'permissions','planned_purge_date': 'plannedPurgeDate','state': 'state','two_factor_required': 'twoFactorRequired','version': 'version',
    }

    
    _account = None
    _id = None
    _name = None
    _permissions = None
    _planned_purge_date = None
    _state = None
    _two_factor_required = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.account = kwargs.get('account', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.permissions = kwargs.get('permissions', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.two_factor_required = kwargs.get('two_factor_required', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def account(self):
        """Gets the account of this Role.

            The account the role belongs to. The role can only be assigned within this account.

        :return: The account of this Role.
        :rtype: Account
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this Role.

            The account the role belongs to. The role can only be assigned within this account.

        :param account: The account of this Role.
        :type: Account
        """

        self._account = account
    
    @property
    def id(self):
        """Gets the id of this Role.

            A unique identifier for the object.

        :return: The id of this Role.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Role.

            A unique identifier for the object.

        :param id: The id of this Role.
        :type: int
        """

        self._id = id
    
    @property
    def name(self):
        """Gets the name of this Role.

            The name used to identify the role.

        :return: The name of this Role.
        :rtype: dict(str, str)
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Role.

            The name used to identify the role.

        :param name: The name of this Role.
        :type: dict(str, str)
        """

        self._name = name
    
    @property
    def permissions(self):
        """Gets the permissions of this Role.

            The permissions granted to users with this role.

        :return: The permissions of this Role.
        :rtype: list[Permission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this Role.

            The permissions granted to users with this role.

        :param permissions: The permissions of this Role.
        :type: list[Permission]
        """

        self._permissions = permissions
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this Role.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :return: The planned_purge_date of this Role.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this Role.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :param planned_purge_date: The planned_purge_date of this Role.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this Role.

            The object's current state.

        :return: The state of this Role.
        :rtype: RoleState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Role.

            The object's current state.

        :param state: The state of this Role.
        :type: RoleState
        """

        self._state = state
    
    @property
    def two_factor_required(self):
        """Gets the two_factor_required of this Role.

            Whether users with this role are required to use two-factor authentication.

        :return: The two_factor_required of this Role.
        :rtype: bool
        """
        return self._two_factor_required

    @two_factor_required.setter
    def two_factor_required(self, two_factor_required):
        """Sets the two_factor_required of this Role.

            Whether users with this role are required to use two-factor authentication.

        :param two_factor_required: The two_factor_required of this Role.
        :type: bool
        """

        self._two_factor_required = two_factor_required
    
    @property
    def version(self):
        """Gets the version of this Role.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :return: The version of this Role.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Role.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :param version: The version of this Role.
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
        if issubclass(Role, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Role):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
