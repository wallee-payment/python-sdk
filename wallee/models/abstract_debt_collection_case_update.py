# coding: utf-8
import pprint
import six
from enum import Enum



class AbstractDebtCollectionCaseUpdate:

    swagger_types = {
    
        'billing_address': 'AddressCreate',
        'contract_date': 'datetime',
        'currency': 'str',
        'due_date': 'datetime',
        'environment': 'DebtCollectionEnvironment',
        'language': 'str',
        'line_items': 'list[LineItemCreate]',
        'space_view_id': 'int',
    }

    attribute_map = {
        'billing_address': 'billingAddress','contract_date': 'contractDate','currency': 'currency','due_date': 'dueDate','environment': 'environment','language': 'language','line_items': 'lineItems','space_view_id': 'spaceViewId',
    }

    
    _billing_address = None
    _contract_date = None
    _currency = None
    _due_date = None
    _environment = None
    _language = None
    _line_items = None
    _space_view_id = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.billing_address = kwargs.get('billing_address', None)
        self.contract_date = kwargs.get('contract_date', None)
        self.currency = kwargs.get('currency', None)
        self.due_date = kwargs.get('due_date', None)
        self.environment = kwargs.get('environment', None)
        self.language = kwargs.get('language', None)
        self.line_items = kwargs.get('line_items', None)
        self.space_view_id = kwargs.get('space_view_id', None)
        

    
    @property
    def billing_address(self):
        """Gets the billing_address of this AbstractDebtCollectionCaseUpdate.

            The billing address of the case identifies the debtor.

        :return: The billing_address of this AbstractDebtCollectionCaseUpdate.
        :rtype: AddressCreate
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this AbstractDebtCollectionCaseUpdate.

            The billing address of the case identifies the debtor.

        :param billing_address: The billing_address of this AbstractDebtCollectionCaseUpdate.
        :type: AddressCreate
        """

        self._billing_address = billing_address
    
    @property
    def contract_date(self):
        """Gets the contract_date of this AbstractDebtCollectionCaseUpdate.

            The contract date is the date on which the contract with the debtor was signed on.

        :return: The contract_date of this AbstractDebtCollectionCaseUpdate.
        :rtype: datetime
        """
        return self._contract_date

    @contract_date.setter
    def contract_date(self, contract_date):
        """Sets the contract_date of this AbstractDebtCollectionCaseUpdate.

            The contract date is the date on which the contract with the debtor was signed on.

        :param contract_date: The contract_date of this AbstractDebtCollectionCaseUpdate.
        :type: datetime
        """

        self._contract_date = contract_date
    
    @property
    def currency(self):
        """Gets the currency of this AbstractDebtCollectionCaseUpdate.

            The currency defines the billing currency of the debt collection case.

        :return: The currency of this AbstractDebtCollectionCaseUpdate.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this AbstractDebtCollectionCaseUpdate.

            The currency defines the billing currency of the debt collection case.

        :param currency: The currency of this AbstractDebtCollectionCaseUpdate.
        :type: str
        """

        self._currency = currency
    
    @property
    def due_date(self):
        """Gets the due_date of this AbstractDebtCollectionCaseUpdate.

            The due date indicates the date on which the amount receivable was due. This date has to be always in the past.

        :return: The due_date of this AbstractDebtCollectionCaseUpdate.
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this AbstractDebtCollectionCaseUpdate.

            The due date indicates the date on which the amount receivable was due. This date has to be always in the past.

        :param due_date: The due_date of this AbstractDebtCollectionCaseUpdate.
        :type: datetime
        """

        self._due_date = due_date
    
    @property
    def environment(self):
        """Gets the environment of this AbstractDebtCollectionCaseUpdate.

            The environment in which this case will be processed. There must be a debt collector configuration present which supports the chosen environment.

        :return: The environment of this AbstractDebtCollectionCaseUpdate.
        :rtype: DebtCollectionEnvironment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this AbstractDebtCollectionCaseUpdate.

            The environment in which this case will be processed. There must be a debt collector configuration present which supports the chosen environment.

        :param environment: The environment of this AbstractDebtCollectionCaseUpdate.
        :type: DebtCollectionEnvironment
        """

        self._environment = environment
    
    @property
    def language(self):
        """Gets the language of this AbstractDebtCollectionCaseUpdate.

            The language indicates the language to be used in the communication with the debtor.

        :return: The language of this AbstractDebtCollectionCaseUpdate.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AbstractDebtCollectionCaseUpdate.

            The language indicates the language to be used in the communication with the debtor.

        :param language: The language of this AbstractDebtCollectionCaseUpdate.
        :type: str
        """

        self._language = language
    
    @property
    def line_items(self):
        """Gets the line_items of this AbstractDebtCollectionCaseUpdate.

            The line items of the debt collection case will be shown on documents sent to the debtor and the total of them makes up total amount to collect.

        :return: The line_items of this AbstractDebtCollectionCaseUpdate.
        :rtype: list[LineItemCreate]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this AbstractDebtCollectionCaseUpdate.

            The line items of the debt collection case will be shown on documents sent to the debtor and the total of them makes up total amount to collect.

        :param line_items: The line_items of this AbstractDebtCollectionCaseUpdate.
        :type: list[LineItemCreate]
        """

        self._line_items = line_items
    
    @property
    def space_view_id(self):
        """Gets the space_view_id of this AbstractDebtCollectionCaseUpdate.

            

        :return: The space_view_id of this AbstractDebtCollectionCaseUpdate.
        :rtype: int
        """
        return self._space_view_id

    @space_view_id.setter
    def space_view_id(self, space_view_id):
        """Sets the space_view_id of this AbstractDebtCollectionCaseUpdate.

            

        :param space_view_id: The space_view_id of this AbstractDebtCollectionCaseUpdate.
        :type: int
        """

        self._space_view_id = space_view_id
    

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
        if issubclass(AbstractDebtCollectionCaseUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AbstractDebtCollectionCaseUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
