from requests import Session

TARGET_IP = "IP_ADDRESS"
TARGET = f"http://{TARGET_IP}/bWAPP"
USERNAME = "bee"
PASSWORD = "bug"
SECURITY_LEVEL = 0

def login(verbose = False):
    auth_session = Session()
    
    auth_data = {
        "login": USERNAME,
        "password": PASSWORD,
        "security_level": SECURITY_LEVEL,
        "form": "submit"
    }

    try:
        if verbose:
            print(f"[+] Login to bWAPP using {USERNAME}:{PASSWORD} ...")
        
        auth_session.post(f"{TARGET}/login.php", data=auth_data, allow_redirects=True)

        if verbose:
            print(f"[+] Login completed succesfully!")

        return auth_session
    except Exception as error:
        if verbose:
            print(f"[-] Error while login to bWAPP ...")
        print(error)
