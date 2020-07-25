# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionAffiliateUpdate:

    swagger_types = {
    
        'id': 'int',
        'version': 'int',
        'language': 'str',
        'meta_data': 'dict(str, str)',
        'name': 'str',
        'state': 'CreationEntityState',
    }

    attribute_map = {
        'id': 'id','version': 'version','language': 'language','meta_data': 'metaData','name': 'name','state': 'state',
    }

    
    _id = None
    _version = None
    _language = None
    _meta_data = None
    _name = None
    _state = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id')

        self.version = kwargs.get('version')

        self.language = kwargs.get('language', None)
        self.meta_data = kwargs.get('meta_data', None)
        self.name = kwargs.get('name', None)
        self.state = kwargs.get('state', None)
        

    
    @property
    def id(self):
        """Gets the id of this SubscriptionAffiliateUpdate.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this SubscriptionAffiliateUpdate.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionAffiliateUpdate.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this SubscriptionAffiliateUpdate.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id
    
    @property
    def version(self):
        """Gets the version of this SubscriptionAffiliateUpdate.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this SubscriptionAffiliateUpdate.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SubscriptionAffiliateUpdate.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this SubscriptionAffiliateUpdate.
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")

        self._version = version
    
    @property
    def language(self):
        """Gets the language of this SubscriptionAffiliateUpdate.

            

        :return: The language of this SubscriptionAffiliateUpdate.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SubscriptionAffiliateUpdate.

            

        :param language: The language of this SubscriptionAffiliateUpdate.
        :type: str
        """

        self._language = language
    
    @property
    def meta_data(self):
        """Gets the meta_data of this SubscriptionAffiliateUpdate.

            Meta data allow to store additional data along the object.

        :return: The meta_data of this SubscriptionAffiliateUpdate.
        :rtype: dict(str, str)
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this SubscriptionAffiliateUpdate.

            Meta data allow to store additional data along the object.

        :param meta_data: The meta_data of this SubscriptionAffiliateUpdate.
        :type: dict(str, str)
        """

        self._meta_data = meta_data
    
    @property
    def name(self):
        """Gets the name of this SubscriptionAffiliateUpdate.

            

        :return: The name of this SubscriptionAffiliateUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionAffiliateUpdate.

            

        :param name: The name of this SubscriptionAffiliateUpdate.
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")
        if name is not None and len(name) < 3:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `3`")

        self._name = name
    
    @property
    def state(self):
        """Gets the state of this SubscriptionAffiliateUpdate.

            

        :return: The state of this SubscriptionAffiliateUpdate.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubscriptionAffiliateUpdate.

            

        :param state: The state of this SubscriptionAffiliateUpdate.
        :type: CreationEntityState
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
        if issubclass(SubscriptionAffiliateUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionAffiliateUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
