import ssl
import sys
from datetime import datetime
from argparse import ArgumentParser
from OpenSSL import crypto


class InputArgs():
    host: str
    port: int
    timeout: int


def get_certificate(host, port, timeout) -> str:
    
    # Retrieve the destination SSL certificate public key
    try:
        cert_pem: str  = ssl.get_server_certificate((host, port), timeout=timeout)
    except Exception as e:
        print (f"A certificate at address {host} couldn't be retrieved. {str(e)}")
        sys.exit(1)
    else:
        return cert_pem


def get_certicicate_expiration_date(cert) -> str:
    
    # Decrypt the input public key
    try: 
        cert_x509 = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
    except Exception as e:
        print(f"There was an issue with the retrieved certificate. {str(e)}")
        sys.exit(1)
    else:
        
        # Extract the expiration date, format and return as string
        exp_timestamp: str = cert_x509.get_notAfter().decode("ascii")
        exp_date: datetime = datetime.strptime(exp_timestamp, "%Y%m%d%H%M%SZ")
        return(str(exp_date))
    

def get_arguments() -> InputArgs:
    
    # Define a simple CLI tool frame
    parser: ArgumentParser = ArgumentParser(description="CLI tool to retrieve the SSL certificate's expiration date")
    parser.add_argument("--host", action="store", dest="host", required=True, help="Destination host")
    parser.add_argument("--port", action="store", dest="port", default=443, help="Destination port (default 443)")
    parser.add_argument("--timeout", action="store", dest="timeout", default=10, help="Timeout in seconds (default 10)")
    
    # Return the input parameters
    args: InputArgs = parser.parse_args()
    return(args)


def main():
    
    # Get input arguments from CLI
    args: InputArgs = get_arguments()

    # Remove protocol and any pages in case provided
    try:
        args.host = args.host.split("://")[1]
    except: 
        pass
    try:
        args.host = args.host.split("/")[0]
    except: 
        pass

    # Retrieve the destination SSL certificate
    certificate = get_certificate(args.host, args.port, args.timeout)
    
    # Extract certificate"s expiration date
    result =  get_certicicate_expiration_date(certificate)

    # Print the result to CLI
    print(f"SSL certificate's expiration date of {args.host} is: {result}")

if __name__=="__main__":
    main()