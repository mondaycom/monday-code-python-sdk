# coding: utf-8

"""
    mcode-sdk-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from monday_code.models.upsert_by_key_from_storage200_response_any_of1 import UpsertByKeyFromStorage200ResponseAnyOf1

class TestUpsertByKeyFromStorage200ResponseAnyOf1(unittest.TestCase):
    """UpsertByKeyFromStorage200ResponseAnyOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpsertByKeyFromStorage200ResponseAnyOf1:
        """Test UpsertByKeyFromStorage200ResponseAnyOf1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpsertByKeyFromStorage200ResponseAnyOf1`
        """
        model = UpsertByKeyFromStorage200ResponseAnyOf1()
        if include_optional:
            return UpsertByKeyFromStorage200ResponseAnyOf1(
                version = None,
                success = True,
                error = ''
            )
        else:
            return UpsertByKeyFromStorage200ResponseAnyOf1(
                success = True,
                error = '',
        )
        """

    def testUpsertByKeyFromStorage200ResponseAnyOf1(self):
        """Test UpsertByKeyFromStorage200ResponseAnyOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
