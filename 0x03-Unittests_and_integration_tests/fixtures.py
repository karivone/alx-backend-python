org_payload = {
    "login": "test_org",
    "id": 123456,
    "repos_url": "https://api.github.com/orgs/test_org/repos",
    "description": "Test organization for unit tests",
}

repos_payload = [
    {"name": "repo1", "license": {"key": "apache-2.0"}},
    {"name": "repo2", "license": {"key": "mit"}},
    {"name": "repo3", "license": None},
]

expected_repos = ["repo1", "repo2", "repo3"]

apache2_repos = ["repo1"]
