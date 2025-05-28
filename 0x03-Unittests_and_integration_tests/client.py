#!/usr/bin/env python3
"""A GitHub organization client."""

from typing import List, Dict, Optional

from utils import (
    get_json,
    access_nested_map,
    memoize,
)


class GithubOrgClient:
    """A GitHub organization client."""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """Initialize the GithubOrgClient."""
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """Return the organization information (memoized)."""
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """Return the URL for the organization's public repositories."""
        return self.org.get("repos_url", "")

    @memoize
    def repos_payload(self) -> List[Dict]:
        """Return the payload (list of repos) from the repos API endpoint (memoized)."""
        return get_json(self._public_repos_url)

    def public_repos(self, license: Optional[str] = None) -> List[str]:
        """
        Return a list of public repository names.

        Optionally filter repositories by license key.
        """
        repos = self.repos_payload
        return [
            repo["name"]
            for repo in repos
            if license is None or self.has_license(repo, license)
        ]

    @staticmethod
    def has_license(repo: Dict[str, Dict], license: str) -> bool:
        """
        Check if the repository has the specified license key.

        Args:
            repo: The repository dictionary.
            license_key: The license key to check for.

        Returns:
            True if the repo has the license key, False otherwise.
        """
        assert license is not None, "license cannot be None"
        try:
            return access_nested_map(repo, ("license", "key")) == license
        except KeyError:
            return False
