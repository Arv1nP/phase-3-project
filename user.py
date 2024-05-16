import hashlib
from data_structures import User  # Importing the User model from data_structures module

class UserHandler:
    def __init__(self, session, username, password):
        self.session = session
        self.username = username
        self.password = password

    def register(self):
        try:
            # Check if the username already exists
            user = self.session.query(User).filter_by(username=self.username).first()
            print("Existing user:", user)  # Debug statement
            if user:
                return False  # Username already exists
            else:
                # Hash the password before storing it
                hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
                print("Hashed password:", hashed_password)  # Debug statement
                new_user = User(username=self.username, password=hashed_password)
                self.session.add(new_user)
                self.session.commit()
                return True  # Registration successful
        except Exception as e:
            print({e})
            self.session.rollback()
            return False

    def login(self):
        try:
            # Retrieve user by username
            user = self.session.query(User).filter_by(username=self.username).first()
            print("User found:", user)
            if user:
                # Hash the input password and compare with the stored hashed password
                input_password_hash = hashlib.sha256(self.password.encode()).hexdigest()
                if user.password == input_password_hash:
                    return True  # Login successful
            return False  # Either user not found or incorrect password
        except Exception as e:
            print({e})
            return False
        

    
