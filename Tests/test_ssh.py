import paramiko

host = '192.168.0.104'
username = 'user'
secret = 'user'
port = 22


def test_ssh():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=username, password=secret, port=port)
    stdin, stdout, stderr = client.exec_command('pwd')
    for item in stdout.readlines():
        assert item == "/home/user\n"
    client.close()
