import unittest
from Telescope import Telescope

class TestTelescope(unittest.TestCase):

    def test_Telescope_init(self):
        item = Telescope(pupil=7)
        self.assertEqual(item.pupil, 7)
        self.assertEqual(item._Telescope__focal, 1200)
        self.assertEqual(item._Telescope__diameter, 203)
        with self.assertRaises(Exception):
            item.add_diameter_focal(-100,-100)
        with self.assertRaises(Exception):
            item.add_diameter_focal(-100, 100)
        with self.assertRaises(Exception):
            item.add_diameter_focal(200, 100)      

if __name__ == "__main__": 
    unittest.main(verbosity=2)