#!/usr/bin/env python3
"""Client module to interact with GitHub organization data."""

from utils import get_json


class GithubOrgClient:
    """GitHub Organization Client."""

    def __init__(self, org_name):
        self.org_name = org_name

    @property
    def org(self):
        """Return organization info from GitHub API."""
        url = f"https://api.github.com/orgs/{self.org_name}"
        return get_json(url)

    @property
    def _public_repos_url(self):
        """Get public repositories URL from the org payload."""
        return self.org["repos_url"]

    def public_repos(self, license=None):
        """Return a list of public repo names, filtered by license if provided."""
        repos = get_json(self._public_repos_url)
        names = [
            repo["name"]
            for repo in repos
            if not license or self.has_license(repo, license)
        ]
        return names
    def has_license(self, repo, license_key):
        license = repo.get("license")
        if not license:
            return False
        return license.get("key") == license_key
