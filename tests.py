import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize("name,genre", [("Острые предметы", "Детективы"), ("Дюна", "Фантастика"),
                                            ("Долгая прогулка", "Ужасы"), ("Как важно быть серьезным", "Комедии"),
                                            ("Незнайка", "Мультфильмы")])
    def test_set_book_genre_valid_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre.get(name) == genre

    @pytest.mark.parametrize("name, genre", [("Острые предметы", "Детективы"), ("Дюна", "Фантастика"),
                                             ("Долгая прогулка", "Ужасы"), ("Как важно быть серьезным", "Комедии"),
                                             ("Незнайка", "Мультфильмы") ])
    def test_get_book_genre_by_book_name(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre





    @pytest.mark.parametrize("genre, books", [('Фантастика', ['Дюна', 'Успеть вспомнить']),
                                         ('Ужасы', ['Долгая прогулка']),
                                         ('Детективы', ['Острые предметы'])])
    def test_get_books_with_specific_genre_for_existing_genre(self, genre, books):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Долгая прогулка')
        collector.set_book_genre('Долгая прогулка', 'Ужасы')
        collector.add_new_book('Успеть вспомнить')
        collector.set_book_genre('Успеть вспомнить', 'Фантастика')
        collector.add_new_book('Острые предметы')
        collector.set_book_genre('Острые предметы', 'Детективы')
        assert collector.get_books_with_specific_genre(genre) == books

    @pytest.mark.parametrize("books_genre, expected_result", [(
            {"Острые предметы": "Детективы", "Долгая прогулка": "Ужасы"},
            {"Острые предметы": "Детективы", "Долгая прогулка": "Ужасы"})])
    def test_get_books_genre_add_existing_genre(self, books_genre, expected_result):
        collector = BooksCollector()
        collector.books_genre = books_genre
        assert collector.get_books_genre() == expected_result

    @pytest.mark.parametrize("name, genre", [("Дюна", "Фантастика"), ("Незнайка", "Мультфильмы"),
                                             ("Как важно быть серьезным", "Комедии")])
    def test_get_books_for_children_add_book_for_children(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == [] if genre in collector.genre_age_rating else [name]

    def test_add_book_in_favorites_add_one_books(self):
        collector = BooksCollector()
        collector.add_new_book("Дюна")
        collector.add_book_in_favorites("Дюна")
        assert collector.get_list_of_favorites_books() == ["Дюна"]

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Дюна")
        collector.add_book_in_favorites("Дюна")
        collector.delete_book_from_favorites("Дюна")
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_list_view_one_book(self):
        collector = BooksCollector()
        collector.add_new_book("Дюна")
        collector.add_book_in_favorites("Дюна")
        assert collector.get_list_of_favorites_books() == ["Дюна"]








