from subprocess import *
server1_status = check_output(["ping", "-c", "3 ", "server1.example.com"])
server2_status = check_output(["ping", "-c", "3 ", "server2.example.com"])
server3_status = check_output(["ping", "-c", "3 ", "server3.example.com"])
wkstn1_status = check_output(["ping", "-c", "3 ", "wkstn1.example.com"])