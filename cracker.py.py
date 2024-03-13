import hashlib			#to use SHA encryption
from colorama import Fore	#to change color of text
from tqdm import tqdm		#for progress bar
import pyfiglet 



def gen_hash(text):
    '''
    SHA - 1 generator function
    :param text: String to be converted into hash value
    :return hash_val: Geberated hash of given string
    '''
    temp = text.strip()	
    hash_val = hashlib.sha1(temp.encode()).hexdigest()	
    return hash_val	
	
def banner_gen(text):
    '''
    Banner generator using figlet
    :param text: text to be converted into ascii banner
    :return banner: ASCII banner value
    '''
    banner = pyfiglet.figlet_format(text) 
    return banner 

def cracker(file,hash):
    '''
    Hash cracker function
    :param file: text file from where words will be read
    :param hash: hash to be craacked
    :return word or none: if hash cracked than it will return word else will return none 
    '''
    global flag,cracked	
    print(file)
    with open(file ,'r') as f:	
        for word in tqdm(f):	
            temp = gen_hash(word)	
            if(temp == hash):
                return word
                break		

if __name__ == '__main__':
    '''
    main function
    '''
    choice = 1
    b = banner_gen('SHA - 1 Generator & Cracker Tool')
    print(b)
    try:
        while(choice != 3):
            choice = int(input("1. For SHA1 hash generation \n2. For Hash cracker \n3. To Exit \nEnter Your choice :"))
            if(choice == 1):
                text = input("Enter text to genrate hash :")
                res = gen_hash(text)
                print("Generated SHA-1 hash is : ",res)
            elif(choice == 2):
                hash = input("Paste your hash to be cracked : ").strip()	
                file = input("Enter your password list file path : ")		    
                x = cracker(file,hash)		
                if(x):			
                    print(f"{Fore.GREEN}Hash cracked, Plain text is : ",x)	
                else:
                    print(f"{Fore.RED}Hash couldn't be cracked ! use longer password list")			
            elif(choice == 3):
                exit()
            else:
                print("Wrong choice")	
    except:
        print(f"{Fore.RED}Unknown Error")