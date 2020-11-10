# coding: utf-8
import pprint
import six
from enum import Enum



class Account:

    swagger_types = {
    
        'active': 'bool',
        'active_or_restricted_active': 'bool',
        'created_by': 'int',
        'created_on': 'datetime',
        'deleted_by': 'int',
        'deleted_on': 'datetime',
        'id': 'int',
        'last_modified_date': 'datetime',
        'name': 'str',
        'parent_account': 'Account',
        'planned_purge_date': 'datetime',
        'restricted_active': 'bool',
        'scope': 'int',
        'state': 'AccountState',
        'subaccount_limit': 'int',
        'type': 'AccountType',
        'version': 'int',
    }

    attribute_map = {
        'active': 'active','active_or_restricted_active': 'activeOrRestrictedActive','created_by': 'createdBy','created_on': 'createdOn','deleted_by': 'deletedBy','deleted_on': 'deletedOn','id': 'id','last_modified_date': 'lastModifiedDate','name': 'name','parent_account': 'parentAccount','planned_purge_date': 'plannedPurgeDate','restricted_active': 'restrictedActive','scope': 'scope','state': 'state','subaccount_limit': 'subaccountLimit','type': 'type','version': 'version',
    }

    
    _active = None
    _active_or_restricted_active = None
    _created_by = None
    _created_on = None
    _deleted_by = None
    _deleted_on = None
    _id = None
    _last_modified_date = None
    _name = None
    _parent_account = None
    _planned_purge_date = None
    _restricted_active = None
    _scope = None
    _state = None
    _subaccount_limit = None
    _type = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.active = kwargs.get('active', None)
        self.active_or_restricted_active = kwargs.get('active_or_restricted_active', None)
        self.created_by = kwargs.get('created_by', None)
        self.created_on = kwargs.get('created_on', None)
        self.deleted_by = kwargs.get('deleted_by', None)
        self.deleted_on = kwargs.get('deleted_on', None)
        self.id = kwargs.get('id', None)
        self.last_modified_date = kwargs.get('last_modified_date', None)
        self.name = kwargs.get('name', None)
        self.parent_account = kwargs.get('parent_account', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.restricted_active = kwargs.get('restricted_active', None)
        self.scope = kwargs.get('scope', None)
        self.state = kwargs.get('state', None)
        self.subaccount_limit = kwargs.get('subaccount_limit', None)
        self.type = kwargs.get('type', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def active(self):
        """Gets the active of this Account.

            Active means that this account and all accounts in the hierarchy are active.

        :return: The active of this Account.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Account.

            Active means that this account and all accounts in the hierarchy are active.

        :param active: The active of this Account.
        :type: bool
        """

        self._active = active
    
    @property
    def active_or_restricted_active(self):
        """Gets the active_or_restricted_active of this Account.

            This property is true when all accounts in the hierarchy are active or restricted active.

        :return: The active_or_restricted_active of this Account.
        :rtype: bool
        """
        return self._active_or_restricted_active

    @active_or_restricted_active.setter
    def active_or_restricted_active(self, active_or_restricted_active):
        """Sets the active_or_restricted_active of this Account.

            This property is true when all accounts in the hierarchy are active or restricted active.

        :param active_or_restricted_active: The active_or_restricted_active of this Account.
        :type: bool
        """

        self._active_or_restricted_active = active_or_restricted_active
    
    @property
    def created_by(self):
        """Gets the created_by of this Account.

            The ID of the user who created this entity.

        :return: The created_by of this Account.
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Account.

            The ID of the user who created this entity.

        :param created_by: The created_by of this Account.
        :type: int
        """

        self._created_by = created_by
    
    @property
    def created_on(self):
        """Gets the created_on of this Account.

            The date and time when this entity was created.

        :return: The created_on of this Account.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Account.

            The date and time when this entity was created.

        :param created_on: The created_on of this Account.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def deleted_by(self):
        """Gets the deleted_by of this Account.

            The ID of a user that deleted this entity.

        :return: The deleted_by of this Account.
        :rtype: int
        """
        return self._deleted_by

    @deleted_by.setter
    def deleted_by(self, deleted_by):
        """Sets the deleted_by of this Account.

            The ID of a user that deleted this entity.

        :param deleted_by: The deleted_by of this Account.
        :type: int
        """

        self._deleted_by = deleted_by
    
    @property
    def deleted_on(self):
        """Gets the deleted_on of this Account.

            The date and time when this entity was deleted.

        :return: The deleted_on of this Account.
        :rtype: datetime
        """
        return self._deleted_on

    @deleted_on.setter
    def deleted_on(self, deleted_on):
        """Sets the deleted_on of this Account.

            The date and time when this entity was deleted.

        :param deleted_on: The deleted_on of this Account.
        :type: datetime
        """

        self._deleted_on = deleted_on
    
    @property
    def id(self):
        """Gets the id of this Account.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this Account.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Account.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this Account.
        :type: int
        """

        self._id = id
    
    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this Account.

            

        :return: The last_modified_date of this Account.
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this Account.

            

        :param last_modified_date: The last_modified_date of this Account.
        :type: datetime
        """

        self._last_modified_date = last_modified_date
    
    @property
    def name(self):
        """Gets the name of this Account.

            The name of the account identifies the account within the administrative interface.

        :return: The name of this Account.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Account.

            The name of the account identifies the account within the administrative interface.

        :param name: The name of this Account.
        :type: str
        """
        if name is not None and len(name) > 200:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")
        if name is not None and len(name) < 3:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `3`")

        self._name = name
    
    @property
    def parent_account(self):
        """Gets the parent_account of this Account.

            The account which is responsible for administering the account.

        :return: The parent_account of this Account.
        :rtype: Account
        """
        return self._parent_account

    @parent_account.setter
    def parent_account(self, parent_account):
        """Sets the parent_account of this Account.

            The account which is responsible for administering the account.

        :param parent_account: The parent_account of this Account.
        :type: Account
        """

        self._parent_account = parent_account
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this Account.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this Account.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this Account.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this Account.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def restricted_active(self):
        """Gets the restricted_active of this Account.

            Restricted active means that at least one account in the hierarchy is only restricted active, but all are either restricted active or active.

        :return: The restricted_active of this Account.
        :rtype: bool
        """
        return self._restricted_active

    @restricted_active.setter
    def restricted_active(self, restricted_active):
        """Sets the restricted_active of this Account.

            Restricted active means that at least one account in the hierarchy is only restricted active, but all are either restricted active or active.

        :param restricted_active: The restricted_active of this Account.
        :type: bool
        """

        self._restricted_active = restricted_active
    
    @property
    def scope(self):
        """Gets the scope of this Account.

            This is the scope to which the account belongs to.

        :return: The scope of this Account.
        :rtype: int
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this Account.

            This is the scope to which the account belongs to.

        :param scope: The scope of this Account.
        :type: int
        """

        self._scope = scope
    
    @property
    def state(self):
        """Gets the state of this Account.

            

        :return: The state of this Account.
        :rtype: AccountState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Account.

            

        :param state: The state of this Account.
        :type: AccountState
        """

        self._state = state
    
    @property
    def subaccount_limit(self):
        """Gets the subaccount_limit of this Account.

            This property restricts the number of subaccounts which can be created within this account.

        :return: The subaccount_limit of this Account.
        :rtype: int
        """
        return self._subaccount_limit

    @subaccount_limit.setter
    def subaccount_limit(self, subaccount_limit):
        """Sets the subaccount_limit of this Account.

            This property restricts the number of subaccounts which can be created within this account.

        :param subaccount_limit: The subaccount_limit of this Account.
        :type: int
        """

        self._subaccount_limit = subaccount_limit
    
    @property
    def type(self):
        """Gets the type of this Account.

            The account type defines which role and capabilities it has.

        :return: The type of this Account.
        :rtype: AccountType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Account.

            The account type defines which role and capabilities it has.

        :param type: The type of this Account.
        :type: AccountType
        """

        self._type = type
    
    @property
    def version(self):
        """Gets the version of this Account.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this Account.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Account.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this Account.
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
        if issubclass(Account, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Account):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
