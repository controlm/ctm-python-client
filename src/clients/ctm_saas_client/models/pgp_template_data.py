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


class PgpTemplateData(object):
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
        'name': 'str',
        'executable_full_path': 'str',
        'exit_code': 'int',
        'passphrase': 'str',
        'recipient': 'str',
        'encryption_attributes': 'str',
        'decryption_attributes': 'str'
    }

    attribute_map = {
        'name': 'name',
        'executable_full_path': 'executableFullPath',
        'exit_code': 'exitCode',
        'passphrase': 'passphrase',
        'recipient': 'recipient',
        'encryption_attributes': 'encryptionAttributes',
        'decryption_attributes': 'decryptionAttributes'
    }

    def __init__(self, name=None, executable_full_path=None, exit_code=0, passphrase=None, recipient=None, encryption_attributes=None, decryption_attributes=None, _configuration=None):  # noqa: E501
        """PgpTemplateData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._executable_full_path = None
        self._exit_code = None
        self._passphrase = None
        self._recipient = None
        self._encryption_attributes = None
        self._decryption_attributes = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if executable_full_path is not None:
            self.executable_full_path = executable_full_path
        if exit_code is not None:
            self.exit_code = exit_code
        if passphrase is not None:
            self.passphrase = passphrase
        if recipient is not None:
            self.recipient = recipient
        if encryption_attributes is not None:
            self.encryption_attributes = encryption_attributes
        if decryption_attributes is not None:
            self.decryption_attributes = decryption_attributes

    @property
    def name(self):
        """Gets the name of this PgpTemplateData.  # noqa: E501

        Template name HIDDEN  # noqa: E501

        :return: The name of this PgpTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PgpTemplateData.

        Template name HIDDEN  # noqa: E501

        :param name: The name of this PgpTemplateData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def executable_full_path(self):
        """Gets the executable_full_path of this PgpTemplateData.  # noqa: E501

        Executable Full Path HIDDEN  # noqa: E501

        :return: The executable_full_path of this PgpTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._executable_full_path

    @executable_full_path.setter
    def executable_full_path(self, executable_full_path):
        """Sets the executable_full_path of this PgpTemplateData.

        Executable Full Path HIDDEN  # noqa: E501

        :param executable_full_path: The executable_full_path of this PgpTemplateData.  # noqa: E501
        :type: str
        """

        self._executable_full_path = executable_full_path

    @property
    def exit_code(self):
        """Gets the exit_code of this PgpTemplateData.  # noqa: E501

        Exit code (default 0) HIDDEN  # noqa: E501

        :return: The exit_code of this PgpTemplateData.  # noqa: E501
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """Sets the exit_code of this PgpTemplateData.

        Exit code (default 0) HIDDEN  # noqa: E501

        :param exit_code: The exit_code of this PgpTemplateData.  # noqa: E501
        :type: int
        """

        self._exit_code = exit_code

    @property
    def passphrase(self):
        """Gets the passphrase of this PgpTemplateData.  # noqa: E501

        passphrase HIDDEN  # noqa: E501

        :return: The passphrase of this PgpTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._passphrase

    @passphrase.setter
    def passphrase(self, passphrase):
        """Sets the passphrase of this PgpTemplateData.

        passphrase HIDDEN  # noqa: E501

        :param passphrase: The passphrase of this PgpTemplateData.  # noqa: E501
        :type: str
        """

        self._passphrase = passphrase

    @property
    def recipient(self):
        """Gets the recipient of this PgpTemplateData.  # noqa: E501

        Recipient HIDDEN  # noqa: E501

        :return: The recipient of this PgpTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this PgpTemplateData.

        Recipient HIDDEN  # noqa: E501

        :param recipient: The recipient of this PgpTemplateData.  # noqa: E501
        :type: str
        """

        self._recipient = recipient

    @property
    def encryption_attributes(self):
        """Gets the encryption_attributes of this PgpTemplateData.  # noqa: E501

        Encryption Attributes HIDDEN  # noqa: E501

        :return: The encryption_attributes of this PgpTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._encryption_attributes

    @encryption_attributes.setter
    def encryption_attributes(self, encryption_attributes):
        """Sets the encryption_attributes of this PgpTemplateData.

        Encryption Attributes HIDDEN  # noqa: E501

        :param encryption_attributes: The encryption_attributes of this PgpTemplateData.  # noqa: E501
        :type: str
        """

        self._encryption_attributes = encryption_attributes

    @property
    def decryption_attributes(self):
        """Gets the decryption_attributes of this PgpTemplateData.  # noqa: E501

        Decryption Attributes HIDDEN  # noqa: E501

        :return: The decryption_attributes of this PgpTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._decryption_attributes

    @decryption_attributes.setter
    def decryption_attributes(self, decryption_attributes):
        """Sets the decryption_attributes of this PgpTemplateData.

        Decryption Attributes HIDDEN  # noqa: E501

        :param decryption_attributes: The decryption_attributes of this PgpTemplateData.  # noqa: E501
        :type: str
        """

        self._decryption_attributes = decryption_attributes

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
        if issubclass(PgpTemplateData, dict):
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
        if not isinstance(other, PgpTemplateData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PgpTemplateData):
            return True

        return self.to_dict() != other.to_dict()