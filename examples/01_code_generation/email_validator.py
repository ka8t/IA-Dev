"""
Email validation module with RFC 5322 compliance and disposable email detection.
"""

import re
import dns.resolver
from typing import Set
from dataclasses import dataclass


class EmailValidationError(Exception):
    """Base exception for email validation errors."""
    pass


class InvalidEmailFormatError(EmailValidationError):
    """Raised when email format is invalid."""
    pass


class DisposableEmailError(EmailValidationError):
    """Raised when email is from a disposable/temporary service."""
    pass


class InvalidDomainError(EmailValidationError):
    """Raised when email domain has no valid MX records."""
    pass


@dataclass
class EmailValidator:
    """
    Validates email addresses with RFC 5322 compliance.

    Attributes:
        check_mx (bool): Whether to verify MX records (default: True)
        dns_timeout (int): DNS query timeout in seconds (default: 3)
        disposable_domains (Set[str]): Set of known disposable email domains

    Example:
        >>> validator = EmailValidator()
        >>> validator.validate("user@example.com")
        True
        >>> validator.validate("invalid-email")
        Traceback (most recent call last):
            ...
        InvalidEmailFormatError: Invalid email format
    """

    check_mx: bool = True
    dns_timeout: int = 3
    disposable_domains: Set[str] = None

    # RFC 5322 compliant regex (simplified but robust)
    EMAIL_REGEX = re.compile(
        r'^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@'
        r'[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?'
        r'(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'
    )

    def __post_init__(self):
        """Initialize disposable domains list."""
        if self.disposable_domains is None:
            self.disposable_domains = {
                'tempmail.com',
                'guerrillamail.com',
                '10minutemail.com',
                'throwaway.email',
                'mailinator.com',
                'trashmail.com',
            }

    def validate(self, email: str) -> bool:
        """
        Validate an email address.

        Args:
            email (str): Email address to validate

        Returns:
            bool: True if email is valid

        Raises:
            InvalidEmailFormatError: If email format is invalid
            DisposableEmailError: If email is from a disposable service
            InvalidDomainError: If domain has no MX records

        Example:
            >>> validator = EmailValidator()
            >>> validator.validate("user@gmail.com")
            True
        """
        # Normalize email
        email = email.strip().lower()

        # Check format
        if not self._validate_format(email):
            raise InvalidEmailFormatError(
                f"Invalid email format: {email}"
            )

        # Extract domain
        domain = email.split('@')[1]

        # Check for disposable domains
        if domain in self.disposable_domains:
            raise DisposableEmailError(
                f"Disposable email domain not allowed: {domain}"
            )

        # Check MX records
        if self.check_mx and not self._has_mx_record(domain):
            raise InvalidDomainError(
                f"Domain has no valid MX records: {domain}"
            )

        return True

    def _validate_format(self, email: str) -> bool:
        """
        Validate email format against RFC 5322.

        Args:
            email (str): Email to validate

        Returns:
            bool: True if format is valid
        """
        if len(email) > 254:  # RFC 5321 max length
            return False

        if not self.EMAIL_REGEX.match(email):
            return False

        # Check local part length (before @)
        local_part = email.split('@')[0]
        if len(local_part) > 64:  # RFC 5321 max local part
            return False

        return True

    def _has_mx_record(self, domain: str) -> bool:
        """
        Check if domain has valid MX records.

        Args:
            domain (str): Domain to check

        Returns:
            bool: True if domain has MX records
        """
        try:
            dns.resolver.resolve(domain, 'MX', lifetime=self.dns_timeout)
            return True
        except (
            dns.resolver.NXDOMAIN,
            dns.resolver.NoAnswer,
            dns.resolver.Timeout,
            dns.exception.DNSException
        ):
            return False
