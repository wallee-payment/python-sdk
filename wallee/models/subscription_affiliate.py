# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionAffiliate:

    swagger_types = {
    
        'external_id': 'str',
        'id': 'int',
        'language': 'str',
        'linked_space_id': 'int',
        'meta_data': 'dict(str, str)',
        'name': 'str',
        'planned_purge_date': 'datetime',
        'reference': 'str',
        'state': 'CreationEntityState',
        'version': 'int',
    }

    attribute_map = {
        'external_id': 'externalId','id': 'id','language': 'language','linked_space_id': 'linkedSpaceId','meta_data': 'metaData','name': 'name','planned_purge_date': 'plannedPurgeDate','reference': 'reference','state': 'state','version': 'version',
    }

    
    _external_id = None
    _id = None
    _language = None
    _linked_space_id = None
    _meta_data = None
    _name = None
    _planned_purge_date = None
    _reference = None
    _state = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.external_id = kwargs.get('external_id', None)
        self.id = kwargs.get('id', None)
        self.language = kwargs.get('language', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.meta_data = kwargs.get('meta_data', None)
        self.name = kwargs.get('name', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.reference = kwargs.get('reference', None)
        self.state = kwargs.get('state', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def external_id(self):
        """Gets the external_id of this SubscriptionAffiliate.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :return: The external_id of this SubscriptionAffiliate.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this SubscriptionAffiliate.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :param external_id: The external_id of this SubscriptionAffiliate.
        :type: str
        """

        self._external_id = external_id
    
    @property
    def id(self):
        """Gets the id of this SubscriptionAffiliate.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this SubscriptionAffiliate.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionAffiliate.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this SubscriptionAffiliate.
        :type: int
        """

        self._id = id
    
    @property
    def language(self):
        """Gets the language of this SubscriptionAffiliate.

            

        :return: The language of this SubscriptionAffiliate.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SubscriptionAffiliate.

            

        :param language: The language of this SubscriptionAffiliate.
        :type: str
        """

        self._language = language
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this SubscriptionAffiliate.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this SubscriptionAffiliate.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this SubscriptionAffiliate.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this SubscriptionAffiliate.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def meta_data(self):
        """Gets the meta_data of this SubscriptionAffiliate.

            Meta data allow to store additional data along the object.

        :return: The meta_data of this SubscriptionAffiliate.
        :rtype: dict(str, str)
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this SubscriptionAffiliate.

            Meta data allow to store additional data along the object.

        :param meta_data: The meta_data of this SubscriptionAffiliate.
        :type: dict(str, str)
        """

        self._meta_data = meta_data
    
    @property
    def name(self):
        """Gets the name of this SubscriptionAffiliate.

            

        :return: The name of this SubscriptionAffiliate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionAffiliate.

            

        :param name: The name of this SubscriptionAffiliate.
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")
        if name is not None and len(name) < 3:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `3`")

        self._name = name
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this SubscriptionAffiliate.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this SubscriptionAffiliate.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this SubscriptionAffiliate.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this SubscriptionAffiliate.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def reference(self):
        """Gets the reference of this SubscriptionAffiliate.

            

        :return: The reference of this SubscriptionAffiliate.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this SubscriptionAffiliate.

            

        :param reference: The reference of this SubscriptionAffiliate.
        :type: str
        """
        if reference is not None and len(reference) > 100:
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `100`")
        if reference is not None and len(reference) < 3:
            raise ValueError("Invalid value for `reference`, length must be greater than or equal to `3`")

        self._reference = reference
    
    @property
    def state(self):
        """Gets the state of this SubscriptionAffiliate.

            

        :return: The state of this SubscriptionAffiliate.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubscriptionAffiliate.

            

        :param state: The state of this SubscriptionAffiliate.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def version(self):
        """Gets the version of this SubscriptionAffiliate.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this SubscriptionAffiliate.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SubscriptionAffiliate.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this SubscriptionAffiliate.
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
        if issubclass(SubscriptionAffiliate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionAffiliate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
