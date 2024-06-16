# certificate_exp_date_checker
SAP task - Certificate Expiry Date Checker

The purpose of this script is to retrieve the SSL/TLS certificate's expiration date of a provided host address (could be either URL or IP address)
The script parameters should be provided as CLI arguments.

## Prerequisites:

* OpenSSL (tested with v24.1.0)

>How to install:
>```sh
>pip install pyOpenSSL==24.1.0
>```

## Syntax:

```txt
python certificate_exp_date_checker.py --host <target_host> --port <target_port> --timeout <timeout_seconds>
```

### Arguments

#### Mandatory
--host
_Target host. Could be either URL or IP address_

#### Optional
--port
_Target port. If not specified, 443 is taken as default_

--timeout (default: 10 seconds)
_Request timeout. If not specified, 10 seconds is taken as default_

## Examples:

### Input
```sh
python certificate-exp-date-checker.py --host 192.168.0.1
```
### Output
```txt
SSL certificate's expiration date of 192.168.0.1 is: 2025-03-07 23:59:59
```

### Input
```sh
python certificate-exp-date-checker.py --host example.com --port 8443 --timeout 5
```
### Output
```txt
SSL certificate's expiration date of example.com is: 2025-03-07 23:59:59
```
