from test_charge import TestCharge
from test_client import TestClient
import unittest


test_classes_to_use = [TestCharge, TestClient]


loader = unittest.TestLoader()
suites_list = []

for test_class in test_classes_to_use:
    suite = loader.loadTestsFromTestCase(test_class)
    suites_list.append(suite)

grand_suite = unittest.TestSuite(suites_list)
runner = unittest.TextTestRunner(verbosity=1)
runner.run(grand_suite)
