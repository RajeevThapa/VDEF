import os
import subprocess

def run_nikto_scan(target_ip):
    # Remove 'http://' or 'https://' prefixes and trailing slash, if present
    target_ip = target_ip.replace('http://', '').replace('https://', '').rstrip('/')

    # Create a safe filename by replacing characters that are invalid in filenames
    safe_target_ip = target_ip.replace(':', '_').replace('/', '_')

    # Construct the output file path
    output_file = f"/home/rajeev/User_rajeev/AAU/AVDEF/scans/nikto/{safe_target_ip}_nikto.txt"

    # Run the Nikto scan using subprocess for better control and error handling
    try:
        # Construct the command to run Nikto
        # command = f"nikto -h {target_ip} -output {output_file}"
        # -Tuning 1 will limit the scan to basic HTTP methods and server identification tests
        command = f"nikto -h {target_ip} -Tuning 1 -output {output_file}"

        # Run the command and capture the output (if any)
        subprocess.run(command, shell=True, check=True)
        
        print(f"Nikto scan completed. Results saved in {output_file}")
    
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running Nikto scan: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    target_ip = "http://testhtml5.vulnweb.com/"  # Ensure it's a URL or IP address
    run_nikto_scan(target_ip)