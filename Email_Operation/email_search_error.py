# !/usr/bin/env python3

"""
email_search_error.py

Defines a custom exception for errors in searching emails.

Description:
This module defines a custom exception class `EmailSearchError` that is raised when there is an error in searching emails. The exception class
inherits from the built-in `Exception` class in Python.
"""


class EmailSearchError(Exception):
    """Exception raised when there is an error searching emails."""

    def __init__(self, message="Failed to search emails."):
        self.message = message
        super().__init__(self.message)
