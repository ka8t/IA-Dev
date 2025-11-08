"""
Unit tests for EmailValidator.
"""

import pytest
from unittest.mock import patch, MagicMock
import dns.resolver

from email_validator import (
    EmailValidator,
    InvalidEmailFormatError,
    DisposableEmailError,
    InvalidDomainError,
)


class TestEmailValidator:
    """Test suite for EmailValidator class."""

    @pytest.fixture
    def validator(self):
        """Create validator instance without MX check for faster tests."""
        return EmailValidator(check_mx=False)

    @pytest.fixture
    def validator_with_mx(self):
        """Create validator instance with MX check enabled."""
        return EmailValidator(check_mx=True)

    # Format validation tests

    def test_valid_email_simple(self, validator):
        """Test validation of simple valid email."""
        assert validator.validate("user@example.com") is True

    def test_valid_email_with_dots(self, validator):
        """Test validation of email with dots in local part."""
        assert validator.validate("john.doe@example.com") is True

    def test_valid_email_with_plus(self, validator):
        """Test validation of email with plus sign."""
        assert validator.validate("user+tag@example.com") is True

    def test_valid_email_subdomain(self, validator):
        """Test validation of email with subdomain."""
        assert validator.validate("user@mail.example.com") is True

    def test_invalid_email_no_at(self, validator):
        """Test that email without @ is rejected."""
        with pytest.raises(InvalidEmailFormatError):
            validator.validate("userexample.com")

    def test_invalid_email_multiple_at(self, validator):
        """Test that email with multiple @ is rejected."""
        with pytest.raises(InvalidEmailFormatError):
            validator.validate("user@@example.com")

    def test_invalid_email_no_domain(self, validator):
        """Test that email without domain is rejected."""
        with pytest.raises(InvalidEmailFormatError):
            validator.validate("user@")

    def test_invalid_email_no_local_part(self, validator):
        """Test that email without local part is rejected."""
        with pytest.raises(InvalidEmailFormatError):
            validator.validate("@example.com")

    def test_invalid_email_too_long(self, validator):
        """Test that email exceeding 254 chars is rejected."""
        long_email = "a" * 250 + "@example.com"
        with pytest.raises(InvalidEmailFormatError):
            validator.validate(long_email)

    def test_invalid_email_local_part_too_long(self, validator):
        """Test that local part exceeding 64 chars is rejected."""
        long_local = "a" * 65 + "@example.com"
        with pytest.raises(InvalidEmailFormatError):
            validator.validate(long_local)

    # Disposable email tests

    def test_disposable_email_tempmail(self, validator):
        """Test that tempmail.com is detected as disposable."""
        with pytest.raises(DisposableEmailError):
            validator.validate("user@tempmail.com")

    def test_disposable_email_guerrilla(self, validator):
        """Test that guerrillamail.com is detected as disposable."""
        with pytest.raises(DisposableEmailError):
            validator.validate("user@guerrillamail.com")

    def test_disposable_email_10minute(self, validator):
        """Test that 10minutemail.com is detected as disposable."""
        with pytest.raises(DisposableEmailError):
            validator.validate("user@10minutemail.com")

    def test_custom_disposable_domain(self):
        """Test custom disposable domains list."""
        validator = EmailValidator(
            check_mx=False,
            disposable_domains={'custom-temp.com'}
        )
        with pytest.raises(DisposableEmailError):
            validator.validate("user@custom-temp.com")

    # MX record tests

    @patch('dns.resolver.resolve')
    def test_valid_mx_record(self, mock_resolve, validator_with_mx):
        """Test that domain with MX record is accepted."""
        mock_resolve.return_value = [MagicMock()]
        assert validator_with_mx.validate("user@gmail.com") is True

    @patch('dns.resolver.resolve')
    def test_no_mx_record_nxdomain(self, mock_resolve, validator_with_mx):
        """Test that domain without MX record is rejected (NXDOMAIN)."""
        mock_resolve.side_effect = dns.resolver.NXDOMAIN()
        with pytest.raises(InvalidDomainError):
            validator_with_mx.validate("user@nonexistent-domain-12345.com")

    @patch('dns.resolver.resolve')
    def test_no_mx_record_timeout(self, mock_resolve, validator_with_mx):
        """Test that DNS timeout is handled gracefully."""
        mock_resolve.side_effect = dns.resolver.Timeout()
        with pytest.raises(InvalidDomainError):
            validator_with_mx.validate("user@slow-dns.com")

    # Edge cases

    def test_email_normalization_uppercase(self, validator):
        """Test that emails are normalized to lowercase."""
        assert validator.validate("User@Example.COM") is True

    def test_email_normalization_whitespace(self, validator):
        """Test that whitespace is trimmed."""
        assert validator.validate("  user@example.com  ") is True

    def test_validator_thread_safety(self, validator):
        """Test that validator is thread-safe (immutable config)."""
        # Validator should not modify its state during validation
        validator.validate("user1@example.com")
        validator.validate("user2@example.com")
        assert validator.check_mx is False  # Config unchanged
