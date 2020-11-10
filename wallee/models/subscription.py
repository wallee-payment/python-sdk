# coding: utf-8
import pprint
import six
from enum import Enum



class Subscription:

    swagger_types = {
    
        'activated_on': 'datetime',
        'affiliate': 'SubscriptionAffiliate',
        'created_on': 'datetime',
        'current_product_version': 'SubscriptionProductVersion',
        'description': 'str',
        'id': 'int',
        'initialized_on': 'datetime',
        'language': 'str',
        'linked_space_id': 'int',
        'planned_purge_date': 'datetime',
        'planned_termination_date': 'datetime',
        'reference': 'str',
        'state': 'SubscriptionState',
        'subscriber': 'Subscriber',
        'terminated_by': 'int',
        'terminated_on': 'datetime',
        'terminating_on': 'datetime',
        'termination_scheduled_on': 'datetime',
        'token': 'Token',
        'version': 'int',
    }

    attribute_map = {
        'activated_on': 'activatedOn','affiliate': 'affiliate','created_on': 'createdOn','current_product_version': 'currentProductVersion','description': 'description','id': 'id','initialized_on': 'initializedOn','language': 'language','linked_space_id': 'linkedSpaceId','planned_purge_date': 'plannedPurgeDate','planned_termination_date': 'plannedTerminationDate','reference': 'reference','state': 'state','subscriber': 'subscriber','terminated_by': 'terminatedBy','terminated_on': 'terminatedOn','terminating_on': 'terminatingOn','termination_scheduled_on': 'terminationScheduledOn','token': 'token','version': 'version',
    }

    
    _activated_on = None
    _affiliate = None
    _created_on = None
    _current_product_version = None
    _description = None
    _id = None
    _initialized_on = None
    _language = None
    _linked_space_id = None
    _planned_purge_date = None
    _planned_termination_date = None
    _reference = None
    _state = None
    _subscriber = None
    _terminated_by = None
    _terminated_on = None
    _terminating_on = None
    _termination_scheduled_on = None
    _token = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.activated_on = kwargs.get('activated_on', None)
        self.affiliate = kwargs.get('affiliate', None)
        self.created_on = kwargs.get('created_on', None)
        self.current_product_version = kwargs.get('current_product_version', None)
        self.description = kwargs.get('description', None)
        self.id = kwargs.get('id', None)
        self.initialized_on = kwargs.get('initialized_on', None)
        self.language = kwargs.get('language', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.planned_termination_date = kwargs.get('planned_termination_date', None)
        self.reference = kwargs.get('reference', None)
        self.state = kwargs.get('state', None)
        self.subscriber = kwargs.get('subscriber', None)
        self.terminated_by = kwargs.get('terminated_by', None)
        self.terminated_on = kwargs.get('terminated_on', None)
        self.terminating_on = kwargs.get('terminating_on', None)
        self.termination_scheduled_on = kwargs.get('termination_scheduled_on', None)
        self.token = kwargs.get('token', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def activated_on(self):
        """Gets the activated_on of this Subscription.

            

        :return: The activated_on of this Subscription.
        :rtype: datetime
        """
        return self._activated_on

    @activated_on.setter
    def activated_on(self, activated_on):
        """Sets the activated_on of this Subscription.

            

        :param activated_on: The activated_on of this Subscription.
        :type: datetime
        """

        self._activated_on = activated_on
    
    @property
    def affiliate(self):
        """Gets the affiliate of this Subscription.

            

        :return: The affiliate of this Subscription.
        :rtype: SubscriptionAffiliate
        """
        return self._affiliate

    @affiliate.setter
    def affiliate(self, affiliate):
        """Sets the affiliate of this Subscription.

            

        :param affiliate: The affiliate of this Subscription.
        :type: SubscriptionAffiliate
        """

        self._affiliate = affiliate
    
    @property
    def created_on(self):
        """Gets the created_on of this Subscription.

            

        :return: The created_on of this Subscription.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Subscription.

            

        :param created_on: The created_on of this Subscription.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def current_product_version(self):
        """Gets the current_product_version of this Subscription.

            

        :return: The current_product_version of this Subscription.
        :rtype: SubscriptionProductVersion
        """
        return self._current_product_version

    @current_product_version.setter
    def current_product_version(self, current_product_version):
        """Sets the current_product_version of this Subscription.

            

        :param current_product_version: The current_product_version of this Subscription.
        :type: SubscriptionProductVersion
        """

        self._current_product_version = current_product_version
    
    @property
    def description(self):
        """Gets the description of this Subscription.

            

        :return: The description of this Subscription.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Subscription.

            

        :param description: The description of this Subscription.
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")

        self._description = description
    
    @property
    def id(self):
        """Gets the id of this Subscription.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this Subscription.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Subscription.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this Subscription.
        :type: int
        """

        self._id = id
    
    @property
    def initialized_on(self):
        """Gets the initialized_on of this Subscription.

            

        :return: The initialized_on of this Subscription.
        :rtype: datetime
        """
        return self._initialized_on

    @initialized_on.setter
    def initialized_on(self, initialized_on):
        """Sets the initialized_on of this Subscription.

            

        :param initialized_on: The initialized_on of this Subscription.
        :type: datetime
        """

        self._initialized_on = initialized_on
    
    @property
    def language(self):
        """Gets the language of this Subscription.

            

        :return: The language of this Subscription.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Subscription.

            

        :param language: The language of this Subscription.
        :type: str
        """

        self._language = language
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this Subscription.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this Subscription.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this Subscription.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this Subscription.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this Subscription.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this Subscription.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this Subscription.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this Subscription.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def planned_termination_date(self):
        """Gets the planned_termination_date of this Subscription.

            

        :return: The planned_termination_date of this Subscription.
        :rtype: datetime
        """
        return self._planned_termination_date

    @planned_termination_date.setter
    def planned_termination_date(self, planned_termination_date):
        """Sets the planned_termination_date of this Subscription.

            

        :param planned_termination_date: The planned_termination_date of this Subscription.
        :type: datetime
        """

        self._planned_termination_date = planned_termination_date
    
    @property
    def reference(self):
        """Gets the reference of this Subscription.

            

        :return: The reference of this Subscription.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Subscription.

            

        :param reference: The reference of this Subscription.
        :type: str
        """
        if reference is not None and len(reference) > 100:
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `100`")

        self._reference = reference
    
    @property
    def state(self):
        """Gets the state of this Subscription.

            

        :return: The state of this Subscription.
        :rtype: SubscriptionState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Subscription.

            

        :param state: The state of this Subscription.
        :type: SubscriptionState
        """

        self._state = state
    
    @property
    def subscriber(self):
        """Gets the subscriber of this Subscription.

            

        :return: The subscriber of this Subscription.
        :rtype: Subscriber
        """
        return self._subscriber

    @subscriber.setter
    def subscriber(self, subscriber):
        """Sets the subscriber of this Subscription.

            

        :param subscriber: The subscriber of this Subscription.
        :type: Subscriber
        """

        self._subscriber = subscriber
    
    @property
    def terminated_by(self):
        """Gets the terminated_by of this Subscription.

            

        :return: The terminated_by of this Subscription.
        :rtype: int
        """
        return self._terminated_by

    @terminated_by.setter
    def terminated_by(self, terminated_by):
        """Sets the terminated_by of this Subscription.

            

        :param terminated_by: The terminated_by of this Subscription.
        :type: int
        """

        self._terminated_by = terminated_by
    
    @property
    def terminated_on(self):
        """Gets the terminated_on of this Subscription.

            

        :return: The terminated_on of this Subscription.
        :rtype: datetime
        """
        return self._terminated_on

    @terminated_on.setter
    def terminated_on(self, terminated_on):
        """Sets the terminated_on of this Subscription.

            

        :param terminated_on: The terminated_on of this Subscription.
        :type: datetime
        """

        self._terminated_on = terminated_on
    
    @property
    def terminating_on(self):
        """Gets the terminating_on of this Subscription.

            

        :return: The terminating_on of this Subscription.
        :rtype: datetime
        """
        return self._terminating_on

    @terminating_on.setter
    def terminating_on(self, terminating_on):
        """Sets the terminating_on of this Subscription.

            

        :param terminating_on: The terminating_on of this Subscription.
        :type: datetime
        """

        self._terminating_on = terminating_on
    
    @property
    def termination_scheduled_on(self):
        """Gets the termination_scheduled_on of this Subscription.

            

        :return: The termination_scheduled_on of this Subscription.
        :rtype: datetime
        """
        return self._termination_scheduled_on

    @termination_scheduled_on.setter
    def termination_scheduled_on(self, termination_scheduled_on):
        """Sets the termination_scheduled_on of this Subscription.

            

        :param termination_scheduled_on: The termination_scheduled_on of this Subscription.
        :type: datetime
        """

        self._termination_scheduled_on = termination_scheduled_on
    
    @property
    def token(self):
        """Gets the token of this Subscription.

            

        :return: The token of this Subscription.
        :rtype: Token
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this Subscription.

            

        :param token: The token of this Subscription.
        :type: Token
        """

        self._token = token
    
    @property
    def version(self):
        """Gets the version of this Subscription.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this Subscription.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Subscription.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this Subscription.
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
        if issubclass(Subscription, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Subscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
