#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from typing import List, Dict
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
import unittest
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient.org"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    # Patch the get_json used in the GithubOrgClient module
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

"""Unit tests for the GithubOrgClient class."""


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class."""

    def test_public_repos_url(self) -> None:
        """
        Test that _public_repos_url property returns the repos_url from the
        mocked org payload.
        """
        fake_payload: Dict[str, str] = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        client = GithubOrgClient("google")

        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock,
            return_value=fake_payload
        ):
            result = client._public_repos_url
            self.assertEqual(result, fake_payload["repos_url"])


if __name__ == "__main__":
    unittest.main()


"""Unit tests for the GithubOrgClient class."""


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient.public_repos method"""

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns expected repo names"""
        # Mock payload returned by get_json
        test_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "gpl"}},
        ]
        mock_get_json.return_value = test_payload

        # Mock _public_repos_url property
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock,
            return_value="https://api.github.com/orgs/test-org/repos"
        ) as mock_url:
            client = GithubOrgClient("test-org")
            result = client.public_repos()

            # Expected output
            expected = ["repo1", "repo2", "repo3"]

            # Assertions
            self.assertEqual(result, expected)
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test-org/repos"
            )


if __name__ == '__main__':
    unittest.main()


"""Unit tests for GithubOrgClient.has_license method."""


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class."""

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(
            self,
            repo: dict,
            license_key: str,
            expected: bool
            ) -> None:
        client = GithubOrgClient("test_org")
        self.assertEqual(client.has_license(repo, license_key), expected)


"""Integration tests for GithubOrgClient.public_repos method."""


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests using real logic except external HTTP calls."""

    @classmethod
    def setUpClass(cls):
        """Patch requests.get to return mock responses using fixture data."""
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()

        def side_effect(url, *args, **kwargs):
            mock_resp = Mock()
            if url == (
                f"https://api.github.com/orgs/{cls.org_payload['login']}"
            ):
                mock_resp.json.return_value = cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                mock_resp.json.return_value = cls.repos_payload
            else:
                mock_resp.json.return_value = {}
            return mock_resp

        mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos returns expected data."""
        client = GithubOrgClient(self.org_payload["login"])
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with license filtering."""
        client = GithubOrgClient(self.org_payload["login"])
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )


if __name__ == "__main__":
    unittest.main()
