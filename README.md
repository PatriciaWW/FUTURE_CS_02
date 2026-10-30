# Phishing Email Detection & Awareness Report

Analysis of three real phishing emails, with risk classification and prevention guidance for non-technical employees.

Completed as part of **Future Interns, Cyber Security Task 2 (2026)**.

> **Educational project.** All samples come from public research collections and are used for study only. Nothing here is a live threat: every URL is defanged and no link or attachment was opened.

## Overview

Most successful phishing attacks work because people cannot tell a fake email from a real one, not because systems are weak. This project works like a security analyst's case file: collect samples, examine headers, inspect sender domains and links, identify indicators, classify the risk, and turn the findings into an awareness document businesses can use.

**Headline finding:** one of the three emails passed every authentication check (SPF, DKIM and DMARC) and was still malicious. Authentication shows who sent a message, not whether the sender is trustworthy.

## Results Summary

| # | Email | Lure | Classification | Deciding evidence |
|---|---|---|---|---|
| 1 | Fake Bradesco/Livelo rewards alert (Portuguese) | Points "expiring today" | **Phishing** | Rented-server envelope sender, unrelated sender domain and link |
| 2 | Fake Microsoft account alert | "Unusual sign-in activity" | **Phishing** | Four unrelated domains, no authentication, fear-based subject |
| 3 | Bitcoin "transaction" with PDF attachment | Unsolicited money offer | **Phishing** | Bait attachment, hidden shortened link, filter-evasion text (all authentication passed) |

## Repository Structure

```text
phishing-analysis-project/
├── README.md       # This file
├── report/         # Final report (PDF)
├── notes/          # Per-email analysis notes (Markdown)
├── evidence/       # Screenshots of header, IP and domain lookups
├── samples/        # Defanged excerpts of the analysed emails
└── analyze_eml.py  # Helper script for reading .eml files safely
```

## Tools Used

| Tool | Purpose |
|---|---|
| Google Messageheader, MXToolbox | Reading and checking email headers |
| WHOIS / RDAP, `nslookup` / `dig` | Ownership and registration of IP addresses and domains |
| VirusTotal, URLScan, AbuseIPDB | Reputation lookups (searched, never visited) |
| Python 3 (standard library `email` module) | Extracting headers, links and attachment names without opening anything |
| VS Code and Markdown | Notes and evidence |
| Git and GitHub | Version control and publishing |
| Claude AI | Translating Portuguese content in Email 1 |

## Analysis Approach

Every email went through the same workflow:

1. **Collect** the sample from a public repository (credited below).
2. **Analyse headers:** From, Return-Path, Reply-To, and the SPF, DKIM and DMARC results recorded by the receiving server.
3. **Inspect the sender domain and links:** compare the identity the email claims with the domains it actually uses.
4. **Identify indicators** using a standard checklist (impersonation, mismatched domains, urgency, suspicious links, attachments, authentication results).
5. **Classify the risk** as Safe, Suspicious or Phishing.
6. **Document** the evidence, the interpretation and the limitations.
7. **Write prevention guidance** in plain language.

### Classification criteria

| Level | Meaning | Action |
|---|---|---|
| **Safe** | Consistent with a legitimate message: known sender, matching domains, expected content, no pressure | Handle normally |
| **Suspicious** | Some warning signs, not enough to be sure | Do not click or reply; verify through another channel; report |
| **Phishing** | Several independent indicators of deception | Do not interact; report; delete |

No single indicator decides a classification. Verdicts rest on several independent indicators, and inconclusive results (`none`, `temperror`, `permerror`) are reported as inconclusive, never as proof of forgery.

## Safety Measures

- Links were never visited and attachments were never opened.
- Samples were read as plain text only, never in a mail client.
- All URLs, domains and addresses in this repository are defanged (for example `hxxps://example[.]com`).
- Attachments were inspected as data in memory, not saved or rendered.

## Running the Helper Script

`analyze_eml.py` parses a `.eml` file and prints key headers, authentication results, the Received chain, defanged links and attachment names. It does not open or execute anything.

```bash
python analyze_eml.py path/to/sample.eml
```

It only uses Python's standard library, so there is nothing to install.

## Limitations

- **Dated samples.** The emails are from 2022 and 2023. Registration and reputation data checked in 2026 may differ from what was true at sending time, so it was used as context only.
- **Links and attachments not followed.** Destinations and contents were inferred from structure, not confirmed.
- **Translation.** Email 1 was machine-translated, which may miss nuance. Conclusions rely mainly on headers, domains and links.
- **Sample set.** All three samples are phishing, so the Safe and Suspicious levels were not exercised against real messages.
- **Small sample size.** Three emails show patterns but do not represent all phishing.

## Sources and Credits

Samples are from the public **phishing_pot** collection by rf-peixoto (<https://github.com/rf-peixoto/phishing_pot>): `sample-1.eml`, `sample-10.eml` and `sample-188.eml`. They were used for study only. All analysis and wording in this repository is original.

Other references: Google Messageheader, MXToolbox, and the public repositories listed in the task brief.

## Author

**Patricia Wachira**