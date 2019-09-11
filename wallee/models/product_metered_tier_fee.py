# coding: utf-8
import pprint
import six
from enum import Enum



class ProductMeteredTierFee:

    swagger_types = {
    
        'fee': 'list[PersistableCurrencyAmount]',
        'id': 'int',
        'metered_fee': 'ProductMeteredFee',
        'start_range': 'float',
        'version': 'int',
    }

    attribute_map = {
        'fee': 'fee','id': 'id','metered_fee': 'meteredFee','start_range': 'startRange','version': 'version',
    }

    
    _fee = None
    _id = None
    _metered_fee = None
    _start_range = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.fee = kwargs.get('fee', None)
        self.id = kwargs.get('id', None)
        self.metered_fee = kwargs.get('metered_fee', None)
        self.start_range = kwargs.get('start_range', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def fee(self):
        """Gets the fee of this ProductMeteredTierFee.

            The fee determines the amount which is charged. The consumed metric is multiplied by the defined fee. The resulting amount is charged at the end of the period.

        :return: The fee of this ProductMeteredTierFee.
        :rtype: list[PersistableCurrencyAmount]
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this ProductMeteredTierFee.

            The fee determines the amount which is charged. The consumed metric is multiplied by the defined fee. The resulting amount is charged at the end of the period.

        :param fee: The fee of this ProductMeteredTierFee.
        :type: list[PersistableCurrencyAmount]
        """

        self._fee = fee
    
    @property
    def id(self):
        """Gets the id of this ProductMeteredTierFee.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this ProductMeteredTierFee.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProductMeteredTierFee.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this ProductMeteredTierFee.
        :type: int
        """

        self._id = id
    
    @property
    def metered_fee(self):
        """Gets the metered_fee of this ProductMeteredTierFee.

            

        :return: The metered_fee of this ProductMeteredTierFee.
        :rtype: ProductMeteredFee
        """
        return self._metered_fee

    @metered_fee.setter
    def metered_fee(self, metered_fee):
        """Sets the metered_fee of this ProductMeteredTierFee.

            

        :param metered_fee: The metered_fee of this ProductMeteredTierFee.
        :type: ProductMeteredFee
        """

        self._metered_fee = metered_fee
    
    @property
    def start_range(self):
        """Gets the start_range of this ProductMeteredTierFee.

            The start range defines the metered consumption of the metric from which on the defined fee gets applied. This means when a subscription consumes a value of 10 or more and the start range is set to 10 the fee defined on the tier will be applied.

        :return: The start_range of this ProductMeteredTierFee.
        :rtype: float
        """
        return self._start_range

    @start_range.setter
    def start_range(self, start_range):
        """Sets the start_range of this ProductMeteredTierFee.

            The start range defines the metered consumption of the metric from which on the defined fee gets applied. This means when a subscription consumes a value of 10 or more and the start range is set to 10 the fee defined on the tier will be applied.

        :param start_range: The start_range of this ProductMeteredTierFee.
        :type: float
        """

        self._start_range = start_range
    
    @property
    def version(self):
        """Gets the version of this ProductMeteredTierFee.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ProductMeteredTierFee.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ProductMeteredTierFee.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ProductMeteredTierFee.
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
        if issubclass(ProductMeteredTierFee, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ProductMeteredTierFee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
