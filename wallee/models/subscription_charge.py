# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionCharge:

    swagger_types = {
    
        'created_on': 'datetime',
        'discarded_by': 'int',
        'discarded_on': 'datetime',
        'external_id': 'str',
        'failed_on': 'datetime',
        'failed_url': 'str',
        'id': 'int',
        'language': 'str',
        'ledger_entries': 'list[SubscriptionLedgerEntry]',
        'linked_space_id': 'int',
        'planned_execution_date': 'datetime',
        'planned_purge_date': 'datetime',
        'processing_type': 'SubscriptionChargeProcessingType',
        'reference': 'str',
        'state': 'SubscriptionChargeState',
        'subscription': 'Subscription',
        'succeed_on': 'datetime',
        'success_url': 'str',
        'transaction': 'Transaction',
        'type': 'SubscriptionChargeType',
        'version': 'int',
    }

    attribute_map = {
        'created_on': 'createdOn','discarded_by': 'discardedBy','discarded_on': 'discardedOn','external_id': 'externalId','failed_on': 'failedOn','failed_url': 'failedUrl','id': 'id','language': 'language','ledger_entries': 'ledgerEntries','linked_space_id': 'linkedSpaceId','planned_execution_date': 'plannedExecutionDate','planned_purge_date': 'plannedPurgeDate','processing_type': 'processingType','reference': 'reference','state': 'state','subscription': 'subscription','succeed_on': 'succeedOn','success_url': 'successUrl','transaction': 'transaction','type': 'type','version': 'version',
    }

    
    _created_on = None
    _discarded_by = None
    _discarded_on = None
    _external_id = None
    _failed_on = None
    _failed_url = None
    _id = None
    _language = None
    _ledger_entries = None
    _linked_space_id = None
    _planned_execution_date = None
    _planned_purge_date = None
    _processing_type = None
    _reference = None
    _state = None
    _subscription = None
    _succeed_on = None
    _success_url = None
    _transaction = None
    _type = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.created_on = kwargs.get('created_on', None)
        self.discarded_by = kwargs.get('discarded_by', None)
        self.discarded_on = kwargs.get('discarded_on', None)
        self.external_id = kwargs.get('external_id', None)
        self.failed_on = kwargs.get('failed_on', None)
        self.failed_url = kwargs.get('failed_url', None)
        self.id = kwargs.get('id', None)
        self.language = kwargs.get('language', None)
        self.ledger_entries = kwargs.get('ledger_entries', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.planned_execution_date = kwargs.get('planned_execution_date', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.processing_type = kwargs.get('processing_type', None)
        self.reference = kwargs.get('reference', None)
        self.state = kwargs.get('state', None)
        self.subscription = kwargs.get('subscription', None)
        self.succeed_on = kwargs.get('succeed_on', None)
        self.success_url = kwargs.get('success_url', None)
        self.transaction = kwargs.get('transaction', None)
        self.type = kwargs.get('type', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def created_on(self):
        """Gets the created_on of this SubscriptionCharge.

            

        :return: The created_on of this SubscriptionCharge.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this SubscriptionCharge.

            

        :param created_on: The created_on of this SubscriptionCharge.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def discarded_by(self):
        """Gets the discarded_by of this SubscriptionCharge.

            

        :return: The discarded_by of this SubscriptionCharge.
        :rtype: int
        """
        return self._discarded_by

    @discarded_by.setter
    def discarded_by(self, discarded_by):
        """Sets the discarded_by of this SubscriptionCharge.

            

        :param discarded_by: The discarded_by of this SubscriptionCharge.
        :type: int
        """

        self._discarded_by = discarded_by
    
    @property
    def discarded_on(self):
        """Gets the discarded_on of this SubscriptionCharge.

            

        :return: The discarded_on of this SubscriptionCharge.
        :rtype: datetime
        """
        return self._discarded_on

    @discarded_on.setter
    def discarded_on(self, discarded_on):
        """Sets the discarded_on of this SubscriptionCharge.

            

        :param discarded_on: The discarded_on of this SubscriptionCharge.
        :type: datetime
        """

        self._discarded_on = discarded_on
    
    @property
    def external_id(self):
        """Gets the external_id of this SubscriptionCharge.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :return: The external_id of this SubscriptionCharge.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this SubscriptionCharge.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :param external_id: The external_id of this SubscriptionCharge.
        :type: str
        """

        self._external_id = external_id
    
    @property
    def failed_on(self):
        """Gets the failed_on of this SubscriptionCharge.

            

        :return: The failed_on of this SubscriptionCharge.
        :rtype: datetime
        """
        return self._failed_on

    @failed_on.setter
    def failed_on(self, failed_on):
        """Sets the failed_on of this SubscriptionCharge.

            

        :param failed_on: The failed_on of this SubscriptionCharge.
        :type: datetime
        """

        self._failed_on = failed_on
    
    @property
    def failed_url(self):
        """Gets the failed_url of this SubscriptionCharge.

            The user will be redirected to failed URL when the transaction could not be authorized or completed. In case no failed URL is specified a default failed page will be displayed.

        :return: The failed_url of this SubscriptionCharge.
        :rtype: str
        """
        return self._failed_url

    @failed_url.setter
    def failed_url(self, failed_url):
        """Sets the failed_url of this SubscriptionCharge.

            The user will be redirected to failed URL when the transaction could not be authorized or completed. In case no failed URL is specified a default failed page will be displayed.

        :param failed_url: The failed_url of this SubscriptionCharge.
        :type: str
        """
        if failed_url is not None and len(failed_url) > 500:
            raise ValueError("Invalid value for `failed_url`, length must be less than or equal to `500`")
        if failed_url is not None and len(failed_url) < 9:
            raise ValueError("Invalid value for `failed_url`, length must be greater than or equal to `9`")

        self._failed_url = failed_url
    
    @property
    def id(self):
        """Gets the id of this SubscriptionCharge.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this SubscriptionCharge.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionCharge.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this SubscriptionCharge.
        :type: int
        """

        self._id = id
    
    @property
    def language(self):
        """Gets the language of this SubscriptionCharge.

            

        :return: The language of this SubscriptionCharge.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SubscriptionCharge.

            

        :param language: The language of this SubscriptionCharge.
        :type: str
        """

        self._language = language
    
    @property
    def ledger_entries(self):
        """Gets the ledger_entries of this SubscriptionCharge.

            

        :return: The ledger_entries of this SubscriptionCharge.
        :rtype: list[SubscriptionLedgerEntry]
        """
        return self._ledger_entries

    @ledger_entries.setter
    def ledger_entries(self, ledger_entries):
        """Sets the ledger_entries of this SubscriptionCharge.

            

        :param ledger_entries: The ledger_entries of this SubscriptionCharge.
        :type: list[SubscriptionLedgerEntry]
        """

        self._ledger_entries = ledger_entries
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this SubscriptionCharge.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this SubscriptionCharge.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this SubscriptionCharge.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this SubscriptionCharge.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def planned_execution_date(self):
        """Gets the planned_execution_date of this SubscriptionCharge.

            

        :return: The planned_execution_date of this SubscriptionCharge.
        :rtype: datetime
        """
        return self._planned_execution_date

    @planned_execution_date.setter
    def planned_execution_date(self, planned_execution_date):
        """Sets the planned_execution_date of this SubscriptionCharge.

            

        :param planned_execution_date: The planned_execution_date of this SubscriptionCharge.
        :type: datetime
        """

        self._planned_execution_date = planned_execution_date
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this SubscriptionCharge.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this SubscriptionCharge.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this SubscriptionCharge.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this SubscriptionCharge.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def processing_type(self):
        """Gets the processing_type of this SubscriptionCharge.

            

        :return: The processing_type of this SubscriptionCharge.
        :rtype: SubscriptionChargeProcessingType
        """
        return self._processing_type

    @processing_type.setter
    def processing_type(self, processing_type):
        """Sets the processing_type of this SubscriptionCharge.

            

        :param processing_type: The processing_type of this SubscriptionCharge.
        :type: SubscriptionChargeProcessingType
        """

        self._processing_type = processing_type
    
    @property
    def reference(self):
        """Gets the reference of this SubscriptionCharge.

            

        :return: The reference of this SubscriptionCharge.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this SubscriptionCharge.

            

        :param reference: The reference of this SubscriptionCharge.
        :type: str
        """
        if reference is not None and len(reference) > 100:
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `100`")

        self._reference = reference
    
    @property
    def state(self):
        """Gets the state of this SubscriptionCharge.

            

        :return: The state of this SubscriptionCharge.
        :rtype: SubscriptionChargeState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubscriptionCharge.

            

        :param state: The state of this SubscriptionCharge.
        :type: SubscriptionChargeState
        """

        self._state = state
    
    @property
    def subscription(self):
        """Gets the subscription of this SubscriptionCharge.

            The field subscription indicates the subscription to which the charge belongs to.

        :return: The subscription of this SubscriptionCharge.
        :rtype: Subscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this SubscriptionCharge.

            The field subscription indicates the subscription to which the charge belongs to.

        :param subscription: The subscription of this SubscriptionCharge.
        :type: Subscription
        """

        self._subscription = subscription
    
    @property
    def succeed_on(self):
        """Gets the succeed_on of this SubscriptionCharge.

            

        :return: The succeed_on of this SubscriptionCharge.
        :rtype: datetime
        """
        return self._succeed_on

    @succeed_on.setter
    def succeed_on(self, succeed_on):
        """Sets the succeed_on of this SubscriptionCharge.

            

        :param succeed_on: The succeed_on of this SubscriptionCharge.
        :type: datetime
        """

        self._succeed_on = succeed_on
    
    @property
    def success_url(self):
        """Gets the success_url of this SubscriptionCharge.

            The user will be redirected to success URL when the transaction could be authorized or completed. In case no success URL is specified a default success page will be displayed.

        :return: The success_url of this SubscriptionCharge.
        :rtype: str
        """
        return self._success_url

    @success_url.setter
    def success_url(self, success_url):
        """Sets the success_url of this SubscriptionCharge.

            The user will be redirected to success URL when the transaction could be authorized or completed. In case no success URL is specified a default success page will be displayed.

        :param success_url: The success_url of this SubscriptionCharge.
        :type: str
        """
        if success_url is not None and len(success_url) > 500:
            raise ValueError("Invalid value for `success_url`, length must be less than or equal to `500`")
        if success_url is not None and len(success_url) < 9:
            raise ValueError("Invalid value for `success_url`, length must be greater than or equal to `9`")

        self._success_url = success_url
    
    @property
    def transaction(self):
        """Gets the transaction of this SubscriptionCharge.

            

        :return: The transaction of this SubscriptionCharge.
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this SubscriptionCharge.

            

        :param transaction: The transaction of this SubscriptionCharge.
        :type: Transaction
        """

        self._transaction = transaction
    
    @property
    def type(self):
        """Gets the type of this SubscriptionCharge.

            

        :return: The type of this SubscriptionCharge.
        :rtype: SubscriptionChargeType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SubscriptionCharge.

            

        :param type: The type of this SubscriptionCharge.
        :type: SubscriptionChargeType
        """

        self._type = type
    
    @property
    def version(self):
        """Gets the version of this SubscriptionCharge.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this SubscriptionCharge.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SubscriptionCharge.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this SubscriptionCharge.
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
        if issubclass(SubscriptionCharge, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionCharge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
