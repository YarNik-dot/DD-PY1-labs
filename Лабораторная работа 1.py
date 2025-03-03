import doctest

class Furniture:
    """
      Класс, представляющий предмет мебели.

      Aтрибуты:
          material (str): Основной материал из которого изготовлена мебель.
          weight (float): Вес мебели в килограммах.
          dimensions (tuple[float, float, float]): Размеры мебели (длина, ширина, высота) в метрах.
      """

    def __init__(self, material: str, weight: float, dimensions: tuple[float, float, float]):
        if weight < 0:
            raise ValueError("Вес должен быть неотрицательным значением")
        if any(dim < 0 for dim in dimensions):
            raise ValueError("Размеры должны быть неотрицательными величинами")

        self.material = material
        self.weight = weight
        self.dimensions = dimensions

    def move(self) -> None:
        """
         Имитируется перемещение мебели.

         Пример:
            >>> f = Furniture("дерево", 10, (1.0, 0.5, 0.7))
            >>> f.move()
            Перемещение мебели...
         """
        print("Перемещение мебели...")

    def display_info(self) -> str:
        """
         Возвращает строку, описывающую мебель и ее атрибуты.

        Пример:
            >>> f = Furniture("металл", 20.5, (1.5, 0.8, 1.0))
            >>> f.display_info()
            'Эта мебель сделана из металла, весит 20,5 кг и имеет размеры (1,5, 0,8, 1,0) метра».
        """
        return f"Эта мебель сделана из {self.material}, весит {self.weight} кг и имеет размеры {self.dimensions} метра"


class Tree:
    """
    Класс "Дерево".

    Атрибуты:
        species (str): Вид дерева (например, "дуб", "клён").
        height (float): Высота дерева в метрах.
        age (int): Возраст дерева в годах.
    """

    def __init__(self, species: str, height: float, age: int):

        if height < 0:
            raise ValueError("Высота должна быть неотрицательным значением")
        if age < 0:
            raise ValueError("Возраст должен быть неотрицательным значением")

        self.species = species
        self.height = height
        self.age = age

    def grow(self, meters: float) -> None:
        """
        Моделирует рост дерева, увеличивая его высоту.

         Пример:
             >>> t = Tree("сосна", 5.0, 10)
             >>> t.grow(2)
             Дерево выросло на 2,0 метра
         """
        if meters < 0:
            raise ValueError("Рост должен быть неотрицательным значением")

        self.height += meters
        print(f"Дерево выросло на {meters} метра")

    def get_age(self) -> int:
        """
         Возвращает возраст дерева.

         Пример:
            >>> t = Tree("берёза", 8.0, 25)
            >>> t.get_age()
            25
        """
        return self.age

    def display_tree_info(self) -> str:
        """
        Возвращает строку, описывающую дерево и его атрибуты.

        Example:
           >>> t = Tree("дуб", 12.3, 75)
           >>> t.display_tree_info()
           'Дерево - дуб, его высота 12.3 метра, возраст 75 лет.'
        """
        return f"Дерево - {self.species}, его высота {self.height} метров, возраст {self.age} лет."


class SocialNetwork:
    """
    Класс, представляющий социальную сеть.

    Атрибуты:
        name (str): Название социальной сети.
        user_count (int): Количество пользователей.
        average_activity (float): Средний балл активности пользователей (например, по шкале 0-100).
    """

    def __init__(self, name: str, user_count: int, average_activity: float):
        if user_count < 0:
            raise ValueError("Количество пользователей должно быть неотрицательным значением")
        if average_activity < 0:
            raise ValueError("Средняя активность должна быть неотрицательной величиной")

        self.name = name
        self.user_count = user_count
        self.average_activity = average_activity

    def add_user(self, count: int) -> None:
        """
         Симулирует добавление нового пользователя путем увеличения user_count.

         Пример:
             >>> sn = SocialNetwork("Instagram", 10000, 40.2)
             >>> sn.add_user(100)
             Добавление 100 пользователей. Новое количество пользователей: 10100
         """
        if count < 0:
            raise ValueError("Количество должно быть неотрицательным значением")
        self.user_count += count
        print(f"Добавление {count} пользователей. Новое количество пользователей: {self.user_count}")

    def get_user_count(self) -> int:
        """
         Возвращает количество пользователей
         Пример:
            >>> sn = SocialNetwork("Twitter", 50000, 60.5)
            >>> sn.get_user_count()
            50000
         """
        return self.user_count

    def display_network_info(self) -> str:
        """
          Возвращает строку, описывающую социальную сеть и ее атрибуты.

        Пример:
           >>> sn = SocialNetwork("Facebook", 2000000, 75.2)
           >>> sn.display_network_info()
           'Социальная сеть Facebook имеет 2000000 пользователей и среднюю активность 75.2.'
        """
        return f"Социальная сеть {self.name} имеет {self.user_count} пользователей и среднюю активность {self.average_activity}."


if __name__ == "__main__":
    doctest.testmod()
