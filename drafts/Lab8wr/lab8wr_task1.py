class Book:
    def __init__(self, title, author, publisher):
        self.__title = title
        self.__author = author
        self.__publisher = publisher

    
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_publisher(self):
        return self.__publisher

    
    def set_title(self, title):
        self.__title = title
    
    def set_author(self, author):
        self.__author = author
    
    def set_publisher(self, publisher):
        self.__publisher = publisher

    def __str__(self):
        return f"Book title: {self.__title}, Author: {self.__author}, Publisher: {self.__publisher}"


