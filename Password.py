import string
import random
gen_password=string.ascii_letters+string.digits+string.punctuation
length=int(input("Please enter the length of the Password : "))
password = ''.join(random.choices(gen_password, k=length))
print("Your Password for entered length is :",password)
