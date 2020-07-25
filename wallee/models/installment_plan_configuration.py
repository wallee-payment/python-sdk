# coding: utf-8
import pprint
import six
from enum import Enum



class InstallmentPlanConfiguration:

    swagger_types = {
    
        'base_currency': 'str',
        'conditions': 'list[int]',
        'id': 'int',
        'installment_fee': 'float',
        'interest_rate': 'float',
        'linked_space_id': 'int',
        'minimal_amount': 'float',
        'name': 'str',
        'payment_method_configurations': 'list[int]',
        'planned_purge_date': 'datetime',
        'sort_order': 'int',
        'space_reference': 'SpaceReference',
        'state': 'CreationEntityState',
        'tax_class': 'TaxClass',
        'terms_and_conditions': 'ResourcePath',
        'title': 'DatabaseTranslatedString',
        'version': 'int',
    }

    attribute_map = {
        'base_currency': 'baseCurrency','conditions': 'conditions','id': 'id','installment_fee': 'installmentFee','interest_rate': 'interestRate','linked_space_id': 'linkedSpaceId','minimal_amount': 'minimalAmount','name': 'name','payment_method_configurations': 'paymentMethodConfigurations','planned_purge_date': 'plannedPurgeDate','sort_order': 'sortOrder','space_reference': 'spaceReference','state': 'state','tax_class': 'taxClass','terms_and_conditions': 'termsAndConditions','title': 'title','version': 'version',
    }

    
    _base_currency = None
    _conditions = None
    _id = None
    _installment_fee = None
    _interest_rate = None
    _linked_space_id = None
    _minimal_amount = None
    _name = None
    _payment_method_configurations = None
    _planned_purge_date = None
    _sort_order = None
    _space_reference = None
    _state = None
    _tax_class = None
    _terms_and_conditions = None
    _title = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.base_currency = kwargs.get('base_currency', None)
        self.conditions = kwargs.get('conditions', None)
        self.id = kwargs.get('id', None)
        self.installment_fee = kwargs.get('installment_fee', None)
        self.interest_rate = kwargs.get('interest_rate', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.minimal_amount = kwargs.get('minimal_amount', None)
        self.name = kwargs.get('name', None)
        self.payment_method_configurations = kwargs.get('payment_method_configurations', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.sort_order = kwargs.get('sort_order', None)
        self.space_reference = kwargs.get('space_reference', None)
        self.state = kwargs.get('state', None)
        self.tax_class = kwargs.get('tax_class', None)
        self.terms_and_conditions = kwargs.get('terms_and_conditions', None)
        self.title = kwargs.get('title', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def base_currency(self):
        """Gets the base_currency of this InstallmentPlanConfiguration.

            The base currency in which the installment fee and minimal amount are defined.

        :return: The base_currency of this InstallmentPlanConfiguration.
        :rtype: str
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this InstallmentPlanConfiguration.

            The base currency in which the installment fee and minimal amount are defined.

        :param base_currency: The base_currency of this InstallmentPlanConfiguration.
        :type: str
        """

        self._base_currency = base_currency
    
    @property
    def conditions(self):
        """Gets the conditions of this InstallmentPlanConfiguration.

            If a transaction meets all selected conditions the installment plan will be available to the customer to be selected.

        :return: The conditions of this InstallmentPlanConfiguration.
        :rtype: list[int]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this InstallmentPlanConfiguration.

            If a transaction meets all selected conditions the installment plan will be available to the customer to be selected.

        :param conditions: The conditions of this InstallmentPlanConfiguration.
        :type: list[int]
        """

        self._conditions = conditions
    
    @property
    def id(self):
        """Gets the id of this InstallmentPlanConfiguration.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this InstallmentPlanConfiguration.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InstallmentPlanConfiguration.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this InstallmentPlanConfiguration.
        :type: int
        """

        self._id = id
    
    @property
    def installment_fee(self):
        """Gets the installment_fee of this InstallmentPlanConfiguration.

            The installment fee is a fixed amount that is charged additionally when applying this installment plan.

        :return: The installment_fee of this InstallmentPlanConfiguration.
        :rtype: float
        """
        return self._installment_fee

    @installment_fee.setter
    def installment_fee(self, installment_fee):
        """Sets the installment_fee of this InstallmentPlanConfiguration.

            The installment fee is a fixed amount that is charged additionally when applying this installment plan.

        :param installment_fee: The installment_fee of this InstallmentPlanConfiguration.
        :type: float
        """

        self._installment_fee = installment_fee
    
    @property
    def interest_rate(self):
        """Gets the interest_rate of this InstallmentPlanConfiguration.

            The interest rate is a percentage of the total amount that is charged additionally when applying this installment plan.

        :return: The interest_rate of this InstallmentPlanConfiguration.
        :rtype: float
        """
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        """Sets the interest_rate of this InstallmentPlanConfiguration.

            The interest rate is a percentage of the total amount that is charged additionally when applying this installment plan.

        :param interest_rate: The interest_rate of this InstallmentPlanConfiguration.
        :type: float
        """

        self._interest_rate = interest_rate
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this InstallmentPlanConfiguration.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this InstallmentPlanConfiguration.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this InstallmentPlanConfiguration.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this InstallmentPlanConfiguration.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def minimal_amount(self):
        """Gets the minimal_amount of this InstallmentPlanConfiguration.

            The installment plan can only be applied if the orders total is at least the defined minimal amount.

        :return: The minimal_amount of this InstallmentPlanConfiguration.
        :rtype: float
        """
        return self._minimal_amount

    @minimal_amount.setter
    def minimal_amount(self, minimal_amount):
        """Sets the minimal_amount of this InstallmentPlanConfiguration.

            The installment plan can only be applied if the orders total is at least the defined minimal amount.

        :param minimal_amount: The minimal_amount of this InstallmentPlanConfiguration.
        :type: float
        """

        self._minimal_amount = minimal_amount
    
    @property
    def name(self):
        """Gets the name of this InstallmentPlanConfiguration.

            The installment plan name is used internally to identify the plan in administrative interfaces.For example it is used within search fields and hence it should be distinct and descriptive.

        :return: The name of this InstallmentPlanConfiguration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstallmentPlanConfiguration.

            The installment plan name is used internally to identify the plan in administrative interfaces.For example it is used within search fields and hence it should be distinct and descriptive.

        :param name: The name of this InstallmentPlanConfiguration.
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name
    
    @property
    def payment_method_configurations(self):
        """Gets the payment_method_configurations of this InstallmentPlanConfiguration.

            A installment plan can be enabled only for specific payment method configurations. Other payment methods will not be selectable by the buyer.

        :return: The payment_method_configurations of this InstallmentPlanConfiguration.
        :rtype: list[int]
        """
        return self._payment_method_configurations

    @payment_method_configurations.setter
    def payment_method_configurations(self, payment_method_configurations):
        """Sets the payment_method_configurations of this InstallmentPlanConfiguration.

            A installment plan can be enabled only for specific payment method configurations. Other payment methods will not be selectable by the buyer.

        :param payment_method_configurations: The payment_method_configurations of this InstallmentPlanConfiguration.
        :type: list[int]
        """

        self._payment_method_configurations = payment_method_configurations
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this InstallmentPlanConfiguration.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this InstallmentPlanConfiguration.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this InstallmentPlanConfiguration.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this InstallmentPlanConfiguration.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def sort_order(self):
        """Gets the sort_order of this InstallmentPlanConfiguration.

            The sort order controls in which order the installation plans are listed. The sort order is used to order the plans in ascending order.

        :return: The sort_order of this InstallmentPlanConfiguration.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this InstallmentPlanConfiguration.

            The sort order controls in which order the installation plans are listed. The sort order is used to order the plans in ascending order.

        :param sort_order: The sort_order of this InstallmentPlanConfiguration.
        :type: int
        """

        self._sort_order = sort_order
    
    @property
    def space_reference(self):
        """Gets the space_reference of this InstallmentPlanConfiguration.

            

        :return: The space_reference of this InstallmentPlanConfiguration.
        :rtype: SpaceReference
        """
        return self._space_reference

    @space_reference.setter
    def space_reference(self, space_reference):
        """Sets the space_reference of this InstallmentPlanConfiguration.

            

        :param space_reference: The space_reference of this InstallmentPlanConfiguration.
        :type: SpaceReference
        """

        self._space_reference = space_reference
    
    @property
    def state(self):
        """Gets the state of this InstallmentPlanConfiguration.

            

        :return: The state of this InstallmentPlanConfiguration.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InstallmentPlanConfiguration.

            

        :param state: The state of this InstallmentPlanConfiguration.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def tax_class(self):
        """Gets the tax_class of this InstallmentPlanConfiguration.

            The tax class determines the taxes which are applicable on all fees linked to the installment plan.

        :return: The tax_class of this InstallmentPlanConfiguration.
        :rtype: TaxClass
        """
        return self._tax_class

    @tax_class.setter
    def tax_class(self, tax_class):
        """Sets the tax_class of this InstallmentPlanConfiguration.

            The tax class determines the taxes which are applicable on all fees linked to the installment plan.

        :param tax_class: The tax_class of this InstallmentPlanConfiguration.
        :type: TaxClass
        """

        self._tax_class = tax_class
    
    @property
    def terms_and_conditions(self):
        """Gets the terms_and_conditions of this InstallmentPlanConfiguration.

            The terms and conditions will be displayed to the customer when he or she selects this installment plan.

        :return: The terms_and_conditions of this InstallmentPlanConfiguration.
        :rtype: ResourcePath
        """
        return self._terms_and_conditions

    @terms_and_conditions.setter
    def terms_and_conditions(self, terms_and_conditions):
        """Sets the terms_and_conditions of this InstallmentPlanConfiguration.

            The terms and conditions will be displayed to the customer when he or she selects this installment plan.

        :param terms_and_conditions: The terms_and_conditions of this InstallmentPlanConfiguration.
        :type: ResourcePath
        """

        self._terms_and_conditions = terms_and_conditions
    
    @property
    def title(self):
        """Gets the title of this InstallmentPlanConfiguration.

            The title of the installment plan is used within the payment process. The title is visible to the buyer.

        :return: The title of this InstallmentPlanConfiguration.
        :rtype: DatabaseTranslatedString
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InstallmentPlanConfiguration.

            The title of the installment plan is used within the payment process. The title is visible to the buyer.

        :param title: The title of this InstallmentPlanConfiguration.
        :type: DatabaseTranslatedString
        """

        self._title = title
    
    @property
    def version(self):
        """Gets the version of this InstallmentPlanConfiguration.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this InstallmentPlanConfiguration.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InstallmentPlanConfiguration.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this InstallmentPlanConfiguration.
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
        if issubclass(InstallmentPlanConfiguration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, InstallmentPlanConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
