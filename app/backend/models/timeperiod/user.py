import time
import csv
import os
import base58
import nacl.signing
import nacl.encoding

class Time:
    """Allocates a unique accumalative prime number and a creation timestamp to a user"""

    PRIMEFILE = "current_prime.txt"


    @classmethod
    def load_current_prime(cls):
        if os.path.exists(cls.PRIMEFILE):
            with open(cls.PRIMEFILE, mode="r") as file:
                cls.current_prime = int(file.read().strip())
        else:
            cls.current_prime = 2 # Start from the first prime number


    @classmethod
    def save_current_prime(cls):
        with open(cls.PRIMEFILE, mode="w") as file:
            file.write(str(cls.current_prime))


    def __init__(self, timestamp, prime):
        self.timestamp = timestamp
        self.prime = prime
    
    def __str__(self):
        return f"Timestamp: {self.timestamp}\nPrime: {self.prime}"
    
    @classmethod
    def get(cls):
        timestamp = cls.create_timestamp()
        prime = cls.fetch_prime()
        return cls(timestamp, prime)
    
    @property
    def timestamp(self):
        return self._timestamp
    
    @timestamp.setter
    def timestamp(self, timestamp):
        self._timestamp = timestamp

    @property
    def prime(self):
        return self._prime
    
    @prime.setter
    def prime(self, prime):
        self._prime = prime

    @staticmethod
    def is_prime(n):
        """Returns True if n is prime"""
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        i = 5
        while i ** 2 <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    @staticmethod
    def next_prime(n):
        """Returns the next prime number after n"""
        n += 1
        while True:
            if Time.is_prime(n):
                return n
            n += 1
    @staticmethod
    def primes_up_to(limit):
        """Returns a list of prime numbers up to a limit"""
        return [x for x in range(2, limit) if Time.is_prime(x)]
    
    @classmethod
    def create_timestamp(cls):
        """Returns the current time in seconds"""
        return time.time()
    
    @classmethod
    def fetch_prime(cls):
        """Returns the next prime number after the current prime number"""
        cls.current_prime = cls.next_prime(cls.current_prime)
        cls.save_current_prime()
        return cls.current_prime



class User(Time): # Wallet | Time Package
    """
    All things in a Folio's functionality that are unique to one User
    """
    
    FILENAME = "users.csv"


    def __init__(self, timestamp, prime, username, private_key, public_key, blockchain_address):
        super().__init__(timestamp, prime)
        self.username = username
        self.private_key = private_key
        self.public_key = public_key
        self.blockchain_address = blockchain_address


    def __str__(self):
        return f"Username: {self.username}\nPrivate: {self.private_key}\nPublic: {self.public_key}\nAddress: {self.blockchain_address}\nTimestamp: {self.timestamp}\nPrime: {self.prime}"


    @classmethod
    def get(cls):
        cls.load_current_prime()
        timestamp = cls.create_timestamp()
        prime = cls.fetch_prime()
        username = cls.create_username()
        private_key = cls.generate_ed25519_keypair(private_key=True) ###
        public_key = cls.generate_ed25519_keypair(private_key=False) ###
        blockchain_address = cls.encode_address()
        
        return cls(timestamp, prime, username, private_key, public_key, blockchain_address)

    @classmethod
    def get_user_by_prime(cls, prime):
        """Returns the user with the given prime number"""
        users = cls.read_user_from_csv(cls.FILENAME)
        if users is None:
            print("No users found. read_user_from_csv() returned None")
            return None
        user_data = next((user for user in users if user["Prime"] == str(prime)), None)
        if user_data:
            return cls(
                timestamp=user_data["Timestamp"],
                prime=user_data["Prime"],
                username=user_data["Username"],
                private_key=user_data["Private Key"],
                public_key=user_data["Public Key"],
                blockchain_address=user_data["Blockchain Address"]
            )
        return None

    @property
    def timestamp(self):
        return self._timestamp
    
    @timestamp.setter
    def timestamp(self, timestamp):
        self._timestamp = timestamp

    @property
    def prime(self):
        return self._prime
    
    @prime.setter
    def prime(self, prime):
        self._prime = prime

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        self._username = username

    @property
    def private_key(self):
        return self._private_key
    
    @private_key.setter
    def private_key(self, private_key):
        self._private_key = private_key

    @property
    def public_key(self):
        return self._public_key
    
    @public_key.setter
    def public_key(self, public_key):
        self._public_key = public_key

    @property
    def blockchain_address(self):
        return self._blockchain_address
    
    @blockchain_address.setter
    def blockchain_address(self, blockchain_address):
        self._blockchain_address = blockchain_address


    def save(self, FILENAME):
        file_exists = os.path.exists(FILENAME) # Check if the file exists
        
        with open(FILENAME, mode="a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Username", "Private Key", "Public Key", "Blockchain Address", "Timestamp", "Prime"])
            writer.writerow([self.username, self.private_key, self.public_key, self.blockchain_address, self.timestamp, self.prime])

    
    @staticmethod
    def create_username():
        """Ask the user for a username. If the username is not unique, ask again, until a unique username is entered"""
        while True:
            username = input("Enter a username: ")
            if User.is_username_unique(username):
                return username
            print("Username already exists. Please try again.")
        
    @staticmethod
    def is_username_unique(username):
        """Check if the username is unique"""
        if not os.path.exists(User.FILENAME):
            return True
        
        with open(User.FILENAME, mode="r") as file:
            reader = csv.reader(file)
            next(reader) # Skip the header
            for row in reader:
                if row[0] == username:
                    return False
        return True
    
    @staticmethod
    def read_user_from_csv(FILENAME):
        """Read the users from the CSV file"""
        users = []
        if os.path.exists(FILENAME):
            with open(FILENAME, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    users.append(row)
            return users
        else:
            print(f"Debug: File {FILENAME} does not exist") 
            return None

    @staticmethod
    def generate_ed25519_keypair(private_key=True):
        key = nacl.signing.SigningKey.generate()
        if private_key:
            return key.encode(encoder=nacl.encoding.HexEncoder).decode()
        else:
            return key.verify_key.encode(encoder=nacl.encoding.HexEncoder).decode()
        
    
    # Encode the public key to a blockchain address using the base58 encoding
    @staticmethod
    def encode_address():
        public_key = User.generate_ed25519_keypair(private_key=False)
        public_key_bytes = bytes.fromhex(public_key)
        return base58.b58encode(public_key_bytes).decode()
    

    # Decode the blockchain address to the public key using the base58 encoding
    @staticmethod
    def decode_address():
        blockchain_address = User.encode_address()
        blockchain_address_bytes = bytes.fromhex(blockchain_address) # Convert the blockchain address to bytes
        return base58.b58decode(blockchain_address_bytes).hex()


def main():
    user = User.get()
    user.save(User.FILENAME)


if __name__ == "__main__":
    main()