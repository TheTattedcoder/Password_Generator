import string
import random

class PW_Gen:
    '''
    Ask the User how long the password should be.
    The password should be 8 - 16 characters long.
    
    '''
    def get_number_len():
        
            while True:
                try:
                    pw_len = int(input("How long will you like your password?: "))
                except ValueError:
                    print('Try again🚫')
                    continue
                if pw_len not in range(8,17):
                    print('Make sure it is 8 - 16 characters')     
                else:
                    break
            return pw_len
   
                 
    def generate_pw(func):
        char = list(string.ascii_letters + string.digits + '!@#$%^&*?')
        random.shuffle(char)
        
        password = []
        for _ in range(func):
            password.append(random.choice(char))
        
        random.shuffle(password)
        
        password = "".join(password)
        
        print(password)
        
        
        
    
        ...
                            

while True:
    option = input('Do you want to generate a password ((Y)es/(N)o): ').capitalize()
    if option == 'Yes'or option == 'Y':
        PW_Gen.generate_pw(PW_Gen.get_number_len())       
    else:
        print('Thank you for using goodbye!')
        quit()



