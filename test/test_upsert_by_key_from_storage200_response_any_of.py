# coding: utf-8

"""
    mcode-sdk-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from monday_code.models.upsert_by_key_from_storage200_response_any_of import UpsertByKeyFromStorage200ResponseAnyOf

class TestUpsertByKeyFromStorage200ResponseAnyOf(unittest.TestCase):
    """UpsertByKeyFromStorage200ResponseAnyOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpsertByKeyFromStorage200ResponseAnyOf:
        """Test UpsertByKeyFromStorage200ResponseAnyOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpsertByKeyFromStorage200ResponseAnyOf`
        """
        model = UpsertByKeyFromStorage200ResponseAnyOf()
        if include_optional:
            return UpsertByKeyFromStorage200ResponseAnyOf(
                error = None,
                success = True,
                version = ''
            )
        else:
            return UpsertByKeyFromStorage200ResponseAnyOf(
                success = True,
                version = '',
        )
        """

    def testUpsertByKeyFromStorage200ResponseAnyOf(self):
        """Test UpsertByKeyFromStorage200ResponseAnyOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
