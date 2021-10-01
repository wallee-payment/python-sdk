# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionProductComponent:

    swagger_types = {
    
        'component_change_weight': 'int',
        'component_group': 'SubscriptionProductComponentGroup',
        'default_component': 'bool',
        'description': 'DatabaseTranslatedString',
        'id': 'int',
        'linked_space_id': 'int',
        'maximal_quantity': 'float',
        'minimal_quantity': 'float',
        'name': 'DatabaseTranslatedString',
        'quantity_step': 'float',
        'reference': 'SubscriptionProductComponentReference',
        'sort_order': 'int',
        'tax_class': 'TaxClass',
        'version': 'int',
    }

    attribute_map = {
        'component_change_weight': 'componentChangeWeight','component_group': 'componentGroup','default_component': 'defaultComponent','description': 'description','id': 'id','linked_space_id': 'linkedSpaceId','maximal_quantity': 'maximalQuantity','minimal_quantity': 'minimalQuantity','name': 'name','quantity_step': 'quantityStep','reference': 'reference','sort_order': 'sortOrder','tax_class': 'taxClass','version': 'version',
    }

    
    _component_change_weight = None
    _component_group = None
    _default_component = None
    _description = None
    _id = None
    _linked_space_id = None
    _maximal_quantity = None
    _minimal_quantity = None
    _name = None
    _quantity_step = None
    _reference = None
    _sort_order = None
    _tax_class = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.component_change_weight = kwargs.get('component_change_weight', None)
        self.component_group = kwargs.get('component_group', None)
        self.default_component = kwargs.get('default_component', None)
        self.description = kwargs.get('description', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.maximal_quantity = kwargs.get('maximal_quantity', None)
        self.minimal_quantity = kwargs.get('minimal_quantity', None)
        self.name = kwargs.get('name', None)
        self.quantity_step = kwargs.get('quantity_step', None)
        self.reference = kwargs.get('reference', None)
        self.sort_order = kwargs.get('sort_order', None)
        self.tax_class = kwargs.get('tax_class', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def component_change_weight(self):
        """Gets the component_change_weight of this SubscriptionProductComponent.

            If a product component changes from one with a lower product component tier (e.g. 1) to one with a higher product component tier (e.g. 3), it is considered an upgrade and a one-time fee could be applied.

        :return: The component_change_weight of this SubscriptionProductComponent.
        :rtype: int
        """
        return self._component_change_weight

    @component_change_weight.setter
    def component_change_weight(self, component_change_weight):
        """Sets the component_change_weight of this SubscriptionProductComponent.

            If a product component changes from one with a lower product component tier (e.g. 1) to one with a higher product component tier (e.g. 3), it is considered an upgrade and a one-time fee could be applied.

        :param component_change_weight: The component_change_weight of this SubscriptionProductComponent.
        :type: int
        """

        self._component_change_weight = component_change_weight
    
    @property
    def component_group(self):
        """Gets the component_group of this SubscriptionProductComponent.

            

        :return: The component_group of this SubscriptionProductComponent.
        :rtype: SubscriptionProductComponentGroup
        """
        return self._component_group

    @component_group.setter
    def component_group(self, component_group):
        """Sets the component_group of this SubscriptionProductComponent.

            

        :param component_group: The component_group of this SubscriptionProductComponent.
        :type: SubscriptionProductComponentGroup
        """

        self._component_group = component_group
    
    @property
    def default_component(self):
        """Gets the default_component of this SubscriptionProductComponent.

            When a component is marked as a 'default' component it is used as the default component in its group and will be preselected in the product configuration.

        :return: The default_component of this SubscriptionProductComponent.
        :rtype: bool
        """
        return self._default_component

    @default_component.setter
    def default_component(self, default_component):
        """Sets the default_component of this SubscriptionProductComponent.

            When a component is marked as a 'default' component it is used as the default component in its group and will be preselected in the product configuration.

        :param default_component: The default_component of this SubscriptionProductComponent.
        :type: bool
        """

        self._default_component = default_component
    
    @property
    def description(self):
        """Gets the description of this SubscriptionProductComponent.

            The component description may contain a longer description which gives the subscriber a better understanding of what the component contains.

        :return: The description of this SubscriptionProductComponent.
        :rtype: DatabaseTranslatedString
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SubscriptionProductComponent.

            The component description may contain a longer description which gives the subscriber a better understanding of what the component contains.

        :param description: The description of this SubscriptionProductComponent.
        :type: DatabaseTranslatedString
        """

        self._description = description
    
    @property
    def id(self):
        """Gets the id of this SubscriptionProductComponent.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this SubscriptionProductComponent.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionProductComponent.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this SubscriptionProductComponent.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this SubscriptionProductComponent.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this SubscriptionProductComponent.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this SubscriptionProductComponent.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this SubscriptionProductComponent.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def maximal_quantity(self):
        """Gets the maximal_quantity of this SubscriptionProductComponent.

            The maximum quantity defines the maximum value which must be entered for the quantity.

        :return: The maximal_quantity of this SubscriptionProductComponent.
        :rtype: float
        """
        return self._maximal_quantity

    @maximal_quantity.setter
    def maximal_quantity(self, maximal_quantity):
        """Sets the maximal_quantity of this SubscriptionProductComponent.

            The maximum quantity defines the maximum value which must be entered for the quantity.

        :param maximal_quantity: The maximal_quantity of this SubscriptionProductComponent.
        :type: float
        """

        self._maximal_quantity = maximal_quantity
    
    @property
    def minimal_quantity(self):
        """Gets the minimal_quantity of this SubscriptionProductComponent.

            The minimal quantity defines the minimum value which must be entered for the quantity.

        :return: The minimal_quantity of this SubscriptionProductComponent.
        :rtype: float
        """
        return self._minimal_quantity

    @minimal_quantity.setter
    def minimal_quantity(self, minimal_quantity):
        """Sets the minimal_quantity of this SubscriptionProductComponent.

            The minimal quantity defines the minimum value which must be entered for the quantity.

        :param minimal_quantity: The minimal_quantity of this SubscriptionProductComponent.
        :type: float
        """

        self._minimal_quantity = minimal_quantity
    
    @property
    def name(self):
        """Gets the name of this SubscriptionProductComponent.

            The component name is shown to the subscriber. It should describe in few words what the component does contain.

        :return: The name of this SubscriptionProductComponent.
        :rtype: DatabaseTranslatedString
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionProductComponent.

            The component name is shown to the subscriber. It should describe in few words what the component does contain.

        :param name: The name of this SubscriptionProductComponent.
        :type: DatabaseTranslatedString
        """

        self._name = name
    
    @property
    def quantity_step(self):
        """Gets the quantity_step of this SubscriptionProductComponent.

            The quantity step defines at which interval the quantity can be increased.

        :return: The quantity_step of this SubscriptionProductComponent.
        :rtype: float
        """
        return self._quantity_step

    @quantity_step.setter
    def quantity_step(self, quantity_step):
        """Sets the quantity_step of this SubscriptionProductComponent.

            The quantity step defines at which interval the quantity can be increased.

        :param quantity_step: The quantity_step of this SubscriptionProductComponent.
        :type: float
        """

        self._quantity_step = quantity_step
    
    @property
    def reference(self):
        """Gets the reference of this SubscriptionProductComponent.

            The component reference is used to identify the component by external systems and it marks components to represent the same component within different product versions.

        :return: The reference of this SubscriptionProductComponent.
        :rtype: SubscriptionProductComponentReference
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this SubscriptionProductComponent.

            The component reference is used to identify the component by external systems and it marks components to represent the same component within different product versions.

        :param reference: The reference of this SubscriptionProductComponent.
        :type: SubscriptionProductComponentReference
        """

        self._reference = reference
    
    @property
    def sort_order(self):
        """Gets the sort_order of this SubscriptionProductComponent.

            The sort order controls in which order the component is listed. The sort order is used to order the components in ascending order.

        :return: The sort_order of this SubscriptionProductComponent.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this SubscriptionProductComponent.

            The sort order controls in which order the component is listed. The sort order is used to order the components in ascending order.

        :param sort_order: The sort_order of this SubscriptionProductComponent.
        :type: int
        """

        self._sort_order = sort_order
    
    @property
    def tax_class(self):
        """Gets the tax_class of this SubscriptionProductComponent.

            The tax class of the component determines the taxes which are applicable on all fees linked with the component.

        :return: The tax_class of this SubscriptionProductComponent.
        :rtype: TaxClass
        """
        return self._tax_class

    @tax_class.setter
    def tax_class(self, tax_class):
        """Sets the tax_class of this SubscriptionProductComponent.

            The tax class of the component determines the taxes which are applicable on all fees linked with the component.

        :param tax_class: The tax_class of this SubscriptionProductComponent.
        :type: TaxClass
        """

        self._tax_class = tax_class
    
    @property
    def version(self):
        """Gets the version of this SubscriptionProductComponent.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this SubscriptionProductComponent.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SubscriptionProductComponent.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this SubscriptionProductComponent.
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
        if issubclass(SubscriptionProductComponent, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionProductComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
