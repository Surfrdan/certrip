#!/usr/bin/env python3
import sys
from socket import socket
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import socket
import ssl

host = sys.argv[1]
port = 443

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
try:
    with socket.create_connection((host, port)) as sock:
        sock.settimeout(0.5)
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            pem_data = ssl.DER_cert_to_PEM_cert(ssock.getpeercert(True))
            cert = x509.load_pem_x509_certificate(str.encode(pem_data), default_backend())
            san = cert.extensions.get_extension_for_oid(x509.oid.ExtensionOID.SUBJECT_ALTERNATIVE_NAME)
            for dns_name in san.value:
                print (dns_name.value)
except ssl.SSLError:
    pass
except socket.timeout:
    pass
