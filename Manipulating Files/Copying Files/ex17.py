from os.path import exists

orig_file = "dummy.txt"
new_file = "dummy2.txt"

print(f'COPYING FROM {orig_file} to {new_file}....')

in_file = open(orig_file)
indata = in_file.read()

print(f'The input file is {len(indata)} bytes long')
print(f'Does the output file exist? {exists(new_file)}')
print("Ready? Hit ENTER or RETURN to continue. Hit CTRL-C to abort")
input("?")

out_file = open(new_file, 'w')
out_file.write(indata)

print(f"SUCCESS! {orig_file} has been successfully copied to {new_file}")

out_file.close()
in_file.close()
