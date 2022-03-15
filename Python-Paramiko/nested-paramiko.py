import paramiko
import sys
import subprocess
#
# we instantiate a new object referencing paramiko's SSHClient class
#
jumphost = "192.168.1.10"
server = "192.168.1.11"

vm = paramiko.SSHClient()
vm.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vm.connect(jumphost, username='root', password='a')

#
vmtransport = vm.get_transport()
server_addr = (server, 22) #edited#
jump_host = (jumphost, 22) #edited#
vmChannel = neededTransport.open_channel("direct-tcpip", jump_host, server_addr)  # Creates the needed channel to send the connection

jhost = paramiko.SSHClient()
jhost.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#jhost.load_host_keys('/home/osmanl/.ssh/known_hosts') #disabled#
jhost.connect(server, username='root', password='a', sock=vmChannel)

stdin, stdout, stderr = jhost.exec_command("cat /home/server")
#
print(stdout.read().decode()) # Decode byte to string
#
jhost.close()
vm.close()
