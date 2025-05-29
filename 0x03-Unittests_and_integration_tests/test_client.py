#!/usr/bin/env python3
"""Integration tests for GithubOrgClient.public_repos method."""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures  import org_payload, repos_payload, expected_repos, apache2_repos


@parameterized_class([{
    "org_payload": org_payload,
    "repos_payload": repos_payload,
    "expected_repos": expected_repos,
    "apache2_repos": apache2_repos,
}])
class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()

        # Helper side_effect function for requests.get().json()
        def json_side_effect(url, *args, **kwargs):
            mock_resp = Mock()
            if url == f"https://api.github.com/orgs/{cls.org_payload['login']}":
                mock_resp.json.return_value = cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                mock_resp.json.return_value = cls.repos_payload
            else:
                mock_resp.json.return_value = {}
            return mock_resp

        mock_get.side_effect = json_side_effect

    @classmethod
    def tearDownClass(cls) -> None:
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        client = GithubOrgClient(self.org_payload["login"])
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        client = GithubOrgClient(self.org_payload["login"])
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)
if __name__ == "__main__":
    unittest.main()
