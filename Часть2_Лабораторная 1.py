class AppleBasket:
    def __init__(self, apple_count: int, max_capacity: int):
        """
        Создание корзины с яблоками.

        :param apple_count: Количество яблок в корзине
        :param max_capacity: Максимальная вместимость корзины

        Примеры:
        >>> basket = AppleBasket(10, 20)  # Инициализация корзины с 10 яблоками и максимальной вместимостью 20
        """
        if not isinstance(apple_count, int):
            raise TypeError("Количество яблок должно быть целым числом")
        if apple_count < 0:
            raise ValueError("Количество яблок не может быть отрицательным числом")
        if not isinstance(max_capacity, int):
            raise TypeError("Максимальная вместимость должна быть целым числом")
        if max_capacity <= 0:
            raise ValueError("Максимальная вместимость должна быть положительным числом")
        self.apple_count = apple_count
        self.max_capacity = max_capacity

    def add_apples(self, count: int) -> None:
        """
        Добавление яблок в корзину.

        :param count: Количество добавляемых яблок

        :raise ValueError: Если количество добавляемых яблок превышает оставшуюся вместимость корзины
        """
        if not isinstance(count, int):
            raise TypeError("Количество добавляемых яблок должно быть целым числом")
        if count < 0:
            raise ValueError("Количество добавляемых яблок не может быть отрицательным числом")
        if self.apple_count + count > self.max_capacity:
            raise ValueError("Превышена максимальная вместимость корзины")
        self.apple_count += count

    def remove_apples(self, count: int) -> None:
        """
        Удаление яблок из корзины.

        :param count: Количество удаляемых яблок

        :raise ValueError: Если количество удаляемых яблок превышает количество яблок в корзине
        """
        if not isinstance(count, int):
            raise TypeError("Количество удаляемых яблок должно быть целым числом")
        if count < 0:
            raise ValueError("Количество удаляемых яблок не может быть отрицательным числом")
        if self.apple_count - count < 0:
            raise ValueError("Нельзя удалить больше яблок, чем есть в корзине")
        self.apple_count -= count

    def get_remaining_capacity(self) -> int:
        """
        Получение оставшейся вместимости корзины.

        :return: Оставшаяся вместимость корзины
        """
        return self.max_capacity - self.apple_count


class BananaBasket:
    def __init__(self, banana_count: int, max_capacity: int):
        """
        Создание корзины с бананами.

        :param banana_count: Количество бананов в корзине
        :param max_capacity: Максимальная вместимость корзины

        Примеры:
        >>> basket = BananaBasket(15, 30)  # Инициализация корзины с 15 бананами и максимальной вместимостью 30
        """
        if not isinstance(banana_count, int):
            raise TypeError("Количество бананов должно быть целым числом")
        if banana_count < 0:
            raise ValueError("Количество бананов не может быть отрицательным числом")
        if not isinstance(max_capacity, int):
            raise TypeError("Максимальная вместимость должна быть целым числом")
        if max_capacity <= 0:
            raise ValueError("Максимальная вместимость должна быть положительным числом")
        self.banana_count = banana_count
        self.max_capacity = max_capacity

    def add_bananas(self, count: int) -> None:
        """
        Добавление бананов в корзину.

        :param count: Количество добавляемых бананов

        :raise ValueError: Если количество добавляемых бананов превышает оставшуюся вместимость корзины
        """
        if not isinstance(count, int):
            raise TypeError("Количество добавляемых бананов должно быть целым числом")
        if count < 0:
            raise ValueError("Количество добавляемых бананов не может быть отрицательным числом")
        if self.banana_count + count > self.max_capacity:
            raise ValueError("Превышена максимальная вместимость корзины")
        self.banana_count += count

    def remove_bananas(self, count: int) -> None:
        """
        Удаление бананов из корзины.

        :param count: Количество удаляемых бананов

        :raise ValueError: Если количество удаляемых бананов превышает количество бананов в корзине
        """
        if not isinstance(count, int):
            raise TypeError("Количество удаляемых бананов должно быть целым числом")
        if count < 0:
            raise ValueError("Количество удаляемых бананов не может быть отрицательным числом")
        if self.banana_count - count < 0:
            raise ValueError("Нельзя удалить больше бананов, чем есть в корзине")
        self.banana_count -= count

    def get_remaining_capacity(self) -> int:
        """
        Получение оставшейся вместимости корзины.

        :return: Оставшаяся вместимость корзины
        """
        return self.max_capacity - self.banana_count


class WatermelonBasket:
    def __init__(self, watermelon_count: int, max_capacity: int):
        """
        Создание корзины с арбузами.
