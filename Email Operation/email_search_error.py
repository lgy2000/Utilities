class email_search_error(Exception):
    """Exception raised when there is an error searching emails."""

    def __init__(self, message="Failed to search emails."):
        self.message = message
        super().__init__(self.message)