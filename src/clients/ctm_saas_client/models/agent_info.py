# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.20.30
    Contact: customer_support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from clients.ctm_saas_client.configuration import Configuration


class AgentInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'node_id': 'str',
        'ctm': 'str'
    }

    attribute_map = {
        'node_id': 'nodeID',
        'ctm': 'ctm'
    }

    def __init__(self, node_id=None, ctm=None, _configuration=None):  # noqa: E501
        """AgentInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._node_id = None
        self._ctm = None
        self.discriminator = None

        self.node_id = node_id
        self.ctm = ctm

    @property
    def node_id(self):
        """Gets the node_id of this AgentInfo.  # noqa: E501

        The Agent nodeID  # noqa: E501

        :return: The node_id of this AgentInfo.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this AgentInfo.

        The Agent nodeID  # noqa: E501

        :param node_id: The node_id of this AgentInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and node_id is None:
            raise ValueError("Invalid value for `node_id`, must not be `None`")  # noqa: E501

        self._node_id = node_id

    @property
    def ctm(self):
        """Gets the ctm of this AgentInfo.  # noqa: E501

        The Control-M name  # noqa: E501

        :return: The ctm of this AgentInfo.  # noqa: E501
        :rtype: str
        """
        return self._ctm

    @ctm.setter
    def ctm(self, ctm):
        """Sets the ctm of this AgentInfo.

        The Control-M name  # noqa: E501

        :param ctm: The ctm of this AgentInfo.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and ctm is None:
            raise ValueError("Invalid value for `ctm`, must not be `None`")  # noqa: E501

        self._ctm = ctm

    def to_dict(self):
        """Returns the model properties as a dict"""
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
            else:
                result[attr] = value
        if issubclass(AgentInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AgentInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AgentInfo):
            return True

        return self.to_dict() != other.to_dict()