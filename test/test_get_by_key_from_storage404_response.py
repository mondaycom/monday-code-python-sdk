# coding: utf-8

"""
    mcode-sdk-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from monday_code.models.get_by_key_from_storage404_response import GetByKeyFromStorage404Response

class TestGetByKeyFromStorage404Response(unittest.TestCase):
    """GetByKeyFromStorage404Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetByKeyFromStorage404Response:
        """Test GetByKeyFromStorage404Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetByKeyFromStorage404Response`
        """
        model = GetByKeyFromStorage404Response()
        if include_optional:
            return GetByKeyFromStorage404Response(
                reason = ''
            )
        else:
            return GetByKeyFromStorage404Response(
                reason = '',
        )
        """

    def testGetByKeyFromStorage404Response(self):
        """Test GetByKeyFromStorage404Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
