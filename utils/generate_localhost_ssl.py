import subprocess
import os


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def generate_self_signed_certificate(domain, out_dir):
    # Generate a self-signed certificate using OpenSSL
    # Create the folder out_dir and subfolders
    os.makedirs(out_dir, exist_ok=True)

    subprocess.run([
        'openssl', 'req', '-x509', '-nodes', '-newkey', 'rsa:2048',
        '-keyout', os.path.join(out_dir, 'privkey.pem'),
        '-out', os.path.join(out_dir, 'fullchain.pem'),
        '-subj', '/CN={}'.format(domain),
        '-days', '365'
    ], check=True)


if __name__ == "__main__":
    # Set your development domain
    dev_domain = "localhost"

    # Set the output directory for the generated certificate
    output_dir = f'ssl'

    # Generate the self-signed certificate
    generate_self_signed_certificate(dev_domain, output_dir)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
