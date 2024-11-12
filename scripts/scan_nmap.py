import os

def run_nmap(target):
    # Remove 'http://' or 'https://' prefixes, if present, and trailing slash
    target = target.replace('http://', '').replace('https://', '').rstrip('/')

    # Create a safe filename by replacing characters that are invalid in filenames
    safe_target = target.replace(':', '_').replace('/', '_')

    # Update the file path to the correct location
    output_file = f"/home/rajeev/User_rajeev/AAU/AVDEF/scans/nmap/{safe_target}_nmap.txt"
    
    # Run the Nmap scan using os.system
    os.system(f"nmap -sV --script vuln {target} -oN {output_file}")
    print(f"Nmap scan completed. Results saved in {output_file}")

if __name__ == "__main__":
    # Replace this with your desired target URL or IP
    target = "http://testhtml5.vulnweb.com"  # Example URL
    run_nmap(target)