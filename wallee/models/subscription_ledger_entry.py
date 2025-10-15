# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionLedgerEntry:

    swagger_types = {
    
        'aggregated_tax_rate': 'float',
        'amount_excluding_tax': 'float',
        'amount_including_tax': 'float',
        'component_reference_name': 'str',
        'component_reference_sku': 'str',
        'created_by': 'int',
        'created_on': 'datetime',
        'discount_including_tax': 'float',
        'external_id': 'str',
        'fee_type': 'ProductFeeType',
        'id': 'int',
        'linked_space_id': 'int',
        'planned_purge_date': 'datetime',
        'pro_rata_calculated': 'bool',
        'quantity': 'float',
        'state': 'SubscriptionLedgerEntryState',
        'subscription_metric_id': 'int',
        'subscription_version': 'int',
        'tax_amount': 'float',
        'taxes': 'list[Tax]',
        'title': 'str',
        'version': 'int',
    }

    attribute_map = {
        'aggregated_tax_rate': 'aggregatedTaxRate','amount_excluding_tax': 'amountExcludingTax','amount_including_tax': 'amountIncludingTax','component_reference_name': 'componentReferenceName','component_reference_sku': 'componentReferenceSku','created_by': 'createdBy','created_on': 'createdOn','discount_including_tax': 'discountIncludingTax','external_id': 'externalId','fee_type': 'feeType','id': 'id','linked_space_id': 'linkedSpaceId','planned_purge_date': 'plannedPurgeDate','pro_rata_calculated': 'proRataCalculated','quantity': 'quantity','state': 'state','subscription_metric_id': 'subscriptionMetricId','subscription_version': 'subscriptionVersion','tax_amount': 'taxAmount','taxes': 'taxes','title': 'title','version': 'version',
    }

    
    _aggregated_tax_rate = None
    _amount_excluding_tax = None
    _amount_including_tax = None
    _component_reference_name = None
    _component_reference_sku = None
    _created_by = None
    _created_on = None
    _discount_including_tax = None
    _external_id = None
    _fee_type = None
    _id = None
    _linked_space_id = None
    _planned_purge_date = None
    _pro_rata_calculated = None
    _quantity = None
    _state = None
    _subscription_metric_id = None
    _subscription_version = None
    _tax_amount = None
    _taxes = None
    _title = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.aggregated_tax_rate = kwargs.get('aggregated_tax_rate', None)
        self.amount_excluding_tax = kwargs.get('amount_excluding_tax', None)
        self.amount_including_tax = kwargs.get('amount_including_tax', None)
        self.component_reference_name = kwargs.get('component_reference_name', None)
        self.component_reference_sku = kwargs.get('component_reference_sku', None)
        self.created_by = kwargs.get('created_by', None)
        self.created_on = kwargs.get('created_on', None)
        self.discount_including_tax = kwargs.get('discount_including_tax', None)
        self.external_id = kwargs.get('external_id', None)
        self.fee_type = kwargs.get('fee_type', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.pro_rata_calculated = kwargs.get('pro_rata_calculated', None)
        self.quantity = kwargs.get('quantity', None)
        self.state = kwargs.get('state', None)
        self.subscription_metric_id = kwargs.get('subscription_metric_id', None)
        self.subscription_version = kwargs.get('subscription_version', None)
        self.tax_amount = kwargs.get('tax_amount', None)
        self.taxes = kwargs.get('taxes', None)
        self.title = kwargs.get('title', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def aggregated_tax_rate(self):
        """Gets the aggregated_tax_rate of this SubscriptionLedgerEntry.

            The total tax rate applied to the ledger entry, calculated from the rates of all tax lines.

        :return: The aggregated_tax_rate of this SubscriptionLedgerEntry.
        :rtype: float
        """
        return self._aggregated_tax_rate

    @aggregated_tax_rate.setter
    def aggregated_tax_rate(self, aggregated_tax_rate):
        """Sets the aggregated_tax_rate of this SubscriptionLedgerEntry.

            The total tax rate applied to the ledger entry, calculated from the rates of all tax lines.

        :param aggregated_tax_rate: The aggregated_tax_rate of this SubscriptionLedgerEntry.
        :type: float
        """

        self._aggregated_tax_rate = aggregated_tax_rate
    
    @property
    def amount_excluding_tax(self):
        """Gets the amount_excluding_tax of this SubscriptionLedgerEntry.

            The leger entry's amount with discounts applied, excluding taxes.

        :return: The amount_excluding_tax of this SubscriptionLedgerEntry.
        :rtype: float
        """
        return self._amount_excluding_tax

    @amount_excluding_tax.setter
    def amount_excluding_tax(self, amount_excluding_tax):
        """Sets the amount_excluding_tax of this SubscriptionLedgerEntry.

            The leger entry's amount with discounts applied, excluding taxes.

        :param amount_excluding_tax: The amount_excluding_tax of this SubscriptionLedgerEntry.
        :type: float
        """

        self._amount_excluding_tax = amount_excluding_tax
    
    @property
    def amount_including_tax(self):
        """Gets the amount_including_tax of this SubscriptionLedgerEntry.

            The leger entry's amount with discounts applied, including taxes.

        :return: The amount_including_tax of this SubscriptionLedgerEntry.
        :rtype: float
        """
        return self._amount_including_tax

    @amount_including_tax.setter
    def amount_including_tax(self, amount_including_tax):
        """Sets the amount_including_tax of this SubscriptionLedgerEntry.

            The leger entry's amount with discounts applied, including taxes.

        :param amount_including_tax: The amount_including_tax of this SubscriptionLedgerEntry.
        :type: float
        """

        self._amount_including_tax = amount_including_tax
    
    @property
    def component_reference_name(self):
        """Gets the component_reference_name of this SubscriptionLedgerEntry.

            

        :return: The component_reference_name of this SubscriptionLedgerEntry.
        :rtype: str
        """
        return self._component_reference_name

    @component_reference_name.setter
    def component_reference_name(self, component_reference_name):
        """Sets the component_reference_name of this SubscriptionLedgerEntry.

            

        :param component_reference_name: The component_reference_name of this SubscriptionLedgerEntry.
        :type: str
        """

        self._component_reference_name = component_reference_name
    
    @property
    def component_reference_sku(self):
        """Gets the component_reference_sku of this SubscriptionLedgerEntry.

            

        :return: The component_reference_sku of this SubscriptionLedgerEntry.
        :rtype: str
        """
        return self._component_reference_sku

    @component_reference_sku.setter
    def component_reference_sku(self, component_reference_sku):
        """Sets the component_reference_sku of this SubscriptionLedgerEntry.

            

        :param component_reference_sku: The component_reference_sku of this SubscriptionLedgerEntry.
        :type: str
        """
        if component_reference_sku is not None and len(component_reference_sku) > 100:
            raise ValueError("Invalid value for `component_reference_sku`, length must be less than or equal to `100`")

        self._component_reference_sku = component_reference_sku
    
    @property
    def created_by(self):
        """Gets the created_by of this SubscriptionLedgerEntry.

            The ID of the user the ledger entry was created by.

        :return: The created_by of this SubscriptionLedgerEntry.
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this SubscriptionLedgerEntry.

            The ID of the user the ledger entry was created by.

        :param created_by: The created_by of this SubscriptionLedgerEntry.
        :type: int
        """

        self._created_by = created_by
    
    @property
    def created_on(self):
        """Gets the created_on of this SubscriptionLedgerEntry.

            The date and time when the object was created.

        :return: The created_on of this SubscriptionLedgerEntry.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this SubscriptionLedgerEntry.

            The date and time when the object was created.

        :param created_on: The created_on of this SubscriptionLedgerEntry.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def discount_including_tax(self):
        """Gets the discount_including_tax of this SubscriptionLedgerEntry.

            The discount allocated to the ledger entry, including taxes.

        :return: The discount_including_tax of this SubscriptionLedgerEntry.
        :rtype: float
        """
        return self._discount_including_tax

    @discount_including_tax.setter
    def discount_including_tax(self, discount_including_tax):
        """Sets the discount_including_tax of this SubscriptionLedgerEntry.

            The discount allocated to the ledger entry, including taxes.

        :param discount_including_tax: The discount_including_tax of this SubscriptionLedgerEntry.
        :type: float
        """

        self._discount_including_tax = discount_including_tax
    
    @property
    def external_id(self):
        """Gets the external_id of this SubscriptionLedgerEntry.

            A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.

        :return: The external_id of this SubscriptionLedgerEntry.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this SubscriptionLedgerEntry.

            A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.

        :param external_id: The external_id of this SubscriptionLedgerEntry.
        :type: str
        """

        self._external_id = external_id
    
    @property
    def fee_type(self):
        """Gets the fee_type of this SubscriptionLedgerEntry.

            

        :return: The fee_type of this SubscriptionLedgerEntry.
        :rtype: ProductFeeType
        """
        return self._fee_type

    @fee_type.setter
    def fee_type(self, fee_type):
        """Sets the fee_type of this SubscriptionLedgerEntry.

            

        :param fee_type: The fee_type of this SubscriptionLedgerEntry.
        :type: ProductFeeType
        """

        self._fee_type = fee_type
    
    @property
    def id(self):
        """Gets the id of this SubscriptionLedgerEntry.

            A unique identifier for the object.

        :return: The id of this SubscriptionLedgerEntry.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionLedgerEntry.

            A unique identifier for the object.

        :param id: The id of this SubscriptionLedgerEntry.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this SubscriptionLedgerEntry.

            The ID of the space this object belongs to.

        :return: The linked_space_id of this SubscriptionLedgerEntry.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this SubscriptionLedgerEntry.

            The ID of the space this object belongs to.

        :param linked_space_id: The linked_space_id of this SubscriptionLedgerEntry.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this SubscriptionLedgerEntry.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :return: The planned_purge_date of this SubscriptionLedgerEntry.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this SubscriptionLedgerEntry.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :param planned_purge_date: The planned_purge_date of this SubscriptionLedgerEntry.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def pro_rata_calculated(self):
        """Gets the pro_rata_calculated of this SubscriptionLedgerEntry.

            

        :return: The pro_rata_calculated of this SubscriptionLedgerEntry.
        :rtype: bool
        """
        return self._pro_rata_calculated

    @pro_rata_calculated.setter
    def pro_rata_calculated(self, pro_rata_calculated):
        """Sets the pro_rata_calculated of this SubscriptionLedgerEntry.

            

        :param pro_rata_calculated: The pro_rata_calculated of this SubscriptionLedgerEntry.
        :type: bool
        """

        self._pro_rata_calculated = pro_rata_calculated
    
    @property
    def quantity(self):
        """Gets the quantity of this SubscriptionLedgerEntry.

            The number of items that were consumed.

        :return: The quantity of this SubscriptionLedgerEntry.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this SubscriptionLedgerEntry.

            The number of items that were consumed.

        :param quantity: The quantity of this SubscriptionLedgerEntry.
        :type: float
        """

        self._quantity = quantity
    
    @property
    def state(self):
        """Gets the state of this SubscriptionLedgerEntry.

            The object's current state.

        :return: The state of this SubscriptionLedgerEntry.
        :rtype: SubscriptionLedgerEntryState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubscriptionLedgerEntry.

            The object's current state.

        :param state: The state of this SubscriptionLedgerEntry.
        :type: SubscriptionLedgerEntryState
        """

        self._state = state
    
    @property
    def subscription_metric_id(self):
        """Gets the subscription_metric_id of this SubscriptionLedgerEntry.

            

        :return: The subscription_metric_id of this SubscriptionLedgerEntry.
        :rtype: int
        """
        return self._subscription_metric_id

    @subscription_metric_id.setter
    def subscription_metric_id(self, subscription_metric_id):
        """Sets the subscription_metric_id of this SubscriptionLedgerEntry.

            

        :param subscription_metric_id: The subscription_metric_id of this SubscriptionLedgerEntry.
        :type: int
        """

        self._subscription_metric_id = subscription_metric_id
    
    @property
    def subscription_version(self):
        """Gets the subscription_version of this SubscriptionLedgerEntry.

            The subscription version that the ledger entry belongs to.

        :return: The subscription_version of this SubscriptionLedgerEntry.
        :rtype: int
        """
        return self._subscription_version

    @subscription_version.setter
    def subscription_version(self, subscription_version):
        """Sets the subscription_version of this SubscriptionLedgerEntry.

            The subscription version that the ledger entry belongs to.

        :param subscription_version: The subscription_version of this SubscriptionLedgerEntry.
        :type: int
        """

        self._subscription_version = subscription_version
    
    @property
    def tax_amount(self):
        """Gets the tax_amount of this SubscriptionLedgerEntry.

            The sum of all taxes applied to the ledger entry.

        :return: The tax_amount of this SubscriptionLedgerEntry.
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this SubscriptionLedgerEntry.

            The sum of all taxes applied to the ledger entry.

        :param tax_amount: The tax_amount of this SubscriptionLedgerEntry.
        :type: float
        """

        self._tax_amount = tax_amount
    
    @property
    def taxes(self):
        """Gets the taxes of this SubscriptionLedgerEntry.

            A set of tax lines, each of which specifies a tax applied to the ledger entry.

        :return: The taxes of this SubscriptionLedgerEntry.
        :rtype: list[Tax]
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """Sets the taxes of this SubscriptionLedgerEntry.

            A set of tax lines, each of which specifies a tax applied to the ledger entry.

        :param taxes: The taxes of this SubscriptionLedgerEntry.
        :type: list[Tax]
        """

        self._taxes = taxes
    
    @property
    def title(self):
        """Gets the title of this SubscriptionLedgerEntry.

            The title that indicates what the ledger entry is about.

        :return: The title of this SubscriptionLedgerEntry.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SubscriptionLedgerEntry.

            The title that indicates what the ledger entry is about.

        :param title: The title of this SubscriptionLedgerEntry.
        :type: str
        """
        if title is not None and len(title) > 150:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `150`")
        if title is not None and len(title) < 1:
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")

        self._title = title
    
    @property
    def version(self):
        """Gets the version of this SubscriptionLedgerEntry.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :return: The version of this SubscriptionLedgerEntry.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SubscriptionLedgerEntry.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :param version: The version of this SubscriptionLedgerEntry.
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
        if issubclass(SubscriptionLedgerEntry, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionLedgerEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
