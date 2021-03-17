import socket
import ssl
import json

domains_url = ["stackoverflow.com", "google.com", "swisscom.ch"]


def ssl_information(hostname: object) -> object:
    context = ssl.create_default_context()
    context.check_hostname = False

    connection = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname, )

    # 5 second timeout
    connection.settimeout(5.0)

    connection.connect((hostname, 443))
    ssl_info = connection.getpeercert()

    # Python subject & issuer objects
    subject = dict(x[0] for x in ssl_info['subject'])
    issued_to = subject['commonName']
    issuer = dict(x[0] for x in ssl_info['issuer'])
    issued_by = issuer['commonName']

    ssl_data = {'subject': subject['commonName'],
                'issuer': issuer['commonName'],
                'start': ssl_info['notBefore'],
                'end': ssl_info['notAfter']
                }

    print(json.dumps(ssl_data))
    ssl.SSLSocket.close(connection)
    return ssl_data


if __name__ == "__main__":
    for value in domains_url:
        try:
            ssl_information(value)

        except Exception as e:
            print(e)
