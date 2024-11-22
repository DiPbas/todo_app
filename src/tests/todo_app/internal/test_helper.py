import pytest
from unittest.mock import Mock, MagicMock
from todo_app.internal.exceptions import NotFoundError
from todo_app.internal.helper import entity_exists  

# Maak een voorbeeld SQLAlchemy modelklasse
class MockModel:
    __name__ = "MockModel"

def test_entity_exists_found():
    # Arrange
    mock_session = Mock()
    mock_entity = Mock()
    mock_session.get = MagicMock(return_value=mock_entity)

    # Act
    result = entity_exists(1, MockModel, mock_session)

    # Assert
    assert result == mock_entity
    mock_session.get.assert_called_once_with(MockModel, 1)

def test_entity_exists_not_found():
    # Arrange
    mock_session = Mock()
    mock_session.get = MagicMock(return_value=None)

    # Act
    with pytest.raises(NotFoundError, match="MockModel with id: 1 not found"):
        entity_exists(1, MockModel, mock_session)

    # Assert
    mock_session.get.assert_called_once_with(MockModel, 1)
