'''
Your goal is to replace the "pass" commands on each of the stack class's methods.
Once you have completed a method you may test to see if it has been completed by
running this script. You can assume all numbers entered into the stack will be between 0 and 1000. See
the method descriptions below for a description of the expected function

#Push Method
  this method should take in an integer called data and insert the varaible to the front of the
  stack array variable. The method should return a boolean value to denote if the process was successful.
#Pop Method
  this method should remove the first element of the array. Make sure to return the value that was removed. 
  In the case of the pop method being called on an empty array return -1
#Peek Method
  this method should return the value of the first element of the array. The array should remain the same 
  after this method is called.
  In the case of the pop method being called on an empty array return -1
#is_empty Method
  this method should return a boolean value to denote if it is empty (true) or not (false)

*Note the use of "type hints"*

'''

class stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data:int) -> bool:
        pass

    def pop(self) -> int:
        pass

    def peek(self) -> int:
        pass

    def is_empty(self) -> bool:
        pass





## do not modify anything below this comment ##
import unittest

class stack_test(unittest.TestCase):
    
    def test_push(self):
        s = stack()
        self.assertEqual(s.push(1),True)
        self.assertEqual(s.push(2),True)
        self.assertEqual(s.push(3),True)
        self.assertEqual(s.push("not valid"),False)
        self.assertListEqual(s.stack, [3,2,1])
        
    def test_pop(self):
        s = stack()
        s.push(3)
        s.push(2)
        s.push(1)
        self.assertEqual(s.pop(),1)
        self.assertEqual(s.pop(),2)
        self.assertEqual(s.pop(),3)
        self.assertEqual(s.pop(),-1)
        self.assertListEqual(s.stack, [])
        
    def test_peek(self):
        s = stack()
        s.push(1)
        self.assertEqual(s.peek(),1)
        s.push(2)
        self.assertEqual(s.peek(),2)
        s.push(3)
        self.assertEqual(s.peek(),3)
        
    def test_is_empty(self):
        s = stack()
        self.assertEqual(s.is_empty(), True)
        s.push(3)
        self.assertEqual(s.is_empty(), False)
        s.pop()
        self.assertEqual(s.is_empty(), True)

if __name__ == '__main__':
    unittest.main()