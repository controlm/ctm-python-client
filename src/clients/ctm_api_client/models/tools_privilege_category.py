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


class ToolsPrivilegeCategory(object):
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
        "cli": "str",
        "batch_impact_manager_report": "str",
        "forecast_report": "str",
    }

    attribute_map = {
        "cli": "Cli",
        "batch_impact_manager_report": "BatchImpactManagerReport",
        "forecast_report": "ForecastReport",
    }

    def __init__(
        self,
        cli=None,
        batch_impact_manager_report=None,
        forecast_report=None,
        _configuration=None,
    ):  # noqa: E501
        """ToolsPrivilegeCategory - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cli = None
        self._batch_impact_manager_report = None
        self._forecast_report = None
        self.discriminator = None

        if cli is not None:
            self.cli = cli
        if batch_impact_manager_report is not None:
            self.batch_impact_manager_report = batch_impact_manager_report
        if forecast_report is not None:
            self.forecast_report = forecast_report

    @property
    def cli(self):
        """Gets the cli of this ToolsPrivilegeCategory.  # noqa: E501

        CLI access level (None, Browse, Update, Full)  # noqa: E501

        :return: The cli of this ToolsPrivilegeCategory.  # noqa: E501
        :rtype: str
        """
        return self._cli

    @cli.setter
    def cli(self, cli):
        """Sets the cli of this ToolsPrivilegeCategory.

        CLI access level (None, Browse, Update, Full)  # noqa: E501

        :param cli: The cli of this ToolsPrivilegeCategory.  # noqa: E501
        :type: str
        """

        self._cli = cli

    @property
    def batch_impact_manager_report(self):
        """Gets the batch_impact_manager_report of this ToolsPrivilegeCategory.  # noqa: E501

        BIM Reports access level (None, Browse, Update, Full)  # noqa: E501

        :return: The batch_impact_manager_report of this ToolsPrivilegeCategory.  # noqa: E501
        :rtype: str
        """
        return self._batch_impact_manager_report

    @batch_impact_manager_report.setter
    def batch_impact_manager_report(self, batch_impact_manager_report):
        """Sets the batch_impact_manager_report of this ToolsPrivilegeCategory.

        BIM Reports access level (None, Browse, Update, Full)  # noqa: E501

        :param batch_impact_manager_report: The batch_impact_manager_report of this ToolsPrivilegeCategory.  # noqa: E501
        :type: str
        """

        self._batch_impact_manager_report = batch_impact_manager_report

    @property
    def forecast_report(self):
        """Gets the forecast_report of this ToolsPrivilegeCategory.  # noqa: E501

        Forecast Reports access level (None, Browse, Update, Full)  # noqa: E501

        :return: The forecast_report of this ToolsPrivilegeCategory.  # noqa: E501
        :rtype: str
        """
        return self._forecast_report

    @forecast_report.setter
    def forecast_report(self, forecast_report):
        """Sets the forecast_report of this ToolsPrivilegeCategory.

        Forecast Reports access level (None, Browse, Update, Full)  # noqa: E501

        :param forecast_report: The forecast_report of this ToolsPrivilegeCategory.  # noqa: E501
        :type: str
        """

        self._forecast_report = forecast_report

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
        if issubclass(ToolsPrivilegeCategory, dict):
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
        if not isinstance(other, ToolsPrivilegeCategory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ToolsPrivilegeCategory):
            return True

        return self.to_dict() != other.to_dict()
