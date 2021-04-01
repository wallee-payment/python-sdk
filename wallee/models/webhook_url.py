# coding: utf-8
import pprint
import six
from enum import Enum



class WebhookUrl:

    swagger_types = {
    
        'application_managed': 'bool',
        'id': 'int',
        'linked_space_id': 'int',
        'name': 'str',
        'planned_purge_date': 'datetime',
        'state': 'CreationEntityState',
        'url': 'str',
        'version': 'int',
    }

    attribute_map = {
        'application_managed': 'applicationManaged','id': 'id','linked_space_id': 'linkedSpaceId','name': 'name','planned_purge_date': 'plannedPurgeDate','state': 'state','url': 'url','version': 'version',
    }

    
    _application_managed = None
    _id = None
    _linked_space_id = None
    _name = None
    _planned_purge_date = None
    _state = None
    _url = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.application_managed = kwargs.get('application_managed', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.url = kwargs.get('url', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def application_managed(self):
        """Gets the application_managed of this WebhookUrl.

            The webhook URL is managed by the application and cannot be changed via the user interface.

        :return: The application_managed of this WebhookUrl.
        :rtype: bool
        """
        return self._application_managed

    @application_managed.setter
    def application_managed(self, application_managed):
        """Sets the application_managed of this WebhookUrl.

            The webhook URL is managed by the application and cannot be changed via the user interface.

        :param application_managed: The application_managed of this WebhookUrl.
        :type: bool
        """

        self._application_managed = application_managed
    
    @property
    def id(self):
        """Gets the id of this WebhookUrl.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this WebhookUrl.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookUrl.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this WebhookUrl.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this WebhookUrl.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this WebhookUrl.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this WebhookUrl.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this WebhookUrl.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this WebhookUrl.

            The URL name is used internally to identify the URL in administrative interfaces. For example it is used within search fields and hence it should be distinct and descriptive.

        :return: The name of this WebhookUrl.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebhookUrl.

            The URL name is used internally to identify the URL in administrative interfaces. For example it is used within search fields and hence it should be distinct and descriptive.

        :param name: The name of this WebhookUrl.
        :type: str
        """
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")

        self._name = name
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this WebhookUrl.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this WebhookUrl.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this WebhookUrl.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this WebhookUrl.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this WebhookUrl.

            

        :return: The state of this WebhookUrl.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this WebhookUrl.

            

        :param state: The state of this WebhookUrl.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def url(self):
        """Gets the url of this WebhookUrl.

            The URL to which the HTTP requests are sent to. An example URL could look like https://www.example.com/some/path?some-query-parameter=value.

        :return: The url of this WebhookUrl.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebhookUrl.

            The URL to which the HTTP requests are sent to. An example URL could look like https://www.example.com/some/path?some-query-parameter=value.

        :param url: The url of this WebhookUrl.
        :type: str
        """
        if url is not None and len(url) > 500:
            raise ValueError("Invalid value for `url`, length must be less than or equal to `500`")
        if url is not None and len(url) < 9:
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `9`")

        self._url = url
    
    @property
    def version(self):
        """Gets the version of this WebhookUrl.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this WebhookUrl.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this WebhookUrl.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this WebhookUrl.
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
        if issubclass(WebhookUrl, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, WebhookUrl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
