from typing import List


class Shape:
    """
    Базовый класс для геометрических фигур.

    Attributes:
        name (str): Название фигуры.
    """

    def __init__(self, name: str) -> None:
        """
        Инициализирует экземпляр класса Shape.
        """
        self.name = name
        self._color: str = "black"  # Инкапсуляция: Цвет фигуры может меняться, но не напрямую.

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Shape.
        """
        return f"Фигура: {self.name}, Цвет: {self._color}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Shape для отладки.
        """
        return f"Shape(name='{self.name}', color='{self._color}')"

    def area(self) -> float:
        """
        Вычисляет площадь фигуры (по умолчанию возвращает 0).
        """
        return 0.0

    def describe(self) -> str:
        """
        Описывает фигуру.
        """
        return f"Это геометрическая фигура под названием {self.name}."

    def set_color(self, color: str) -> None:
        """
        Устанавливает цвет фигуры.
        """
        self._color = color

    def get_color(self) -> str:
        """
        Возвращает цвет фигуры.
        """
        return self._color


class Circle(Shape):
    """
    Класс, представляющий круг, наследник класса Shape.

    Attributes:
        name (str): Название фигуры (всегда "Круг").
        radius (float): Радиус круга.
    """

    def __init__(self, radius: float) -> None:
        """
        Инициализирует экземпляр класса Circle.
        Расширяет конструктор базового класса, добавляя атрибут радиус.
        """
        super().__init__(name="Круг")
        self.radius = radius

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Circle.
        Перегружает метод базового класса, добавляя информацию о радиусе.
        """
        return f"{super().__str__()}, Радиус: {self.radius}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Circle для отладки.
        Перегружает метод базового класса, добавляя информацию о радиусе.
        """
        return f"Circle(radius={self.radius}, color = {self._color})"

    def area(self) -> float:
        """
        Вычисляет площадь круга.
        Перегружает метод базового класса, предоставляя конкретную реализацию для круга.
        """
        return 3.14159 * self.radius * self.radius

    def describe(self) -> str:
        """
        Описывает круг.
        Перегружает метод базового класса, добавляя информацию о радиусе.
        """
        return f"Это круг радиусом {self.radius}."

    def get_circumference(self) -> float:
        """
        Вычисляет длину окружности круга.
        """
        return 2 * 3.14159 * self.radius

    def set_color(self, color: str) -> None:
        """
        Устанавливает цвет круга.
        Перегружает метод базового класса, чтобы добавить проверку на допустимый цвет.
        """
        if color in ["red", "green", "blue"]:
            self._color = color
        else:
            print("Недопустимый цвет для круга.")


if __name__ == "__main__":
    shape = Shape("Неопределенная фигура")
    print(shape)
    print(repr(shape))
    print(shape.area())
    print(shape.describe())
    shape.set_color("yellow")
    print(shape)

    circle = Circle(radius=5.0)
    print(circle)
    print(repr(circle))
    print(circle.area())
    print(circle.describe())
    print(circle.get_circumference())
    circle.set_color("red")
    print(circle)
    circle.set_color("purple")  # Попытка установить недопустимый цвет
    print(circle)
    print(circle.get_color())