#!/usr/bin/env python3
import argparse
import ipaddress

def validate_ip(ip_address):
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        print("Invalid IP address")
        return False

def validate_port(port):
    try:
        int_port = int(port)
        if int_port >= 1 and int_port <= 65535:
            return True
        else:
            raise ValueError
    except ValueError:
        print("Invalid port number")

    return False

def validate_args(args):
    if validate_ip(args.ip_address) and validate_port(args.port):
        if args.verbose:
            print("Valid input")
        return True
    else:
        return False
            

def main():
    parser = argparse.ArgumentParser(
        prog='shellgen',
        description='generates a php reverse shell',
        epilog='there are no more arguments'
    )
    parser.add_argument(
        "-a", "--ip-address",
        required=True,
        help="IP address to forward packets to"
    )
    parser.add_argument(
        "-p", "--port",
        required=True,
        help="Port number for packets to be forwarded to"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose mode"
    )
    args = parser.parse_args()
    #print(args)
    validate_args(args)
    

if __name__ == "__main__":
    main()


