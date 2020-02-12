# Roy
class Book:
    def __init__(self, title, price, pages):
        self.title = title
        self.price = price
        self.pages = pages

    def get_details(self):
        return 'Title: ' + self.title + '\nPrice: ' + str(self.price) \
            + '\nPages: ' + str(self.pages)

    def is_expensive(self):
        return self.price > 600