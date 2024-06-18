import hashlib
from data_structures import User, UserInfo, Note  # Importing the User model from data_structures module

class UserHandler:
    def __init__(self, session, username, password=None):
        self.session = session
        self.username = username
        self.password = password

    def register(self, email):
        try:
            # Check if the username already exists
            user = self.session.query(User).filter_by(username=self.username).first()
            if user:
                return False  # Username already exists
            else:
                # Hash the password before storing it
                hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
                new_user = User(username=self.username, password=hashed_password)
                self.session.add(new_user)
                self.session.commit()

                # Add user information (email)
                user_info = UserInfo(username=self.username, email=email)
                self.session.add(user_info)
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
            if user:
                # Hash the input password and compare with the stored hashed password
                input_password_hash = hashlib.sha256(self.password.encode()).hexdigest()
                if user.password == input_password_hash:
                    return True  # Login successful
            return False  # Either user not found or incorrect password
        except Exception as e:
            print({e})
            return False
        

    def progress(self, lang):
        try:
            # Retrieve user by username
            user = self.session.query(User).filter_by(username=self.username).first()
            if user:
                if lang == 'en':
                    user.words_learned_en += 3
                elif lang == 'fr':
                    user.words_learned_fr += 3
                elif lang == 'it':
                    user.words_learned_it += 3
                # Commit the changes to the database
                self.session.commit()
                return True
        except Exception as e:
            print({e})
            self.session.rollback()
            return False
        
    def get_progress(self):
        try:
            # Retrieve user by username
            user = self.session.query(User).filter_by(username=self.username).first()
            if user:
                progress = {
                    'English': user.words_learned_en,
                    'French': user.words_learned_fr,
                    'Italian': user.words_learned_it
                }
                return progress
            else:
                print("User not found.")
                return None
        except Exception as e:
            print({e})
            return None
        

    def add_note(self, note, words, lang, title):
        try:
            user = self.session.query(User).filter_by(username=self.username).first()
            if user:
                new_note = Note(username=self.username, note=note, words=words, lang=lang, title=title)
                self.session.add(new_note)
                self.session.commit()

                return True
            
            if not user:
                print("User not found!")
                return False
        
        except Exception as e:
            print({e})
            return None 
        

    def get_notes(self):
        try:
            user = self.session.query(User).filter_by(username=self.username).first()
            if user:
                notes = self.session.query(Note).filter_by(username=self.username).order_by(Note.id.desc()).all()
                formatted_notes = [
                    f"Language: {note.lang}, Words: {note.words}, Title: {note.title}, Note: {note.note}"
                    for note in notes
                ]
                result = "\n".join(formatted_notes)
                return result
                
        except Exception as e:
            print({e})
            return None
        