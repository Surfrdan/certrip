import sys
from socket import socket
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import socket
import ssl

def certrip(host, port):
    host = host.rstrip()
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    try:
        with socket.create_connection((host, port), timeout=0.3) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                pem_data = ssl.DER_cert_to_PEM_cert(ssock.getpeercert(True))
                cert = x509.load_pem_x509_certificate(str.encode(pem_data), default_backend())
                san = cert.extensions.get_extension_for_oid(x509.oid.ExtensionOID.SUBJECT_ALTERNATIVE_NAME)
                dns_names = []
                for dns_name in san.value:
                    dns_names.append(dns_name.value)
                sock.close()
                return dns_names
    except ssl.SSLError:
        sys.exit()
        pass
    except socket.timeout:
        sys.exit()
        pass
    except TimeoutError:
        sys.exit()
        pass
    except socket.gaierror:
        sys.exit()
        pass
    except ConnectionRefusedError:
        sys.exit()
        pass
    except OSError:
        sys.exit()
        pass
