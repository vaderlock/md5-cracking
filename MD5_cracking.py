import hashlib
import time

flag = 0

#print("ALL THE ALGORITHMS IN THIS MODULE")
#print(hashlib.algorithms_guaranteed)

md5_hashcode = input("Enter md5 hash: ")

list = input("Input file name: ")

try:
    pass_file = open (list, "r")
except: 
    print("No files were found here.")
    quit()

for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest == md5_hashcode:
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("PASSWORD HAS BEEN CRACKED")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("PASSWORD IS " + word )
        flag = 1
        break 

if flag == 0: 
    print("PASSWORD WAS NOT FOUND IN FILE")

