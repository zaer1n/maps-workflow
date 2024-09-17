class RuleException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

class RuleViolation(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
