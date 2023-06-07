import smtplib
import logging
from email.mime.text import MIMEText
import sys

# Mengatur level debug
logging.basicConfig(level=logging.DEBUG, filename='debug.log', filemode='w')

org_std = sys.stdout, sys.stderr
sys.stdout = sys.stderr = open('debug.log', 'w')

logger = logging.getLogger('smtplib')
logger.addHandler(logging.FileHandler('debug.log'))

# Mengatur koneksi SMTP ke server Office 365
smtp_server = 'smtp.office365.com'
smtp_port = 587
username = '...'
password = '...'

# Membuat objek koneksi SMTP
server = smtplib.SMTP(smtp_server, smtp_port)
server.set_debuglevel(1)

try:
    # Melakukan koneksi ke server dan mengaktifkan TLS
    server.starttls()

    # Login menggunakan username dan password
    server.login(username, password)

    # Membuat email
    sender = '...'
    recipient = '...'
    subject = 'Contoh Email dari Outlook ke Gmail'
    body = 'Halo, ini adalah contoh email yang dikirimkan melalui SMTP server Office 365.'
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipient

    # Menyimpan informasi email yang dikirim ke dalam log
    # log_info = f'Sender: {sender}\nRecipient: {recipient}\nSubject: {subject}\nBody: {body}'
    # logging.info(log_info)

    # Mengirimkan email
    server.sendmail(sender, recipient, message.as_string())
    print('Email berhasil dikirim!')

except Exception as e:
    print('Email gagal dikirim. Kesalahan:', str(e))

finally:
    # Menutup koneksi SMTP
    server.quit()

sys.stdout, sys.stderr = org_std

# Membaca file log/debug
with open('debug.log', 'r') as log_file:
    smtp_log = log_file.readlines()

# 1. Cetak pesan EHLO
def print_ehlo_message(smtp_log):
    for step in smtp_log:
        if 'send:' in step and 'ehlo' in step:
            ehlo_message = step.strip()
            print(ehlo_message)
            break

# 2. Cetak pesan dukungan TLS
def print_tls_support_message(smtp_log):
    for step in smtp_log:
        if 'reply:' in step and '250-STARTTLS' in step:
            tls_support_message = step.strip()
            print(tls_support_message)
            break

# 3. Cetak pesan server siap mengirim email
def print_server_ready_message(smtp_log):
    for step in smtp_log:
        if 'retcode (220); Msg: b\'2.0.0' in step:
            server_ready_message = step.strip()
            print(server_ready_message)
            break

# 4. Cetak pesan username yang sudah di-hash
def print_auth_login_message(smtp_log):
    for step in smtp_log:
        if 'send:' in step and 'AUTH LOGIN' in step:
            auth_login_message = step.strip()
            print(auth_login_message)
            break

# 5. Cetak pesan balasan server dari hello message
def print_hello_response_message(smtp_log):
    for step in smtp_log:
        if 'reply: b\'250-' in step and 'Hello' in step:
            hello_response_message = step.strip()
            print(hello_response_message)
            break

# 6. Cetak pesan koneksi ditutup
def print_connection_closed_message(smtp_log):
    for step in smtp_log:
        if 'reply: b\'221' in step and 'Service closing transmission channel' in step:
            connection_closed_message = step.strip()
            print(connection_closed_message)
            break

# Memanggil fungsi-fungsi untuk menjawab soal-soal
print_ehlo_message(smtp_log)
print_tls_support_message(smtp_log)
print_server_ready_message(smtp_log)
print_auth_login_message(smtp_log)
print_hello_response_message(smtp_log)
print_connection_closed_message(smtp_log)
