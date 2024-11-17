from sqlmodel import SQLModel, MetaData

# Gebruik een gedeeld MetaData object
shared_metadata = MetaData()

class BaseModel(SQLModel):
    __abstract__ = True
    metadata = shared_metadata
