# coding: utf-8

"""
    mcode-sdk-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.2.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from monday_code.models.publish_message_response import PublishMessageResponse

class TestPublishMessageResponse(unittest.TestCase):
    """PublishMessageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PublishMessageResponse:
        """Test PublishMessageResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PublishMessageResponse`
        """
        model = PublishMessageResponse()
        if include_optional:
            return PublishMessageResponse(
                id = ''
            )
        else:
            return PublishMessageResponse(
                id = '',
        )
        """

    def testPublishMessageResponse(self):
        """Test PublishMessageResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
