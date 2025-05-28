#!/usr/bin/env python3
"""Unit tests for utils functions: access_nested_map, get_json, memoize."""

import unittest
from typing import Mapping, Sequence, Any
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence[str], expected: Any
    ) -> None:
        """Test valid nested map access."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Sequence[str]
    ) -> None:
        """Test KeyError for invalid access."""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """Tests for get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: dict) -> None:
        """Test JSON response returned from URL."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch(
                "utils.requests.get", return_value=mock_response
        ) as mock_get:
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator."""

    def test_memoize(self):
        """Test that memoized method is only called once."""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_obj = TestClass()

        with patch.object(
            test_obj, 'a_method', wraps=test_obj.a_method
        ) as mocked:
            first = test_obj.a_property
            second = test_obj.a_property

            self.assertEqual(first, 42)
            self.assertEqual(second, 42)
            mocked.assert_called_once()


if __name__ == "__main__":
    unittest.main()
