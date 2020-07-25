# coding: utf-8
import pprint
import six
from enum import Enum



class Scope:

    swagger_types = {
    
        'domain_name': 'str',
        'features': 'list[Feature]',
        'id': 'int',
        'machine_name': 'str',
        'name': 'str',
        'planned_purge_date': 'datetime',
        'port': 'int',
        'ssl_active': 'bool',
        'state': 'CreationEntityState',
        'themes': 'list[str]',
        'url': 'str',
        'version': 'int',
    }

    attribute_map = {
        'domain_name': 'domainName','features': 'features','id': 'id','machine_name': 'machineName','name': 'name','planned_purge_date': 'plannedPurgeDate','port': 'port','ssl_active': 'sslActive','state': 'state','themes': 'themes','url': 'url','version': 'version',
    }

    
    _domain_name = None
    _features = None
    _id = None
    _machine_name = None
    _name = None
    _planned_purge_date = None
    _port = None
    _ssl_active = None
    _state = None
    _themes = None
    _url = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.domain_name = kwargs.get('domain_name', None)
        self.features = kwargs.get('features', None)
        self.id = kwargs.get('id', None)
        self.machine_name = kwargs.get('machine_name', None)
        self.name = kwargs.get('name', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.port = kwargs.get('port', None)
        self.ssl_active = kwargs.get('ssl_active', None)
        self.state = kwargs.get('state', None)
        self.themes = kwargs.get('themes', None)
        self.url = kwargs.get('url', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def domain_name(self):
        """Gets the domain_name of this Scope.

            The domain name to which this scope is mapped to.

        :return: The domain_name of this Scope.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this Scope.

            The domain name to which this scope is mapped to.

        :param domain_name: The domain_name of this Scope.
        :type: str
        """
        if domain_name is not None and len(domain_name) > 40:
            raise ValueError("Invalid value for `domain_name`, length must be less than or equal to `40`")

        self._domain_name = domain_name
    
    @property
    def features(self):
        """Gets the features of this Scope.

            

        :return: The features of this Scope.
        :rtype: list[Feature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this Scope.

            

        :param features: The features of this Scope.
        :type: list[Feature]
        """

        self._features = features
    
    @property
    def id(self):
        """Gets the id of this Scope.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this Scope.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Scope.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this Scope.
        :type: int
        """

        self._id = id
    
    @property
    def machine_name(self):
        """Gets the machine_name of this Scope.

            

        :return: The machine_name of this Scope.
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        """Sets the machine_name of this Scope.

            

        :param machine_name: The machine_name of this Scope.
        :type: str
        """
        if machine_name is not None and len(machine_name) > 50:
            raise ValueError("Invalid value for `machine_name`, length must be less than or equal to `50`")

        self._machine_name = machine_name
    
    @property
    def name(self):
        """Gets the name of this Scope.

            The name of the scope is shown to the user where the user should select a scope.

        :return: The name of this Scope.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Scope.

            The name of the scope is shown to the user where the user should select a scope.

        :param name: The name of this Scope.
        :type: str
        """
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")

        self._name = name
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this Scope.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this Scope.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this Scope.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this Scope.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def port(self):
        """Gets the port of this Scope.

            The port number to which this scope is mapped to.

        :return: The port of this Scope.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this Scope.

            The port number to which this scope is mapped to.

        :param port: The port of this Scope.
        :type: int
        """

        self._port = port
    
    @property
    def ssl_active(self):
        """Gets the ssl_active of this Scope.

            Define whether the scope supports SSL.

        :return: The ssl_active of this Scope.
        :rtype: bool
        """
        return self._ssl_active

    @ssl_active.setter
    def ssl_active(self, ssl_active):
        """Sets the ssl_active of this Scope.

            Define whether the scope supports SSL.

        :param ssl_active: The ssl_active of this Scope.
        :type: bool
        """

        self._ssl_active = ssl_active
    
    @property
    def state(self):
        """Gets the state of this Scope.

            

        :return: The state of this Scope.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Scope.

            

        :param state: The state of this Scope.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def themes(self):
        """Gets the themes of this Scope.

            The themes determines how the application layout, look and feel is. By providing multiple themes you can fallback to other themes.

        :return: The themes of this Scope.
        :rtype: list[str]
        """
        return self._themes

    @themes.setter
    def themes(self, themes):
        """Sets the themes of this Scope.

            The themes determines how the application layout, look and feel is. By providing multiple themes you can fallback to other themes.

        :param themes: The themes of this Scope.
        :type: list[str]
        """

        self._themes = themes
    
    @property
    def url(self):
        """Gets the url of this Scope.

            

        :return: The url of this Scope.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Scope.

            

        :param url: The url of this Scope.
        :type: str
        """

        self._url = url
    
    @property
    def version(self):
        """Gets the version of this Scope.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this Scope.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Scope.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this Scope.
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
        if issubclass(Scope, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Scope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
