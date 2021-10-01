# coding: utf-8
import pprint
import six
from enum import Enum



class Role:

    swagger_types = {
    
        'account': 'Account',
        'id': 'int',
        'name': 'DatabaseTranslatedString',
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

            The account to which this role belongs to. This role can only be assigned within the assigned account and the sub accounts of the assigned account.

        :return: The account of this Role.
        :rtype: Account
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this Role.

            The account to which this role belongs to. This role can only be assigned within the assigned account and the sub accounts of the assigned account.

        :param account: The account of this Role.
        :type: Account
        """

        self._account = account
    
    @property
    def id(self):
        """Gets the id of this Role.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this Role.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Role.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this Role.
        :type: int
        """

        self._id = id
    
    @property
    def name(self):
        """Gets the name of this Role.

            The name of this role is used to identify the role within administrative interfaces.

        :return: The name of this Role.
        :rtype: DatabaseTranslatedString
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Role.

            The name of this role is used to identify the role within administrative interfaces.

        :param name: The name of this Role.
        :type: DatabaseTranslatedString
        """

        self._name = name
    
    @property
    def permissions(self):
        """Gets the permissions of this Role.

            Set of permissions that are granted to this role.

        :return: The permissions of this Role.
        :rtype: list[Permission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this Role.

            Set of permissions that are granted to this role.

        :param permissions: The permissions of this Role.
        :type: list[Permission]
        """

        self._permissions = permissions
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this Role.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this Role.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this Role.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this Role.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this Role.

            

        :return: The state of this Role.
        :rtype: RoleState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Role.

            

        :param state: The state of this Role.
        :type: RoleState
        """

        self._state = state
    
    @property
    def two_factor_required(self):
        """Gets the two_factor_required of this Role.

            Defines whether having been granted this role will force a user to use two-factor authentication.

        :return: The two_factor_required of this Role.
        :rtype: bool
        """
        return self._two_factor_required

    @two_factor_required.setter
    def two_factor_required(self, two_factor_required):
        """Sets the two_factor_required of this Role.

            Defines whether having been granted this role will force a user to use two-factor authentication.

        :param two_factor_required: The two_factor_required of this Role.
        :type: bool
        """

        self._two_factor_required = two_factor_required
    
    @property
    def version(self):
        """Gets the version of this Role.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this Role.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Role.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

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
