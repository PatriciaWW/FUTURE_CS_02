# Sample 2: A Fake Account Security alert that impersonates Microsoft Security Team

**Source:** [phishing_pot sample-10.eml](https://github.com/rf-peixoto/phishing_pot/blob/main/email/sample-10.eml)
**Analyzed:** 2026-10-01
**Classification:** Phishing

---

## 1. Overview
*KEY HEADERS*
**From:** "Microsoft account team", _ <no-reply@access-accsecurity.com>
**Reply-To:** sotrecognizd@gmail.com
**Return-Path:** bounce@thcultarfdes.co.uk
**To:** phishing@pot
**Subject:** Microsoft account unusual signin activity
**Date:** Fri, 08 Sep 2023 05:47:04 +0000

*AUTHENTICATION*
**Authentication-Results:** spf=none (sender IP is 89.144.44.2) smtp.mailfrom=thcultarfdes.co.uk; dkim=none (message not signed) header.d=none;dmarc=permerror action=none header.from=access-accsecurity.com;
Received-SPF: None (protection.outlook.com: thcultarfdes.co.uk does not designate permitted sender hosts)

## 2. Header Analysis
| Check | Result | Interpretation |
|---|---|---|
| SPF | none | No SPF record was published for the envelope sender domain, so the sending server's authorization couldn't be verified |
| DKIM | none | No signature present hence suspicious. Established senders such as Microsoft sign their mail, so absence is unexpected, though not proof on its own.  |
| DMARC | permerror |Inconclusive since there was a permanent error thus the evaluation couldn't be completed |
| Origin IP | 89.144.44.2 | WHOIS shows that 89.144.44.0/24 was registered in February 2026 to MSCode (Poland). Because this allocation post-dates the email (sent 2023), the current registration cannot be used to attribute the original sending infrastructure, and this indicator was treated as inconclusive.The classification relies on the sender domains, authentication results, and message content.|


## 3. Links and Domains
| Defanged item | Finding |
|---|---|
| hxxp://thebandalisty[.]com/track/o43062rdzGz18708448Gdrw1821750fYo33632dSjh176 | unrelated to the sender's domain |


## 4. Indicators
**Brand Impersonation:** Display name "Microsoft account team" with a non-Microsoft sending domain.

**Suspicious sender domain:** access-accsecurity.com: security-themed wording, not a Microsoft domain (WHOIS to confirm). The Reply-to and Return-Path also have domains not affiliated to Microsoft.

**Mismatched From, Reply-to and Return-path:** They all differ

**No sender authentication:** SPF none, DKIM none, DMARC permerror

**Fear-based subject:** "Microsoft account unusual signin activity" plays on account-compromise anxiety

**Suspicious Link:** The link's domain is not related to any of the domains and also not one from Microsoft

## 5. Verdict
**Phishing.** The email presents itself as "Microsoft account team" but
is sent from `access-accsecurity.com`, a domain I could not associate with
Microsoft, with a different bounce domain (`thcultarfdes.co.uk`), a Gmail
Reply-To, and a link to a fourth unrelated domain (`thebandalisty[.]com`).
No sender authentication was present (SPF none, DKIM none, DMARC
permerror), so nothing verified the sender's identity. Together with the
fear-based subject line, these independent indicators point to a
credential-harvesting attempt impersonating Microsoft.


## 6. How the attack works
The sender sends a message that looks like a Microsoft Security alert saying someone signed in to the receiver's account from an unusual place. The goal is to alarm the receiver into clicking the link, which leads to a fake sign-in page. Anything entered there goes to the attacker, who can then take over the account. The link, sender address, and reply address all belong to unrelated parties, not Microsoft.


## 7. What users should do
1. Don't click links in unexpected "unusual sign-in" alerts. Open Microsoft's site by typing the address yourself and review your sign-in activity there.
2. Check the sender's actual address, not just the display name.
3. Treat a Gmail reply address on a "corporate" security notice as a warning sign.
4. Report it to IT or security, then delete it.
5. If you did enter credentials, change the password immediately and enable multi-factor authentication.