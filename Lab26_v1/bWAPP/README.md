# bWAPP v2.2

This folder describe how to exploit several vulnerabilities in bWAPP with different security   levels.

***\_\_init\_\_.py*** and ***auth.py*** are used to set local python module to use for login and set target options like **IP_ADDRESS**, **USERNAME** and **PASSWORD** (default: bee/bug), and **SECURITY_LEVEL**

1. Set **TARGET_IP** in **auth.py**
   Change `TARGET_IP = "IP_ADDRESS"` to your desired IP Host
2. Set **SECURITY_LEVEL** in **auth.py**
   By default is set to 0 for low-level security.

### Set PYTHONPATH to load module

As suggestion you should set the PYTHONPATH variable to load correctly the local module used for bWAPP and use login methods and variables defined.

Go to *Lab26_v1* directory and run

```
export PYTHONPATH=$(pwd)
```

### File Upload

All file upload vulnerabilities are described into *file-upload* directory, you can examine scripts to understand how it works.

> ***unrestricted-file-upload-low.py***
>
> Work for low-level security and upload basic web shell in php.
>
> Change MAX_FILE_SIZE to bypass file size check when upload and start an interactive local shell to perform HTTP request after succesfully upload.
