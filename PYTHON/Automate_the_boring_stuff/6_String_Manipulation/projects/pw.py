#!../../bin/python3
# pw.py - An insecure locker program.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
            'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
            'luggage': '12345'}

import sys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]       # first command line arg is the account name
if account in PASSWORDS.keys():
    import pyperclip
    pyperclip.copy(PASSWORDS[account])
    print(f'Password for {account} copied to clipboard.')
    print('Do you want to display the copied password? (Y/N)')
    answer = input().lower()
    if answer == 'y':
        import time
        time.sleep(1)
        print(pyperclip.paste())
else:
    print(f'There is no account name {account}')