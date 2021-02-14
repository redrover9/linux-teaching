from subprocess import *
server1_status = check_output(["ping", "server1.example.com"])
server2_status = check_output(["ping", "server2.example.com"])
server3_status = check_output(["ping", "server3.example.com"])
wkstn1_status = check_output(["ping", "wkstn1.example.com"])