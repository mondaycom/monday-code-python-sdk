# coding: utf-8

"""
    mcode-sdk-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from monday_code.models.upsert_by_key_from_storage200_response import UpsertByKeyFromStorage200Response

class TestUpsertByKeyFromStorage200Response(unittest.TestCase):
    """UpsertByKeyFromStorage200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpsertByKeyFromStorage200Response:
        """Test UpsertByKeyFromStorage200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpsertByKeyFromStorage200Response`
        """
        model = UpsertByKeyFromStorage200Response()
        if include_optional:
            return UpsertByKeyFromStorage200Response(
                error = '',
                success = True,
                version = monday_code.models.version.version()
            )
        else:
            return UpsertByKeyFromStorage200Response(
                error = '',
                success = True,
                version = monday_code.models.version.version(),
        )
        """

    def testUpsertByKeyFromStorage200Response(self):
        """Test UpsertByKeyFromStorage200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
