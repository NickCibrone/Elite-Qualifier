import unittest
from main import final_responses
from main import action_responses



class TestCase(unittest.TestCase):
  
  def test_upper(self): 
      self.assertListEqual(final_responses, action_responses)


if __name__ == '__main__':
    unittest.main()