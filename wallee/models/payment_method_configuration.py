# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentMethodConfiguration:

    swagger_types = {
    
        'data_collection_type': 'DataCollectionType',
        'description': 'DatabaseTranslatedString',
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
        'title': 'DatabaseTranslatedString',
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

            The data collection type determines who is collecting the payment information. This can be done either by the processor (offsite) or by our application (onsite).

        :return: The data_collection_type of this PaymentMethodConfiguration.
        :rtype: DataCollectionType
        """
        return self._data_collection_type

    @data_collection_type.setter
    def data_collection_type(self, data_collection_type):
        """Sets the data_collection_type of this PaymentMethodConfiguration.

            The data collection type determines who is collecting the payment information. This can be done either by the processor (offsite) or by our application (onsite).

        :param data_collection_type: The data_collection_type of this PaymentMethodConfiguration.
        :type: DataCollectionType
        """

        self._data_collection_type = data_collection_type
    
    @property
    def description(self):
        """Gets the description of this PaymentMethodConfiguration.

            The payment method configuration description can be used to show a text during the payment process. Choose an appropriate description as it will be displayed to your customer.

        :return: The description of this PaymentMethodConfiguration.
        :rtype: DatabaseTranslatedString
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PaymentMethodConfiguration.

            The payment method configuration description can be used to show a text during the payment process. Choose an appropriate description as it will be displayed to your customer.

        :param description: The description of this PaymentMethodConfiguration.
        :type: DatabaseTranslatedString
        """

        self._description = description
    
    @property
    def id(self):
        """Gets the id of this PaymentMethodConfiguration.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentMethodConfiguration.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentMethodConfiguration.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentMethodConfiguration.
        :type: int
        """

        self._id = id
    
    @property
    def image_resource_path(self):
        """Gets the image_resource_path of this PaymentMethodConfiguration.

            The image of the payment method configuration overrides the default image of the payment method.

        :return: The image_resource_path of this PaymentMethodConfiguration.
        :rtype: ResourcePath
        """
        return self._image_resource_path

    @image_resource_path.setter
    def image_resource_path(self, image_resource_path):
        """Sets the image_resource_path of this PaymentMethodConfiguration.

            The image of the payment method configuration overrides the default image of the payment method.

        :param image_resource_path: The image_resource_path of this PaymentMethodConfiguration.
        :type: ResourcePath
        """

        self._image_resource_path = image_resource_path
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this PaymentMethodConfiguration.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this PaymentMethodConfiguration.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this PaymentMethodConfiguration.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this PaymentMethodConfiguration.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this PaymentMethodConfiguration.

            The payment method configuration name is used internally to identify the payment method configuration. For example the name is used within search fields and hence it should be distinct and descriptive.

        :return: The name of this PaymentMethodConfiguration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentMethodConfiguration.

            The payment method configuration name is used internally to identify the payment method configuration. For example the name is used within search fields and hence it should be distinct and descriptive.

        :param name: The name of this PaymentMethodConfiguration.
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name
    
    @property
    def one_click_payment_mode(self):
        """Gets the one_click_payment_mode of this PaymentMethodConfiguration.

            When the buyer is present on the payment page or within the iFrame the payment details can be stored automatically. The buyer will be able to use the stored payment details for subsequent transactions. When the transaction already contains a token one-click payments are disabled anyway

        :return: The one_click_payment_mode of this PaymentMethodConfiguration.
        :rtype: OneClickPaymentMode
        """
        return self._one_click_payment_mode

    @one_click_payment_mode.setter
    def one_click_payment_mode(self, one_click_payment_mode):
        """Sets the one_click_payment_mode of this PaymentMethodConfiguration.

            When the buyer is present on the payment page or within the iFrame the payment details can be stored automatically. The buyer will be able to use the stored payment details for subsequent transactions. When the transaction already contains a token one-click payments are disabled anyway

        :param one_click_payment_mode: The one_click_payment_mode of this PaymentMethodConfiguration.
        :type: OneClickPaymentMode
        """

        self._one_click_payment_mode = one_click_payment_mode
    
    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentMethodConfiguration.

            

        :return: The payment_method of this PaymentMethodConfiguration.
        :rtype: int
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PaymentMethodConfiguration.

            

        :param payment_method: The payment_method of this PaymentMethodConfiguration.
        :type: int
        """

        self._payment_method = payment_method
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this PaymentMethodConfiguration.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this PaymentMethodConfiguration.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this PaymentMethodConfiguration.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this PaymentMethodConfiguration.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def resolved_description(self):
        """Gets the resolved_description of this PaymentMethodConfiguration.

            The resolved description uses the specified description or the default one when it is not overridden.

        :return: The resolved_description of this PaymentMethodConfiguration.
        :rtype: dict(str, str)
        """
        return self._resolved_description

    @resolved_description.setter
    def resolved_description(self, resolved_description):
        """Sets the resolved_description of this PaymentMethodConfiguration.

            The resolved description uses the specified description or the default one when it is not overridden.

        :param resolved_description: The resolved_description of this PaymentMethodConfiguration.
        :type: dict(str, str)
        """

        self._resolved_description = resolved_description
    
    @property
    def resolved_image_url(self):
        """Gets the resolved_image_url of this PaymentMethodConfiguration.

            The resolved URL of the image to use with this payment method.

        :return: The resolved_image_url of this PaymentMethodConfiguration.
        :rtype: str
        """
        return self._resolved_image_url

    @resolved_image_url.setter
    def resolved_image_url(self, resolved_image_url):
        """Sets the resolved_image_url of this PaymentMethodConfiguration.

            The resolved URL of the image to use with this payment method.

        :param resolved_image_url: The resolved_image_url of this PaymentMethodConfiguration.
        :type: str
        """

        self._resolved_image_url = resolved_image_url
    
    @property
    def resolved_title(self):
        """Gets the resolved_title of this PaymentMethodConfiguration.

            The resolved title uses the specified title or the default one when it is not overridden.

        :return: The resolved_title of this PaymentMethodConfiguration.
        :rtype: dict(str, str)
        """
        return self._resolved_title

    @resolved_title.setter
    def resolved_title(self, resolved_title):
        """Sets the resolved_title of this PaymentMethodConfiguration.

            The resolved title uses the specified title or the default one when it is not overridden.

        :param resolved_title: The resolved_title of this PaymentMethodConfiguration.
        :type: dict(str, str)
        """

        self._resolved_title = resolved_title
    
    @property
    def sort_order(self):
        """Gets the sort_order of this PaymentMethodConfiguration.

            The sort order of the payment method determines the ordering of the methods shown to the user during the payment process.

        :return: The sort_order of this PaymentMethodConfiguration.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this PaymentMethodConfiguration.

            The sort order of the payment method determines the ordering of the methods shown to the user during the payment process.

        :param sort_order: The sort_order of this PaymentMethodConfiguration.
        :type: int
        """

        self._sort_order = sort_order
    
    @property
    def space_id(self):
        """Gets the space_id of this PaymentMethodConfiguration.

            

        :return: The space_id of this PaymentMethodConfiguration.
        :rtype: int
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this PaymentMethodConfiguration.

            

        :param space_id: The space_id of this PaymentMethodConfiguration.
        :type: int
        """

        self._space_id = space_id
    
    @property
    def state(self):
        """Gets the state of this PaymentMethodConfiguration.

            

        :return: The state of this PaymentMethodConfiguration.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentMethodConfiguration.

            

        :param state: The state of this PaymentMethodConfiguration.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def title(self):
        """Gets the title of this PaymentMethodConfiguration.

            The title of the payment method configuration is used within the payment process. The title is visible to the customer.

        :return: The title of this PaymentMethodConfiguration.
        :rtype: DatabaseTranslatedString
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PaymentMethodConfiguration.

            The title of the payment method configuration is used within the payment process. The title is visible to the customer.

        :param title: The title of this PaymentMethodConfiguration.
        :type: DatabaseTranslatedString
        """

        self._title = title
    
    @property
    def version(self):
        """Gets the version of this PaymentMethodConfiguration.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this PaymentMethodConfiguration.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PaymentMethodConfiguration.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

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
