# coding: utf-8
import pprint
import six
from enum import Enum



class DocumentTemplate:

    swagger_types = {
    
        'default_template': 'bool',
        'delivery_enabled': 'bool',
        'id': 'int',
        'linked_space_id': 'int',
        'name': 'str',
        'planned_purge_date': 'datetime',
        'space_id': 'int',
        'state': 'CreationEntityState',
        'template_resource': 'ResourcePath',
        'type': 'int',
        'version': 'int',
    }

    attribute_map = {
        'default_template': 'defaultTemplate','delivery_enabled': 'deliveryEnabled','id': 'id','linked_space_id': 'linkedSpaceId','name': 'name','planned_purge_date': 'plannedPurgeDate','space_id': 'spaceId','state': 'state','template_resource': 'templateResource','type': 'type','version': 'version',
    }

    
    _default_template = None
    _delivery_enabled = None
    _id = None
    _linked_space_id = None
    _name = None
    _planned_purge_date = None
    _space_id = None
    _state = None
    _template_resource = None
    _type = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.default_template = kwargs.get('default_template', None)
        self.delivery_enabled = kwargs.get('delivery_enabled', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.space_id = kwargs.get('space_id', None)
        self.state = kwargs.get('state', None)
        self.template_resource = kwargs.get('template_resource', None)
        self.type = kwargs.get('type', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def default_template(self):
        """Gets the default_template of this DocumentTemplate.

            The default document template is used whenever no specific template is specified for a particular template type.

        :return: The default_template of this DocumentTemplate.
        :rtype: bool
        """
        return self._default_template

    @default_template.setter
    def default_template(self, default_template):
        """Sets the default_template of this DocumentTemplate.

            The default document template is used whenever no specific template is specified for a particular template type.

        :param default_template: The default_template of this DocumentTemplate.
        :type: bool
        """

        self._default_template = default_template
    
    @property
    def delivery_enabled(self):
        """Gets the delivery_enabled of this DocumentTemplate.

            

        :return: The delivery_enabled of this DocumentTemplate.
        :rtype: bool
        """
        return self._delivery_enabled

    @delivery_enabled.setter
    def delivery_enabled(self, delivery_enabled):
        """Sets the delivery_enabled of this DocumentTemplate.

            

        :param delivery_enabled: The delivery_enabled of this DocumentTemplate.
        :type: bool
        """

        self._delivery_enabled = delivery_enabled
    
    @property
    def id(self):
        """Gets the id of this DocumentTemplate.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this DocumentTemplate.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentTemplate.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this DocumentTemplate.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this DocumentTemplate.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this DocumentTemplate.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this DocumentTemplate.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this DocumentTemplate.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this DocumentTemplate.

            

        :return: The name of this DocumentTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocumentTemplate.

            

        :param name: The name of this DocumentTemplate.
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this DocumentTemplate.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this DocumentTemplate.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this DocumentTemplate.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this DocumentTemplate.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def space_id(self):
        """Gets the space_id of this DocumentTemplate.

            

        :return: The space_id of this DocumentTemplate.
        :rtype: int
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this DocumentTemplate.

            

        :param space_id: The space_id of this DocumentTemplate.
        :type: int
        """

        self._space_id = space_id
    
    @property
    def state(self):
        """Gets the state of this DocumentTemplate.

            

        :return: The state of this DocumentTemplate.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DocumentTemplate.

            

        :param state: The state of this DocumentTemplate.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def template_resource(self):
        """Gets the template_resource of this DocumentTemplate.

            

        :return: The template_resource of this DocumentTemplate.
        :rtype: ResourcePath
        """
        return self._template_resource

    @template_resource.setter
    def template_resource(self, template_resource):
        """Sets the template_resource of this DocumentTemplate.

            

        :param template_resource: The template_resource of this DocumentTemplate.
        :type: ResourcePath
        """

        self._template_resource = template_resource
    
    @property
    def type(self):
        """Gets the type of this DocumentTemplate.

            

        :return: The type of this DocumentTemplate.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DocumentTemplate.

            

        :param type: The type of this DocumentTemplate.
        :type: int
        """

        self._type = type
    
    @property
    def version(self):
        """Gets the version of this DocumentTemplate.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this DocumentTemplate.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DocumentTemplate.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this DocumentTemplate.
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
        if issubclass(DocumentTemplate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, DocumentTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
