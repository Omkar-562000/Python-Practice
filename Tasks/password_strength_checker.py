import getpass # This is the module 
print("=" * 40)
print("PASSWORD STRENGTH CHECKER".center(40))
print("=" * 40)

password = getpass.getpass("[?] Enter Password : ").strip()

print()
print(f"[*] Password Length     :       {len(password)}")
print(f"[*] Password            :       {password}")

if len(password) <= 8 :
    print("Pass")
else:
    print("Fail")

if any(char.isupper() for char in password) :
    print("Pass")
else:
    print("Fail")

if any(char.isdigit() for char in password) :
    print("Pass")
else:
    print("Fail")

