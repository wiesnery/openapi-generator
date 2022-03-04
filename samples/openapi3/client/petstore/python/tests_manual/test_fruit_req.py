# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import petstore_api
from petstore_api.model import apple_req
from petstore_api.model import banana_req
from petstore_api.model.fruit_req import FruitReq


class TestFruitReq(unittest.TestCase):
    """FruitReq unit test stubs"""
    length_cm = 20.3

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_fruit_access_errors(self):
        fruit = FruitReq(length_cm=self.length_cm)

        # setting a value that doesn't exist raises an exception
        # with a key
        with self.assertRaises(AttributeError):
            fruit['invalid_variable'] = 'some value'
        # with setattr
        with self.assertRaises(AttributeError):
            setattr(fruit, 'invalid_variable', 'some value')

        # getting a value that doesn't exist raises an exception
        # with a key
        with self.assertRaises(AttributeError):
            invalid_variable = fruit['cultivar']

        with self.assertRaises(AttributeError):
            getattr(fruit, 'cultivar')

    def test_FruitReq_banana(self):
        """Test FruitReq"""

        # make an instance of Fruit, a composed schema oneOf model
        # banana test
        fruit = FruitReq(length_cm=self.length_cm)
        # check its properties
        self.assertEqual(fruit.length_cm, self.length_cm)
        self.assertEqual(fruit['length_cm'], self.length_cm)
        self.assertEqual(getattr(fruit, 'length_cm'), self.length_cm)
        # check the dict representation
        self.assertEqual(
            fruit.to_dict(),
            {
                'length_cm': self.length_cm,
            }
        )

        # with getattr
        self.assertEqual(getattr(fruit, 'cultivar', 'some value'), 'some value')

        # make sure that the ModelComposed class properties are correct
        # model._composed_schemas stores the anyOf/allOf/oneOf info
        self.assertEqual(
            fruit._composed_schemas,
            {
                'anyOf': [],
                'allOf': [],
                'oneOf': [
                    apple_req.AppleReq,
                    banana_req.BananaReq,
                    type(None),
                ],
            }
        )
        # model._composed_instances is a list of the instances that were
        # made from the anyOf/allOf/OneOf classes in model._composed_schemas
        for composed_instance in fruit._composed_instances:
            if composed_instance.__class__ == banana_req.BananaReq:
                banana_instance = composed_instance
        self.assertEqual(
            fruit._composed_instances,
            [banana_instance]
        )
        # model._var_name_to_model_instances maps the variable name to the
        # model instances which store that variable
        self.assertEqual(
            fruit._var_name_to_model_instances,
            {
                'length_cm': [fruit, banana_instance],
            }
        )
        self.assertEqual(
            fruit._additional_properties_model_instances, [fruit]
        )

        # if we modify one of the properties owned by multiple
        # model_instances we get an exception when we try to access that
        # property because the retrieved values are not all the same
        banana_instance.length_cm = 4.56
        with self.assertRaises(petstore_api.ApiValueError):
            some_length_cm = fruit.length_cm

    def test_invalid_inputs(self):
        # including extra parameters raises an exception
        with self.assertRaises(petstore_api.ApiValueError):
            fruit = FruitReq(
                length_cm=self.length_cm,
                unknown_property='some value'
            )

        # including input parameters for two oneOf instances raise an exception
        with self.assertRaises(petstore_api.ApiValueError):
            fruit = FruitReq(
                length_cm=self.length_cm,
                cultivar='granny smith'
            )

    def test_FruitReq_apple(self):
        """Test FruitReq"""

        # apple test
        cultivar = 'golden delicious'
        fruit = FruitReq(cultivar=cultivar)
        # check its properties
        self.assertEqual(fruit.cultivar, cultivar)
        self.assertEqual(fruit['cultivar'], cultivar)
        self.assertEqual(getattr(fruit, 'cultivar'), cultivar)
        # check the dict representation
        self.assertEqual(
            fruit.to_dict(),
            {
                'cultivar': cultivar
            }
        )

        # model._composed_instances is a list of the instances that were
        # made from the anyOf/allOf/OneOf classes in model._composed_schemas
        for composed_instance in fruit._composed_instances:
            if composed_instance.__class__ == apple_req.AppleReq:
                apple_instance = composed_instance
        self.assertEqual(
            fruit._composed_instances,
            [apple_instance]
        )
        # model._var_name_to_model_instances maps the variable name to the
        # model instances which store that variable
        self.assertEqual(
            fruit._var_name_to_model_instances,
            {
                'cultivar': [fruit, apple_instance],
            }
        )
        self.assertEqual(
            fruit._additional_properties_model_instances, [fruit]
        )

    def test_null_fruit(self):
        # we can pass in None
        fruit = FruitReq(None)
        assert fruit is None


if __name__ == '__main__':
    unittest.main()