# Задание 2.
#
# У вас есть класс BookService, который использует интерфейс BookRepository для получения информации
# о книгах из базы данных. Ваша задача написать unit-тесты для BookService,
# используя Mockito для создания мок-объекта BookRepository.
from abc import ABC, abstractmethod


class BookService:

    def __init__(self, book_repository):
        self.book_repository = book_repository

    def find_book_by_id(self, id_my):
        return self.book_repository.find_by_id(id_my)

    def find_all_books(self):
        return self.book_repository.find_all()


class BookRepository(ABC):

    @abstractmethod
    def find_by_id(self, id_my):
        pass

    @abstractmethod
    def find_all(self):
        pass
