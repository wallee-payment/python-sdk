# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentMethodConfiguration:

    swagger_types = {
    
        'data_collection_type': 'DataCollectionType',
        'description': 'dict(str, str)',
        'id': 'int',
        'image_resource_path': 'ResourcePath',
        'linked_space_id': 'int',
        'name': 'str',
        'one_click_payment_mode': 'OneClickPaymentMode',
        'payment_method': 'int',
        'planned_purge_date': 'datetime',
        'resolved_description': 'dict(str, str)',
        'resolved_image_url': 'str',
        'resolved_title': 'dict(str, str)',
        'sort_order': 'int',
        'space_id': 'int',
        'state': 'CreationEntityState',
        'title': 'dict(str, str)',
        'version': 'int',
    }

    attribute_map = {
        'data_collection_type': 'dataCollectionType','description': 'description','id': 'id','image_resource_path': 'imageResourcePath','linked_space_id': 'linkedSpaceId','name': 'name','one_click_payment_mode': 'oneClickPaymentMode','payment_method': 'paymentMethod','planned_purge_date': 'plannedPurgeDate','resolved_description': 'resolvedDescription','resolved_image_url': 'resolvedImageUrl','resolved_title': 'resolvedTitle','sort_order': 'sortOrder','space_id': 'spaceId','state': 'state','title': 'title','version': 'version',
    }

    
    _data_collection_type = None
    _description = None
    _id = None
    _image_resource_path = None
    _linked_space_id = None
    _name = None
    _one_click_payment_mode = None
    _payment_method = None
    _planned_purge_date = None
    _resolved_description = None
    _resolved_image_url = None
    _resolved_title = None
    _sort_order = None
    _space_id = None
    _state = None
    _title = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.data_collection_type = kwargs.get('data_collection_type', None)
        self.description = kwargs.get('description', None)
        self.id = kwargs.get('id', None)
        self.image_resource_path = kwargs.get('image_resource_path', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.one_click_payment_mode = kwargs.get('one_click_payment_mode', None)
        self.payment_method = kwargs.get('payment_method', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.resolved_description = kwargs.get('resolved_description', None)
        self.resolved_image_url = kwargs.get('resolved_image_url', None)
        self.resolved_title = kwargs.get('resolved_title', None)
        self.sort_order = kwargs.get('sort_order', None)
        self.space_id = kwargs.get('space_id', None)
        self.state = kwargs.get('state', None)
        self.title = kwargs.get('title', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def data_collection_type(self):
        """Gets the data_collection_type of this PaymentMethodConfiguration.

            The data collection type specifies how the payment information is collected.

        :return: The data_collection_type of this PaymentMethodConfiguration.
        :rtype: DataCollectionType
        """
        return self._data_collection_type

    @data_collection_type.setter
    def data_collection_type(self, data_collection_type):
        """Sets the data_collection_type of this PaymentMethodConfiguration.

            The data collection type specifies how the payment information is collected.

        :param data_collection_type: The data_collection_type of this PaymentMethodConfiguration.
        :type: DataCollectionType
        """

        self._data_collection_type = data_collection_type
    
    @property
    def description(self):
        """Gets the description of this PaymentMethodConfiguration.

            A customer-facing custom description for the payment method.

        :return: The description of this PaymentMethodConfiguration.
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PaymentMethodConfiguration.

            A customer-facing custom description for the payment method.

        :param description: The description of this PaymentMethodConfiguration.
        :type: dict(str, str)
        """

        self._description = description
    
    @property
    def id(self):
        """Gets the id of this PaymentMethodConfiguration.

            A unique identifier for the object.

        :return: The id of this PaymentMethodConfiguration.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentMethodConfiguration.

            A unique identifier for the object.

        :param id: The id of this PaymentMethodConfiguration.
        :type: int
        """

        self._id = id
    
    @property
    def image_resource_path(self):
        """Gets the image_resource_path of this PaymentMethodConfiguration.

            The resource path to a custom image for the payment method, displayed to the customer for visual identification.

        :return: The image_resource_path of this PaymentMethodConfiguration.
        :rtype: ResourcePath
        """
        return self._image_resource_path

    @image_resource_path.setter
    def image_resource_path(self, image_resource_path):
        """Sets the image_resource_path of this PaymentMethodConfiguration.

            The resource path to a custom image for the payment method, displayed to the customer for visual identification.

        :param image_resource_path: The image_resource_path of this PaymentMethodConfiguration.
        :type: ResourcePath
        """

        self._image_resource_path = image_resource_path
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this PaymentMethodConfiguration.

            The ID of the space this object belongs to.

        :return: The linked_space_id of this PaymentMethodConfiguration.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this PaymentMethodConfiguration.

            The ID of the space this object belongs to.

        :param linked_space_id: The linked_space_id of this PaymentMethodConfiguration.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this PaymentMethodConfiguration.

            The name used to identify the payment method configuration.

        :return: The name of this PaymentMethodConfiguration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentMethodConfiguration.

            The name used to identify the payment method configuration.

        :param name: The name of this PaymentMethodConfiguration.
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name
    
    @property
    def one_click_payment_mode(self):
        """Gets the one_click_payment_mode of this PaymentMethodConfiguration.

            The one-click payment mode determines whether the customer can save their payment details for later payments.

        :return: The one_click_payment_mode of this PaymentMethodConfiguration.
        :rtype: OneClickPaymentMode
        """
        return self._one_click_payment_mode

    @one_click_payment_mode.setter
    def one_click_payment_mode(self, one_click_payment_mode):
        """Sets the one_click_payment_mode of this PaymentMethodConfiguration.

            The one-click payment mode determines whether the customer can save their payment details for later payments.

        :param one_click_payment_mode: The one_click_payment_mode of this PaymentMethodConfiguration.
        :type: OneClickPaymentMode
        """

        self._one_click_payment_mode = one_click_payment_mode
    
    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentMethodConfiguration.

            The payment method that the configuration is for.

        :return: The payment_method of this PaymentMethodConfiguration.
        :rtype: int
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PaymentMethodConfiguration.

            The payment method that the configuration is for.

        :param payment_method: The payment_method of this PaymentMethodConfiguration.
        :type: int
        """

        self._payment_method = payment_method
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this PaymentMethodConfiguration.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :return: The planned_purge_date of this PaymentMethodConfiguration.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this PaymentMethodConfiguration.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :param planned_purge_date: The planned_purge_date of this PaymentMethodConfiguration.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def resolved_description(self):
        """Gets the resolved_description of this PaymentMethodConfiguration.

            The description of the payment method displayed to the customer. If a custom description is defined, it will be used; otherwise, the default description of the payment method will be shown.

        :return: The resolved_description of this PaymentMethodConfiguration.
        :rtype: dict(str, str)
        """
        return self._resolved_description

    @resolved_description.setter
    def resolved_description(self, resolved_description):
        """Sets the resolved_description of this PaymentMethodConfiguration.

            The description of the payment method displayed to the customer. If a custom description is defined, it will be used; otherwise, the default description of the payment method will be shown.

        :param resolved_description: The resolved_description of this PaymentMethodConfiguration.
        :type: dict(str, str)
        """

        self._resolved_description = resolved_description
    
    @property
    def resolved_image_url(self):
        """Gets the resolved_image_url of this PaymentMethodConfiguration.

            The URL to the image of the payment method displayed to the customer. If a custom image is defined, it will be used; otherwise, the default image of the payment method will be shown.

        :return: The resolved_image_url of this PaymentMethodConfiguration.
        :rtype: str
        """
        return self._resolved_image_url

    @resolved_image_url.setter
    def resolved_image_url(self, resolved_image_url):
        """Sets the resolved_image_url of this PaymentMethodConfiguration.

            The URL to the image of the payment method displayed to the customer. If a custom image is defined, it will be used; otherwise, the default image of the payment method will be shown.

        :param resolved_image_url: The resolved_image_url of this PaymentMethodConfiguration.
        :type: str
        """

        self._resolved_image_url = resolved_image_url
    
    @property
    def resolved_title(self):
        """Gets the resolved_title of this PaymentMethodConfiguration.

            The title of the payment method displayed to the customer. If a custom title is defined, it will be used; otherwise, the default title of the payment method will be shown.

        :return: The resolved_title of this PaymentMethodConfiguration.
        :rtype: dict(str, str)
        """
        return self._resolved_title

    @resolved_title.setter
    def resolved_title(self, resolved_title):
        """Sets the resolved_title of this PaymentMethodConfiguration.

            The title of the payment method displayed to the customer. If a custom title is defined, it will be used; otherwise, the default title of the payment method will be shown.

        :param resolved_title: The resolved_title of this PaymentMethodConfiguration.
        :type: dict(str, str)
        """

        self._resolved_title = resolved_title
    
    @property
    def sort_order(self):
        """Gets the sort_order of this PaymentMethodConfiguration.

            When listing payment methods, they can be sorted by this number.

        :return: The sort_order of this PaymentMethodConfiguration.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this PaymentMethodConfiguration.

            When listing payment methods, they can be sorted by this number.

        :param sort_order: The sort_order of this PaymentMethodConfiguration.
        :type: int
        """

        self._sort_order = sort_order
    
    @property
    def space_id(self):
        """Gets the space_id of this PaymentMethodConfiguration.

            The ID of the space this object belongs to.

        :return: The space_id of this PaymentMethodConfiguration.
        :rtype: int
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this PaymentMethodConfiguration.

            The ID of the space this object belongs to.

        :param space_id: The space_id of this PaymentMethodConfiguration.
        :type: int
        """

        self._space_id = space_id
    
    @property
    def state(self):
        """Gets the state of this PaymentMethodConfiguration.

            The object's current state.

        :return: The state of this PaymentMethodConfiguration.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentMethodConfiguration.

            The object's current state.

        :param state: The state of this PaymentMethodConfiguration.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def title(self):
        """Gets the title of this PaymentMethodConfiguration.

            A customer-facing custom title for the payment method.

        :return: The title of this PaymentMethodConfiguration.
        :rtype: dict(str, str)
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PaymentMethodConfiguration.

            A customer-facing custom title for the payment method.

        :param title: The title of this PaymentMethodConfiguration.
        :type: dict(str, str)
        """

        self._title = title
    
    @property
    def version(self):
        """Gets the version of this PaymentMethodConfiguration.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :return: The version of this PaymentMethodConfiguration.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PaymentMethodConfiguration.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :param version: The version of this PaymentMethodConfiguration.
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
        if issubclass(PaymentMethodConfiguration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentMethodConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
