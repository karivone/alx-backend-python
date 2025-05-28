#!/usr/bin/env python3
import unittest
import sys

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromName('test_client')
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("OK")
        sys.exit(0)
    else:
        print("FAILED")
        sys.exit(1)
