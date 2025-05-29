#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

class TestGithubOrgClient(unittest.TestCase):

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the correct list of repo names"""
        mock_get_json.return_value = repos_payload

        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = org_payload
            client = GithubOrgClient("testorg")
            result = client.public_repos()
            self.assertEqual(result, expected_repos)

    @patch('client.get_json')
    def test_public_repos_with_license(self, mock_get_json):
        """Test filtering public_repos by license"""
        mock_get_json.return_value = repos_payload

        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = org_payload
            client = GithubOrgClient("testorg")
            result = client.public_repos(license="apache-2.0")
            self.assertEqual(result, apache2_repos)

if __name__ == "__main__":
    unittest.main()
