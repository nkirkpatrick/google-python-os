#!/usr/bin/env python3
import requests
import socket
def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return True

def check_connectivity():
    status_code = requests.get("http://www.google.com")
    return True
