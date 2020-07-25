# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionUpdate:

    swagger_types = {
    
        'id': 'int',
        'version': 'int',
        'affiliate': 'int',
        'description': 'str',
        'planned_termination_date': 'datetime',
    }

    attribute_map = {
        'id': 'id','version': 'version','affiliate': 'affiliate','description': 'description','planned_termination_date': 'plannedTerminationDate',
    }

    
    _id = None
    _version = None
    _affiliate = None
    _description = None
    _planned_termination_date = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id')

        self.version = kwargs.get('version')

        self.affiliate = kwargs.get('affiliate', None)
        self.description = kwargs.get('description', None)
        self.planned_termination_date = kwargs.get('planned_termination_date', None)
        

    
    @property
    def id(self):
        """Gets the id of this SubscriptionUpdate.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this SubscriptionUpdate.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionUpdate.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this SubscriptionUpdate.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id
    
    @property
    def version(self):
        """Gets the version of this SubscriptionUpdate.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this SubscriptionUpdate.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SubscriptionUpdate.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this SubscriptionUpdate.
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")

        self._version = version
    
    @property
    def affiliate(self):
        """Gets the affiliate of this SubscriptionUpdate.

            

        :return: The affiliate of this SubscriptionUpdate.
        :rtype: int
        """
        return self._affiliate

    @affiliate.setter
    def affiliate(self, affiliate):
        """Sets the affiliate of this SubscriptionUpdate.

            

        :param affiliate: The affiliate of this SubscriptionUpdate.
        :type: int
        """

        self._affiliate = affiliate
    
    @property
    def description(self):
        """Gets the description of this SubscriptionUpdate.

            

        :return: The description of this SubscriptionUpdate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SubscriptionUpdate.

            

        :param description: The description of this SubscriptionUpdate.
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")

        self._description = description
    
    @property
    def planned_termination_date(self):
        """Gets the planned_termination_date of this SubscriptionUpdate.

            

        :return: The planned_termination_date of this SubscriptionUpdate.
        :rtype: datetime
        """
        return self._planned_termination_date

    @planned_termination_date.setter
    def planned_termination_date(self, planned_termination_date):
        """Sets the planned_termination_date of this SubscriptionUpdate.

            

        :param planned_termination_date: The planned_termination_date of this SubscriptionUpdate.
        :type: datetime
        """

        self._planned_termination_date = planned_termination_date
    

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
        if issubclass(SubscriptionUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
