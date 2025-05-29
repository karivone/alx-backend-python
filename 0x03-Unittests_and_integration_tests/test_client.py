#!/usr/bin/env python3
"""Integration tests for GithubOrgClient.public_repos method."""

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized_class

from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

from github_client import GithubOrgClient


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient using real logic except external calls."""

    @classmethod
    def setUpClass(cls) -> None:
        """Setup patcher for requests.get and configure side_effect for json() to return fixtures."""
        cls.get_patcher = patch('github_client.requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Helper side_effect function for requests.get().json()
        def side_effect(url, *args, **kwargs):
            mock_resp = MagicMock()

            if url == f"https://api.github.com/orgs/{cls.org_payload['login']}":
                mock_resp.json.return_value = cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                mock_resp.json.return_value = cls.repos_payload
            else:
                mock_resp.json.return_value = {}

            return mock_resp

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patching requests.get."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        # Example test using the setup mocks
        client = GithubOrgClient(self.org_payload['login'])
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)
