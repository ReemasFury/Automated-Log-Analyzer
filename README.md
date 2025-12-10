## Automated Log Analyzer
## 📌 Project Overview
This tool is a Python-based security script designed to automate the detection of **Brute Force Attacks** from server logs. It parse raw log data, identifies failed authentication attempts using Regex and alerts the user if a specific IP address exceeds the security threshold.

## 🛠 Skills Demonstrated
* **Python Automation:** File I/O streaming and scripting.
* **Log Analysis:** Parsing unstructured into actionable intelligence.
* **Threat Detection:** Implementing logic to identify anomalous behaviour(Brute Force).
* **Regex:** Using Regular Expression for pattern matching (IP extraction).

## 🚀 How To Run
1. Clone the repository:
   ```
   git clone [https://github.com/ReemasFury/Automated-Log-Analyzer.git](https://github.com/ReemasFury/Automated-Log-Analyzer.git)
  
2. Navigate to the directory:
   ```
   cd Automated-Log-Analyzer
   
3. Run the script:
   ```
   python log_analyzer.py

4. Sample Output:
   ```
   --- SECURITY REPORT ---
    Total Failed Logins Found: 7
    [ALERT] POTENTIAL BRUTE FORCE DETECTED!
    Source IP: 203.0.113.45
    Attempt Count: 6
    Action: Recommend blocking IP in Firewall.
  

