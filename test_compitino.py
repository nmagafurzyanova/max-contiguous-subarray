import unittest
from compitino_python import max_contiguous_subarray

class TestMain(unittest.TestCase):
    '''
    Test case per la funzione max_contiguous_subarray.
    '''
    def test_max_contiguous_subarray(self):
        # controllo per una lista dei numeri random:
        self.assertEqual(max_contiguous_subarray([1,2,-1,3,4,1]), (10, [1,2,-1,3,4,1]))
        # controllo per una lista che contiene solo 0:
        self.assertEqual(max_contiguous_subarray([0]), (0, [0]))
        # controllo per una lista dei soli elementi negativi:
        self.assertEqual(max_contiguous_subarray([-17,-11,-13]), (-11, [-11]))
        # controllo Exception per una lista vuota:
        self.assertRaises(TypeError, lambda: max_contiguous_subarray([]))
        
if __name__ == '__main__':
    unittest.main()