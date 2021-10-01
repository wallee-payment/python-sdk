# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionChargeCreate:

    swagger_types = {
    
        'external_id': 'str',
        'failed_url': 'str',
        'planned_execution_date': 'datetime',
        'processing_type': 'SubscriptionChargeProcessingType',
        'reference': 'str',
        'subscription': 'int',
        'success_url': 'str',
    }

    attribute_map = {
        'external_id': 'externalId','failed_url': 'failedUrl','planned_execution_date': 'plannedExecutionDate','processing_type': 'processingType','reference': 'reference','subscription': 'subscription','success_url': 'successUrl',
    }

    
    _external_id = None
    _failed_url = None
    _planned_execution_date = None
    _processing_type = None
    _reference = None
    _subscription = None
    _success_url = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.external_id = kwargs.get('external_id')

        self.failed_url = kwargs.get('failed_url', None)
        self.planned_execution_date = kwargs.get('planned_execution_date', None)
        self.processing_type = kwargs.get('processing_type')

        self.reference = kwargs.get('reference', None)
        self.subscription = kwargs.get('subscription')

        self.success_url = kwargs.get('success_url', None)
        

    
    @property
    def external_id(self):
        """Gets the external_id of this SubscriptionChargeCreate.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :return: The external_id of this SubscriptionChargeCreate.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this SubscriptionChargeCreate.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :param external_id: The external_id of this SubscriptionChargeCreate.
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")

        self._external_id = external_id
    
    @property
    def failed_url(self):
        """Gets the failed_url of this SubscriptionChargeCreate.

            The user will be redirected to failed URL when the transaction could not be authorized or completed. In case no failed URL is specified a default failed page will be displayed.

        :return: The failed_url of this SubscriptionChargeCreate.
        :rtype: str
        """
        return self._failed_url

    @failed_url.setter
    def failed_url(self, failed_url):
        """Sets the failed_url of this SubscriptionChargeCreate.

            The user will be redirected to failed URL when the transaction could not be authorized or completed. In case no failed URL is specified a default failed page will be displayed.

        :param failed_url: The failed_url of this SubscriptionChargeCreate.
        :type: str
        """
        if failed_url is not None and len(failed_url) > 500:
            raise ValueError("Invalid value for `failed_url`, length must be less than or equal to `500`")
        if failed_url is not None and len(failed_url) < 9:
            raise ValueError("Invalid value for `failed_url`, length must be greater than or equal to `9`")

        self._failed_url = failed_url
    
    @property
    def planned_execution_date(self):
        """Gets the planned_execution_date of this SubscriptionChargeCreate.

            

        :return: The planned_execution_date of this SubscriptionChargeCreate.
        :rtype: datetime
        """
        return self._planned_execution_date

    @planned_execution_date.setter
    def planned_execution_date(self, planned_execution_date):
        """Sets the planned_execution_date of this SubscriptionChargeCreate.

            

        :param planned_execution_date: The planned_execution_date of this SubscriptionChargeCreate.
        :type: datetime
        """

        self._planned_execution_date = planned_execution_date
    
    @property
    def processing_type(self):
        """Gets the processing_type of this SubscriptionChargeCreate.

            

        :return: The processing_type of this SubscriptionChargeCreate.
        :rtype: SubscriptionChargeProcessingType
        """
        return self._processing_type

    @processing_type.setter
    def processing_type(self, processing_type):
        """Sets the processing_type of this SubscriptionChargeCreate.

            

        :param processing_type: The processing_type of this SubscriptionChargeCreate.
        :type: SubscriptionChargeProcessingType
        """
        if processing_type is None:
            raise ValueError("Invalid value for `processing_type`, must not be `None`")

        self._processing_type = processing_type
    
    @property
    def reference(self):
        """Gets the reference of this SubscriptionChargeCreate.

            

        :return: The reference of this SubscriptionChargeCreate.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this SubscriptionChargeCreate.

            

        :param reference: The reference of this SubscriptionChargeCreate.
        :type: str
        """
        if reference is not None and len(reference) > 100:
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `100`")

        self._reference = reference
    
    @property
    def subscription(self):
        """Gets the subscription of this SubscriptionChargeCreate.

            The field subscription indicates the subscription to which the charge belongs to.

        :return: The subscription of this SubscriptionChargeCreate.
        :rtype: int
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this SubscriptionChargeCreate.

            The field subscription indicates the subscription to which the charge belongs to.

        :param subscription: The subscription of this SubscriptionChargeCreate.
        :type: int
        """
        if subscription is None:
            raise ValueError("Invalid value for `subscription`, must not be `None`")

        self._subscription = subscription
    
    @property
    def success_url(self):
        """Gets the success_url of this SubscriptionChargeCreate.

            The user will be redirected to success URL when the transaction could be authorized or completed. In case no success URL is specified a default success page will be displayed.

        :return: The success_url of this SubscriptionChargeCreate.
        :rtype: str
        """
        return self._success_url

    @success_url.setter
    def success_url(self, success_url):
        """Sets the success_url of this SubscriptionChargeCreate.

            The user will be redirected to success URL when the transaction could be authorized or completed. In case no success URL is specified a default success page will be displayed.

        :param success_url: The success_url of this SubscriptionChargeCreate.
        :type: str
        """
        if success_url is not None and len(success_url) > 500:
            raise ValueError("Invalid value for `success_url`, length must be less than or equal to `500`")
        if success_url is not None and len(success_url) < 9:
            raise ValueError("Invalid value for `success_url`, length must be greater than or equal to `9`")

        self._success_url = success_url
    

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
        if issubclass(SubscriptionChargeCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionChargeCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
