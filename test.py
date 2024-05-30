import os
import sys
import subprocess
import socket

def get_subdomains(domain):
    subdomains = set()
    try:
        output = subprocess.check_output(['amass', 'enum', '-d', domain, '-o', 'output1.txt'])
        with open('output.txt', 'r') as file:
            lines = file.readlines()
        for line in lines:
            subdomains.add(line.strip())
    except:
        pass

    return subdomains

def get_subdomain_ips(subdomains):
    ips = {}
    for subdomain in subdomains:
        try:
            ip = socket.gethostbyname(subdomain)
            ips[subdomain] = ip
        except:
            pass

    return ips

def check_ip_status(ip):
    status = ""
    try:
        response = os.system("ping -c 1 " + ip)
        if response == 0:
            status = "Active"
        else:
            status = "Inactive"
    except:
        status = "Unknown"

    return status

domain = input("Enter the domain name: ")
subdomains = get_subdomains(domain)
ips = get_subdomain_ips(subdomains)

results = []

for subdomain, ip in ips.items():
    status = check_ip_status(ip)
    results.append((subdomain, ip, status))

print("{:<30} {:<20} {:<10}".format("Subdomain", "IP Address", "Status"))
for result in results:
    print("{:<30} {:<20} {:<10}".format(result[0], result[1], result[2]))
