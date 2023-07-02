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
    def start_count_Id(self, value=1):
        self.value = value
        return self.value

    def increment_Id(self):
        self.value += 1
        return self.value

    def display_Id(self):
        print(f"Текущее значение Id {self.value}")

    def reset_Id(self):
        self.value = 0
        return self.value


# Класс Password

class Password:
    def __init__(self):
        self.password = str(input("Введите пароль:\n"))
    def get(self):  # Получение хэша для пароля с проверкой
        if isinstance(self.password, str) and (len(self.password) >= 8):
            pass_hash_ = hashlib.sha256(self.password.encode()).hexdigest()
        else:
            raise("Пароль должен быть строковым и больше 8 символов")
        return pass_hash_

    def check(self, hash_): # Проверка совпадения хэша пароля
        check_sum = True
        if Password.get() != hash_:
            check_sum = False
        return check_sum

# Класс Product

class Product:

    def __init__(self, name, price, rating):
        self._id_ = 1
        if isinstance(name, str):  # проверка типа
            self._name_ = name  #Задаем имя продукта
        else:
            raise("Имя продукта должно быть строкой", TypeError)
        if isinstance(price, float) and (price >= 0): #
            self.price = round(price, 2) #
        else:
            raise("Цена должна быть действительным числом >= 0", TypeError)
        if isinstance(rating, float) and (rating >= 0):  # проверка типа
            self.rating = round(rating, 2)  #Задаем рейтинг
        else:
            raise("Рейтинг доложен быть числом больше 0", TypeError)

    def __str__(self) -> str:
        return f"{self._id_}_{self._name_}"

    def __repr__(self) -> str:
        return f"Product(id={self._id_}, name={self._name_}, price={self.price}, rating={self.rating})"

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
class User():

    def __init__(self, username: str):
        self._id_ = 1
        if isinstance(username, str):  # проверка типа
            self._username_ = username  #Задаем имя пользователя
        else:
            raise("Имя пользователя должно быть строкой", TypeError)

        self.userpassword = Password()
        self._cart_ = Cart()



    def __str__(self) -> str:
        return f"{self._id_}_{self._username_}"

    def __repr__(self) -> str:
        return f"User={self._id_}, name={self._username_})"


# Класс Store

class Store():
    def __init__(self):
        user_1 = str(input("Добрый день!\nВы попали в магазин Продуктовых товаров\nВведите свой username :\n"))
        user1 = User(user_1)
        print("Вы успешно зарегистрировались в Магазине\n", "Ваш пользователь:", user1._username_)
        print("Ваша корзина товаров выглядит вот так:\n", user1._cart_.__str__())

        frog = "in"
        while frog != "out":
            prod = Store.add_product(self)
            print(f"Хотите добавить случайны продукт {prod} к себе в корзину?")
            if_or_no = str(input("Введите Да или Yes:\n"))
            if (if_or_no == "Да") or (if_or_no == "Yes"):
                user1._cart_.add(prod, 1)
                print("Ваша корзина товаров выглядит вот так:\n", user1._cart_.__str__())
            else:
                frog = "out"
                print("Спасибо за посещение нашего магазина")

    def add_product(self):
        prod1 = Product(get_product(), get_price(), get_rating())
        return prod1.__repr__()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Store()
