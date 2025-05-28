import fixtures
print("fixtures file location:", fixtures.__file__)
print("fixtures attributes:", dir(fixtures))
print("org_payload in fixtures?", hasattr(fixtures, "org_payload"))
