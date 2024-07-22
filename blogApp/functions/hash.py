from passlib.hash import sha256_crypt


class Hash:
    
    def hash(value:str):
        value = value.encode('utf-8') 
        hash_value = sha256_crypt.hash(value)
        
        return hash_value

    def verify(value:str, hash:str):
        return sha256_crypt.verify(value, hash)
    
if __name__ == "__main__":
    print(Hash.hash("1234"))
