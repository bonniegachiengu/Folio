import csv
import os
from user import User, Time

class Moment(User, Time):
    """User moment which is the user details and a timestamp of now."""

    FILENAME = "users.csv"
    MOMENTFILE = "moment.csv"

    def __init__(self, timestamp, prime, username, public_key, private_key, blockchain_address, now_timestamp):
        """Initializes the user moment."""
        User.__init__(self, timestamp, prime, username, public_key, private_key, blockchain_address)
        Time.__init__(self, now_timestamp, prime)
        self.now_timestamp = now_timestamp
        self.active = {}

    def __str__(self):
        """Returns the string representation of the user's active moment."""
        return f"{self.active}"
    
    def __repr__(self):
        """Returns the string representation of the user's active moment."""
        return f"{self.active}"
    
    @classmethod
    def get(cls, prime):
        user = User.get_user_by_prime(prime)
        if not user:
            raise ValueError(f"No user found with prime: {prime}")
        
        now_timestamp = cls.create_timestamp()
        active = {
            "timestamp": now_timestamp,
            "user": user
        }

        moment = cls(user.timestamp, user.prime, user.username, user.public_key, user.private_key, user.blockchain_address, now_timestamp)
        moment.active = active

        cls.save_moment_to_csv(cls.MOMENTFILE, moment.active)
        return moment

    @property
    def now_timestamp(self):
        return self._now_timestamp
    
    @now_timestamp.setter
    def now_timestamp(self, now_timestamp):
        self._now_timestamp = now_timestamp

    @property
    def active(self):
        return self._active
    
    @active.setter
    def active(self, active):
        self._active = active
        
    @staticmethod
    def save_moment_to_csv(filepath, moment_data):
        file_exists = os.path.exists(filepath)
        with open(filepath, mode='a', newline='') as file:
            fieldnames = ['timestamp', 'prime', 'username', 'public_key', 'private_key', 'blockchain_address']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow({
                'timestamp': moment_data['timestamp'],
                'prime': moment_data['user'].prime,
                'username': moment_data['user'].username,
                'public_key': moment_data['user'].public_key,
                'private_key': moment_data['user'].private_key,
                'blockchain_address': moment_data['user'].blockchain_address
            })

def main():
    Moment.get(19)

if __name__ == "__main__":
    main()