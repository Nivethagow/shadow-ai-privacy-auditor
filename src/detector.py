import re


class PrivacyDetector:

    def __init__(self):

        self.patterns = [

            {
                "regex": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
                "label": "EMAIL",
                "category": "Names & Contact Information",
                "risk": "Medium",
                "confidence": 0.95,
                "explanation": "Email addresses can reveal personal contact details."
            },

            {
                "regex": r"\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b",
                "label": "PHONE",
                "category": "Names & Contact Information",
                "risk": "Medium",
                "confidence": 0.90,
                "explanation": "Phone numbers are personally identifiable information."
            },

            {
                "regex": r"\b\d{3}-\d{2}-\d{4}\b",
                "label": "SSN",
                "category": "Government Identifier",
                "risk": "High",
                "confidence": 0.98,
                "explanation": "Social Security Numbers are sensitive government identifiers."
            },

            {
                "regex": r"\b(?:\d{4}[- ]?){3}\d{4}\b",
                "label": "CREDIT_CARD",
                "category": "Financial Identifier",
                "risk": "High",
                "confidence": 0.97,
                "explanation": "Financial identifiers should not be shared publicly."
            },

            {
                "regex": r"(?i)(password|passwd|pwd)\s*[:=]\s*[^\s.,!?]+",
                "label": "PASSWORD",
                "category": "Credentials",
                "risk": "Critical",
                "confidence": 0.96,
                "explanation": "Passwords can allow unauthorized account access."
            },

            {
                "regex": r"\bsk-[A-Za-z0-9]{10,}\b",
                "label": "API_KEY",
                "category": "Credentials",
                "risk": "Critical",
                "confidence": 0.98,
                "explanation": "API keys can provide access to external services."
            },
            {
                "regex": r"\bEMP[-_]\d{3,6}\b",
                "label": "EMPLOYEE_ID",
                "category": "Employee Information",
                "risk": "Medium",
                "confidence": 0.90,
                "explanation": "Employee identifiers may expose internal organizational information."
            }

        ]


        self.keyword_rules = {

            "Medical Information": {

                "keywords": [
                    "diabetes",
                    "cancer",
                    "copd",
                    "hypertension",
                    "diagnosis",
                    "medical record",
                    "prescription",
                    "medication",
                    "blood pressure"
                ],

                "risk": "High",
                "confidence": 0.85
            },


            "Confidential Organization Information": {

                "keywords": [
                    "internal use only",
                    "private document",
                    "confidential report",
                    "financial report",
                    "secret project"
                ],

                "risk": "High",
                "confidence": 0.85
            },


            "Employee Information": {

                "keywords": [
                    "staff id",
                    "employee number",
                    "volunteer id"
                ],

                "risk": "Medium",
                "confidence": 0.80
            }

        }



    def detect(self, text):

        findings = []
        seen = set()


        # Regex based detection

        for item in self.patterns:

            for match in re.finditer(item["regex"], text):

                key = (match.group(), item["label"])

                if key not in seen:

                    findings.append({

                        "text": match.group(),
                        "label": item["label"],
                        "category": item["category"],
                        "risk": item["risk"],
                        "confidence": item["confidence"],
                        "explanation": item["explanation"],
                        "start": match.start(),
                        "end": match.end()

                    })

                    seen.add(key)



        # Simple name detection

        name_pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

        for match in re.finditer(name_pattern, text):

            name = match.group()

            if name.lower() not in [
                "Social Security",
                "Financial Report"
            ]:

                key = (name, "NAME")

                if key not in seen:

                    findings.append({

                        "text": name,
                        "label": "NAME",
                        "category": "Names & Contact Information",
                        "risk": "Medium",
                        "confidence": 0.75,
                        "explanation": "Personal names may identify individuals.",
                        "start": match.start(),
                        "end": match.end()

                    })

                    seen.add(key)



        # Keyword detection

        lower_text = text.lower()


        for category, rule in self.keyword_rules.items():

            for keyword in rule["keywords"]:

                start = lower_text.find(keyword)

                if start != -1:

                    key = (keyword, category)

                    if key not in seen:

                        findings.append({

                            "text": text[start:start+len(keyword)],
                            "label": category.upper().replace(" ", "_"),
                            "category": category,
                            "risk": rule["risk"],
                            "confidence": rule["confidence"],
                            "explanation":
                                f"Detected sensitive {category.lower()} that may require protection.",
                            "start": start,
                            "end": start + len(keyword)

                        })

                        seen.add(key)



        return findings
