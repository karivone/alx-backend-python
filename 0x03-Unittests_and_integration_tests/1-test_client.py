#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from fixtures import org_payload

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
        # Arrange
        expected_result = {"login": org_name, "id": 1234}
        mock_get_json.return_value = expected_result

        # Act
        client = GithubOrgClient(org_name)
        result = client.org

        # Assert
        self.assertEqual(result, expected_result)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3
"""Unit tests for the GithubOrgClient class."""

import unittest
from unittest.mock import patch, PropertyMock
from typing import Dict
from client import GithubOrgClient


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

#!/usr/bin/env python3
"""Unit test for GithubOrgClient.public_repos."""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        # Mock the payload for get_json
        test_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
        ]
        mock_get_json.return_value = test_payload

        # Mock the _public_repos_url property
        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock,
            return_value="https://api.github.com/orgs/test-org/repos"
        ) as mock_public_repos_url:
            # Create instance and call the method
            client = GithubOrgClient("test-org")
            repos = client.public_repos()

            # Assert the repos are what we expect
            expected_repos = ["repo1", "repo2"]
            self.assertEqual(repos, expected_repos)

            # Assert the mocked property was called once
            mock_public_repos_url.assert_called_once()

        # Assert get_json was called once
        mock_get_json.assert_called_once()

#!/usr/bin/env python3
"""Unit tests for GithubOrgClient.has_license method."""

import unittest
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class."""

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: dict, license_key: str, expected: bool) -> None:
        """Test that has_license returns True if repo has the given license key,
        else False.
        """
        client = GithubOrgClient("test_org")
        self.assertEqual(client.has_license(repo, license_key), expected)

#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient
"""

import unittest
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit test class for GithubOrgClient"""

    def test_has_license(self) -> None:
        """Test that has_license correctly identifies the license match"""
        client = GithubOrgClient("google")

        test_cases = [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]

        for repo, license_key, expected in test_cases:
            with self.subTest(repo=repo, license_key=license_key):
                self.assertEqual(client.has_license(repo, license_key), expected)

#!/usr/bin/env python3
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient using real logic except external calls."""

    @classmethod
    def setUpClass(cls) -> None:
        """Setup patcher for requests.get and configure side_effect for json() to return fixtures."""
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()

        # Helper side_effect function for requests.get().json()
        def json_side_effect(url, *args, **kwargs):
            mock_resp = Mock()
            if url == "https://api.github.com/orgs/google":
                mock_resp.json.return_value = cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                mock_resp.json.return_value = cls.repos_payload
            else:
                mock_resp.json.return_value = {}
            return mock_resp

        mock_get.side_effect = json_side_effect

    @classmethod
    def tearDownClass(cls) -> None:
        """Stop patcher for requests.get."""
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """Test that public_repos returns expected repo names."""
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """Test public_repos with license filtering (apache-2.0)."""
        client = GithubOrgClient("google")
        repos = client.public_repos(license_key="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)

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
