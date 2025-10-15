# coding: utf-8
import pprint
import six
from enum import Enum



class DunningCase:

    swagger_types = {
    
        'canceled_on': 'datetime',
        'created_on': 'datetime',
        'derecognized_on': 'datetime',
        'failed_on': 'datetime',
        'flow': 'DunningFlow',
        'id': 'int',
        'initial_invoice': 'TransactionInvoice',
        'linked_space_id': 'int',
        'linked_transaction': 'int',
        'planned_purge_date': 'datetime',
        'state': 'DunningCaseState',
        'succeeded_on': 'datetime',
        'version': 'int',
    }

    attribute_map = {
        'canceled_on': 'canceledOn','created_on': 'createdOn','derecognized_on': 'derecognizedOn','failed_on': 'failedOn','flow': 'flow','id': 'id','initial_invoice': 'initialInvoice','linked_space_id': 'linkedSpaceId','linked_transaction': 'linkedTransaction','planned_purge_date': 'plannedPurgeDate','state': 'state','succeeded_on': 'succeededOn','version': 'version',
    }

    
    _canceled_on = None
    _created_on = None
    _derecognized_on = None
    _failed_on = None
    _flow = None
    _id = None
    _initial_invoice = None
    _linked_space_id = None
    _linked_transaction = None
    _planned_purge_date = None
    _state = None
    _succeeded_on = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.canceled_on = kwargs.get('canceled_on', None)
        self.created_on = kwargs.get('created_on', None)
        self.derecognized_on = kwargs.get('derecognized_on', None)
        self.failed_on = kwargs.get('failed_on', None)
        self.flow = kwargs.get('flow', None)
        self.id = kwargs.get('id', None)
        self.initial_invoice = kwargs.get('initial_invoice', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.linked_transaction = kwargs.get('linked_transaction', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.succeeded_on = kwargs.get('succeeded_on', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def canceled_on(self):
        """Gets the canceled_on of this DunningCase.

            

        :return: The canceled_on of this DunningCase.
        :rtype: datetime
        """
        return self._canceled_on

    @canceled_on.setter
    def canceled_on(self, canceled_on):
        """Sets the canceled_on of this DunningCase.

            

        :param canceled_on: The canceled_on of this DunningCase.
        :type: datetime
        """

        self._canceled_on = canceled_on
    
    @property
    def created_on(self):
        """Gets the created_on of this DunningCase.

            The date and time when the object was created.

        :return: The created_on of this DunningCase.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this DunningCase.

            The date and time when the object was created.

        :param created_on: The created_on of this DunningCase.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def derecognized_on(self):
        """Gets the derecognized_on of this DunningCase.

            

        :return: The derecognized_on of this DunningCase.
        :rtype: datetime
        """
        return self._derecognized_on

    @derecognized_on.setter
    def derecognized_on(self, derecognized_on):
        """Sets the derecognized_on of this DunningCase.

            

        :param derecognized_on: The derecognized_on of this DunningCase.
        :type: datetime
        """

        self._derecognized_on = derecognized_on
    
    @property
    def failed_on(self):
        """Gets the failed_on of this DunningCase.

            

        :return: The failed_on of this DunningCase.
        :rtype: datetime
        """
        return self._failed_on

    @failed_on.setter
    def failed_on(self, failed_on):
        """Sets the failed_on of this DunningCase.

            

        :param failed_on: The failed_on of this DunningCase.
        :type: datetime
        """

        self._failed_on = failed_on
    
    @property
    def flow(self):
        """Gets the flow of this DunningCase.

            

        :return: The flow of this DunningCase.
        :rtype: DunningFlow
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this DunningCase.

            

        :param flow: The flow of this DunningCase.
        :type: DunningFlow
        """

        self._flow = flow
    
    @property
    def id(self):
        """Gets the id of this DunningCase.

            A unique identifier for the object.

        :return: The id of this DunningCase.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DunningCase.

            A unique identifier for the object.

        :param id: The id of this DunningCase.
        :type: int
        """

        self._id = id
    
    @property
    def initial_invoice(self):
        """Gets the initial_invoice of this DunningCase.

            

        :return: The initial_invoice of this DunningCase.
        :rtype: TransactionInvoice
        """
        return self._initial_invoice

    @initial_invoice.setter
    def initial_invoice(self, initial_invoice):
        """Sets the initial_invoice of this DunningCase.

            

        :param initial_invoice: The initial_invoice of this DunningCase.
        :type: TransactionInvoice
        """

        self._initial_invoice = initial_invoice
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this DunningCase.

            The ID of the space this object belongs to.

        :return: The linked_space_id of this DunningCase.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this DunningCase.

            The ID of the space this object belongs to.

        :param linked_space_id: The linked_space_id of this DunningCase.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def linked_transaction(self):
        """Gets the linked_transaction of this DunningCase.

            The payment transaction this object is linked to.

        :return: The linked_transaction of this DunningCase.
        :rtype: int
        """
        return self._linked_transaction

    @linked_transaction.setter
    def linked_transaction(self, linked_transaction):
        """Sets the linked_transaction of this DunningCase.

            The payment transaction this object is linked to.

        :param linked_transaction: The linked_transaction of this DunningCase.
        :type: int
        """

        self._linked_transaction = linked_transaction
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this DunningCase.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :return: The planned_purge_date of this DunningCase.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this DunningCase.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :param planned_purge_date: The planned_purge_date of this DunningCase.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this DunningCase.

            The object's current state.

        :return: The state of this DunningCase.
        :rtype: DunningCaseState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DunningCase.

            The object's current state.

        :param state: The state of this DunningCase.
        :type: DunningCaseState
        """

        self._state = state
    
    @property
    def succeeded_on(self):
        """Gets the succeeded_on of this DunningCase.

            

        :return: The succeeded_on of this DunningCase.
        :rtype: datetime
        """
        return self._succeeded_on

    @succeeded_on.setter
    def succeeded_on(self, succeeded_on):
        """Sets the succeeded_on of this DunningCase.

            

        :param succeeded_on: The succeeded_on of this DunningCase.
        :type: datetime
        """

        self._succeeded_on = succeeded_on
    
    @property
    def version(self):
        """Gets the version of this DunningCase.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :return: The version of this DunningCase.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DunningCase.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :param version: The version of this DunningCase.
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
        if issubclass(DunningCase, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, DunningCase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
