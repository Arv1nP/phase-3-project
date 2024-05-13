from data_structures import User  # Assuming User is imported from data_structures

class UserHandler:

    @staticmethod
    def register(session, username, password):
        try:
            user = session.query(User).filter_by(username=username).first()
            if user:
                print("Username already exists")
                return False
            else:
                new_user = User(username=username, password=password)
                session.add(new_user)
                session.commit()
                print("User registered successfully!")
                return True
        except Exception as e:
            print(f"An error occurred during registration: {e}")
            session.rollback()
            return False

    @staticmethod
    def login(session, username, password):
        try:
            user = session.query(User).filter_by(username=username, password=password).first()
            if user:
                print("Login successful!")
                return True
            else:
                print("Invalid username or password. Please try again.")
                return False
        except Exception as e:
            print(f"An error occurred during login: {e}")
            return False
