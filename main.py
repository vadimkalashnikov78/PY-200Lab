# Это тестовое задание по курсу DEV-PY200. S23. Объектно-ориентированное программирование на языке Python
import hashlib
import random

# Данные для генерации случайных значений в магазин продуктов


def get_product() -> str:  # Задание названия продукта случайным выборов из файла products.txt
    with open("products.txt", encoding="UTF-8") as f:
        return random.choice([index_.strip() for index_ in f.readlines()])


def get_price() -> float:  # Задание цены продукта случайным выборов
    price = round(random.uniform(100.0, 1000.0), 2)
    return price


def get_rating() -> float:  # Задание рейтинга продукта
    rating = round(random.uniform(0.0, 5.0), 2)
    return rating

# Клаcc IdCounter


class IdCounter:
    def __init__(self):
        self.value = 1

    def current_id(self):
        self.value += 1
        return self.value

    def display_id(self):
        print(f"Текущее значение Id {self.value}")

    def reset_id(self):
        self.value = 0
        return self.value


# Класс Password

class Password:
    def __init__(self):
        self.password = str(input("Введите пароль, он должен быть строковым и больше 8 символов:\n"))

    def get(self):  # Получение хэша для пароля с проверкой
        if isinstance(self.password, str) and (len(self.password) >= 8):
            pass_hash_ = hashlib.sha256(self.password.encode()).hexdigest()
        else:
            raise "Пароль должен быть строковым и больше 8 символов"
        return pass_hash_

    def check(self, hash_):  # Проверка совпадения хэша пароля
        check_sum = True
        if Password.get(self) != hash_:
            check_sum = False
        return check_sum

# Класс Product


class Product:

    def __init__(self, name, price, rating, product_id: IdCounter):
        self._product_id_ = product_id.current_id()
        self.name = self.check_name(name)
        self.price = self.check_price(price)
        self.rating = self.check_rating(rating)

    def check_name(self, name_: str):
        if isinstance(name_, str):  # проверка типа
            return str(name_)  # Задаем имя продукта
        else:
            raise("Имя продукта должно быть строкой", TypeError)

    def check_price(self, price_: float):
        if isinstance(price_, float) and (price_ >= 0):  # проверка типа и значения
            return round(price_, 2)  # Задаем цену
        else:
            raise("Цена должна быть действительным числом >= 0", TypeError)

    def check_rating(self, rating_: float):
        if isinstance(rating_, float) and (rating_ >= 0):  # проверка типа
            return round(rating_, 2)  # Задаем рейтинг
        else:
            raise ("Рейтинг доложен быть числом больше 0", TypeError)

    def __str__(self) -> str:
        return f"{self._product_id_}_{self.name}"

    def __repr__(self) -> str:
        return f"Product(id={self._product_id_}, name={self.name}, price={self.price}, rating={self.rating})"

# Класс Cart


class Cart:
    def __init__(self):
        self.content = {
        }

    def add(self, product: Product, quantity: int):
        self.content[product] = quantity

    def remove(self, product: Product):
        del self.content[product]

    def __str__(self):
        return f"{self.content}"


# Класс User
class User:

    def __init__(self, username: str, user_id: IdCounter):
        self._user_id_ = user_id.current_id()
        self._username_ = self.check_username(username)
        self.userpassword = Password()
        self._cart_ = Cart()

    def check_username(self, username):
        if isinstance(username, str):
            return str(username)
        else:
            raise("Имя пользователя должно быть строкой", TypeError)

    def __str__(self) -> str:
        return f"{self._user_id_}_{self._username_}"

    def __repr__(self) -> str:
        return f"User={self._user_id_}, name={self._username_})"


# Класс Store

class Store:
    def __init__(self):
        product_id = IdCounter()  # Запуск счетчика продуктов
        user_id = IdCounter()  # Запуск счетчика пользователей

        user_1 = str(input("Добрый день!\nВы попали в магазин Продуктовых товаров\nВведите свой username :\n"))
        user1 = User(user_1, user_id)
        print("Вы успешно зарегистрировались в Магазине\n", "Ваш пользователь:", user1._username_)
        print("Ваша корзина товаров выглядит вот так:\n", user1._cart_.__str__())

        frog = "in"
        while frog != "out":
            prod = Store.add_product(product_id)
            print(f"Хотите добавить случайны продукт {prod.__repr__()} к себе в корзину?")
            if_or_no = str(input("Введите Да или Yes, или наберите любое другое слово для выхода:\n"))
            if (if_or_no == "Да") or (if_or_no == "Yes"):
                user1._cart_.add(prod, 1)
                print("Ваша корзина товаров выглядит вот так:\n", user1._cart_.__str__())
            else:
                frog = "out"
                print("Спасибо за посещение нашего магазина\n")
                print("Ваша продуктовая корзина выглядит так:\n")
                print(user1._cart_.__str__())

    def add_product(product_id: IdCounter):
        prod1 = Product(get_product(), get_price(), get_rating(), product_id)
        return prod1


if __name__ == '__main__':
    Store()

