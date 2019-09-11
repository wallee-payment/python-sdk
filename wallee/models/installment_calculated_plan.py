# coding: utf-8
import pprint
import six
from enum import Enum



class InstallmentCalculatedPlan:

    swagger_types = {
    
        'configuration': 'InstallmentPlanConfiguration',
        'payment_method_configurations': 'list[PaymentMethodConfiguration]',
        'slices': 'list[InstallmentCalculatedSlice]',
        'total_amount': 'float',
        'transaction': 'Transaction',
    }

    attribute_map = {
        'configuration': 'configuration','payment_method_configurations': 'paymentMethodConfigurations','slices': 'slices','total_amount': 'totalAmount','transaction': 'transaction',
    }

    
    _configuration = None
    _payment_method_configurations = None
    _slices = None
    _total_amount = None
    _transaction = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.configuration = kwargs.get('configuration', None)
        self.payment_method_configurations = kwargs.get('payment_method_configurations', None)
        self.slices = kwargs.get('slices', None)
        self.total_amount = kwargs.get('total_amount', None)
        self.transaction = kwargs.get('transaction', None)
        

    
    @property
    def configuration(self):
        """Gets the configuration of this InstallmentCalculatedPlan.

            

        :return: The configuration of this InstallmentCalculatedPlan.
        :rtype: InstallmentPlanConfiguration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this InstallmentCalculatedPlan.

            

        :param configuration: The configuration of this InstallmentCalculatedPlan.
        :type: InstallmentPlanConfiguration
        """

        self._configuration = configuration
    
    @property
    def payment_method_configurations(self):
        """Gets the payment_method_configurations of this InstallmentCalculatedPlan.

            

        :return: The payment_method_configurations of this InstallmentCalculatedPlan.
        :rtype: list[PaymentMethodConfiguration]
        """
        return self._payment_method_configurations

    @payment_method_configurations.setter
    def payment_method_configurations(self, payment_method_configurations):
        """Sets the payment_method_configurations of this InstallmentCalculatedPlan.

            

        :param payment_method_configurations: The payment_method_configurations of this InstallmentCalculatedPlan.
        :type: list[PaymentMethodConfiguration]
        """

        self._payment_method_configurations = payment_method_configurations
    
    @property
    def slices(self):
        """Gets the slices of this InstallmentCalculatedPlan.

            

        :return: The slices of this InstallmentCalculatedPlan.
        :rtype: list[InstallmentCalculatedSlice]
        """
        return self._slices

    @slices.setter
    def slices(self, slices):
        """Sets the slices of this InstallmentCalculatedPlan.

            

        :param slices: The slices of this InstallmentCalculatedPlan.
        :type: list[InstallmentCalculatedSlice]
        """

        self._slices = slices
    
    @property
    def total_amount(self):
        """Gets the total_amount of this InstallmentCalculatedPlan.

            

        :return: The total_amount of this InstallmentCalculatedPlan.
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this InstallmentCalculatedPlan.

            

        :param total_amount: The total_amount of this InstallmentCalculatedPlan.
        :type: float
        """

        self._total_amount = total_amount
    
    @property
    def transaction(self):
        """Gets the transaction of this InstallmentCalculatedPlan.

            

        :return: The transaction of this InstallmentCalculatedPlan.
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this InstallmentCalculatedPlan.

            

        :param transaction: The transaction of this InstallmentCalculatedPlan.
        :type: Transaction
        """

        self._transaction = transaction
    

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
        if issubclass(InstallmentCalculatedPlan, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, InstallmentCalculatedPlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
