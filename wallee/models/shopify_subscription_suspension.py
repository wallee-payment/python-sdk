# coding: utf-8
import pprint
import six
from enum import Enum



class ShopifySubscriptionSuspension:

    swagger_types = {
    
        'created_by': 'int',
        'created_on': 'datetime',
        'ended_by': 'int',
        'ended_on': 'datetime',
        'id': 'int',
        'initiator': 'ShopifySubscriptionSuspensionInitiator',
        'linked_space_id': 'int',
        'planned_end_date': 'datetime',
        'shop': 'int',
        'state': 'ShopifySubscriptionSuspensionState',
        'subscription': 'ShopifySubscription',
        'type': 'ShopifySubscriptionSuspensionType',
        'version': 'int',
    }

    attribute_map = {
        'created_by': 'createdBy','created_on': 'createdOn','ended_by': 'endedBy','ended_on': 'endedOn','id': 'id','initiator': 'initiator','linked_space_id': 'linkedSpaceId','planned_end_date': 'plannedEndDate','shop': 'shop','state': 'state','subscription': 'subscription','type': 'type','version': 'version',
    }

    
    _created_by = None
    _created_on = None
    _ended_by = None
    _ended_on = None
    _id = None
    _initiator = None
    _linked_space_id = None
    _planned_end_date = None
    _shop = None
    _state = None
    _subscription = None
    _type = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.created_by = kwargs.get('created_by', None)
        self.created_on = kwargs.get('created_on', None)
        self.ended_by = kwargs.get('ended_by', None)
        self.ended_on = kwargs.get('ended_on', None)
        self.id = kwargs.get('id', None)
        self.initiator = kwargs.get('initiator', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.planned_end_date = kwargs.get('planned_end_date', None)
        self.shop = kwargs.get('shop', None)
        self.state = kwargs.get('state', None)
        self.subscription = kwargs.get('subscription', None)
        self.type = kwargs.get('type', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def created_by(self):
        """Gets the created_by of this ShopifySubscriptionSuspension.

            

        :return: The created_by of this ShopifySubscriptionSuspension.
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ShopifySubscriptionSuspension.

            

        :param created_by: The created_by of this ShopifySubscriptionSuspension.
        :type: int
        """

        self._created_by = created_by
    
    @property
    def created_on(self):
        """Gets the created_on of this ShopifySubscriptionSuspension.

            

        :return: The created_on of this ShopifySubscriptionSuspension.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this ShopifySubscriptionSuspension.

            

        :param created_on: The created_on of this ShopifySubscriptionSuspension.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def ended_by(self):
        """Gets the ended_by of this ShopifySubscriptionSuspension.

            

        :return: The ended_by of this ShopifySubscriptionSuspension.
        :rtype: int
        """
        return self._ended_by

    @ended_by.setter
    def ended_by(self, ended_by):
        """Sets the ended_by of this ShopifySubscriptionSuspension.

            

        :param ended_by: The ended_by of this ShopifySubscriptionSuspension.
        :type: int
        """

        self._ended_by = ended_by
    
    @property
    def ended_on(self):
        """Gets the ended_on of this ShopifySubscriptionSuspension.

            

        :return: The ended_on of this ShopifySubscriptionSuspension.
        :rtype: datetime
        """
        return self._ended_on

    @ended_on.setter
    def ended_on(self, ended_on):
        """Sets the ended_on of this ShopifySubscriptionSuspension.

            

        :param ended_on: The ended_on of this ShopifySubscriptionSuspension.
        :type: datetime
        """

        self._ended_on = ended_on
    
    @property
    def id(self):
        """Gets the id of this ShopifySubscriptionSuspension.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this ShopifySubscriptionSuspension.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShopifySubscriptionSuspension.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this ShopifySubscriptionSuspension.
        :type: int
        """

        self._id = id
    
    @property
    def initiator(self):
        """Gets the initiator of this ShopifySubscriptionSuspension.

            

        :return: The initiator of this ShopifySubscriptionSuspension.
        :rtype: ShopifySubscriptionSuspensionInitiator
        """
        return self._initiator

    @initiator.setter
    def initiator(self, initiator):
        """Sets the initiator of this ShopifySubscriptionSuspension.

            

        :param initiator: The initiator of this ShopifySubscriptionSuspension.
        :type: ShopifySubscriptionSuspensionInitiator
        """

        self._initiator = initiator
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this ShopifySubscriptionSuspension.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this ShopifySubscriptionSuspension.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this ShopifySubscriptionSuspension.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this ShopifySubscriptionSuspension.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def planned_end_date(self):
        """Gets the planned_end_date of this ShopifySubscriptionSuspension.

            

        :return: The planned_end_date of this ShopifySubscriptionSuspension.
        :rtype: datetime
        """
        return self._planned_end_date

    @planned_end_date.setter
    def planned_end_date(self, planned_end_date):
        """Sets the planned_end_date of this ShopifySubscriptionSuspension.

            

        :param planned_end_date: The planned_end_date of this ShopifySubscriptionSuspension.
        :type: datetime
        """

        self._planned_end_date = planned_end_date
    
    @property
    def shop(self):
        """Gets the shop of this ShopifySubscriptionSuspension.

            

        :return: The shop of this ShopifySubscriptionSuspension.
        :rtype: int
        """
        return self._shop

    @shop.setter
    def shop(self, shop):
        """Sets the shop of this ShopifySubscriptionSuspension.

            

        :param shop: The shop of this ShopifySubscriptionSuspension.
        :type: int
        """

        self._shop = shop
    
    @property
    def state(self):
        """Gets the state of this ShopifySubscriptionSuspension.

            

        :return: The state of this ShopifySubscriptionSuspension.
        :rtype: ShopifySubscriptionSuspensionState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShopifySubscriptionSuspension.

            

        :param state: The state of this ShopifySubscriptionSuspension.
        :type: ShopifySubscriptionSuspensionState
        """

        self._state = state
    
    @property
    def subscription(self):
        """Gets the subscription of this ShopifySubscriptionSuspension.

            

        :return: The subscription of this ShopifySubscriptionSuspension.
        :rtype: ShopifySubscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this ShopifySubscriptionSuspension.

            

        :param subscription: The subscription of this ShopifySubscriptionSuspension.
        :type: ShopifySubscription
        """

        self._subscription = subscription
    
    @property
    def type(self):
        """Gets the type of this ShopifySubscriptionSuspension.

            

        :return: The type of this ShopifySubscriptionSuspension.
        :rtype: ShopifySubscriptionSuspensionType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShopifySubscriptionSuspension.

            

        :param type: The type of this ShopifySubscriptionSuspension.
        :type: ShopifySubscriptionSuspensionType
        """

        self._type = type
    
    @property
    def version(self):
        """Gets the version of this ShopifySubscriptionSuspension.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ShopifySubscriptionSuspension.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShopifySubscriptionSuspension.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ShopifySubscriptionSuspension.
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
        if issubclass(ShopifySubscriptionSuspension, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ShopifySubscriptionSuspension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
