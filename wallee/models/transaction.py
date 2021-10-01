# coding: utf-8
import pprint
import six
from enum import Enum



class Transaction:

    swagger_types = {
    
        'accept_header': 'str',
        'accept_language_header': 'str',
        'allowed_payment_method_brands': 'list[PaymentMethodBrand]',
        'allowed_payment_method_configurations': 'list[int]',
        'authorization_amount': 'float',
        'authorization_environment': 'ChargeAttemptEnvironment',
        'authorization_sales_channel': 'int',
        'authorization_timeout_on': 'datetime',
        'authorized_on': 'datetime',
        'auto_confirmation_enabled': 'bool',
        'billing_address': 'Address',
        'charge_retry_enabled': 'bool',
        'completed_amount': 'float',
        'completed_on': 'datetime',
        'completion_behavior': 'TransactionCompletionBehavior',
        'completion_timeout_on': 'datetime',
        'confirmed_by': 'int',
        'confirmed_on': 'datetime',
        'created_by': 'int',
        'created_on': 'datetime',
        'currency': 'str',
        'customer_email_address': 'str',
        'customer_id': 'str',
        'customers_presence': 'CustomersPresence',
        'delivery_decision_made_on': 'datetime',
        'device_session_identifier': 'str',
        'emails_disabled': 'bool',
        'end_of_life': 'datetime',
        'environment': 'Environment',
        'environment_selection_strategy': 'TransactionEnvironmentSelectionStrategy',
        'failed_on': 'datetime',
        'failed_url': 'str',
        'failure_reason': 'FailureReason',
        'group': 'TransactionGroup',
        'id': 'int',
        'internet_protocol_address': 'str',
        'internet_protocol_address_country': 'str',
        'invoice_merchant_reference': 'str',
        'java_enabled': 'bool',
        'language': 'str',
        'line_items': 'list[LineItem]',
        'linked_space_id': 'int',
        'merchant_reference': 'str',
        'meta_data': 'dict(str, str)',
        'parent': 'int',
        'payment_connector_configuration': 'PaymentConnectorConfiguration',
        'planned_purge_date': 'datetime',
        'processing_on': 'datetime',
        'refunded_amount': 'float',
        'screen_color_depth': 'str',
        'screen_height': 'str',
        'screen_width': 'str',
        'shipping_address': 'Address',
        'shipping_method': 'str',
        'space_view_id': 'int',
        'state': 'TransactionState',
        'success_url': 'str',
        'terminal': 'PaymentTerminal',
        'time_zone': 'str',
        'token': 'Token',
        'tokenization_mode': 'TokenizationMode',
        'total_applied_fees': 'float',
        'total_settled_amount': 'float',
        'user_agent_header': 'str',
        'user_failure_message': 'str',
        'user_interface_type': 'TransactionUserInterfaceType',
        'version': 'int',
        'window_height': 'str',
        'window_width': 'str',
    }

    attribute_map = {
        'accept_header': 'acceptHeader','accept_language_header': 'acceptLanguageHeader','allowed_payment_method_brands': 'allowedPaymentMethodBrands','allowed_payment_method_configurations': 'allowedPaymentMethodConfigurations','authorization_amount': 'authorizationAmount','authorization_environment': 'authorizationEnvironment','authorization_sales_channel': 'authorizationSalesChannel','authorization_timeout_on': 'authorizationTimeoutOn','authorized_on': 'authorizedOn','auto_confirmation_enabled': 'autoConfirmationEnabled','billing_address': 'billingAddress','charge_retry_enabled': 'chargeRetryEnabled','completed_amount': 'completedAmount','completed_on': 'completedOn','completion_behavior': 'completionBehavior','completion_timeout_on': 'completionTimeoutOn','confirmed_by': 'confirmedBy','confirmed_on': 'confirmedOn','created_by': 'createdBy','created_on': 'createdOn','currency': 'currency','customer_email_address': 'customerEmailAddress','customer_id': 'customerId','customers_presence': 'customersPresence','delivery_decision_made_on': 'deliveryDecisionMadeOn','device_session_identifier': 'deviceSessionIdentifier','emails_disabled': 'emailsDisabled','end_of_life': 'endOfLife','environment': 'environment','environment_selection_strategy': 'environmentSelectionStrategy','failed_on': 'failedOn','failed_url': 'failedUrl','failure_reason': 'failureReason','group': 'group','id': 'id','internet_protocol_address': 'internetProtocolAddress','internet_protocol_address_country': 'internetProtocolAddressCountry','invoice_merchant_reference': 'invoiceMerchantReference','java_enabled': 'javaEnabled','language': 'language','line_items': 'lineItems','linked_space_id': 'linkedSpaceId','merchant_reference': 'merchantReference','meta_data': 'metaData','parent': 'parent','payment_connector_configuration': 'paymentConnectorConfiguration','planned_purge_date': 'plannedPurgeDate','processing_on': 'processingOn','refunded_amount': 'refundedAmount','screen_color_depth': 'screenColorDepth','screen_height': 'screenHeight','screen_width': 'screenWidth','shipping_address': 'shippingAddress','shipping_method': 'shippingMethod','space_view_id': 'spaceViewId','state': 'state','success_url': 'successUrl','terminal': 'terminal','time_zone': 'timeZone','token': 'token','tokenization_mode': 'tokenizationMode','total_applied_fees': 'totalAppliedFees','total_settled_amount': 'totalSettledAmount','user_agent_header': 'userAgentHeader','user_failure_message': 'userFailureMessage','user_interface_type': 'userInterfaceType','version': 'version','window_height': 'windowHeight','window_width': 'windowWidth',
    }

    
    _accept_header = None
    _accept_language_header = None
    _allowed_payment_method_brands = None
    _allowed_payment_method_configurations = None
    _authorization_amount = None
    _authorization_environment = None
    _authorization_sales_channel = None
    _authorization_timeout_on = None
    _authorized_on = None
    _auto_confirmation_enabled = None
    _billing_address = None
    _charge_retry_enabled = None
    _completed_amount = None
    _completed_on = None
    _completion_behavior = None
    _completion_timeout_on = None
    _confirmed_by = None
    _confirmed_on = None
    _created_by = None
    _created_on = None
    _currency = None
    _customer_email_address = None
    _customer_id = None
    _customers_presence = None
    _delivery_decision_made_on = None
    _device_session_identifier = None
    _emails_disabled = None
    _end_of_life = None
    _environment = None
    _environment_selection_strategy = None
    _failed_on = None
    _failed_url = None
    _failure_reason = None
    _group = None
    _id = None
    _internet_protocol_address = None
    _internet_protocol_address_country = None
    _invoice_merchant_reference = None
    _java_enabled = None
    _language = None
    _line_items = None
    _linked_space_id = None
    _merchant_reference = None
    _meta_data = None
    _parent = None
    _payment_connector_configuration = None
    _planned_purge_date = None
    _processing_on = None
    _refunded_amount = None
    _screen_color_depth = None
    _screen_height = None
    _screen_width = None
    _shipping_address = None
    _shipping_method = None
    _space_view_id = None
    _state = None
    _success_url = None
    _terminal = None
    _time_zone = None
    _token = None
    _tokenization_mode = None
    _total_applied_fees = None
    _total_settled_amount = None
    _user_agent_header = None
    _user_failure_message = None
    _user_interface_type = None
    _version = None
    _window_height = None
    _window_width = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.accept_header = kwargs.get('accept_header', None)
        self.accept_language_header = kwargs.get('accept_language_header', None)
        self.allowed_payment_method_brands = kwargs.get('allowed_payment_method_brands', None)
        self.allowed_payment_method_configurations = kwargs.get('allowed_payment_method_configurations', None)
        self.authorization_amount = kwargs.get('authorization_amount', None)
        self.authorization_environment = kwargs.get('authorization_environment', None)
        self.authorization_sales_channel = kwargs.get('authorization_sales_channel', None)
        self.authorization_timeout_on = kwargs.get('authorization_timeout_on', None)
        self.authorized_on = kwargs.get('authorized_on', None)
        self.auto_confirmation_enabled = kwargs.get('auto_confirmation_enabled', None)
        self.billing_address = kwargs.get('billing_address', None)
        self.charge_retry_enabled = kwargs.get('charge_retry_enabled', None)
        self.completed_amount = kwargs.get('completed_amount', None)
        self.completed_on = kwargs.get('completed_on', None)
        self.completion_behavior = kwargs.get('completion_behavior', None)
        self.completion_timeout_on = kwargs.get('completion_timeout_on', None)
        self.confirmed_by = kwargs.get('confirmed_by', None)
        self.confirmed_on = kwargs.get('confirmed_on', None)
        self.created_by = kwargs.get('created_by', None)
        self.created_on = kwargs.get('created_on', None)
        self.currency = kwargs.get('currency', None)
        self.customer_email_address = kwargs.get('customer_email_address', None)
        self.customer_id = kwargs.get('customer_id', None)
        self.customers_presence = kwargs.get('customers_presence', None)
        self.delivery_decision_made_on = kwargs.get('delivery_decision_made_on', None)
        self.device_session_identifier = kwargs.get('device_session_identifier', None)
        self.emails_disabled = kwargs.get('emails_disabled', None)
        self.end_of_life = kwargs.get('end_of_life', None)
        self.environment = kwargs.get('environment', None)
        self.environment_selection_strategy = kwargs.get('environment_selection_strategy', None)
        self.failed_on = kwargs.get('failed_on', None)
        self.failed_url = kwargs.get('failed_url', None)
        self.failure_reason = kwargs.get('failure_reason', None)
        self.group = kwargs.get('group', None)
        self.id = kwargs.get('id', None)
        self.internet_protocol_address = kwargs.get('internet_protocol_address', None)
        self.internet_protocol_address_country = kwargs.get('internet_protocol_address_country', None)
        self.invoice_merchant_reference = kwargs.get('invoice_merchant_reference', None)
        self.java_enabled = kwargs.get('java_enabled', None)
        self.language = kwargs.get('language', None)
        self.line_items = kwargs.get('line_items', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.merchant_reference = kwargs.get('merchant_reference', None)
        self.meta_data = kwargs.get('meta_data', None)
        self.parent = kwargs.get('parent', None)
        self.payment_connector_configuration = kwargs.get('payment_connector_configuration', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.processing_on = kwargs.get('processing_on', None)
        self.refunded_amount = kwargs.get('refunded_amount', None)
        self.screen_color_depth = kwargs.get('screen_color_depth', None)
        self.screen_height = kwargs.get('screen_height', None)
        self.screen_width = kwargs.get('screen_width', None)
        self.shipping_address = kwargs.get('shipping_address', None)
        self.shipping_method = kwargs.get('shipping_method', None)
        self.space_view_id = kwargs.get('space_view_id', None)
        self.state = kwargs.get('state', None)
        self.success_url = kwargs.get('success_url', None)
        self.terminal = kwargs.get('terminal', None)
        self.time_zone = kwargs.get('time_zone', None)
        self.token = kwargs.get('token', None)
        self.tokenization_mode = kwargs.get('tokenization_mode', None)
        self.total_applied_fees = kwargs.get('total_applied_fees', None)
        self.total_settled_amount = kwargs.get('total_settled_amount', None)
        self.user_agent_header = kwargs.get('user_agent_header', None)
        self.user_failure_message = kwargs.get('user_failure_message', None)
        self.user_interface_type = kwargs.get('user_interface_type', None)
        self.version = kwargs.get('version', None)
        self.window_height = kwargs.get('window_height', None)
        self.window_width = kwargs.get('window_width', None)
        

    
    @property
    def accept_header(self):
        """Gets the accept_header of this Transaction.

            

        :return: The accept_header of this Transaction.
        :rtype: str
        """
        return self._accept_header

    @accept_header.setter
    def accept_header(self, accept_header):
        """Sets the accept_header of this Transaction.

            

        :param accept_header: The accept_header of this Transaction.
        :type: str
        """

        self._accept_header = accept_header
    
    @property
    def accept_language_header(self):
        """Gets the accept_language_header of this Transaction.

            The accept language contains the header which indicates the language preferences of the buyer.

        :return: The accept_language_header of this Transaction.
        :rtype: str
        """
        return self._accept_language_header

    @accept_language_header.setter
    def accept_language_header(self, accept_language_header):
        """Sets the accept_language_header of this Transaction.

            The accept language contains the header which indicates the language preferences of the buyer.

        :param accept_language_header: The accept_language_header of this Transaction.
        :type: str
        """

        self._accept_language_header = accept_language_header
    
    @property
    def allowed_payment_method_brands(self):
        """Gets the allowed_payment_method_brands of this Transaction.

            

        :return: The allowed_payment_method_brands of this Transaction.
        :rtype: list[PaymentMethodBrand]
        """
        return self._allowed_payment_method_brands

    @allowed_payment_method_brands.setter
    def allowed_payment_method_brands(self, allowed_payment_method_brands):
        """Sets the allowed_payment_method_brands of this Transaction.

            

        :param allowed_payment_method_brands: The allowed_payment_method_brands of this Transaction.
        :type: list[PaymentMethodBrand]
        """

        self._allowed_payment_method_brands = allowed_payment_method_brands
    
    @property
    def allowed_payment_method_configurations(self):
        """Gets the allowed_payment_method_configurations of this Transaction.

            

        :return: The allowed_payment_method_configurations of this Transaction.
        :rtype: list[int]
        """
        return self._allowed_payment_method_configurations

    @allowed_payment_method_configurations.setter
    def allowed_payment_method_configurations(self, allowed_payment_method_configurations):
        """Sets the allowed_payment_method_configurations of this Transaction.

            

        :param allowed_payment_method_configurations: The allowed_payment_method_configurations of this Transaction.
        :type: list[int]
        """

        self._allowed_payment_method_configurations = allowed_payment_method_configurations
    
    @property
    def authorization_amount(self):
        """Gets the authorization_amount of this Transaction.

            

        :return: The authorization_amount of this Transaction.
        :rtype: float
        """
        return self._authorization_amount

    @authorization_amount.setter
    def authorization_amount(self, authorization_amount):
        """Sets the authorization_amount of this Transaction.

            

        :param authorization_amount: The authorization_amount of this Transaction.
        :type: float
        """

        self._authorization_amount = authorization_amount
    
    @property
    def authorization_environment(self):
        """Gets the authorization_environment of this Transaction.

            The environment in which this transaction was successfully authorized.

        :return: The authorization_environment of this Transaction.
        :rtype: ChargeAttemptEnvironment
        """
        return self._authorization_environment

    @authorization_environment.setter
    def authorization_environment(self, authorization_environment):
        """Sets the authorization_environment of this Transaction.

            The environment in which this transaction was successfully authorized.

        :param authorization_environment: The authorization_environment of this Transaction.
        :type: ChargeAttemptEnvironment
        """

        self._authorization_environment = authorization_environment
    
    @property
    def authorization_sales_channel(self):
        """Gets the authorization_sales_channel of this Transaction.

            The sales channel through which the transaction was placed.

        :return: The authorization_sales_channel of this Transaction.
        :rtype: int
        """
        return self._authorization_sales_channel

    @authorization_sales_channel.setter
    def authorization_sales_channel(self, authorization_sales_channel):
        """Sets the authorization_sales_channel of this Transaction.

            The sales channel through which the transaction was placed.

        :param authorization_sales_channel: The authorization_sales_channel of this Transaction.
        :type: int
        """

        self._authorization_sales_channel = authorization_sales_channel
    
    @property
    def authorization_timeout_on(self):
        """Gets the authorization_timeout_on of this Transaction.

            This is the time on which the transaction will be timed out when it is not at least authorized. The timeout time may change over time.

        :return: The authorization_timeout_on of this Transaction.
        :rtype: datetime
        """
        return self._authorization_timeout_on

    @authorization_timeout_on.setter
    def authorization_timeout_on(self, authorization_timeout_on):
        """Sets the authorization_timeout_on of this Transaction.

            This is the time on which the transaction will be timed out when it is not at least authorized. The timeout time may change over time.

        :param authorization_timeout_on: The authorization_timeout_on of this Transaction.
        :type: datetime
        """

        self._authorization_timeout_on = authorization_timeout_on
    
    @property
    def authorized_on(self):
        """Gets the authorized_on of this Transaction.

            

        :return: The authorized_on of this Transaction.
        :rtype: datetime
        """
        return self._authorized_on

    @authorized_on.setter
    def authorized_on(self, authorized_on):
        """Sets the authorized_on of this Transaction.

            

        :param authorized_on: The authorized_on of this Transaction.
        :type: datetime
        """

        self._authorized_on = authorized_on
    
    @property
    def auto_confirmation_enabled(self):
        """Gets the auto_confirmation_enabled of this Transaction.

            When auto confirmation is enabled the transaction can be confirmed by the user and does not require an explicit confirmation through the web service API.

        :return: The auto_confirmation_enabled of this Transaction.
        :rtype: bool
        """
        return self._auto_confirmation_enabled

    @auto_confirmation_enabled.setter
    def auto_confirmation_enabled(self, auto_confirmation_enabled):
        """Sets the auto_confirmation_enabled of this Transaction.

            When auto confirmation is enabled the transaction can be confirmed by the user and does not require an explicit confirmation through the web service API.

        :param auto_confirmation_enabled: The auto_confirmation_enabled of this Transaction.
        :type: bool
        """

        self._auto_confirmation_enabled = auto_confirmation_enabled
    
    @property
    def billing_address(self):
        """Gets the billing_address of this Transaction.

            

        :return: The billing_address of this Transaction.
        :rtype: Address
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this Transaction.

            

        :param billing_address: The billing_address of this Transaction.
        :type: Address
        """

        self._billing_address = billing_address
    
    @property
    def charge_retry_enabled(self):
        """Gets the charge_retry_enabled of this Transaction.

            When the charging of the customer fails we can retry the charging. This implies that we redirect the user back to the payment page which allows the customer to retry. By default we will retry.

        :return: The charge_retry_enabled of this Transaction.
        :rtype: bool
        """
        return self._charge_retry_enabled

    @charge_retry_enabled.setter
    def charge_retry_enabled(self, charge_retry_enabled):
        """Sets the charge_retry_enabled of this Transaction.

            When the charging of the customer fails we can retry the charging. This implies that we redirect the user back to the payment page which allows the customer to retry. By default we will retry.

        :param charge_retry_enabled: The charge_retry_enabled of this Transaction.
        :type: bool
        """

        self._charge_retry_enabled = charge_retry_enabled
    
    @property
    def completed_amount(self):
        """Gets the completed_amount of this Transaction.

            The completed amount is the total amount which has been captured so far.

        :return: The completed_amount of this Transaction.
        :rtype: float
        """
        return self._completed_amount

    @completed_amount.setter
    def completed_amount(self, completed_amount):
        """Sets the completed_amount of this Transaction.

            The completed amount is the total amount which has been captured so far.

        :param completed_amount: The completed_amount of this Transaction.
        :type: float
        """

        self._completed_amount = completed_amount
    
    @property
    def completed_on(self):
        """Gets the completed_on of this Transaction.

            

        :return: The completed_on of this Transaction.
        :rtype: datetime
        """
        return self._completed_on

    @completed_on.setter
    def completed_on(self, completed_on):
        """Sets the completed_on of this Transaction.

            

        :param completed_on: The completed_on of this Transaction.
        :type: datetime
        """

        self._completed_on = completed_on
    
    @property
    def completion_behavior(self):
        """Gets the completion_behavior of this Transaction.

            The completion behavior controls when the transaction is completed.

        :return: The completion_behavior of this Transaction.
        :rtype: TransactionCompletionBehavior
        """
        return self._completion_behavior

    @completion_behavior.setter
    def completion_behavior(self, completion_behavior):
        """Sets the completion_behavior of this Transaction.

            The completion behavior controls when the transaction is completed.

        :param completion_behavior: The completion_behavior of this Transaction.
        :type: TransactionCompletionBehavior
        """

        self._completion_behavior = completion_behavior
    
    @property
    def completion_timeout_on(self):
        """Gets the completion_timeout_on of this Transaction.

            

        :return: The completion_timeout_on of this Transaction.
        :rtype: datetime
        """
        return self._completion_timeout_on

    @completion_timeout_on.setter
    def completion_timeout_on(self, completion_timeout_on):
        """Sets the completion_timeout_on of this Transaction.

            

        :param completion_timeout_on: The completion_timeout_on of this Transaction.
        :type: datetime
        """

        self._completion_timeout_on = completion_timeout_on
    
    @property
    def confirmed_by(self):
        """Gets the confirmed_by of this Transaction.

            

        :return: The confirmed_by of this Transaction.
        :rtype: int
        """
        return self._confirmed_by

    @confirmed_by.setter
    def confirmed_by(self, confirmed_by):
        """Sets the confirmed_by of this Transaction.

            

        :param confirmed_by: The confirmed_by of this Transaction.
        :type: int
        """

        self._confirmed_by = confirmed_by
    
    @property
    def confirmed_on(self):
        """Gets the confirmed_on of this Transaction.

            

        :return: The confirmed_on of this Transaction.
        :rtype: datetime
        """
        return self._confirmed_on

    @confirmed_on.setter
    def confirmed_on(self, confirmed_on):
        """Sets the confirmed_on of this Transaction.

            

        :param confirmed_on: The confirmed_on of this Transaction.
        :type: datetime
        """

        self._confirmed_on = confirmed_on
    
    @property
    def created_by(self):
        """Gets the created_by of this Transaction.

            

        :return: The created_by of this Transaction.
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Transaction.

            

        :param created_by: The created_by of this Transaction.
        :type: int
        """

        self._created_by = created_by
    
    @property
    def created_on(self):
        """Gets the created_on of this Transaction.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this Transaction.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Transaction.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this Transaction.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def currency(self):
        """Gets the currency of this Transaction.

            

        :return: The currency of this Transaction.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Transaction.

            

        :param currency: The currency of this Transaction.
        :type: str
        """

        self._currency = currency
    
    @property
    def customer_email_address(self):
        """Gets the customer_email_address of this Transaction.

            The customer email address is the email address of the customer. If no email address is provided on the shipping or billing address this address is used.

        :return: The customer_email_address of this Transaction.
        :rtype: str
        """
        return self._customer_email_address

    @customer_email_address.setter
    def customer_email_address(self, customer_email_address):
        """Sets the customer_email_address of this Transaction.

            The customer email address is the email address of the customer. If no email address is provided on the shipping or billing address this address is used.

        :param customer_email_address: The customer_email_address of this Transaction.
        :type: str
        """
        if customer_email_address is not None and len(customer_email_address) > 254:
            raise ValueError("Invalid value for `customer_email_address`, length must be less than or equal to `254`")

        self._customer_email_address = customer_email_address
    
    @property
    def customer_id(self):
        """Gets the customer_id of this Transaction.

            

        :return: The customer_id of this Transaction.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Transaction.

            

        :param customer_id: The customer_id of this Transaction.
        :type: str
        """

        self._customer_id = customer_id
    
    @property
    def customers_presence(self):
        """Gets the customers_presence of this Transaction.

            The customer's presence indicates what kind of authentication methods can be used during the authorization of the transaction. If no value is provided, 'Virtually Present' is used by default.

        :return: The customers_presence of this Transaction.
        :rtype: CustomersPresence
        """
        return self._customers_presence

    @customers_presence.setter
    def customers_presence(self, customers_presence):
        """Sets the customers_presence of this Transaction.

            The customer's presence indicates what kind of authentication methods can be used during the authorization of the transaction. If no value is provided, 'Virtually Present' is used by default.

        :param customers_presence: The customers_presence of this Transaction.
        :type: CustomersPresence
        """

        self._customers_presence = customers_presence
    
    @property
    def delivery_decision_made_on(self):
        """Gets the delivery_decision_made_on of this Transaction.

            This date indicates when the decision has been made if a transaction should be delivered or not.

        :return: The delivery_decision_made_on of this Transaction.
        :rtype: datetime
        """
        return self._delivery_decision_made_on

    @delivery_decision_made_on.setter
    def delivery_decision_made_on(self, delivery_decision_made_on):
        """Sets the delivery_decision_made_on of this Transaction.

            This date indicates when the decision has been made if a transaction should be delivered or not.

        :param delivery_decision_made_on: The delivery_decision_made_on of this Transaction.
        :type: datetime
        """

        self._delivery_decision_made_on = delivery_decision_made_on
    
    @property
    def device_session_identifier(self):
        """Gets the device_session_identifier of this Transaction.

            The device session identifier links the transaction with the session identifier provided in the URL of the device data JavaScript. This allows to link the transaction with the collected device data of the buyer.

        :return: The device_session_identifier of this Transaction.
        :rtype: str
        """
        return self._device_session_identifier

    @device_session_identifier.setter
    def device_session_identifier(self, device_session_identifier):
        """Sets the device_session_identifier of this Transaction.

            The device session identifier links the transaction with the session identifier provided in the URL of the device data JavaScript. This allows to link the transaction with the collected device data of the buyer.

        :param device_session_identifier: The device_session_identifier of this Transaction.
        :type: str
        """
        if device_session_identifier is not None and len(device_session_identifier) > 40:
            raise ValueError("Invalid value for `device_session_identifier`, length must be less than or equal to `40`")
        if device_session_identifier is not None and len(device_session_identifier) < 10:
            raise ValueError("Invalid value for `device_session_identifier`, length must be greater than or equal to `10`")

        self._device_session_identifier = device_session_identifier
    
    @property
    def emails_disabled(self):
        """Gets the emails_disabled of this Transaction.

            Flag indicating whether email sending is disabled for this particular transaction. Defaults to false.

        :return: The emails_disabled of this Transaction.
        :rtype: bool
        """
        return self._emails_disabled

    @emails_disabled.setter
    def emails_disabled(self, emails_disabled):
        """Sets the emails_disabled of this Transaction.

            Flag indicating whether email sending is disabled for this particular transaction. Defaults to false.

        :param emails_disabled: The emails_disabled of this Transaction.
        :type: bool
        """

        self._emails_disabled = emails_disabled
    
    @property
    def end_of_life(self):
        """Gets the end_of_life of this Transaction.

            The transaction's end of life indicates the date from which on no operation can be carried out anymore.

        :return: The end_of_life of this Transaction.
        :rtype: datetime
        """
        return self._end_of_life

    @end_of_life.setter
    def end_of_life(self, end_of_life):
        """Sets the end_of_life of this Transaction.

            The transaction's end of life indicates the date from which on no operation can be carried out anymore.

        :param end_of_life: The end_of_life of this Transaction.
        :type: datetime
        """

        self._end_of_life = end_of_life
    
    @property
    def environment(self):
        """Gets the environment of this Transaction.

            

        :return: The environment of this Transaction.
        :rtype: Environment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this Transaction.

            

        :param environment: The environment of this Transaction.
        :type: Environment
        """

        self._environment = environment
    
    @property
    def environment_selection_strategy(self):
        """Gets the environment_selection_strategy of this Transaction.

            The environment selection strategy determines how the environment (test or production) for processing the transaction is selected.

        :return: The environment_selection_strategy of this Transaction.
        :rtype: TransactionEnvironmentSelectionStrategy
        """
        return self._environment_selection_strategy

    @environment_selection_strategy.setter
    def environment_selection_strategy(self, environment_selection_strategy):
        """Sets the environment_selection_strategy of this Transaction.

            The environment selection strategy determines how the environment (test or production) for processing the transaction is selected.

        :param environment_selection_strategy: The environment_selection_strategy of this Transaction.
        :type: TransactionEnvironmentSelectionStrategy
        """

        self._environment_selection_strategy = environment_selection_strategy
    
    @property
    def failed_on(self):
        """Gets the failed_on of this Transaction.

            

        :return: The failed_on of this Transaction.
        :rtype: datetime
        """
        return self._failed_on

    @failed_on.setter
    def failed_on(self, failed_on):
        """Sets the failed_on of this Transaction.

            

        :param failed_on: The failed_on of this Transaction.
        :type: datetime
        """

        self._failed_on = failed_on
    
    @property
    def failed_url(self):
        """Gets the failed_url of this Transaction.

            The user will be redirected to failed URL when the transaction could not be authorized or completed. In case no failed URL is specified a default failed page will be displayed.

        :return: The failed_url of this Transaction.
        :rtype: str
        """
        return self._failed_url

    @failed_url.setter
    def failed_url(self, failed_url):
        """Sets the failed_url of this Transaction.

            The user will be redirected to failed URL when the transaction could not be authorized or completed. In case no failed URL is specified a default failed page will be displayed.

        :param failed_url: The failed_url of this Transaction.
        :type: str
        """
        if failed_url is not None and len(failed_url) > 2000:
            raise ValueError("Invalid value for `failed_url`, length must be less than or equal to `2000`")
        if failed_url is not None and len(failed_url) < 9:
            raise ValueError("Invalid value for `failed_url`, length must be greater than or equal to `9`")

        self._failed_url = failed_url
    
    @property
    def failure_reason(self):
        """Gets the failure_reason of this Transaction.

            The failure reason describes why the transaction failed. This is only provided when the transaction is marked as failed.

        :return: The failure_reason of this Transaction.
        :rtype: FailureReason
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this Transaction.

            The failure reason describes why the transaction failed. This is only provided when the transaction is marked as failed.

        :param failure_reason: The failure_reason of this Transaction.
        :type: FailureReason
        """

        self._failure_reason = failure_reason
    
    @property
    def group(self):
        """Gets the group of this Transaction.

            

        :return: The group of this Transaction.
        :rtype: TransactionGroup
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this Transaction.

            

        :param group: The group of this Transaction.
        :type: TransactionGroup
        """

        self._group = group
    
    @property
    def id(self):
        """Gets the id of this Transaction.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this Transaction.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Transaction.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this Transaction.
        :type: int
        """

        self._id = id
    
    @property
    def internet_protocol_address(self):
        """Gets the internet_protocol_address of this Transaction.

            The Internet Protocol (IP) address identifies the device of the buyer.

        :return: The internet_protocol_address of this Transaction.
        :rtype: str
        """
        return self._internet_protocol_address

    @internet_protocol_address.setter
    def internet_protocol_address(self, internet_protocol_address):
        """Sets the internet_protocol_address of this Transaction.

            The Internet Protocol (IP) address identifies the device of the buyer.

        :param internet_protocol_address: The internet_protocol_address of this Transaction.
        :type: str
        """

        self._internet_protocol_address = internet_protocol_address
    
    @property
    def internet_protocol_address_country(self):
        """Gets the internet_protocol_address_country of this Transaction.

            

        :return: The internet_protocol_address_country of this Transaction.
        :rtype: str
        """
        return self._internet_protocol_address_country

    @internet_protocol_address_country.setter
    def internet_protocol_address_country(self, internet_protocol_address_country):
        """Sets the internet_protocol_address_country of this Transaction.

            

        :param internet_protocol_address_country: The internet_protocol_address_country of this Transaction.
        :type: str
        """

        self._internet_protocol_address_country = internet_protocol_address_country
    
    @property
    def invoice_merchant_reference(self):
        """Gets the invoice_merchant_reference of this Transaction.

            

        :return: The invoice_merchant_reference of this Transaction.
        :rtype: str
        """
        return self._invoice_merchant_reference

    @invoice_merchant_reference.setter
    def invoice_merchant_reference(self, invoice_merchant_reference):
        """Sets the invoice_merchant_reference of this Transaction.

            

        :param invoice_merchant_reference: The invoice_merchant_reference of this Transaction.
        :type: str
        """
        if invoice_merchant_reference is not None and len(invoice_merchant_reference) > 100:
            raise ValueError("Invalid value for `invoice_merchant_reference`, length must be less than or equal to `100`")

        self._invoice_merchant_reference = invoice_merchant_reference
    
    @property
    def java_enabled(self):
        """Gets the java_enabled of this Transaction.

            

        :return: The java_enabled of this Transaction.
        :rtype: bool
        """
        return self._java_enabled

    @java_enabled.setter
    def java_enabled(self, java_enabled):
        """Sets the java_enabled of this Transaction.

            

        :param java_enabled: The java_enabled of this Transaction.
        :type: bool
        """

        self._java_enabled = java_enabled
    
    @property
    def language(self):
        """Gets the language of this Transaction.

            

        :return: The language of this Transaction.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Transaction.

            

        :param language: The language of this Transaction.
        :type: str
        """

        self._language = language
    
    @property
    def line_items(self):
        """Gets the line_items of this Transaction.

            

        :return: The line_items of this Transaction.
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this Transaction.

            

        :param line_items: The line_items of this Transaction.
        :type: list[LineItem]
        """

        self._line_items = line_items
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this Transaction.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this Transaction.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this Transaction.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this Transaction.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def merchant_reference(self):
        """Gets the merchant_reference of this Transaction.

            

        :return: The merchant_reference of this Transaction.
        :rtype: str
        """
        return self._merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, merchant_reference):
        """Sets the merchant_reference of this Transaction.

            

        :param merchant_reference: The merchant_reference of this Transaction.
        :type: str
        """
        if merchant_reference is not None and len(merchant_reference) > 100:
            raise ValueError("Invalid value for `merchant_reference`, length must be less than or equal to `100`")

        self._merchant_reference = merchant_reference
    
    @property
    def meta_data(self):
        """Gets the meta_data of this Transaction.

            Meta data allow to store additional data along the object.

        :return: The meta_data of this Transaction.
        :rtype: dict(str, str)
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this Transaction.

            Meta data allow to store additional data along the object.

        :param meta_data: The meta_data of this Transaction.
        :type: dict(str, str)
        """

        self._meta_data = meta_data
    
    @property
    def parent(self):
        """Gets the parent of this Transaction.

            

        :return: The parent of this Transaction.
        :rtype: int
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this Transaction.

            

        :param parent: The parent of this Transaction.
        :type: int
        """

        self._parent = parent
    
    @property
    def payment_connector_configuration(self):
        """Gets the payment_connector_configuration of this Transaction.

            

        :return: The payment_connector_configuration of this Transaction.
        :rtype: PaymentConnectorConfiguration
        """
        return self._payment_connector_configuration

    @payment_connector_configuration.setter
    def payment_connector_configuration(self, payment_connector_configuration):
        """Sets the payment_connector_configuration of this Transaction.

            

        :param payment_connector_configuration: The payment_connector_configuration of this Transaction.
        :type: PaymentConnectorConfiguration
        """

        self._payment_connector_configuration = payment_connector_configuration
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this Transaction.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this Transaction.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this Transaction.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this Transaction.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def processing_on(self):
        """Gets the processing_on of this Transaction.

            

        :return: The processing_on of this Transaction.
        :rtype: datetime
        """
        return self._processing_on

    @processing_on.setter
    def processing_on(self, processing_on):
        """Sets the processing_on of this Transaction.

            

        :param processing_on: The processing_on of this Transaction.
        :type: datetime
        """

        self._processing_on = processing_on
    
    @property
    def refunded_amount(self):
        """Gets the refunded_amount of this Transaction.

            The refunded amount is the total amount which has been refunded so far.

        :return: The refunded_amount of this Transaction.
        :rtype: float
        """
        return self._refunded_amount

    @refunded_amount.setter
    def refunded_amount(self, refunded_amount):
        """Sets the refunded_amount of this Transaction.

            The refunded amount is the total amount which has been refunded so far.

        :param refunded_amount: The refunded_amount of this Transaction.
        :type: float
        """

        self._refunded_amount = refunded_amount
    
    @property
    def screen_color_depth(self):
        """Gets the screen_color_depth of this Transaction.

            

        :return: The screen_color_depth of this Transaction.
        :rtype: str
        """
        return self._screen_color_depth

    @screen_color_depth.setter
    def screen_color_depth(self, screen_color_depth):
        """Sets the screen_color_depth of this Transaction.

            

        :param screen_color_depth: The screen_color_depth of this Transaction.
        :type: str
        """

        self._screen_color_depth = screen_color_depth
    
    @property
    def screen_height(self):
        """Gets the screen_height of this Transaction.

            

        :return: The screen_height of this Transaction.
        :rtype: str
        """
        return self._screen_height

    @screen_height.setter
    def screen_height(self, screen_height):
        """Sets the screen_height of this Transaction.

            

        :param screen_height: The screen_height of this Transaction.
        :type: str
        """

        self._screen_height = screen_height
    
    @property
    def screen_width(self):
        """Gets the screen_width of this Transaction.

            

        :return: The screen_width of this Transaction.
        :rtype: str
        """
        return self._screen_width

    @screen_width.setter
    def screen_width(self, screen_width):
        """Sets the screen_width of this Transaction.

            

        :param screen_width: The screen_width of this Transaction.
        :type: str
        """

        self._screen_width = screen_width
    
    @property
    def shipping_address(self):
        """Gets the shipping_address of this Transaction.

            

        :return: The shipping_address of this Transaction.
        :rtype: Address
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this Transaction.

            

        :param shipping_address: The shipping_address of this Transaction.
        :type: Address
        """

        self._shipping_address = shipping_address
    
    @property
    def shipping_method(self):
        """Gets the shipping_method of this Transaction.

            

        :return: The shipping_method of this Transaction.
        :rtype: str
        """
        return self._shipping_method

    @shipping_method.setter
    def shipping_method(self, shipping_method):
        """Sets the shipping_method of this Transaction.

            

        :param shipping_method: The shipping_method of this Transaction.
        :type: str
        """
        if shipping_method is not None and len(shipping_method) > 200:
            raise ValueError("Invalid value for `shipping_method`, length must be less than or equal to `200`")

        self._shipping_method = shipping_method
    
    @property
    def space_view_id(self):
        """Gets the space_view_id of this Transaction.

            

        :return: The space_view_id of this Transaction.
        :rtype: int
        """
        return self._space_view_id

    @space_view_id.setter
    def space_view_id(self, space_view_id):
        """Sets the space_view_id of this Transaction.

            

        :param space_view_id: The space_view_id of this Transaction.
        :type: int
        """

        self._space_view_id = space_view_id
    
    @property
    def state(self):
        """Gets the state of this Transaction.

            

        :return: The state of this Transaction.
        :rtype: TransactionState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Transaction.

            

        :param state: The state of this Transaction.
        :type: TransactionState
        """

        self._state = state
    
    @property
    def success_url(self):
        """Gets the success_url of this Transaction.

            The user will be redirected to success URL when the transaction could be authorized or completed. In case no success URL is specified a default success page will be displayed.

        :return: The success_url of this Transaction.
        :rtype: str
        """
        return self._success_url

    @success_url.setter
    def success_url(self, success_url):
        """Sets the success_url of this Transaction.

            The user will be redirected to success URL when the transaction could be authorized or completed. In case no success URL is specified a default success page will be displayed.

        :param success_url: The success_url of this Transaction.
        :type: str
        """
        if success_url is not None and len(success_url) > 2000:
            raise ValueError("Invalid value for `success_url`, length must be less than or equal to `2000`")
        if success_url is not None and len(success_url) < 9:
            raise ValueError("Invalid value for `success_url`, length must be greater than or equal to `9`")

        self._success_url = success_url
    
    @property
    def terminal(self):
        """Gets the terminal of this Transaction.

            The terminal on which the payment was processed.

        :return: The terminal of this Transaction.
        :rtype: PaymentTerminal
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this Transaction.

            The terminal on which the payment was processed.

        :param terminal: The terminal of this Transaction.
        :type: PaymentTerminal
        """

        self._terminal = terminal
    
    @property
    def time_zone(self):
        """Gets the time_zone of this Transaction.

            The time zone defines in which time zone the customer is located in. The time zone may affects how dates are formatted when interacting with the customer.

        :return: The time_zone of this Transaction.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this Transaction.

            The time zone defines in which time zone the customer is located in. The time zone may affects how dates are formatted when interacting with the customer.

        :param time_zone: The time_zone of this Transaction.
        :type: str
        """

        self._time_zone = time_zone
    
    @property
    def token(self):
        """Gets the token of this Transaction.

            

        :return: The token of this Transaction.
        :rtype: Token
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this Transaction.

            

        :param token: The token of this Transaction.
        :type: Token
        """

        self._token = token
    
    @property
    def tokenization_mode(self):
        """Gets the tokenization_mode of this Transaction.

            The tokenization mode controls if and how the tokenization of payment information is applied to the transaction.

        :return: The tokenization_mode of this Transaction.
        :rtype: TokenizationMode
        """
        return self._tokenization_mode

    @tokenization_mode.setter
    def tokenization_mode(self, tokenization_mode):
        """Sets the tokenization_mode of this Transaction.

            The tokenization mode controls if and how the tokenization of payment information is applied to the transaction.

        :param tokenization_mode: The tokenization_mode of this Transaction.
        :type: TokenizationMode
        """

        self._tokenization_mode = tokenization_mode
    
    @property
    def total_applied_fees(self):
        """Gets the total_applied_fees of this Transaction.

            The total applied fees is the sum of all fees that have been applied so far.

        :return: The total_applied_fees of this Transaction.
        :rtype: float
        """
        return self._total_applied_fees

    @total_applied_fees.setter
    def total_applied_fees(self, total_applied_fees):
        """Sets the total_applied_fees of this Transaction.

            The total applied fees is the sum of all fees that have been applied so far.

        :param total_applied_fees: The total_applied_fees of this Transaction.
        :type: float
        """

        self._total_applied_fees = total_applied_fees
    
    @property
    def total_settled_amount(self):
        """Gets the total_settled_amount of this Transaction.

            The total settled amount is the total amount which has been settled so far.

        :return: The total_settled_amount of this Transaction.
        :rtype: float
        """
        return self._total_settled_amount

    @total_settled_amount.setter
    def total_settled_amount(self, total_settled_amount):
        """Sets the total_settled_amount of this Transaction.

            The total settled amount is the total amount which has been settled so far.

        :param total_settled_amount: The total_settled_amount of this Transaction.
        :type: float
        """

        self._total_settled_amount = total_settled_amount
    
    @property
    def user_agent_header(self):
        """Gets the user_agent_header of this Transaction.

            The user agent header provides the exact string which contains the user agent of the buyer.

        :return: The user_agent_header of this Transaction.
        :rtype: str
        """
        return self._user_agent_header

    @user_agent_header.setter
    def user_agent_header(self, user_agent_header):
        """Sets the user_agent_header of this Transaction.

            The user agent header provides the exact string which contains the user agent of the buyer.

        :param user_agent_header: The user_agent_header of this Transaction.
        :type: str
        """

        self._user_agent_header = user_agent_header
    
    @property
    def user_failure_message(self):
        """Gets the user_failure_message of this Transaction.

            The failure message describes for an end user why the transaction is failed in the language of the user. This is only provided when the transaction is marked as failed.

        :return: The user_failure_message of this Transaction.
        :rtype: str
        """
        return self._user_failure_message

    @user_failure_message.setter
    def user_failure_message(self, user_failure_message):
        """Sets the user_failure_message of this Transaction.

            The failure message describes for an end user why the transaction is failed in the language of the user. This is only provided when the transaction is marked as failed.

        :param user_failure_message: The user_failure_message of this Transaction.
        :type: str
        """

        self._user_failure_message = user_failure_message
    
    @property
    def user_interface_type(self):
        """Gets the user_interface_type of this Transaction.

            The user interface type defines through which user interface the transaction has been processed resp. created.

        :return: The user_interface_type of this Transaction.
        :rtype: TransactionUserInterfaceType
        """
        return self._user_interface_type

    @user_interface_type.setter
    def user_interface_type(self, user_interface_type):
        """Sets the user_interface_type of this Transaction.

            The user interface type defines through which user interface the transaction has been processed resp. created.

        :param user_interface_type: The user_interface_type of this Transaction.
        :type: TransactionUserInterfaceType
        """

        self._user_interface_type = user_interface_type
    
    @property
    def version(self):
        """Gets the version of this Transaction.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this Transaction.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Transaction.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this Transaction.
        :type: int
        """

        self._version = version
    
    @property
    def window_height(self):
        """Gets the window_height of this Transaction.

            

        :return: The window_height of this Transaction.
        :rtype: str
        """
        return self._window_height

    @window_height.setter
    def window_height(self, window_height):
        """Sets the window_height of this Transaction.

            

        :param window_height: The window_height of this Transaction.
        :type: str
        """

        self._window_height = window_height
    
    @property
    def window_width(self):
        """Gets the window_width of this Transaction.

            

        :return: The window_width of this Transaction.
        :rtype: str
        """
        return self._window_width

    @window_width.setter
    def window_width(self, window_width):
        """Sets the window_width of this Transaction.

            

        :param window_width: The window_width of this Transaction.
        :type: str
        """

        self._window_width = window_width
    

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
        if issubclass(Transaction, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Transaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
