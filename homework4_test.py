from unittest.mock import Mock
from homework4 import BookService, BookRepository


def test_book_service():
    mock_br = Mock(spec=BookRepository)
    mock_br.find_by_id.return_value = 3
    bs = BookService(mock_br)
    assert bs.find_book_by_id(0) == 3

    mock_br.find_all.return_value = [30, 20, 10]
    assert bs.find_all_books() == [30, 20, 10]
