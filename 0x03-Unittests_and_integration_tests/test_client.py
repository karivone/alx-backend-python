#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient  # Ensure this matches your actual file structure


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient.org"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")  # Patch the get_json used in the GithubOrgClient module
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct data"""
        expected_result = {"login": org_name, "id": 1234}
        mock_get_json.return_value = expected_result

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_result)
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
        )


if __name__ == '__main__':
    unittest.main()
