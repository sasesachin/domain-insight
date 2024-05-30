#programe to find subdomains, ip address, ASN details and status
import dns.resolver
from ipwhois import IPWhois
import subprocess

def load_subdomains(wordlist_file):
    with open(wordlist_file) as f:
        subdomains = [line.strip() for line in f.readlines()]
    return subdomains


def resolve_subdomain(subdomain, target_domain):
    try:
        answers = dns.resolver.resolve(subdomain + "." + target_domain)
        return answers
    except (dns.resolver.NoNameservers, dns.resolver.NXDOMAIN, dns.resolver.LifetimeTimeout):
        return []


def get_ipwhois_result(ip_address):
    ipwhois_result = IPWhois(ip_address).lookup_rdap()
    return ipwhois_result


def check_ping(ip_address):
    ping_response = subprocess.call(['ping', '-c', '1', '-w', '1', ip_address])
    return ping_response == 0


def main():
    target_domain = "domain_name"
    wordlist_file = "subdomains.txt"

    subdomains = load_subdomains(wordlist_file)

    for subdomain in subdomains:
        answers = resolve_subdomain(subdomain, target_domain)
        for rdata in answers:
            ip_address = rdata.address
            ipwhois_result = get_ipwhois_result(ip_address)
            is_active = check_ping(ip_address)
            
            print(f"Subdomain: {subdomain}.{target_domain}")
            print(f"IP Address: {ip_address}")
            print(f"ASN: {ipwhois_result['asn']}")
            print(f"ASN Description: {ipwhois_result.get('asn_description')}")
            print(f"Is Active: {'Yes' if is_active else 'No'}")
            print("="*50)

if __name__ == '__main__':
    main()
