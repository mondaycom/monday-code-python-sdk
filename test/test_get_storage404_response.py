# coding: utf-8

"""
    mcode-sdk-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from monday_sdk.models.get_storage404_response import GetStorage404Response

class TestGetStorage404Response(unittest.TestCase):
    """GetStorage404Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetStorage404Response:
        """Test GetStorage404Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetStorage404Response`
        """
        model = GetStorage404Response()
        if include_optional:
            return GetStorage404Response(
                reason = ''
            )
        else:
            return GetStorage404Response(
                reason = '',
        )
        """

    def testGetStorage404Response(self):
        """Test GetStorage404Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
