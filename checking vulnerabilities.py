import subprocess

domain = input('Enter website url: ')
output = subprocess.check_output(f'nslookup {domain}', shell = True, encoding = 'UTF-8')
print(output)
