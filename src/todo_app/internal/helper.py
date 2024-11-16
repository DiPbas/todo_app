from todo_app.internal.exceptions import NotFoundError



def entity_exists(entity_id: int, model, session):
    """
    Generic method to check if an entity exists in the database.

    Args:
        entity_id (int): The ID of the entity to check.
        model (Base): The SQLAlchemy model class.
        session (Session): The database session.

    Returns:
        Base: The found entity.

    Raises:
        NotFoundError: If the entity does not exist.
    """
    entity = session.get(model, entity_id)
    if not entity:
        raise NotFoundError(detail=f"{model.__name__} with id: {entity_id} not found")
    return entity