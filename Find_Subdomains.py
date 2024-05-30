import os
import sys
import subprocess

def get_subdomains(domain):
    subdomains = set()
    try:
        output = subprocess.check_output(['amass', 'enum', '-d', domain, '-o', 'output.txt'])
        with open('output.txt', 'r') as file:
            lines = file.readlines()
        for line in lines:
            subdomains.add(line.strip())
    except:
        pass

    return subdomains

domain = input("Enter the domain name: ")
subdomains = get_subdomains(domain)

print("Subdomains:")
for subdomain in subdomains:
    print("- " + subdomain)
