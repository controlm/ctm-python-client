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


class CertificateSigningRequestData(object):
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
        "organization": "str",
        "organization_unit": "str",
        "city_locality": "str",
        "state_province": "str",
        "country": "str",
        "email_address": "str",
    }

    attribute_map = {
        "organization": "organization",
        "organization_unit": "organizationUnit",
        "city_locality": "cityLocality",
        "state_province": "stateProvince",
        "country": "country",
        "email_address": "emailAddress",
    }

    def __init__(
        self,
        organization=None,
        organization_unit=None,
        city_locality=None,
        state_province=None,
        country=None,
        email_address=None,
        _configuration=None,
    ):  # noqa: E501
        """CertificateSigningRequestData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._organization = None
        self._organization_unit = None
        self._city_locality = None
        self._state_province = None
        self._country = None
        self._email_address = None
        self.discriminator = None

        if organization is not None:
            self.organization = organization
        if organization_unit is not None:
            self.organization_unit = organization_unit
        if city_locality is not None:
            self.city_locality = city_locality
        if state_province is not None:
            self.state_province = state_province
        if country is not None:
            self.country = country
        if email_address is not None:
            self.email_address = email_address

    @property
    def organization(self):
        """Gets the organization of this CertificateSigningRequestData.  # noqa: E501

        The organization HIDDEN  # noqa: E501

        :return: The organization of this CertificateSigningRequestData.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this CertificateSigningRequestData.

        The organization HIDDEN  # noqa: E501

        :param organization: The organization of this CertificateSigningRequestData.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def organization_unit(self):
        """Gets the organization_unit of this CertificateSigningRequestData.  # noqa: E501

        The organizationUnit HIDDEN  # noqa: E501

        :return: The organization_unit of this CertificateSigningRequestData.  # noqa: E501
        :rtype: str
        """
        return self._organization_unit

    @organization_unit.setter
    def organization_unit(self, organization_unit):
        """Sets the organization_unit of this CertificateSigningRequestData.

        The organizationUnit HIDDEN  # noqa: E501

        :param organization_unit: The organization_unit of this CertificateSigningRequestData.  # noqa: E501
        :type: str
        """

        self._organization_unit = organization_unit

    @property
    def city_locality(self):
        """Gets the city_locality of this CertificateSigningRequestData.  # noqa: E501

        The cityLocality HIDDEN  # noqa: E501

        :return: The city_locality of this CertificateSigningRequestData.  # noqa: E501
        :rtype: str
        """
        return self._city_locality

    @city_locality.setter
    def city_locality(self, city_locality):
        """Sets the city_locality of this CertificateSigningRequestData.

        The cityLocality HIDDEN  # noqa: E501

        :param city_locality: The city_locality of this CertificateSigningRequestData.  # noqa: E501
        :type: str
        """

        self._city_locality = city_locality

    @property
    def state_province(self):
        """Gets the state_province of this CertificateSigningRequestData.  # noqa: E501

        The stateProvince HIDDEN  # noqa: E501

        :return: The state_province of this CertificateSigningRequestData.  # noqa: E501
        :rtype: str
        """
        return self._state_province

    @state_province.setter
    def state_province(self, state_province):
        """Sets the state_province of this CertificateSigningRequestData.

        The stateProvince HIDDEN  # noqa: E501

        :param state_province: The state_province of this CertificateSigningRequestData.  # noqa: E501
        :type: str
        """

        self._state_province = state_province

    @property
    def country(self):
        """Gets the country of this CertificateSigningRequestData.  # noqa: E501

        The country HIDDEN  # noqa: E501

        :return: The country of this CertificateSigningRequestData.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CertificateSigningRequestData.

        The country HIDDEN  # noqa: E501

        :param country: The country of this CertificateSigningRequestData.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def email_address(self):
        """Gets the email_address of this CertificateSigningRequestData.  # noqa: E501

        The emailAddress HIDDEN  # noqa: E501

        :return: The email_address of this CertificateSigningRequestData.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this CertificateSigningRequestData.

        The emailAddress HIDDEN  # noqa: E501

        :param email_address: The email_address of this CertificateSigningRequestData.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

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
        if issubclass(CertificateSigningRequestData, dict):
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
        if not isinstance(other, CertificateSigningRequestData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CertificateSigningRequestData):
            return True

        return self.to_dict() != other.to_dict()