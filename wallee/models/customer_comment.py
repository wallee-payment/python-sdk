# coding: utf-8
import pprint
import six
from enum import Enum



class CustomerComment:

    swagger_types = {
    
        'content': 'str',
        'created_by': 'int',
        'created_on': 'datetime',
        'customer': 'int',
        'edited_by': 'int',
        'edited_on': 'datetime',
        'id': 'int',
        'linked_space_id': 'int',
        'pinned': 'bool',
        'version': 'int',
    }

    attribute_map = {
        'content': 'content','created_by': 'createdBy','created_on': 'createdOn','customer': 'customer','edited_by': 'editedBy','edited_on': 'editedOn','id': 'id','linked_space_id': 'linkedSpaceId','pinned': 'pinned','version': 'version',
    }

    
    _content = None
    _created_by = None
    _created_on = None
    _customer = None
    _edited_by = None
    _edited_on = None
    _id = None
    _linked_space_id = None
    _pinned = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.content = kwargs.get('content', None)
        self.created_by = kwargs.get('created_by', None)
        self.created_on = kwargs.get('created_on', None)
        self.customer = kwargs.get('customer', None)
        self.edited_by = kwargs.get('edited_by', None)
        self.edited_on = kwargs.get('edited_on', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.pinned = kwargs.get('pinned', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def content(self):
        """Gets the content of this CustomerComment.

            The comment's actual content.

        :return: The content of this CustomerComment.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CustomerComment.

            The comment's actual content.

        :param content: The content of this CustomerComment.
        :type: str
        """
        if content is not None and len(content) > 262144:
            raise ValueError("Invalid value for `content`, length must be less than or equal to `262144`")

        self._content = content
    
    @property
    def created_by(self):
        """Gets the created_by of this CustomerComment.

            The ID of the user the comment was created by.

        :return: The created_by of this CustomerComment.
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CustomerComment.

            The ID of the user the comment was created by.

        :param created_by: The created_by of this CustomerComment.
        :type: int
        """

        self._created_by = created_by
    
    @property
    def created_on(self):
        """Gets the created_on of this CustomerComment.

            The date and time when the object was created.

        :return: The created_on of this CustomerComment.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this CustomerComment.

            The date and time when the object was created.

        :param created_on: The created_on of this CustomerComment.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def customer(self):
        """Gets the customer of this CustomerComment.

            The customer that the object belongs to.

        :return: The customer of this CustomerComment.
        :rtype: int
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this CustomerComment.

            The customer that the object belongs to.

        :param customer: The customer of this CustomerComment.
        :type: int
        """

        self._customer = customer
    
    @property
    def edited_by(self):
        """Gets the edited_by of this CustomerComment.

            The ID of the user the comment was last updated by.

        :return: The edited_by of this CustomerComment.
        :rtype: int
        """
        return self._edited_by

    @edited_by.setter
    def edited_by(self, edited_by):
        """Sets the edited_by of this CustomerComment.

            The ID of the user the comment was last updated by.

        :param edited_by: The edited_by of this CustomerComment.
        :type: int
        """

        self._edited_by = edited_by
    
    @property
    def edited_on(self):
        """Gets the edited_on of this CustomerComment.

            The date and time when the comment was last updated.

        :return: The edited_on of this CustomerComment.
        :rtype: datetime
        """
        return self._edited_on

    @edited_on.setter
    def edited_on(self, edited_on):
        """Sets the edited_on of this CustomerComment.

            The date and time when the comment was last updated.

        :param edited_on: The edited_on of this CustomerComment.
        :type: datetime
        """

        self._edited_on = edited_on
    
    @property
    def id(self):
        """Gets the id of this CustomerComment.

            A unique identifier for the object.

        :return: The id of this CustomerComment.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomerComment.

            A unique identifier for the object.

        :param id: The id of this CustomerComment.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this CustomerComment.

            The ID of the space this object belongs to.

        :return: The linked_space_id of this CustomerComment.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this CustomerComment.

            The ID of the space this object belongs to.

        :param linked_space_id: The linked_space_id of this CustomerComment.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def pinned(self):
        """Gets the pinned of this CustomerComment.

            Whether the comment is pinned to the top.

        :return: The pinned of this CustomerComment.
        :rtype: bool
        """
        return self._pinned

    @pinned.setter
    def pinned(self, pinned):
        """Sets the pinned of this CustomerComment.

            Whether the comment is pinned to the top.

        :param pinned: The pinned of this CustomerComment.
        :type: bool
        """

        self._pinned = pinned
    
    @property
    def version(self):
        """Gets the version of this CustomerComment.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :return: The version of this CustomerComment.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CustomerComment.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :param version: The version of this CustomerComment.
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
        if issubclass(CustomerComment, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, CustomerComment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
