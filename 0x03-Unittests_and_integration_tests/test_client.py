#!/usr/bin/env python3
"""Integration tests for GithubOrgClient.public_repos method."""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


@parameterized_class([{
    "org_payload": org_payload,
    "repos_payload": repos_payload,
    "expected_repos": expected_repos,
    "apache2_repos": apache2_repos,
}])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient using real logic except external calls."""

    @classmethod
    def setUpClass(cls) -> None:
        """Patch get_json to return values from fixtures based on input URL."""
        cls.get_patcher = patch('client.get_json')
        mock_get_json = cls.get_patcher.start()

        def json_side_effect(url):
            if url == f"https://api.github.com/orgs/{cls.org_payload['login']}":
                return cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                return cls.repos_payload
            return {}

        mock_get_json.side_effect = json_side_effect

    @classmethod
    def tearDownClass(cls) -> None:
        """Stop the get_json patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """Test that public_repos returns expected repo names."""
        client = GithubOrgClient(self.org_payload["login"])
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """Test public_repos returns only repos with the apache-2.0 license."""
        client = GithubOrgClient(self.org_payload["login"])
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
