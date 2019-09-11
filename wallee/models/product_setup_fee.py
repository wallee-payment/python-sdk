# coding: utf-8
import pprint
import six
from enum import Enum



class ProductSetupFee:

    swagger_types = {
    
        'component': 'SubscriptionProductComponent',
        'description': 'DatabaseTranslatedString',
        'id': 'int',
        'linked_space_id': 'int',
        'name': 'DatabaseTranslatedString',
        'on_downgrade_credited_amount': 'list[PersistableCurrencyAmount]',
        'on_upgrade_credited_amount': 'list[PersistableCurrencyAmount]',
        'setup_fee': 'list[PersistableCurrencyAmount]',
        'type': 'ProductFeeType',
        'version': 'int',
    }

    attribute_map = {
        'component': 'component','description': 'description','id': 'id','linked_space_id': 'linkedSpaceId','name': 'name','on_downgrade_credited_amount': 'onDowngradeCreditedAmount','on_upgrade_credited_amount': 'onUpgradeCreditedAmount','setup_fee': 'setupFee','type': 'type','version': 'version',
    }

    
    _component = None
    _description = None
    _id = None
    _linked_space_id = None
    _name = None
    _on_downgrade_credited_amount = None
    _on_upgrade_credited_amount = None
    _setup_fee = None
    _type = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.component = kwargs.get('component', None)
        self.description = kwargs.get('description', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.on_downgrade_credited_amount = kwargs.get('on_downgrade_credited_amount', None)
        self.on_upgrade_credited_amount = kwargs.get('on_upgrade_credited_amount', None)
        self.setup_fee = kwargs.get('setup_fee', None)
        self.type = kwargs.get('type', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def component(self):
        """Gets the component of this ProductSetupFee.

            

        :return: The component of this ProductSetupFee.
        :rtype: SubscriptionProductComponent
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this ProductSetupFee.

            

        :param component: The component of this ProductSetupFee.
        :type: SubscriptionProductComponent
        """

        self._component = component
    
    @property
    def description(self):
        """Gets the description of this ProductSetupFee.

            The description of a component fee describes the fee to the subscriber. The description may be shown in documents or on certain user interfaces.

        :return: The description of this ProductSetupFee.
        :rtype: DatabaseTranslatedString
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProductSetupFee.

            The description of a component fee describes the fee to the subscriber. The description may be shown in documents or on certain user interfaces.

        :param description: The description of this ProductSetupFee.
        :type: DatabaseTranslatedString
        """

        self._description = description
    
    @property
    def id(self):
        """Gets the id of this ProductSetupFee.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this ProductSetupFee.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProductSetupFee.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this ProductSetupFee.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this ProductSetupFee.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this ProductSetupFee.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this ProductSetupFee.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this ProductSetupFee.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this ProductSetupFee.

            The name of the fee should describe for the subscriber in few words for what the fee is for.

        :return: The name of this ProductSetupFee.
        :rtype: DatabaseTranslatedString
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductSetupFee.

            The name of the fee should describe for the subscriber in few words for what the fee is for.

        :param name: The name of this ProductSetupFee.
        :type: DatabaseTranslatedString
        """

        self._name = name
    
    @property
    def on_downgrade_credited_amount(self):
        """Gets the on_downgrade_credited_amount of this ProductSetupFee.

            When the subscription is changed and the change is considered as a downgrade the amount defined by this property will be credited to the subscriber.

        :return: The on_downgrade_credited_amount of this ProductSetupFee.
        :rtype: list[PersistableCurrencyAmount]
        """
        return self._on_downgrade_credited_amount

    @on_downgrade_credited_amount.setter
    def on_downgrade_credited_amount(self, on_downgrade_credited_amount):
        """Sets the on_downgrade_credited_amount of this ProductSetupFee.

            When the subscription is changed and the change is considered as a downgrade the amount defined by this property will be credited to the subscriber.

        :param on_downgrade_credited_amount: The on_downgrade_credited_amount of this ProductSetupFee.
        :type: list[PersistableCurrencyAmount]
        """

        self._on_downgrade_credited_amount = on_downgrade_credited_amount
    
    @property
    def on_upgrade_credited_amount(self):
        """Gets the on_upgrade_credited_amount of this ProductSetupFee.

            When the subscription is changed and the change is considered as a upgrade the amount defined by this property will be credited to the subscriber.

        :return: The on_upgrade_credited_amount of this ProductSetupFee.
        :rtype: list[PersistableCurrencyAmount]
        """
        return self._on_upgrade_credited_amount

    @on_upgrade_credited_amount.setter
    def on_upgrade_credited_amount(self, on_upgrade_credited_amount):
        """Sets the on_upgrade_credited_amount of this ProductSetupFee.

            When the subscription is changed and the change is considered as a upgrade the amount defined by this property will be credited to the subscriber.

        :param on_upgrade_credited_amount: The on_upgrade_credited_amount of this ProductSetupFee.
        :type: list[PersistableCurrencyAmount]
        """

        self._on_upgrade_credited_amount = on_upgrade_credited_amount
    
    @property
    def setup_fee(self):
        """Gets the setup_fee of this ProductSetupFee.

            The setup fee is charged when the subscriber subscribes to this component. The setup fee is debited with the first charge for the subscriptions.

        :return: The setup_fee of this ProductSetupFee.
        :rtype: list[PersistableCurrencyAmount]
        """
        return self._setup_fee

    @setup_fee.setter
    def setup_fee(self, setup_fee):
        """Sets the setup_fee of this ProductSetupFee.

            The setup fee is charged when the subscriber subscribes to this component. The setup fee is debited with the first charge for the subscriptions.

        :param setup_fee: The setup_fee of this ProductSetupFee.
        :type: list[PersistableCurrencyAmount]
        """

        self._setup_fee = setup_fee
    
    @property
    def type(self):
        """Gets the type of this ProductSetupFee.

            

        :return: The type of this ProductSetupFee.
        :rtype: ProductFeeType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProductSetupFee.

            

        :param type: The type of this ProductSetupFee.
        :type: ProductFeeType
        """

        self._type = type
    
    @property
    def version(self):
        """Gets the version of this ProductSetupFee.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ProductSetupFee.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ProductSetupFee.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ProductSetupFee.
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
        if issubclass(ProductSetupFee, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ProductSetupFee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
