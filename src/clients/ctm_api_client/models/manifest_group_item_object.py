# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.20.215
    Contact: customer_support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from clients.ctm_api_client.configuration import Configuration


class ManifestGroupItemObject(object):
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
    swagger_types = {"name": "str", "icon_base64": "str"}

    attribute_map = {"name": "name", "icon_base64": "iconBase64"}

    def __init__(self, name=None, icon_base64=None, _configuration=None):  # noqa: E501
        """ManifestGroupItemObject - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._icon_base64 = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if icon_base64 is not None:
            self.icon_base64 = icon_base64

    @property
    def name(self):
        """Gets the name of this ManifestGroupItemObject.  # noqa: E501


        :return: The name of this ManifestGroupItemObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ManifestGroupItemObject.


        :param name: The name of this ManifestGroupItemObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def icon_base64(self):
        """Gets the icon_base64 of this ManifestGroupItemObject.  # noqa: E501


        :return: The icon_base64 of this ManifestGroupItemObject.  # noqa: E501
        :rtype: str
        """
        return self._icon_base64

    @icon_base64.setter
    def icon_base64(self, icon_base64):
        """Sets the icon_base64 of this ManifestGroupItemObject.


        :param icon_base64: The icon_base64 of this ManifestGroupItemObject.  # noqa: E501
        :type: str
        """

        self._icon_base64 = icon_base64

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(ManifestGroupItemObject, dict):
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
        if not isinstance(other, ManifestGroupItemObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ManifestGroupItemObject):
            return True

        return self.to_dict() != other.to_dict()