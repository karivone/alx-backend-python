#!/usr/bin/env python3

org_payload = {
    "login": "google",
    "id": 1234,
    "url": "https://api.github.com/orgs/google",
    "repos_url": "https://api.github.com/orgs/google/repos"
}

repos_payload = [
    {"name": "repo1", "license": {"key": "apache-2.0"}},
    {"name": "repo2", "license": {"key": "mit"}},
    {"name": "repo3", "license": None},
]

expected_repos = ["repo1", "repo2", "repo3"]

apache2_repos = ["repo1"]
