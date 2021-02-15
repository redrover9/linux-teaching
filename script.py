from subprocess import *
try: 
	server1_status = check_output(["ping", "-c", "3", "server1.example.com"])
except CalledProcessError as server1_error:
	print(server1_error)
try: 
	server2_status = check_output(["ping", "-c", "3", "server2.example.com"])
except CalledProcessError as server2_error:
	print(server2_error)
try: 
	server3_status = check_output(["ping", "-c", "3", "server3.example.com"])
except CalledProcessError as server3_error:
	print(server3_error)
try: 
	wkstn1_status = check_output(["ping", "-c", "3", "wkstn1.example.com"])
except CalledProcessError as wkstn1_error:
	print(wkstn1_error)
