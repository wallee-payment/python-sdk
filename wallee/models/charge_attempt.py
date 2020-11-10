# coding: utf-8
import pprint
import six
from enum import Enum
from . import TransactionAwareEntity


class ChargeAttempt(TransactionAwareEntity):

    swagger_types = {
    
        'charge': 'Charge',
        'completion_behavior': 'TransactionCompletionBehavior',
        'connector_configuration': 'PaymentConnectorConfiguration',
        'created_on': 'datetime',
        'environment': 'ChargeAttemptEnvironment',
        'failed_on': 'datetime',
        'failure_reason': 'FailureReason',
        'initializing_token_version': 'bool',
        'invocation': 'ConnectorInvocation',
        'labels': 'list[Label]',
        'language': 'str',
        'next_update_on': 'datetime',
        'planned_purge_date': 'datetime',
        'redirection_url': 'str',
        'sales_channel': 'int',
        'space_view_id': 'int',
        'state': 'ChargeAttemptState',
        'succeeded_on': 'datetime',
        'terminal': 'PaymentTerminal',
        'time_zone': 'str',
        'timeout_on': 'datetime',
        'token_version': 'TokenVersion',
        'user_failure_message': 'str',
        'version': 'int',
    }

    attribute_map = {
        'charge': 'charge','completion_behavior': 'completionBehavior','connector_configuration': 'connectorConfiguration','created_on': 'createdOn','environment': 'environment','failed_on': 'failedOn','failure_reason': 'failureReason','initializing_token_version': 'initializingTokenVersion','invocation': 'invocation','labels': 'labels','language': 'language','next_update_on': 'nextUpdateOn','planned_purge_date': 'plannedPurgeDate','redirection_url': 'redirectionUrl','sales_channel': 'salesChannel','space_view_id': 'spaceViewId','state': 'state','succeeded_on': 'succeededOn','terminal': 'terminal','time_zone': 'timeZone','timeout_on': 'timeoutOn','token_version': 'tokenVersion','user_failure_message': 'userFailureMessage','version': 'version',
    }

    
    _charge = None
    _completion_behavior = None
    _connector_configuration = None
    _created_on = None
    _environment = None
    _failed_on = None
    _failure_reason = None
    _initializing_token_version = None
    _invocation = None
    _labels = None
    _language = None
    _next_update_on = None
    _planned_purge_date = None
    _redirection_url = None
    _sales_channel = None
    _space_view_id = None
    _state = None
    _succeeded_on = None
    _terminal = None
    _time_zone = None
    _timeout_on = None
    _token_version = None
    _user_failure_message = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.charge = kwargs.get('charge', None)
        self.completion_behavior = kwargs.get('completion_behavior', None)
        self.connector_configuration = kwargs.get('connector_configuration', None)
        self.created_on = kwargs.get('created_on', None)
        self.environment = kwargs.get('environment', None)
        self.failed_on = kwargs.get('failed_on', None)
        self.failure_reason = kwargs.get('failure_reason', None)
        self.initializing_token_version = kwargs.get('initializing_token_version', None)
        self.invocation = kwargs.get('invocation', None)
        self.labels = kwargs.get('labels', None)
        self.language = kwargs.get('language', None)
        self.next_update_on = kwargs.get('next_update_on', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.redirection_url = kwargs.get('redirection_url', None)
        self.sales_channel = kwargs.get('sales_channel', None)
        self.space_view_id = kwargs.get('space_view_id', None)
        self.state = kwargs.get('state', None)
        self.succeeded_on = kwargs.get('succeeded_on', None)
        self.terminal = kwargs.get('terminal', None)
        self.time_zone = kwargs.get('time_zone', None)
        self.timeout_on = kwargs.get('timeout_on', None)
        self.token_version = kwargs.get('token_version', None)
        self.user_failure_message = kwargs.get('user_failure_message', None)
        self.version = kwargs.get('version', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def charge(self):
        """Gets the charge of this ChargeAttempt.

            

        :return: The charge of this ChargeAttempt.
        :rtype: Charge
        """
        return self._charge

    @charge.setter
    def charge(self, charge):
        """Sets the charge of this ChargeAttempt.

            

        :param charge: The charge of this ChargeAttempt.
        :type: Charge
        """

        self._charge = charge
    
    @property
    def completion_behavior(self):
        """Gets the completion_behavior of this ChargeAttempt.

            

        :return: The completion_behavior of this ChargeAttempt.
        :rtype: TransactionCompletionBehavior
        """
        return self._completion_behavior

    @completion_behavior.setter
    def completion_behavior(self, completion_behavior):
        """Sets the completion_behavior of this ChargeAttempt.

            

        :param completion_behavior: The completion_behavior of this ChargeAttempt.
        :type: TransactionCompletionBehavior
        """

        self._completion_behavior = completion_behavior
    
    @property
    def connector_configuration(self):
        """Gets the connector_configuration of this ChargeAttempt.

            

        :return: The connector_configuration of this ChargeAttempt.
        :rtype: PaymentConnectorConfiguration
        """
        return self._connector_configuration

    @connector_configuration.setter
    def connector_configuration(self, connector_configuration):
        """Sets the connector_configuration of this ChargeAttempt.

            

        :param connector_configuration: The connector_configuration of this ChargeAttempt.
        :type: PaymentConnectorConfiguration
        """

        self._connector_configuration = connector_configuration
    
    @property
    def created_on(self):
        """Gets the created_on of this ChargeAttempt.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this ChargeAttempt.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this ChargeAttempt.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this ChargeAttempt.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def environment(self):
        """Gets the environment of this ChargeAttempt.

            

        :return: The environment of this ChargeAttempt.
        :rtype: ChargeAttemptEnvironment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this ChargeAttempt.

            

        :param environment: The environment of this ChargeAttempt.
        :type: ChargeAttemptEnvironment
        """

        self._environment = environment
    
    @property
    def failed_on(self):
        """Gets the failed_on of this ChargeAttempt.

            

        :return: The failed_on of this ChargeAttempt.
        :rtype: datetime
        """
        return self._failed_on

    @failed_on.setter
    def failed_on(self, failed_on):
        """Sets the failed_on of this ChargeAttempt.

            

        :param failed_on: The failed_on of this ChargeAttempt.
        :type: datetime
        """

        self._failed_on = failed_on
    
    @property
    def failure_reason(self):
        """Gets the failure_reason of this ChargeAttempt.

            

        :return: The failure_reason of this ChargeAttempt.
        :rtype: FailureReason
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this ChargeAttempt.

            

        :param failure_reason: The failure_reason of this ChargeAttempt.
        :type: FailureReason
        """

        self._failure_reason = failure_reason
    
    @property
    def initializing_token_version(self):
        """Gets the initializing_token_version of this ChargeAttempt.

            

        :return: The initializing_token_version of this ChargeAttempt.
        :rtype: bool
        """
        return self._initializing_token_version

    @initializing_token_version.setter
    def initializing_token_version(self, initializing_token_version):
        """Sets the initializing_token_version of this ChargeAttempt.

            

        :param initializing_token_version: The initializing_token_version of this ChargeAttempt.
        :type: bool
        """

        self._initializing_token_version = initializing_token_version
    
    @property
    def invocation(self):
        """Gets the invocation of this ChargeAttempt.

            

        :return: The invocation of this ChargeAttempt.
        :rtype: ConnectorInvocation
        """
        return self._invocation

    @invocation.setter
    def invocation(self, invocation):
        """Sets the invocation of this ChargeAttempt.

            

        :param invocation: The invocation of this ChargeAttempt.
        :type: ConnectorInvocation
        """

        self._invocation = invocation
    
    @property
    def labels(self):
        """Gets the labels of this ChargeAttempt.

            

        :return: The labels of this ChargeAttempt.
        :rtype: list[Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ChargeAttempt.

            

        :param labels: The labels of this ChargeAttempt.
        :type: list[Label]
        """

        self._labels = labels
    
    @property
    def language(self):
        """Gets the language of this ChargeAttempt.

            

        :return: The language of this ChargeAttempt.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ChargeAttempt.

            

        :param language: The language of this ChargeAttempt.
        :type: str
        """

        self._language = language
    
    @property
    def next_update_on(self):
        """Gets the next_update_on of this ChargeAttempt.

            

        :return: The next_update_on of this ChargeAttempt.
        :rtype: datetime
        """
        return self._next_update_on

    @next_update_on.setter
    def next_update_on(self, next_update_on):
        """Sets the next_update_on of this ChargeAttempt.

            

        :param next_update_on: The next_update_on of this ChargeAttempt.
        :type: datetime
        """

        self._next_update_on = next_update_on
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this ChargeAttempt.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this ChargeAttempt.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this ChargeAttempt.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this ChargeAttempt.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def redirection_url(self):
        """Gets the redirection_url of this ChargeAttempt.

            

        :return: The redirection_url of this ChargeAttempt.
        :rtype: str
        """
        return self._redirection_url

    @redirection_url.setter
    def redirection_url(self, redirection_url):
        """Sets the redirection_url of this ChargeAttempt.

            

        :param redirection_url: The redirection_url of this ChargeAttempt.
        :type: str
        """

        self._redirection_url = redirection_url
    
    @property
    def sales_channel(self):
        """Gets the sales_channel of this ChargeAttempt.

            

        :return: The sales_channel of this ChargeAttempt.
        :rtype: int
        """
        return self._sales_channel

    @sales_channel.setter
    def sales_channel(self, sales_channel):
        """Sets the sales_channel of this ChargeAttempt.

            

        :param sales_channel: The sales_channel of this ChargeAttempt.
        :type: int
        """

        self._sales_channel = sales_channel
    
    @property
    def space_view_id(self):
        """Gets the space_view_id of this ChargeAttempt.

            

        :return: The space_view_id of this ChargeAttempt.
        :rtype: int
        """
        return self._space_view_id

    @space_view_id.setter
    def space_view_id(self, space_view_id):
        """Sets the space_view_id of this ChargeAttempt.

            

        :param space_view_id: The space_view_id of this ChargeAttempt.
        :type: int
        """

        self._space_view_id = space_view_id
    
    @property
    def state(self):
        """Gets the state of this ChargeAttempt.

            

        :return: The state of this ChargeAttempt.
        :rtype: ChargeAttemptState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ChargeAttempt.

            

        :param state: The state of this ChargeAttempt.
        :type: ChargeAttemptState
        """

        self._state = state
    
    @property
    def succeeded_on(self):
        """Gets the succeeded_on of this ChargeAttempt.

            

        :return: The succeeded_on of this ChargeAttempt.
        :rtype: datetime
        """
        return self._succeeded_on

    @succeeded_on.setter
    def succeeded_on(self, succeeded_on):
        """Sets the succeeded_on of this ChargeAttempt.

            

        :param succeeded_on: The succeeded_on of this ChargeAttempt.
        :type: datetime
        """

        self._succeeded_on = succeeded_on
    
    @property
    def terminal(self):
        """Gets the terminal of this ChargeAttempt.

            

        :return: The terminal of this ChargeAttempt.
        :rtype: PaymentTerminal
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this ChargeAttempt.

            

        :param terminal: The terminal of this ChargeAttempt.
        :type: PaymentTerminal
        """

        self._terminal = terminal
    
    @property
    def time_zone(self):
        """Gets the time_zone of this ChargeAttempt.

            

        :return: The time_zone of this ChargeAttempt.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this ChargeAttempt.

            

        :param time_zone: The time_zone of this ChargeAttempt.
        :type: str
        """

        self._time_zone = time_zone
    
    @property
    def timeout_on(self):
        """Gets the timeout_on of this ChargeAttempt.

            

        :return: The timeout_on of this ChargeAttempt.
        :rtype: datetime
        """
        return self._timeout_on

    @timeout_on.setter
    def timeout_on(self, timeout_on):
        """Sets the timeout_on of this ChargeAttempt.

            

        :param timeout_on: The timeout_on of this ChargeAttempt.
        :type: datetime
        """

        self._timeout_on = timeout_on
    
    @property
    def token_version(self):
        """Gets the token_version of this ChargeAttempt.

            

        :return: The token_version of this ChargeAttempt.
        :rtype: TokenVersion
        """
        return self._token_version

    @token_version.setter
    def token_version(self, token_version):
        """Sets the token_version of this ChargeAttempt.

            

        :param token_version: The token_version of this ChargeAttempt.
        :type: TokenVersion
        """

        self._token_version = token_version
    
    @property
    def user_failure_message(self):
        """Gets the user_failure_message of this ChargeAttempt.

            The user failure message contains the message for the user in case the attempt failed. The message is localized into the language specified on the transaction.

        :return: The user_failure_message of this ChargeAttempt.
        :rtype: str
        """
        return self._user_failure_message

    @user_failure_message.setter
    def user_failure_message(self, user_failure_message):
        """Sets the user_failure_message of this ChargeAttempt.

            The user failure message contains the message for the user in case the attempt failed. The message is localized into the language specified on the transaction.

        :param user_failure_message: The user_failure_message of this ChargeAttempt.
        :type: str
        """
        if user_failure_message is not None and len(user_failure_message) > 2000:
            raise ValueError("Invalid value for `user_failure_message`, length must be less than or equal to `2000`")

        self._user_failure_message = user_failure_message
    
    @property
    def version(self):
        """Gets the version of this ChargeAttempt.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ChargeAttempt.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ChargeAttempt.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ChargeAttempt.
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
        if issubclass(ChargeAttempt, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ChargeAttempt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
