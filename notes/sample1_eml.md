# Sample 1: Fake Bradesco/Livelo "points expiring today" alert

**Source:** [phishing_pot sample-1.eml](https://github.com/rf-peixoto/phishing_pot/blob/main/email/sample-1.eml)
**Analyzed:** 2026-10-01
**Classification:** Phishing

This sample contained non-English content (Portuguese). Text was
translated into English using Claude AI to understand the message.

## 1. Overview
*KEY HEADERS*
**From:** BANCO DO BRADESCO LIVELO <banco.bradesco@atendimento.com.br>
**Reply-To:** None
**Return-Path:** root@ubuntu-s-1vcpu-1gb-35gb-intel-sfo3-06
**To:** phishing@pot
**Subject(original):** CLIENTE PRIME - BRADESCO LIVELO: Seu cartão tem 92.990 pontos LIVELO expirando hoje!
**Subject(translated):** PRIME CLIENT - BRADESCO LIVELO: Your card has 92,990 LIVELO points expiring today!
**Date:** Tue, 19 Sep 2023 18:35:49 +0000

*AUTHENTICATION*
**Authentication-Results:** spf=temperror (sender IP is 137.184.34.4) smtp.mailfrom=ubuntu-s-1vcpu-1gb-35gb-intel-sfo3-06;dkim=none (message not signed) header.d=none;dmarc=temperror action=none header.from=atendimento.com.br;c
**Received-SPF:** TempError (protection.outlook.com: error in processing during lookup of ubuntu-s-1vcpu-1gb-35gb-intel-sfo3-06: DNS Timeout)

* ATTACHMENTS (names only, NOT opened) *
None


## 2. Header Analysis
| Check | Result | Interpretation |
|---|---|---|
| SPF | temperror with IP Unkown | Inconclusive since there was a temporary DNS problem which prevented the check |
| DKIM | none | No signature present hence suspicious since large legitimate organizations almost always sign their mails  |
| DMARC | temperror|Inconclusive since there was a temporary error thus the evaluation couldn't be completed |
| Origin IP | 137.184.34.4 | |


## 3. Links and Domains
| Defanged item | Finding |
|---|---|
| hxxps://blog1seguimentmydomaine2bra[.]me/ | |
| hxxps://fonts[.]googleapis[.]com/css2? | |
| family=Signika:wght@300;500;700&amp;display=swap| |
| hxxps://fonts[.]gstatic[.]com | |


## 4. Indicators
()
**Brand impersonation:**  The display name "BANCO DO BRADESCO LIVELO" and subject "CLIENTE PRIME - BRADESCO LIVELO"
**Sender domain is not the bank's:**  From domain is `atendimento.com.br` (a generic word meaning "customer service"), not Bradesco's own domain (verify against the bank's official site)
**Unconfigured server as sender:** Envelope sender `root@ubuntu-s-1vcpu-1gb-35gb-intel-sfo3-06`
**No sender authentication:** SPF temperror, DKIM none, DMARC temperror
**Urgency** Subject: points "expirando hoje" (expiring today) 
**Reward lure and flattery:** "92.990 pontos" (a large points balance) and "CLIENTE PRIME" (exclusive-customer framing)
**Suspicious link:** Main link goes to unrelated `.me` domain 

## 5. Verdict
**Phishing.** The message presents itself as Bradesco/Livelo but was
sent from `atendimento.com.br`, a domain I could not associate with the bank,
using the envelope sender `root@ubuntu-s-1vcpu-1gb-35gb-intel-sfo3-06`, the
default hostname of a rented server rather than a bank mail system. It
carried no DKIM signature and its SPF and DMARC checks were inconclusive, so
nothing verified the sender. The subject combines urgency ("expiring today")
with a large reward balance, and the main link points to an unrelated domain.
These independent indicators are consistent with a credential or card-data
harvesting attempt.


## 6. How the attack works
The attacker sends a message styled as a bank rewards notice claiming the
reader has a large number of loyalty points about to expire. The urgency
pushes the reader to act without thinking. The link leads away from the
bank to a page controlled by the attacker. Anything entered there goes
to the attacker, who can use it for fraud. The email came from a rented
server, not the bank.

## 7. What users should do
1. Never click a link in an unexpected "your points are expiring" message.
2. Open the bank or rewards site by typing its address or using its
   official app, then check your balance there.
3. Check the sender's actual address and domain, not just the display name.
4. Be suspicious of rewards that expire "today" and of large point balances.
5. Report the email to IT or the bank's official fraud channel, then delete it.
6. If you entered details, contact the bank immediately and change
   passwords.