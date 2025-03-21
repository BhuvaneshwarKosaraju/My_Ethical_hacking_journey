import whois

def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        print("\n🔍 Domain Information")
        print("---------------------")
        print(f"Domain: {w.domain_name}")
        print(f"Registrar: {w.registrar}")
        print(f"Creation Date: {w.creation_date}")
        print(f"Expiration Date: {w.expiration_date}")
        print(f"Name Servers: {w.name_servers}")
        print(f"Status: {w.status}")
    except Exception as e:
        print("Error:", e)

# Example usage
if __name__ == "__main__":
    domain = input("Enter domain to lookup: ")
    whois_lookup(domain)
