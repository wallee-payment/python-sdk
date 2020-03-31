# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionVersion:

    swagger_types = {
    
        'activated_on': 'datetime',
        'billing_currency': 'str',
        'component_configurations': 'list[SubscriptionComponentConfiguration]',
        'created_on': 'datetime',
        'expected_last_period_end': 'datetime',
        'failed_on': 'datetime',
        'id': 'int',
        'language': 'str',
        'linked_space_id': 'int',
        'planned_purge_date': 'datetime',
        'planned_termination_date': 'datetime',
        'product_version': 'SubscriptionProductVersion',
        'selected_components': 'list[SubscriptionProductComponent]',
        'state': 'SubscriptionVersionState',
        'subscription': 'Subscription',
        'terminated_on': 'datetime',
        'terminating_on': 'datetime',
        'termination_issued_on': 'datetime',
        'version': 'int',
    }

    attribute_map = {
        'activated_on': 'activatedOn','billing_currency': 'billingCurrency','component_configurations': 'componentConfigurations','created_on': 'createdOn','expected_last_period_end': 'expectedLastPeriodEnd','failed_on': 'failedOn','id': 'id','language': 'language','linked_space_id': 'linkedSpaceId','planned_purge_date': 'plannedPurgeDate','planned_termination_date': 'plannedTerminationDate','product_version': 'productVersion','selected_components': 'selectedComponents','state': 'state','subscription': 'subscription','terminated_on': 'terminatedOn','terminating_on': 'terminatingOn','termination_issued_on': 'terminationIssuedOn','version': 'version',
    }

    
    _activated_on = None
    _billing_currency = None
    _component_configurations = None
    _created_on = None
    _expected_last_period_end = None
    _failed_on = None
    _id = None
    _language = None
    _linked_space_id = None
    _planned_purge_date = None
    _planned_termination_date = None
    _product_version = None
    _selected_components = None
    _state = None
    _subscription = None
    _terminated_on = None
    _terminating_on = None
    _termination_issued_on = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.activated_on = kwargs.get('activated_on', None)
        self.billing_currency = kwargs.get('billing_currency', None)
        self.component_configurations = kwargs.get('component_configurations', None)
        self.created_on = kwargs.get('created_on', None)
        self.expected_last_period_end = kwargs.get('expected_last_period_end', None)
        self.failed_on = kwargs.get('failed_on', None)
        self.id = kwargs.get('id', None)
        self.language = kwargs.get('language', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.planned_termination_date = kwargs.get('planned_termination_date', None)
        self.product_version = kwargs.get('product_version', None)
        self.selected_components = kwargs.get('selected_components', None)
        self.state = kwargs.get('state', None)
        self.subscription = kwargs.get('subscription', None)
        self.terminated_on = kwargs.get('terminated_on', None)
        self.terminating_on = kwargs.get('terminating_on', None)
        self.termination_issued_on = kwargs.get('termination_issued_on', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def activated_on(self):
        """Gets the activated_on of this SubscriptionVersion.

            

        :return: The activated_on of this SubscriptionVersion.
        :rtype: datetime
        """
        return self._activated_on

    @activated_on.setter
    def activated_on(self, activated_on):
        """Sets the activated_on of this SubscriptionVersion.

            

        :param activated_on: The activated_on of this SubscriptionVersion.
        :type: datetime
        """

        self._activated_on = activated_on
    
    @property
    def billing_currency(self):
        """Gets the billing_currency of this SubscriptionVersion.

            The subscriber is charged in the billing currency. The billing currency has to be one of the enabled currencies on the subscription product.

        :return: The billing_currency of this SubscriptionVersion.
        :rtype: str
        """
        return self._billing_currency

    @billing_currency.setter
    def billing_currency(self, billing_currency):
        """Sets the billing_currency of this SubscriptionVersion.

            The subscriber is charged in the billing currency. The billing currency has to be one of the enabled currencies on the subscription product.

        :param billing_currency: The billing_currency of this SubscriptionVersion.
        :type: str
        """

        self._billing_currency = billing_currency
    
    @property
    def component_configurations(self):
        """Gets the component_configurations of this SubscriptionVersion.

            

        :return: The component_configurations of this SubscriptionVersion.
        :rtype: list[SubscriptionComponentConfiguration]
        """
        return self._component_configurations

    @component_configurations.setter
    def component_configurations(self, component_configurations):
        """Sets the component_configurations of this SubscriptionVersion.

            

        :param component_configurations: The component_configurations of this SubscriptionVersion.
        :type: list[SubscriptionComponentConfiguration]
        """

        self._component_configurations = component_configurations
    
    @property
    def created_on(self):
        """Gets the created_on of this SubscriptionVersion.

            

        :return: The created_on of this SubscriptionVersion.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this SubscriptionVersion.

            

        :param created_on: The created_on of this SubscriptionVersion.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def expected_last_period_end(self):
        """Gets the expected_last_period_end of this SubscriptionVersion.

            The expected last period end is the date on which the projected end date of the last period is. This is only a projection and as such the actual date may be different.

        :return: The expected_last_period_end of this SubscriptionVersion.
        :rtype: datetime
        """
        return self._expected_last_period_end

    @expected_last_period_end.setter
    def expected_last_period_end(self, expected_last_period_end):
        """Sets the expected_last_period_end of this SubscriptionVersion.

            The expected last period end is the date on which the projected end date of the last period is. This is only a projection and as such the actual date may be different.

        :param expected_last_period_end: The expected_last_period_end of this SubscriptionVersion.
        :type: datetime
        """

        self._expected_last_period_end = expected_last_period_end
    
    @property
    def failed_on(self):
        """Gets the failed_on of this SubscriptionVersion.

            

        :return: The failed_on of this SubscriptionVersion.
        :rtype: datetime
        """
        return self._failed_on

    @failed_on.setter
    def failed_on(self, failed_on):
        """Sets the failed_on of this SubscriptionVersion.

            

        :param failed_on: The failed_on of this SubscriptionVersion.
        :type: datetime
        """

        self._failed_on = failed_on
    
    @property
    def id(self):
        """Gets the id of this SubscriptionVersion.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this SubscriptionVersion.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionVersion.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this SubscriptionVersion.
        :type: int
        """

        self._id = id
    
    @property
    def language(self):
        """Gets the language of this SubscriptionVersion.

            

        :return: The language of this SubscriptionVersion.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SubscriptionVersion.

            

        :param language: The language of this SubscriptionVersion.
        :type: str
        """

        self._language = language
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this SubscriptionVersion.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this SubscriptionVersion.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this SubscriptionVersion.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this SubscriptionVersion.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this SubscriptionVersion.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this SubscriptionVersion.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this SubscriptionVersion.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this SubscriptionVersion.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def planned_termination_date(self):
        """Gets the planned_termination_date of this SubscriptionVersion.

            

        :return: The planned_termination_date of this SubscriptionVersion.
        :rtype: datetime
        """
        return self._planned_termination_date

    @planned_termination_date.setter
    def planned_termination_date(self, planned_termination_date):
        """Sets the planned_termination_date of this SubscriptionVersion.

            

        :param planned_termination_date: The planned_termination_date of this SubscriptionVersion.
        :type: datetime
        """

        self._planned_termination_date = planned_termination_date
    
    @property
    def product_version(self):
        """Gets the product_version of this SubscriptionVersion.

            

        :return: The product_version of this SubscriptionVersion.
        :rtype: SubscriptionProductVersion
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        """Sets the product_version of this SubscriptionVersion.

            

        :param product_version: The product_version of this SubscriptionVersion.
        :type: SubscriptionProductVersion
        """

        self._product_version = product_version
    
    @property
    def selected_components(self):
        """Gets the selected_components of this SubscriptionVersion.

            

        :return: The selected_components of this SubscriptionVersion.
        :rtype: list[SubscriptionProductComponent]
        """
        return self._selected_components

    @selected_components.setter
    def selected_components(self, selected_components):
        """Sets the selected_components of this SubscriptionVersion.

            

        :param selected_components: The selected_components of this SubscriptionVersion.
        :type: list[SubscriptionProductComponent]
        """

        self._selected_components = selected_components
    
    @property
    def state(self):
        """Gets the state of this SubscriptionVersion.

            

        :return: The state of this SubscriptionVersion.
        :rtype: SubscriptionVersionState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubscriptionVersion.

            

        :param state: The state of this SubscriptionVersion.
        :type: SubscriptionVersionState
        """

        self._state = state
    
    @property
    def subscription(self):
        """Gets the subscription of this SubscriptionVersion.

            

        :return: The subscription of this SubscriptionVersion.
        :rtype: Subscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this SubscriptionVersion.

            

        :param subscription: The subscription of this SubscriptionVersion.
        :type: Subscription
        """

        self._subscription = subscription
    
    @property
    def terminated_on(self):
        """Gets the terminated_on of this SubscriptionVersion.

            

        :return: The terminated_on of this SubscriptionVersion.
        :rtype: datetime
        """
        return self._terminated_on

    @terminated_on.setter
    def terminated_on(self, terminated_on):
        """Sets the terminated_on of this SubscriptionVersion.

            

        :param terminated_on: The terminated_on of this SubscriptionVersion.
        :type: datetime
        """

        self._terminated_on = terminated_on
    
    @property
    def terminating_on(self):
        """Gets the terminating_on of this SubscriptionVersion.

            

        :return: The terminating_on of this SubscriptionVersion.
        :rtype: datetime
        """
        return self._terminating_on

    @terminating_on.setter
    def terminating_on(self, terminating_on):
        """Sets the terminating_on of this SubscriptionVersion.

            

        :param terminating_on: The terminating_on of this SubscriptionVersion.
        :type: datetime
        """

        self._terminating_on = terminating_on
    
    @property
    def termination_issued_on(self):
        """Gets the termination_issued_on of this SubscriptionVersion.

            

        :return: The termination_issued_on of this SubscriptionVersion.
        :rtype: datetime
        """
        return self._termination_issued_on

    @termination_issued_on.setter
    def termination_issued_on(self, termination_issued_on):
        """Sets the termination_issued_on of this SubscriptionVersion.

            

        :param termination_issued_on: The termination_issued_on of this SubscriptionVersion.
        :type: datetime
        """

        self._termination_issued_on = termination_issued_on
    
    @property
    def version(self):
        """Gets the version of this SubscriptionVersion.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this SubscriptionVersion.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SubscriptionVersion.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this SubscriptionVersion.
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
        if issubclass(SubscriptionVersion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
