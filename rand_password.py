import string
import random 

class random_password:
    
    def __init__(self,length,special):
        self.length=length
        self.special=special
    
    

    def generate(self):
        password=""
        rand_length=random.randint(int(self.length)+1,20)
        
        if self.special:
            for i in range(rand_length):
                char=random.choice(string.ascii_letters)
                sp_cahr=str(random.choice(string.punctuation))
                numbers=str(random.randint(0,9))
                password+=random.choice([sp_cahr,numbers,char])
        else:
            for i in range(rand_length):
                char=random.choice(string.ascii_letters)
                sp_cahr=str(random.choice(string.punctuation))
                numbers=str(random.randint(0,9))
                password+=random.choice([numbers,char])
        return password


        