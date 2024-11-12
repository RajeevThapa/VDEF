# Passive Scan
import os
import time
import subprocess
import yaml
import requests
from zapv2 import ZAPv2

def start_zap_daemon():
    """Start ZAP in daemon mode with API key disabled."""
    zap_command = "zaproxy -daemon -port 8081 -config api.disablekey=true"
    
    try:
        # Start ZAP as a background process without waiting for stdout/stderr
        process = subprocess.Popen(zap_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        print("Waiting for ZAP to start...")
        time.sleep(20)  # Give ZAP some time to initialize (increase if needed)
        
        # Check if ZAP is running by querying the API endpoint
        zap_url = "http://localhost:8081"
        response = requests.get(zap_url)
        
        if response.status_code == 200:
            print("ZAP started successfully in daemon mode.")
        else:
            print(f"Failed to connect to ZAP daemon. Status code: {response.status_code}")
            process.kill()  # Terminate the process if ZAP did not start
            exit(1)
    
    except Exception as e:
        print(f"Error while starting ZAP daemon: {e}")
        exit(1)

def run_passive_scan():
    """Run a passive scan on the target URL."""
    # Load configuration from YAML file
    with open('/home/rajeev/User_rajeev/AAU/AVDEF/configs/zap_config.yaml') as config_file:
        config = yaml.safe_load(config_file)

    # Get the target URL and output directory from the config
    target_url = config["target_url"]
    output_dir = config["output_dir"]

    # Make sure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Sanitize the target URL to create a valid filename
    safe_target_url = target_url.replace('http://', '').replace('https://', '').replace('/', '_')

    # Set the output file path
    output_file = os.path.join(output_dir, f"{safe_target_url}_zap_report.html")

    # Start ZAP instance (ensure ZAP is running in daemon mode)
    zap = ZAPv2()

    print(f"Starting passive scan on {target_url}...")

    try:
        # Open the URL in ZAP for initial processing
        zap.urlopen(target_url)
        time.sleep(2)  # Wait for the page to load

        # Wait for passive scan to complete
        # The passive scan happens as part of URL crawling, so there’s no need to call scan() explicitly

        # Give it time for the passive scan to process the responses
        print("Passive scan is in progress...")
        time.sleep(10)  # Sleep for some time to allow passive scan to process responses

        print("ZAP passive scan completed.")

        # Save the scan results as an HTML report
        with open(output_file, 'w') as f:
            f.write(zap.core.htmlreport())

        print(f"ZAP passive scan results saved to {output_file}")
    except Exception as e:
        print(f"Error during passive scan: {e}")

if __name__ == "__main__":
    start_zap_daemon()  # Start ZAP daemon with no API key required
    run_passive_scan()  # Run the passive scan