# coding: utf-8
import pprint
import six
from enum import Enum



class DebtCollectionCaseDocument:

    swagger_types = {
    
        'created_on': 'datetime',
        'debt_collection_case': 'int',
        'file_name': 'str',
        'id': 'int',
        'labels': 'list[Label]',
        'linked_space_id': 'int',
        'mime_type': 'str',
        'planned_purge_date': 'datetime',
        'storage_id': 'str',
        'unique_id': 'str',
        'version': 'int',
    }

    attribute_map = {
        'created_on': 'createdOn','debt_collection_case': 'debtCollectionCase','file_name': 'fileName','id': 'id','labels': 'labels','linked_space_id': 'linkedSpaceId','mime_type': 'mimeType','planned_purge_date': 'plannedPurgeDate','storage_id': 'storageId','unique_id': 'uniqueId','version': 'version',
    }

    
    _created_on = None
    _debt_collection_case = None
    _file_name = None
    _id = None
    _labels = None
    _linked_space_id = None
    _mime_type = None
    _planned_purge_date = None
    _storage_id = None
    _unique_id = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.created_on = kwargs.get('created_on', None)
        self.debt_collection_case = kwargs.get('debt_collection_case', None)
        self.file_name = kwargs.get('file_name', None)
        self.id = kwargs.get('id', None)
        self.labels = kwargs.get('labels', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.mime_type = kwargs.get('mime_type', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.storage_id = kwargs.get('storage_id', None)
        self.unique_id = kwargs.get('unique_id', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def created_on(self):
        """Gets the created_on of this DebtCollectionCaseDocument.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this DebtCollectionCaseDocument.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this DebtCollectionCaseDocument.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this DebtCollectionCaseDocument.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def debt_collection_case(self):
        """Gets the debt_collection_case of this DebtCollectionCaseDocument.

            

        :return: The debt_collection_case of this DebtCollectionCaseDocument.
        :rtype: int
        """
        return self._debt_collection_case

    @debt_collection_case.setter
    def debt_collection_case(self, debt_collection_case):
        """Sets the debt_collection_case of this DebtCollectionCaseDocument.

            

        :param debt_collection_case: The debt_collection_case of this DebtCollectionCaseDocument.
        :type: int
        """

        self._debt_collection_case = debt_collection_case
    
    @property
    def file_name(self):
        """Gets the file_name of this DebtCollectionCaseDocument.

            

        :return: The file_name of this DebtCollectionCaseDocument.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this DebtCollectionCaseDocument.

            

        :param file_name: The file_name of this DebtCollectionCaseDocument.
        :type: str
        """
        if file_name is not None and len(file_name) > 100:
            raise ValueError("Invalid value for `file_name`, length must be less than or equal to `100`")

        self._file_name = file_name
    
    @property
    def id(self):
        """Gets the id of this DebtCollectionCaseDocument.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this DebtCollectionCaseDocument.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DebtCollectionCaseDocument.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this DebtCollectionCaseDocument.
        :type: int
        """

        self._id = id
    
    @property
    def labels(self):
        """Gets the labels of this DebtCollectionCaseDocument.

            

        :return: The labels of this DebtCollectionCaseDocument.
        :rtype: list[Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this DebtCollectionCaseDocument.

            

        :param labels: The labels of this DebtCollectionCaseDocument.
        :type: list[Label]
        """

        self._labels = labels
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this DebtCollectionCaseDocument.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this DebtCollectionCaseDocument.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this DebtCollectionCaseDocument.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this DebtCollectionCaseDocument.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def mime_type(self):
        """Gets the mime_type of this DebtCollectionCaseDocument.

            

        :return: The mime_type of this DebtCollectionCaseDocument.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this DebtCollectionCaseDocument.

            

        :param mime_type: The mime_type of this DebtCollectionCaseDocument.
        :type: str
        """

        self._mime_type = mime_type
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this DebtCollectionCaseDocument.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this DebtCollectionCaseDocument.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this DebtCollectionCaseDocument.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this DebtCollectionCaseDocument.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def storage_id(self):
        """Gets the storage_id of this DebtCollectionCaseDocument.

            

        :return: The storage_id of this DebtCollectionCaseDocument.
        :rtype: str
        """
        return self._storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        """Sets the storage_id of this DebtCollectionCaseDocument.

            

        :param storage_id: The storage_id of this DebtCollectionCaseDocument.
        :type: str
        """
        if storage_id is not None and len(storage_id) > 100:
            raise ValueError("Invalid value for `storage_id`, length must be less than or equal to `100`")

        self._storage_id = storage_id
    
    @property
    def unique_id(self):
        """Gets the unique_id of this DebtCollectionCaseDocument.

            

        :return: The unique_id of this DebtCollectionCaseDocument.
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this DebtCollectionCaseDocument.

            

        :param unique_id: The unique_id of this DebtCollectionCaseDocument.
        :type: str
        """
        if unique_id is not None and len(unique_id) > 500:
            raise ValueError("Invalid value for `unique_id`, length must be less than or equal to `500`")

        self._unique_id = unique_id
    
    @property
    def version(self):
        """Gets the version of this DebtCollectionCaseDocument.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this DebtCollectionCaseDocument.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DebtCollectionCaseDocument.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this DebtCollectionCaseDocument.
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
        if issubclass(DebtCollectionCaseDocument, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, DebtCollectionCaseDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
