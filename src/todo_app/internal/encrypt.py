from passlib.context import CryptContext


hash_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return hash_context.verify(plain_password, hashed_password)


def hash_password(password: str) -> str:
    return hash_context.hash(password)
