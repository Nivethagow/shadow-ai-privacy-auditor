# Shadow AI Privacy Auditor - Test Cases

## Overview

This document contains fictional test cases used to validate the Shadow AI Privacy Auditor detection and redaction capabilities.

All test data is synthetic and created only for testing purposes.

The tests verify:
- Sensitive information detection accuracy
- Correct category classification
- Risk identification
- Safe redaction
- Avoidance of unnecessary redaction

---

## Test Case 1: Email Detection

### Input

Contact Adrian Clara at adrian.clara@example.com regarding the project.


### Expected Detection

- EMAIL

### Expected Result

The email address should be detected and replaced with:

[EMAIL]

---

## Test Case 2: Phone Number Detection

### Input

Call Adrian at 555-123-4567 for project updates.

### Expected Detection

- PHONE

### Expected Result

The phone number should be detected and redacted.

---

## Test Case 3: Social Security Number Detection

### Input

The employee SSN is 123-45-6789.


### Expected Detection

- SSN

### Expected Result

The SSN should be classified as a high-risk government identifier and replaced with:

[SSN]


---

## Test Case 4: Password Detection

### Input

Password = TestPassword123

### Expected Detection

- PASSWORD

### Expected Result

The password should be detected as a critical credential risk and replaced with:

[PASSWORD]

---

## Test Case 5: API Key Detection

### Input

API key: sk-test123456789

### Expected Detection

- API_KEY

### Expected Result

The API credential should be detected as a critical risk and redacted.

---

## Test Case 6: Employee Information Detection

### Input

Employee ID: EMP-45892

### Expected Detection

- EMPLOYEE_ID

### Expected Result

The employee identifier should be detected as internal employee information and replaced with:

[EMPLOYEE_ID]

---

## Test Case 7: Medical Information Detection

### Input

Patient record indicates diabetes and blood pressure concerns.


### Expected Detection

- MEDICAL_INFORMATION

### Expected Result

Medical information should be detected as sensitive personal information and redacted.

---

## Test Case 8: Confidential Organization Information Detection

### Input

This confidential financial report contains internal project details.

### Expected Detection

- CONFIDENTIAL_ORGANIZATION_INFORMATION

### Expected Result

Confidential organizational information should be identified and replaced with an appropriate placeholder.

---

## Test Case 9: Multiple Sensitive Information Detection

### Input

Adrian Clara email is adrian.clara@example.com.
Password = TestPassword123.
Employee ID: EMP-45892.


### Expected Detection

- NAME
- EMAIL
- PASSWORD
- EMPLOYEE_ID

### Expected Result

Multiple sensitive items should be detected and replaced with appropriate placeholders.

---

## Test Case 10: Safe Text Validation

### Input

The project meeting is scheduled for 3:00 PM tomorrow.


### Expected Detection

None

### Expected Result

The text should remain unchanged.

This validates that the system does not over-redact normal business communication.

---

# Test Coverage Summary

| Sensitive Category | Covered |
|---|---|
| Names and Contact Information | Yes |
| Government Identifiers | Yes |
| Financial Identifiers | Yes |
| Passwords and API Credentials | Yes |
| Medical Information | Yes |
| Employee Information | Yes |
| Confidential Organization Information | Yes |
| Safe Text Handling | Yes |

