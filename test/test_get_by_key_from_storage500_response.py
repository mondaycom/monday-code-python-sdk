# coding: utf-8

"""
    mcode-sdk-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from monday_code.models.get_by_key_from_storage500_response import GetByKeyFromStorage500Response

class TestGetByKeyFromStorage500Response(unittest.TestCase):
    """GetByKeyFromStorage500Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetByKeyFromStorage500Response:
        """Test GetByKeyFromStorage500Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetByKeyFromStorage500Response`
        """
        model = GetByKeyFromStorage500Response()
        if include_optional:
            return GetByKeyFromStorage500Response(
                reason = ''
            )
        else:
            return GetByKeyFromStorage500Response(
        )
        """

    def testGetByKeyFromStorage500Response(self):
        """Test GetByKeyFromStorage500Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
