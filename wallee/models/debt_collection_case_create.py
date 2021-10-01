# coding: utf-8
import pprint
import six
from enum import Enum
from . import AbstractDebtCollectionCaseUpdate


class DebtCollectionCaseCreate(AbstractDebtCollectionCaseUpdate):

    swagger_types = {
    
        'collector_configuration': 'int',
        'external_id': 'str',
        'reference': 'str',
    }

    attribute_map = {
        'collector_configuration': 'collectorConfiguration','external_id': 'externalId','reference': 'reference',
    }

    
    _collector_configuration = None
    _external_id = None
    _reference = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.collector_configuration = kwargs.get('collector_configuration', None)
        self.external_id = kwargs.get('external_id')

        self.reference = kwargs.get('reference')

        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def collector_configuration(self):
        """Gets the collector_configuration of this DebtCollectionCaseCreate.

            The collector configuration determines how the debt collection case is processed.

        :return: The collector_configuration of this DebtCollectionCaseCreate.
        :rtype: int
        """
        return self._collector_configuration

    @collector_configuration.setter
    def collector_configuration(self, collector_configuration):
        """Sets the collector_configuration of this DebtCollectionCaseCreate.

            The collector configuration determines how the debt collection case is processed.

        :param collector_configuration: The collector_configuration of this DebtCollectionCaseCreate.
        :type: int
        """

        self._collector_configuration = collector_configuration
    
    @property
    def external_id(self):
        """Gets the external_id of this DebtCollectionCaseCreate.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :return: The external_id of this DebtCollectionCaseCreate.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this DebtCollectionCaseCreate.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :param external_id: The external_id of this DebtCollectionCaseCreate.
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")

        self._external_id = external_id
    
    @property
    def reference(self):
        """Gets the reference of this DebtCollectionCaseCreate.

            The case reference is used in the communication with the debtor. It should be unique and it should be linkable with the source of the debt collection case.

        :return: The reference of this DebtCollectionCaseCreate.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this DebtCollectionCaseCreate.

            The case reference is used in the communication with the debtor. It should be unique and it should be linkable with the source of the debt collection case.

        :param reference: The reference of this DebtCollectionCaseCreate.
        :type: str
        """
        if reference is None:
            raise ValueError("Invalid value for `reference`, must not be `None`")

        self._reference = reference
    

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
        if issubclass(DebtCollectionCaseCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, DebtCollectionCaseCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
