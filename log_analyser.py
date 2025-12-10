import re
from collections import Counter

# CONFIGURATION
log_file = 'server_logs.txt'
thresh = 5 # Alert if failed attempts > 5

def parse_logs(file_path):
    """
    Read the log files and extracts IP addresses from FAILED login lines.
    """
    failed_ips = []
    
    # REGEX explanation:
    # We are looking for lines that contain 'LOGIN_FAILED'
    # Then we grab the ip addresses at the end
    # r"IP: (\d+\.\d+\.\d+\.\d+)"
    ip_pattern = r"IP: (\d+\.\d+\.\d+\.\d+)"
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Check if the line is failed login
                match = re.search(ip_pattern, line)
                if "LOGIN_FAILED" in line:
                    # Search for the IP address in that line
                    failed_ips.append(match.group(1))    
        return failed_ips
    
    except FileNotFoundError:
        print (f"Error: The file {file_path} was not found.")
        return []
    

def detect_threats(ip_list):
    """
    Counts occurances of each IP and checks against the threshold.
    """
    # Counter creates a dictionary like {"IP_Address":count}
    ip_count = Counter(ip_list)
    
    print("--------Security ALert--------")
    print(f"Total Failed login attempts found: {len(ip_list)}")
    
    found_threat = False
    for ip, count in ip_count.items():
        if count >= thresh:
            print(f"[ALERT] POTENTIAL BRUTE FORCE DETECTED")
            print(f"Source ip: {ip}")
            print(f"Attempt count: {count}")
            print(f"Action: Recommend bocking IP in Firewall.")
            found_threat = True
            
    if not found_threat:
        print(f"No threats detected. System Secure.")
        
    
# Main Exececution
if __name__ == '__main__':
    print("Running Log Analysis Tool....")
    failures = parse_logs(log_file)
    detect_threats(failures)    