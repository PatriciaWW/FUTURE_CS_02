# Sample 2: A Fake Account Security alert that impersonates Microsoft Security Team

# Sample [N]: Bitcoin "transaction" lure with PDF attachment

**Source:** [phishing_pot sample-188.eml](https://github.com/rf-peixoto/phishing_pot/blob/main/email/sample-188.eml)
**Analyzed:** 2026-10-02
**Classification:** Phishing
---

## 1. Overview
*KEY HEADERS*
**From:** Annikki Muckey <dorothyleejux3@gmail.com>
**Reply-To:** None
**Return-Path:** dorothyleejux3@gmail.com
**To / Bcc:** `addedbad@gmail.com` / `phishing@pot`
**Subject:** Bitcoin.Transaction.0.7495.BTC
**Date:** Mon, 26 Dec 2022 00:57:07 -0800

*AUTHENTICATION*
**Authentication-Results:** spf=pass (sender IP is 209.85.128.170) smtp.mailfrom=gmail.com; dkim=pass (signature was verified) header.d=gmail.com;dmarc=pass action=none header.from=gmail.com;compauth=pass reason=100
Received-SPF: Pass (protection.outlook.com: domain of gmail.com designates 209.85.128.170 as permitted sender) receiver=protection.outlook.com; client-ip=209.85.128.170; helo=mail-yw1-f170.google.com; pr=C
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;        d=gmail.com; s=20210112;        h=to:subject:message-id:date:from:mime-version:from:to:cc:subject         :date:message-id:reply-to;        bh=FktiDVpS09qe

*AUTHENTICATION*
**Authentication-Results:** spf=none (sender IP is 89.144.44.2) smtp.mailfrom=thcultarfdes.co.uk; dkim=none (message not signed) header.d=none;dmarc=permerror action=none header.from=access-accsecurity.com;
Received-SPF: None (protection.outlook.com: thcultarfdes.co.uk does not designate permitted sender hosts)

## 2. Header Analysis
| Check | Result | Interpretation |
|---|---|---|
| SPF | `pass` | IP 209.85.128.170 (HELO mail-yw1-f170.google.com) authorized for gmail.com. |
| DKIM | `pass` (`d=gmail.com`) | Signed by Gmail; content unaltered. |
| DMARC | `pass` (`header.from=gmail.com`) | Aligned with the From domain. |
| Origin | Gmail web submission (`with HTTP`) | Sender's own IP not exposed. |

All authentication checks passed because the message was sent from a genuine
Gmail account. This shows the sender's mail provider, not trustworthiness.


## 3. Links and Domains
| Defanged item | Finding |
|---|---|
| GO.Get.Bitcoin.0.7495.BTCwkS9HOxBaj6TeHJUKYMScs24gJigILcOkRvO.pdf | unrelated to the sender's domain |


## 4. Indicators
**Brand Impersonation:** Display name "Microsoft account team" with a non-Microsoft sending domain.

**Suspicious sender domain:** access-accsecurity.com: security-themed wording, not a Microsoft domain (WHOIS to confirm). The Reply-to and Return-Path also have domains not affiliated to Microsoft.

**Mismatched From, Reply-to and Return-path:** They all differ

**No sender authentication:** SPF none, DKIM none, DMARC permerror

**Fear-based subject:** "Microsoft account unusual signin activity" plays on account-compromise anxiety

**Suspicious Link:** The link's domain is not related to any of the domains and also not one from Microsoft

## 5. Verdict
**Phishing (high confidence).** Authentication passed, but an unsolicited
message from a free account with a random address offers a large sum with no
context, adds unrelated filler text to evade filters, and attaches a PDF with a
bait filename whose page is a clickable image linking to a URL shortener,
hiding the destination. Microsoft's filter also scored it as spam (SCL 5) and
routed it to Junk.



## 6. How the attack works
The sender sends a message that looks like a Microsoft Security alert saying someone signed in to the receiver's account from an unusual place. The goal is to alarm the receiver into clicking the link, which leads to a fake sign-in page. Anything entered there goes to the attacker, who can then take over the account. The link, sender address, and reply address all belong to unrelated parties, not Microsoft.


## 7. What users should do
1. Don't click links in unexpected "unusual sign-in" alerts. Open Microsoft's site by typing the address yourself and review your sign-in activity there.
2. Check the sender's actual address, not just the display name.
3. Treat a Gmail reply address on a "corporate" security notice as a warning sign.
4. Report it to IT or security, then delete it.
5. If you did enter credentials, change the password immediately and enable multi-factor authentication.