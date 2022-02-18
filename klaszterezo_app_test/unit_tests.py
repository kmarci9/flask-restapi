import os
import unittest
import unittest
from unittest.mock import Mock, patch, MagicMock
from jsonschema import ValidationError
from klaszterezo_app_logic.jsonvalidator import  JsonValidator, InvalidJsonException


class TestValidator(unittest.TestCase):

  def test_invalid_group_len(self):
    json_groups = """{"group_1": [[0.1, -0.2], [0.4, -0.5, 0.6]],"group_2": [[0.33, 0.42, -0.1]],"group_3": [[-0.7564, 0.9845, 0.66], [-0.55,-0.55, -0.55], [0.3, 0.33, 0.333]]}"""
    jv = JsonValidator()
    with self.assertRaises(InvalidJsonException) as context:
      jv.validate_json(json_groups)
      print (str(context.exception))
    self.assertTrue('Invalid length of input arrays, every array must have the same size' in str(context.exception))

  def test_invalid_group_type(self):
    json_groups = """{"group_1": [[0.1, -0.2, "0.3"], [0.4, -0.5, 0.6]],"group_2": [[0.33, 0.42, -0.1]],"group_3": [[-0.7564, 0.9845, 0.66], [-0.55,-0.55, -0.55], [0.3, 0.33, 0.333]]}"""
    jv = JsonValidator()
    with self.assertRaises(ValidationError) as context:
      jv.validate_json(json_groups)
      print (str(context.exception))
    self.assertTrue("'0.3' is not of type 'number'" in str(context.exception))

  def test_group_naming(self):
    json_groups = """{"group_1": [[0.1, -0.2, 0.3], [0.4, -0.5, 0.6]],"group_8": [[0.33, 0.42, -0.1]],"group_3": [[-0.7564, 0.9845, 0.66], [-0.55,-0.55, -0.55], [0.3, 0.33, 0.333]]}"""
    jv = JsonValidator()
    with self.assertRaises(InvalidJsonException) as context:
      jv.validate_json(json_groups)
      print (str(context.exception))
    self.assertTrue('Invalid group numbering, group numbers should be continuous starting from 1' in str(context.exception))

  def test_invalid_groupnaming(self):
    json_groups = """{"asd": [[0.1, -0.2, 0.3], [0.4, -0.5, 0.6]],"group_8": [[0.33, 0.42, -0.1]],"group_3": [[-0.7564, 0.9845, 0.66], [-0.55,-0.55, -0.55], [0.3, 0.33, 0.333]]}"""
    jv = JsonValidator()
    with self.assertRaises(ValidationError) as context:
      jv.validate_json(json_groups)
      print (str(context.exception))
    self.assertTrue("'asd' does not match any of the regexes: '^group_[1-9]+$'" in str(context.exception))
    


# python -m unittest unit_tests.py


if __name__ == "__main__":
    unittest.main()



