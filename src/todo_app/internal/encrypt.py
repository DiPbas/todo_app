# from passlib.context import CryptContext


# hash_context = CryptContext(schemes=["bcrypt"], deprecated="auto")





def hash_password(password: str) -> str:
    return password + "fakehash"
