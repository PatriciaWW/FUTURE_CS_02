import re
import sys
from email import policy
from email.utils import parseaddr
from email.parser import BytesParser

def defang(url: str) -> str:
    return url.replace("http", "hxxp").replace(".", "[.]")

path = sys.argv[1]
with open(path, "rb") as f:
    msg = BytesParser(policy=policy.default).parse(f)

print("=== KEY HEADERS ===")
for h in ["From", "Reply-To", "Return-Path", "To", "Subject", "Date"]:
    print(f"{h}: {msg[h]}")
    
print("\n=== AUTHENTICATION ===")
for h in ["Authentication-Results", "Received-SPF", "DKIM-Signature"]:
    for value in msg.get_all(h, []):
        print(f"{h}: {str(value)[:200]}")

print("\n=== RECEIVED CHAIN (top = last hop, bottom = origin) ===")
for i, r in enumerate(msg.get_all("Received", []), 1):
    print(f"{i}. {' '.join(str(r).split())[:160]}")

print("\n=== LINKS FOUND (defanged, NOT visited) ===")
body = msg.get_body(preferencelist=("html", "plain"))
text = body.get_content() if body else ""
for url in sorted(set(re.findall(r'https?://[^\s"\'<>]+', text))):
    print(defang(url))



print("\n=== ATTACHMENTS (names only, NOT opened) ===")
for part in msg.iter_attachments():
    print(part.get_filename())