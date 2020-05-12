# coding: utf-8
import pprint
import six
from enum import Enum



class ShopifyIntegration:

    swagger_types = {
    
        'allow_invoice_download': 'bool',
        'allowed_payment_method_configurations': 'list[PaymentMethodConfiguration]',
        'app_version': 'ShopifyIntegrationAppVersion',
        'currency': 'str',
        'id': 'int',
        'installed': 'bool',
        'integrated_payment_form_enabled': 'bool',
        'language': 'str',
        'login_name': 'str',
        'name': 'str',
        'planned_purge_date': 'datetime',
        'proxy_path': 'str',
        'replace_payment_method_image': 'bool',
        'shop_name': 'str',
        'show_payment_information': 'bool',
        'show_subscription_information': 'bool',
        'space_id': 'int',
        'space_view_id': 'int',
        'state': 'CreationEntityState',
        'version': 'int',
    }

    attribute_map = {
        'allow_invoice_download': 'allowInvoiceDownload','allowed_payment_method_configurations': 'allowedPaymentMethodConfigurations','app_version': 'appVersion','currency': 'currency','id': 'id','installed': 'installed','integrated_payment_form_enabled': 'integratedPaymentFormEnabled','language': 'language','login_name': 'loginName','name': 'name','planned_purge_date': 'plannedPurgeDate','proxy_path': 'proxyPath','replace_payment_method_image': 'replacePaymentMethodImage','shop_name': 'shopName','show_payment_information': 'showPaymentInformation','show_subscription_information': 'showSubscriptionInformation','space_id': 'spaceId','space_view_id': 'spaceViewId','state': 'state','version': 'version',
    }

    
    _allow_invoice_download = None
    _allowed_payment_method_configurations = None
    _app_version = None
    _currency = None
    _id = None
    _installed = None
    _integrated_payment_form_enabled = None
    _language = None
    _login_name = None
    _name = None
    _planned_purge_date = None
    _proxy_path = None
    _replace_payment_method_image = None
    _shop_name = None
    _show_payment_information = None
    _show_subscription_information = None
    _space_id = None
    _space_view_id = None
    _state = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.allow_invoice_download = kwargs.get('allow_invoice_download', None)
        self.allowed_payment_method_configurations = kwargs.get('allowed_payment_method_configurations', None)
        self.app_version = kwargs.get('app_version', None)
        self.currency = kwargs.get('currency', None)
        self.id = kwargs.get('id', None)
        self.installed = kwargs.get('installed', None)
        self.integrated_payment_form_enabled = kwargs.get('integrated_payment_form_enabled', None)
        self.language = kwargs.get('language', None)
        self.login_name = kwargs.get('login_name', None)
        self.name = kwargs.get('name', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.proxy_path = kwargs.get('proxy_path', None)
        self.replace_payment_method_image = kwargs.get('replace_payment_method_image', None)
        self.shop_name = kwargs.get('shop_name', None)
        self.show_payment_information = kwargs.get('show_payment_information', None)
        self.show_subscription_information = kwargs.get('show_subscription_information', None)
        self.space_id = kwargs.get('space_id', None)
        self.space_view_id = kwargs.get('space_view_id', None)
        self.state = kwargs.get('state', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def allow_invoice_download(self):
        """Gets the allow_invoice_download of this ShopifyIntegration.

            

        :return: The allow_invoice_download of this ShopifyIntegration.
        :rtype: bool
        """
        return self._allow_invoice_download

    @allow_invoice_download.setter
    def allow_invoice_download(self, allow_invoice_download):
        """Sets the allow_invoice_download of this ShopifyIntegration.

            

        :param allow_invoice_download: The allow_invoice_download of this ShopifyIntegration.
        :type: bool
        """

        self._allow_invoice_download = allow_invoice_download
    
    @property
    def allowed_payment_method_configurations(self):
        """Gets the allowed_payment_method_configurations of this ShopifyIntegration.

            

        :return: The allowed_payment_method_configurations of this ShopifyIntegration.
        :rtype: list[PaymentMethodConfiguration]
        """
        return self._allowed_payment_method_configurations

    @allowed_payment_method_configurations.setter
    def allowed_payment_method_configurations(self, allowed_payment_method_configurations):
        """Sets the allowed_payment_method_configurations of this ShopifyIntegration.

            

        :param allowed_payment_method_configurations: The allowed_payment_method_configurations of this ShopifyIntegration.
        :type: list[PaymentMethodConfiguration]
        """

        self._allowed_payment_method_configurations = allowed_payment_method_configurations
    
    @property
    def app_version(self):
        """Gets the app_version of this ShopifyIntegration.

            

        :return: The app_version of this ShopifyIntegration.
        :rtype: ShopifyIntegrationAppVersion
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this ShopifyIntegration.

            

        :param app_version: The app_version of this ShopifyIntegration.
        :type: ShopifyIntegrationAppVersion
        """

        self._app_version = app_version
    
    @property
    def currency(self):
        """Gets the currency of this ShopifyIntegration.

            

        :return: The currency of this ShopifyIntegration.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ShopifyIntegration.

            

        :param currency: The currency of this ShopifyIntegration.
        :type: str
        """

        self._currency = currency
    
    @property
    def id(self):
        """Gets the id of this ShopifyIntegration.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this ShopifyIntegration.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShopifyIntegration.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this ShopifyIntegration.
        :type: int
        """

        self._id = id
    
    @property
    def installed(self):
        """Gets the installed of this ShopifyIntegration.

            

        :return: The installed of this ShopifyIntegration.
        :rtype: bool
        """
        return self._installed

    @installed.setter
    def installed(self, installed):
        """Sets the installed of this ShopifyIntegration.

            

        :param installed: The installed of this ShopifyIntegration.
        :type: bool
        """

        self._installed = installed
    
    @property
    def integrated_payment_form_enabled(self):
        """Gets the integrated_payment_form_enabled of this ShopifyIntegration.

            Enabling the integrated payment form will embed the payment form in the Shopify shop. The app needs to be installed for this to be possible.

        :return: The integrated_payment_form_enabled of this ShopifyIntegration.
        :rtype: bool
        """
        return self._integrated_payment_form_enabled

    @integrated_payment_form_enabled.setter
    def integrated_payment_form_enabled(self, integrated_payment_form_enabled):
        """Sets the integrated_payment_form_enabled of this ShopifyIntegration.

            Enabling the integrated payment form will embed the payment form in the Shopify shop. The app needs to be installed for this to be possible.

        :param integrated_payment_form_enabled: The integrated_payment_form_enabled of this ShopifyIntegration.
        :type: bool
        """

        self._integrated_payment_form_enabled = integrated_payment_form_enabled
    
    @property
    def language(self):
        """Gets the language of this ShopifyIntegration.

            The checkout language forces a specific language in the checkout. Without a checkout language the browser setting of the buyer is used to determine the language.

        :return: The language of this ShopifyIntegration.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ShopifyIntegration.

            The checkout language forces a specific language in the checkout. Without a checkout language the browser setting of the buyer is used to determine the language.

        :param language: The language of this ShopifyIntegration.
        :type: str
        """

        self._language = language
    
    @property
    def login_name(self):
        """Gets the login_name of this ShopifyIntegration.

            The login name is used to link a specific Shopify payment gateway to this integration.This login name is to be filled into the appropriate field in the shops payment gateway configuration.

        :return: The login_name of this ShopifyIntegration.
        :rtype: str
        """
        return self._login_name

    @login_name.setter
    def login_name(self, login_name):
        """Sets the login_name of this ShopifyIntegration.

            The login name is used to link a specific Shopify payment gateway to this integration.This login name is to be filled into the appropriate field in the shops payment gateway configuration.

        :param login_name: The login_name of this ShopifyIntegration.
        :type: str
        """

        self._login_name = login_name
    
    @property
    def name(self):
        """Gets the name of this ShopifyIntegration.

            The integration name is used internally to identify a specific integration.For example the name is used withinsearch fields and hence it should be distinct and descriptive.

        :return: The name of this ShopifyIntegration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShopifyIntegration.

            The integration name is used internally to identify a specific integration.For example the name is used withinsearch fields and hence it should be distinct and descriptive.

        :param name: The name of this ShopifyIntegration.
        :type: str
        """

        self._name = name
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this ShopifyIntegration.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this ShopifyIntegration.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this ShopifyIntegration.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this ShopifyIntegration.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def proxy_path(self):
        """Gets the proxy_path of this ShopifyIntegration.

            Define the path of the proxy URL. This only needs to be changed if the apps proxy URL is overwritten in the Shopify store.

        :return: The proxy_path of this ShopifyIntegration.
        :rtype: str
        """
        return self._proxy_path

    @proxy_path.setter
    def proxy_path(self, proxy_path):
        """Sets the proxy_path of this ShopifyIntegration.

            Define the path of the proxy URL. This only needs to be changed if the apps proxy URL is overwritten in the Shopify store.

        :param proxy_path: The proxy_path of this ShopifyIntegration.
        :type: str
        """

        self._proxy_path = proxy_path
    
    @property
    def replace_payment_method_image(self):
        """Gets the replace_payment_method_image of this ShopifyIntegration.

            

        :return: The replace_payment_method_image of this ShopifyIntegration.
        :rtype: bool
        """
        return self._replace_payment_method_image

    @replace_payment_method_image.setter
    def replace_payment_method_image(self, replace_payment_method_image):
        """Sets the replace_payment_method_image of this ShopifyIntegration.

            

        :param replace_payment_method_image: The replace_payment_method_image of this ShopifyIntegration.
        :type: bool
        """

        self._replace_payment_method_image = replace_payment_method_image
    
    @property
    def shop_name(self):
        """Gets the shop_name of this ShopifyIntegration.

            The store address is used to link a specific Shopify shop to this integration. This is the name used in the Shopifys admin URL: [storeAddress].myshopify.com

        :return: The shop_name of this ShopifyIntegration.
        :rtype: str
        """
        return self._shop_name

    @shop_name.setter
    def shop_name(self, shop_name):
        """Sets the shop_name of this ShopifyIntegration.

            The store address is used to link a specific Shopify shop to this integration. This is the name used in the Shopifys admin URL: [storeAddress].myshopify.com

        :param shop_name: The shop_name of this ShopifyIntegration.
        :type: str
        """

        self._shop_name = shop_name
    
    @property
    def show_payment_information(self):
        """Gets the show_payment_information of this ShopifyIntegration.

            

        :return: The show_payment_information of this ShopifyIntegration.
        :rtype: bool
        """
        return self._show_payment_information

    @show_payment_information.setter
    def show_payment_information(self, show_payment_information):
        """Sets the show_payment_information of this ShopifyIntegration.

            

        :param show_payment_information: The show_payment_information of this ShopifyIntegration.
        :type: bool
        """

        self._show_payment_information = show_payment_information
    
    @property
    def show_subscription_information(self):
        """Gets the show_subscription_information of this ShopifyIntegration.

            

        :return: The show_subscription_information of this ShopifyIntegration.
        :rtype: bool
        """
        return self._show_subscription_information

    @show_subscription_information.setter
    def show_subscription_information(self, show_subscription_information):
        """Sets the show_subscription_information of this ShopifyIntegration.

            

        :param show_subscription_information: The show_subscription_information of this ShopifyIntegration.
        :type: bool
        """

        self._show_subscription_information = show_subscription_information
    
    @property
    def space_id(self):
        """Gets the space_id of this ShopifyIntegration.

            

        :return: The space_id of this ShopifyIntegration.
        :rtype: int
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this ShopifyIntegration.

            

        :param space_id: The space_id of this ShopifyIntegration.
        :type: int
        """

        self._space_id = space_id
    
    @property
    def space_view_id(self):
        """Gets the space_view_id of this ShopifyIntegration.

            

        :return: The space_view_id of this ShopifyIntegration.
        :rtype: int
        """
        return self._space_view_id

    @space_view_id.setter
    def space_view_id(self, space_view_id):
        """Sets the space_view_id of this ShopifyIntegration.

            

        :param space_view_id: The space_view_id of this ShopifyIntegration.
        :type: int
        """

        self._space_view_id = space_view_id
    
    @property
    def state(self):
        """Gets the state of this ShopifyIntegration.

            

        :return: The state of this ShopifyIntegration.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShopifyIntegration.

            

        :param state: The state of this ShopifyIntegration.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def version(self):
        """Gets the version of this ShopifyIntegration.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ShopifyIntegration.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShopifyIntegration.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ShopifyIntegration.
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
        if issubclass(ShopifyIntegration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ShopifyIntegration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
