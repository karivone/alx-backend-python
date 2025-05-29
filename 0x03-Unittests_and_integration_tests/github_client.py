import requests


class GithubOrgClient:
    """Client to interact with GitHub organization endpoints."""

    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org_name):
        self.org_name = org_name

    def org(self):
        """Fetch organization data from GitHub."""
        url = self.ORG_URL.format(self.org_name)
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def public_repos(self):
        """Return list of public repository names for the organization."""
        org_data = self.org()
        repos_url = org_data.get("repos_url")
        if not repos_url:
            return []

        response = requests.get(repos_url)
        response.raise_for_status()
        repos = response.json()

        # Extract and return repo names
        return [repo["name"] for repo in repos]
