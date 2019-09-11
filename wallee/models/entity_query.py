# coding: utf-8
import pprint
import six
from enum import Enum



class EntityQuery:

    swagger_types = {
    
        'filter': 'EntityQueryFilter',
        'language': 'str',
        'number_of_entities': 'int',
        'order_bys': 'list[EntityQueryOrderBy]',
        'starting_entity': 'int',
    }

    attribute_map = {
        'filter': 'filter','language': 'language','number_of_entities': 'numberOfEntities','order_bys': 'orderBys','starting_entity': 'startingEntity',
    }

    
    _filter = None
    _language = None
    _number_of_entities = None
    _order_bys = None
    _starting_entity = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.filter = kwargs.get('filter', None)
        self.language = kwargs.get('language', None)
        self.number_of_entities = kwargs.get('number_of_entities', None)
        self.order_bys = kwargs.get('order_bys', None)
        self.starting_entity = kwargs.get('starting_entity', None)
        

    
    @property
    def filter(self):
        """Gets the filter of this EntityQuery.

            The filter node defines the root filter node of the query. The root node may contain multiple sub nodes with different filters in it.

        :return: The filter of this EntityQuery.
        :rtype: EntityQueryFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this EntityQuery.

            The filter node defines the root filter node of the query. The root node may contain multiple sub nodes with different filters in it.

        :param filter: The filter of this EntityQuery.
        :type: EntityQueryFilter
        """

        self._filter = filter
    
    @property
    def language(self):
        """Gets the language of this EntityQuery.

            The language is applied to the ordering of the entities returned. Some entity fields are language dependent and hence the language is required to order them.

        :return: The language of this EntityQuery.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this EntityQuery.

            The language is applied to the ordering of the entities returned. Some entity fields are language dependent and hence the language is required to order them.

        :param language: The language of this EntityQuery.
        :type: str
        """

        self._language = language
    
    @property
    def number_of_entities(self):
        """Gets the number_of_entities of this EntityQuery.

            The number of entities defines how many entities should be returned. There is a maximum of 100 entities.

        :return: The number_of_entities of this EntityQuery.
        :rtype: int
        """
        return self._number_of_entities

    @number_of_entities.setter
    def number_of_entities(self, number_of_entities):
        """Sets the number_of_entities of this EntityQuery.

            The number of entities defines how many entities should be returned. There is a maximum of 100 entities.

        :param number_of_entities: The number_of_entities of this EntityQuery.
        :type: int
        """

        self._number_of_entities = number_of_entities
    
    @property
    def order_bys(self):
        """Gets the order_bys of this EntityQuery.

            The order bys allows to define the ordering of the entities returned by the search.

        :return: The order_bys of this EntityQuery.
        :rtype: list[EntityQueryOrderBy]
        """
        return self._order_bys

    @order_bys.setter
    def order_bys(self, order_bys):
        """Sets the order_bys of this EntityQuery.

            The order bys allows to define the ordering of the entities returned by the search.

        :param order_bys: The order_bys of this EntityQuery.
        :type: list[EntityQueryOrderBy]
        """

        self._order_bys = order_bys
    
    @property
    def starting_entity(self):
        """Gets the starting_entity of this EntityQuery.

            The 'starting entity' defines the entity number at which the returned result should start. The entity number is the consecutive number of the entity as returned and it is not the entity id.

        :return: The starting_entity of this EntityQuery.
        :rtype: int
        """
        return self._starting_entity

    @starting_entity.setter
    def starting_entity(self, starting_entity):
        """Sets the starting_entity of this EntityQuery.

            The 'starting entity' defines the entity number at which the returned result should start. The entity number is the consecutive number of the entity as returned and it is not the entity id.

        :param starting_entity: The starting_entity of this EntityQuery.
        :type: int
        """

        self._starting_entity = starting_entity
    

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
        if issubclass(EntityQuery, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, EntityQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
