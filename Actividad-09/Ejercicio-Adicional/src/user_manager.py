class UserNotFoundError(Exception):
    pass

class UserAlreadyExistsError(Exception):
    pass

# clase UserManager 
class UserManager:
    # constructor
    def __init__(self, hash_service=None, repo=None, email_service=None):
        self.hash_service = hash_service or self._default_hash_service()
        self.repo = repo or self._default_repo()
        self.email_service = email_service

    # metodod para hash y verificar
    def _default_hash_service(self):
        # Hash por defecto si no se provee nada (inseguro, solo para no romper).
        class DefaultHashService:
            def hash(self, plain_text: str) -> str:
                return plain_text
            def verify(self, plain_text: str, hashed_text: str) -> bool:
                return plain_text == hashed_text
        return DefaultHashService()
    
    # repo por defecto si no se provee nada
    def _default_repo(self):
        # Repo interno por defecto
        class InternalRepo:
            def __init__(self):
                self.data = {}
            def save_user(self, username, hashed_pw):
                if username in self.data:
                    raise UserAlreadyExistsError(f"'{username}' ya existe.")
                self.data[username] = hashed_pw
            def get_user(self, username):
                return self.data.get(username)
            def exists(self, username):
                return username in self.data
        return InternalRepo()
    
    # verifica si el usuario existe en el repositorio
    def user_exists(self, username):
        return self.repo.exists(username)

    # verifica si el usuario y la contraseña son correctos
    def authenticate_user(self, username, password):
        stored_hash = self.repo.get_user(username)
        if stored_hash is None:
            raise UserNotFoundError(f"El usuario '{username}' no existe.")
        return self.hash_service.verify(password, stored_hash)
    
    # agrega un nuevo usuario al repositorio
    def add_user(self, username, password):
        hashed = self.hash_service.hash(password)
        self.repo.save_user(username, hashed)
        # Enviamos correo si se inyectó un email_service
        if self.email_service:
            self.email_service.send_welcome_email(username)