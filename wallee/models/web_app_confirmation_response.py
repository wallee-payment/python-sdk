# coding: utf-8
import pprint
import six
from enum import Enum



class WebAppConfirmationResponse:

    swagger_types = {
    
        'access_token': 'str',
        'scope': 'str',
        'space': 'Space',
        'state': 'str',
        'token_type': 'str',
    }

    attribute_map = {
        'access_token': 'access_token','scope': 'scope','space': 'space','state': 'state','token_type': 'token_type',
    }

    
    _access_token = None
    _scope = None
    _space = None
    _state = None
    _token_type = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.access_token = kwargs.get('access_token', None)
        self.scope = kwargs.get('scope', None)
        self.space = kwargs.get('space', None)
        self.state = kwargs.get('state', None)
        self.token_type = kwargs.get('token_type', None)
        

    
    @property
    def access_token(self):
        """Gets the access_token of this WebAppConfirmationResponse.

            The access code grants permissions to the web service API according to the OAuth standard.

        :return: The access_token of this WebAppConfirmationResponse.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this WebAppConfirmationResponse.

            The access code grants permissions to the web service API according to the OAuth standard.

        :param access_token: The access_token of this WebAppConfirmationResponse.
        :type: str
        """

        self._access_token = access_token
    
    @property
    def scope(self):
        """Gets the scope of this WebAppConfirmationResponse.

            The scope contains the permissions granted to the web app within the space.

        :return: The scope of this WebAppConfirmationResponse.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this WebAppConfirmationResponse.

            The scope contains the permissions granted to the web app within the space.

        :param scope: The scope of this WebAppConfirmationResponse.
        :type: str
        """

        self._scope = scope
    
    @property
    def space(self):
        """Gets the space of this WebAppConfirmationResponse.

            This is the space into which the web app is installed into.

        :return: The space of this WebAppConfirmationResponse.
        :rtype: Space
        """
        return self._space

    @space.setter
    def space(self, space):
        """Sets the space of this WebAppConfirmationResponse.

            This is the space into which the web app is installed into.

        :param space: The space of this WebAppConfirmationResponse.
        :type: Space
        """

        self._space = space
    
    @property
    def state(self):
        """Gets the state of this WebAppConfirmationResponse.

            The state contains the state parameter content provided when initiating the app installation.

        :return: The state of this WebAppConfirmationResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this WebAppConfirmationResponse.

            The state contains the state parameter content provided when initiating the app installation.

        :param state: The state of this WebAppConfirmationResponse.
        :type: str
        """

        self._state = state
    
    @property
    def token_type(self):
        """Gets the token_type of this WebAppConfirmationResponse.

            The token type indicates the type of the access token. The type determines the authentication mechanism to use for accessing the web service API.

        :return: The token_type of this WebAppConfirmationResponse.
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this WebAppConfirmationResponse.

            The token type indicates the type of the access token. The type determines the authentication mechanism to use for accessing the web service API.

        :param token_type: The token_type of this WebAppConfirmationResponse.
        :type: str
        """

        self._token_type = token_type
    

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
        if issubclass(WebAppConfirmationResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, WebAppConfirmationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
