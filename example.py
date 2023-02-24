from time import time


def timelog(funk):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = funk(*args, **kwargs)
        t2 = time()
        print(f'Woktime is: {round(t2-t1, 100)} sec')
        return result
    return wrapper


class Product:

    product = 'Abstract product'

    __meta = 'Analytic signal'

    def __init__(self, name):

        self.product = name

    @timelog
    def add_to_cart(self, count):
        print(f'Add {count} product[{self.product}] to cart')
        print(f'Add {count} product[{self.product}] to cart')
        print(f'Add {count} product[{self.product}] to cart')
        print(f'Add {count} product[{self.product}] to cart')
        print(f'Add {count} product[{self.product}] to cart')


    def edit_description(self):
        print(f'Edit Description')

    def add_review(self, text):
        print(f'Add rewiev:', text)


class Form:

    product = None

    def save_product_form(self):
        print(f'Save[{self.product}] to cart')


class Book(Product, Form):
    @timelog
    def __init__(self, name, author, pages):
        super().__init__(name=name)
        self.name = name
        self.author = author
        self.pages = pages

    def __add__(self, other):
        return Book(
                    name=f'{self.name}|{other.name}',
                    author=f'{self.author}|{other.author}',
                    pages=self.pages + other.pages
                    )

    def __str__(self):
        return f'BOOK: {self.author}, {self.name}'

    def get_pages_count(self):
        print(f'pages count in this book: {self.pages}')

    @timelog
    def add_to_cart(self, count):
        super().add_to_cart(count)
        print(f'Add {count} product[{self.product}] added to cart')

