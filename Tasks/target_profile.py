# ------Imports-------
from datetime import date
# ------Header Section----------
print("=" * 40)
# center the title within border width
print("[Target Profile Report Generator]".center(40))
print("=" * 40)
print()
# ------User Input----------
# strip() removes accidental whitespace from inputs

target_name = input("[?] Target Name : ").strip()
target_ip = input("[?] IP Address : ").strip()
target_domain = input("[?] Domain : ").strip()
target_os = input("[?] OS : ").strip().upper()
target_ports = input("[?] Open Ports :").strip()
target_active_services = input("[?] Is Active (yes/no) : ").strip().lower()
target_risk = input("[?] Risk Level:").strip().upper()
target_notes = input("[?] Notes : ").strip()
# -------If--else---Condition
# ── PROCESS DATA ────────────────────────
# Convert yes/no input to True/False string
# Multiple formats accepted for better usability
if target_active_services in ['yes', 'y','true','1']:
    target_active_services= "True"
else:
    target_active_services= "False"
# Get current date for timestamp
present_time = date.today()
# ------Print Statements------
print(f"[*] Target Name     :    {target_name}")
print(f"[*] IP Address      :    {target_ip}")
print(f"[*] Domain          :    {target_domain}")
print(f"[*] OS              :    {target_os}")
print(f"[*] Open Ports      :    {target_ports}")
print(f"[*] Is Active       :    {target_active_services}")
print(f"[*] Risk Level      :    {target_risk}")
print(f"[*] Notes           :    {target_notes}")
# -------Print an empty line
print()
# -------Footer Section-------
print("=" * 40)
print("[*] Profile Saved Successfully ")
print(f"[*] Scan timestamp : {present_time}")
print("=" * 40)