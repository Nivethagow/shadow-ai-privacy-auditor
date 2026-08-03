# Planning Document

> Complete this document **before writing any code**. This is part of the evaluation.
> Your intent here will be compared against what you actually built in `docs/architecture.md`.

---

## Tech Stack

**Framework / Language:**

Python with Streamlit

> Why did you choose this stack?

Python provides strong support for text processing, regular expressions, and natural language processing libraries. Streamlit enables rapid development of a simple and interactive web application without requiring a separate frontend framework. This allows us to focus on building an accurate privacy detection and redaction workflow within the hackathon timeline.

**Key Libraries:**

Streamlit - Web application interface
spaCy - Named Entity Recognition (NER) for detecting names and organizations
Python re library - Regular expression-based detection for structured sensitive information such as emails, identifiers, and credentials
Pandas - Supporting test case management and detection result analysis

**Detection Approach / AI Provider (if any):**

> Are you using regular expressions, keyword lists, an NLP/NER library, an AI model, or a combination? If you use an AI provider, which one and why?

We will use a hybrid detection approach combining rule-based methods and NLP techniques.
Regular expressions will detect structured sensitive information such as emails, phone numbers, SSNs, API keys, and access credentials.
Keyword-based rules will identify medical, confidential, and organizational information.
spaCy NER will be used to detect person names and organization entities.
No external AI provider will be used for the core detection process because keeping the detection local improves privacy and avoids sending user content to third-party services.

---
## Detection Categories

| Category | Detect? | Planned technique |
|----------|---------|-------------------|
| Names & contact information | Yes | spaCy NER for names; regex patterns for emails and phone numbers |
| Government or financial identifiers | Yes | Regex patterns for SSN, credit card numbers, and account identifiers |
| Passwords, API keys or credentials | Yes | Regex patterns for API keys, passwords, and authentication tokens |
| Medical or sensitive personal information | Yes | Keyword-based detection for medical conditions and health-related terms |
| Employee, client or volunteer information | Yes | Regex and keyword rules for employee IDs and organizational identifiers |
| Confidential organizational or project information | Yes | Keyword detection for internal projects, budgets, confidential files, and business terms |

---

## Phases & Priorities

| Phase | Target Dates | Goals |
|-------|-------------|-------|
| 1 | July 29 - July 30 | Understand requirements, attend orientation, define solution approach, select technology stack, and complete planning |
| 2 | July 31 - August 2 | Build Streamlit application, implement detection logic, create highlighting and redaction workflow, and test functionality |
| 3 | August 3 | Perform final testing, complete documentation, deploy application, and prepare walkthrough submission |

---

## What I'll Cut If Time Is Short

If time is limited, I will prioritize a reliable Tier 1 privacy auditing workflow over advanced features.

The first features I would remove are:
- Browser extension integration
- Real-time monitoring
- Multilingual support
- Advanced machine learning models or custom-trained models

The core functionality that will remain:
- Detection of sensitive information using regex, keyword rules, and NLP-based entity recognition
- Clear explanations of detected risks
- Highlighting of sensitive information before sharing with AI tools
- User-controlled redaction with meaningful labels such as [NAME], [EMAIL], and [API_KEY]
- Validation using fictional test cases to ensure sensitive information is detected while safe text remains unchanged

The priority is to build a dependable privacy checkpoint that prevents accidental exposure of sensitive information before users interact with public AI platforms.

---

## Open Questions / Risks

Potential technical risks identified:

- False positives from pattern-based detection:
  Regex rules may match text that appears sensitive but is actually safe. To reduce this risk, detection rules will be combined with validation logic and tested against both risky and non-sensitive examples.

- Name and entity detection accuracy:
  NLP-based entity recognition may not detect every name format correctly or may identify non-sensitive entities incorrectly. We will combine spaCy NER with rule-based validation to improve reliability.

- Over-redaction:
  Removing too much information can reduce the usefulness of the user's prompt. The system will preserve normal content and only replace information classified as sensitive.

- Detection coverage:
  Sensitive information can appear in many formats. Initial implementation will focus on high-value categories such as names, contact information, credentials, identifiers, medical information, and confidential project details.

- Data privacy:
  All testing examples will be synthetic or fictional. The application will not store user input or send text to external AI services during detection.
