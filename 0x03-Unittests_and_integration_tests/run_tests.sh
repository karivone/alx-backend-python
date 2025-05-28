#!/bin/bash

echo "Running tests in directory: $(pwd)"
echo "Python version:"
python3 --version

echo "Checking fixtures module..."
python3 -c "
import fixtures
print('fixtures module location:', fixtures.__file__)
print('fixtures attributes:', dir(fixtures))
print('org_payload present?', 'org_payload' in dir(fixtures))
"

echo "Running unittest with PYTHONPATH=."
PYTHONPATH=. python3 -m unittest -q test_client.py -v

TEST_EXIT_CODE=$?

if [ $TEST_EXIT_CODE -eq 0 ]; then
  echo 'Tests passed successfully.'
else
  echo 'Tests failed or had errors.'
fi

exit $TEST_EXIT_CODE
