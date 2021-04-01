# coding: utf-8
import pprint
import six
from enum import Enum



class Permission:

    swagger_types = {
    
        'description': 'dict(str, str)',
        'feature': 'int',
        'group': 'bool',
        'id': 'int',
        'leaf': 'bool',
        'name': 'dict(str, str)',
        'parent': 'int',
        'path_to_root': 'list[int]',
        'title': 'dict(str, str)',
        'two_factor_required': 'bool',
        'web_app_enabled': 'bool',
    }

    attribute_map = {
        'description': 'description','feature': 'feature','group': 'group','id': 'id','leaf': 'leaf','name': 'name','parent': 'parent','path_to_root': 'pathToRoot','title': 'title','two_factor_required': 'twoFactorRequired','web_app_enabled': 'webAppEnabled',
    }

    
    _description = None
    _feature = None
    _group = None
    _id = None
    _leaf = None
    _name = None
    _parent = None
    _path_to_root = None
    _title = None
    _two_factor_required = None
    _web_app_enabled = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.description = kwargs.get('description', None)
        self.feature = kwargs.get('feature', None)
        self.group = kwargs.get('group', None)
        self.id = kwargs.get('id', None)
        self.leaf = kwargs.get('leaf', None)
        self.name = kwargs.get('name', None)
        self.parent = kwargs.get('parent', None)
        self.path_to_root = kwargs.get('path_to_root', None)
        self.title = kwargs.get('title', None)
        self.two_factor_required = kwargs.get('two_factor_required', None)
        self.web_app_enabled = kwargs.get('web_app_enabled', None)
        

    
    @property
    def description(self):
        """Gets the description of this Permission.

            

        :return: The description of this Permission.
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Permission.

            

        :param description: The description of this Permission.
        :type: dict(str, str)
        """

        self._description = description
    
    @property
    def feature(self):
        """Gets the feature of this Permission.

            

        :return: The feature of this Permission.
        :rtype: int
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this Permission.

            

        :param feature: The feature of this Permission.
        :type: int
        """

        self._feature = feature
    
    @property
    def group(self):
        """Gets the group of this Permission.

            

        :return: The group of this Permission.
        :rtype: bool
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this Permission.

            

        :param group: The group of this Permission.
        :type: bool
        """

        self._group = group
    
    @property
    def id(self):
        """Gets the id of this Permission.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this Permission.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Permission.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this Permission.
        :type: int
        """

        self._id = id
    
    @property
    def leaf(self):
        """Gets the leaf of this Permission.

            

        :return: The leaf of this Permission.
        :rtype: bool
        """
        return self._leaf

    @leaf.setter
    def leaf(self, leaf):
        """Sets the leaf of this Permission.

            

        :param leaf: The leaf of this Permission.
        :type: bool
        """

        self._leaf = leaf
    
    @property
    def name(self):
        """Gets the name of this Permission.

            

        :return: The name of this Permission.
        :rtype: dict(str, str)
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Permission.

            

        :param name: The name of this Permission.
        :type: dict(str, str)
        """

        self._name = name
    
    @property
    def parent(self):
        """Gets the parent of this Permission.

            

        :return: The parent of this Permission.
        :rtype: int
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this Permission.

            

        :param parent: The parent of this Permission.
        :type: int
        """

        self._parent = parent
    
    @property
    def path_to_root(self):
        """Gets the path_to_root of this Permission.

            

        :return: The path_to_root of this Permission.
        :rtype: list[int]
        """
        return self._path_to_root

    @path_to_root.setter
    def path_to_root(self, path_to_root):
        """Sets the path_to_root of this Permission.

            

        :param path_to_root: The path_to_root of this Permission.
        :type: list[int]
        """

        self._path_to_root = path_to_root
    
    @property
    def title(self):
        """Gets the title of this Permission.

            

        :return: The title of this Permission.
        :rtype: dict(str, str)
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Permission.

            

        :param title: The title of this Permission.
        :type: dict(str, str)
        """

        self._title = title
    
    @property
    def two_factor_required(self):
        """Gets the two_factor_required of this Permission.

            

        :return: The two_factor_required of this Permission.
        :rtype: bool
        """
        return self._two_factor_required

    @two_factor_required.setter
    def two_factor_required(self, two_factor_required):
        """Sets the two_factor_required of this Permission.

            

        :param two_factor_required: The two_factor_required of this Permission.
        :type: bool
        """

        self._two_factor_required = two_factor_required
    
    @property
    def web_app_enabled(self):
        """Gets the web_app_enabled of this Permission.

            

        :return: The web_app_enabled of this Permission.
        :rtype: bool
        """
        return self._web_app_enabled

    @web_app_enabled.setter
    def web_app_enabled(self, web_app_enabled):
        """Sets the web_app_enabled of this Permission.

            

        :param web_app_enabled: The web_app_enabled of this Permission.
        :type: bool
        """

        self._web_app_enabled = web_app_enabled
    

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
        if issubclass(Permission, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Permission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
