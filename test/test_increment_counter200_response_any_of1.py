# coding: utf-8

"""
    mcode-sdk-api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.2.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from monday_code.models.increment_counter200_response_any_of1 import IncrementCounter200ResponseAnyOf1

class TestIncrementCounter200ResponseAnyOf1(unittest.TestCase):
    """IncrementCounter200ResponseAnyOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IncrementCounter200ResponseAnyOf1:
        """Test IncrementCounter200ResponseAnyOf1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IncrementCounter200ResponseAnyOf1`
        """
        model = IncrementCounter200ResponseAnyOf1()
        if include_optional:
            return IncrementCounter200ResponseAnyOf1(
                error = None,
                success = True,
                new_counter_value = 1.337,
                message = ''
            )
        else:
            return IncrementCounter200ResponseAnyOf1(
                success = True,
                new_counter_value = 1.337,
                message = '',
        )
        """

    def testIncrementCounter200ResponseAnyOf1(self):
        """Test IncrementCounter200ResponseAnyOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
