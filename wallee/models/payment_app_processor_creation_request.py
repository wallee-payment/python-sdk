# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentAppProcessorCreationRequest:

    swagger_types = {
    
        'documentation_url': 'str',
        'external_id': 'str',
        'name': 'str',
        'production_mode_url': 'str',
        'svg_icon': 'str',
    }

    attribute_map = {
        'documentation_url': 'documentationUrl','external_id': 'externalId','name': 'name','production_mode_url': 'productionModeUrl','svg_icon': 'svgIcon',
    }

    
    _documentation_url = None
    _external_id = None
    _name = None
    _production_mode_url = None
    _svg_icon = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.documentation_url = kwargs.get('documentation_url')

        self.external_id = kwargs.get('external_id')

        self.name = kwargs.get('name')

        self.production_mode_url = kwargs.get('production_mode_url', None)
        self.svg_icon = kwargs.get('svg_icon')

        

    
    @property
    def documentation_url(self):
        """Gets the documentation_url of this PaymentAppProcessorCreationRequest.

            The documentation URL has to point to a description of how to configure and use the processor.

        :return: The documentation_url of this PaymentAppProcessorCreationRequest.
        :rtype: str
        """
        return self._documentation_url

    @documentation_url.setter
    def documentation_url(self, documentation_url):
        """Sets the documentation_url of this PaymentAppProcessorCreationRequest.

            The documentation URL has to point to a description of how to configure and use the processor.

        :param documentation_url: The documentation_url of this PaymentAppProcessorCreationRequest.
        :type: str
        """
        if documentation_url is None:
            raise ValueError("Invalid value for `documentation_url`, must not be `None`")

        self._documentation_url = documentation_url
    
    @property
    def external_id(self):
        """Gets the external_id of this PaymentAppProcessorCreationRequest.

            The external ID identifies the processor within the external system. It has to be unique per space and for any subsequent update the same ID must be sent.

        :return: The external_id of this PaymentAppProcessorCreationRequest.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this PaymentAppProcessorCreationRequest.

            The external ID identifies the processor within the external system. It has to be unique per space and for any subsequent update the same ID must be sent.

        :param external_id: The external_id of this PaymentAppProcessorCreationRequest.
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")
        if external_id is not None and len(external_id) > 40:
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `40`")
        if external_id is not None and len(external_id) < 1:
            raise ValueError("Invalid value for `external_id`, length must be greater than or equal to `1`")

        self._external_id = external_id
    
    @property
    def name(self):
        """Gets the name of this PaymentAppProcessorCreationRequest.

            The name of the processor will be displayed within the user interfaces that the merchant is interacting with.

        :return: The name of this PaymentAppProcessorCreationRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentAppProcessorCreationRequest.

            The name of the processor will be displayed within the user interfaces that the merchant is interacting with.

        :param name: The name of this PaymentAppProcessorCreationRequest.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name
    
    @property
    def production_mode_url(self):
        """Gets the production_mode_url of this PaymentAppProcessorCreationRequest.

            The production mode URL has to point to a site on which the merchant can set up the production mode for the processor.

        :return: The production_mode_url of this PaymentAppProcessorCreationRequest.
        :rtype: str
        """
        return self._production_mode_url

    @production_mode_url.setter
    def production_mode_url(self, production_mode_url):
        """Sets the production_mode_url of this PaymentAppProcessorCreationRequest.

            The production mode URL has to point to a site on which the merchant can set up the production mode for the processor.

        :param production_mode_url: The production_mode_url of this PaymentAppProcessorCreationRequest.
        :type: str
        """

        self._production_mode_url = production_mode_url
    
    @property
    def svg_icon(self):
        """Gets the svg_icon of this PaymentAppProcessorCreationRequest.

            The SVG icon will be displayed to the user to represent this processor.

        :return: The svg_icon of this PaymentAppProcessorCreationRequest.
        :rtype: str
        """
        return self._svg_icon

    @svg_icon.setter
    def svg_icon(self, svg_icon):
        """Sets the svg_icon of this PaymentAppProcessorCreationRequest.

            The SVG icon will be displayed to the user to represent this processor.

        :param svg_icon: The svg_icon of this PaymentAppProcessorCreationRequest.
        :type: str
        """
        if svg_icon is None:
            raise ValueError("Invalid value for `svg_icon`, must not be `None`")
        if svg_icon is not None and len(svg_icon) > 10000:
            raise ValueError("Invalid value for `svg_icon`, length must be less than or equal to `10000`")

        self._svg_icon = svg_icon
    

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
        if issubclass(PaymentAppProcessorCreationRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentAppProcessorCreationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
