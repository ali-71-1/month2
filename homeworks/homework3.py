# homework_3.py

# Константа стоимости одной поездки
TRIP_COST = 20


class TransportCard:
    def __init__(self, owner: str):
        self.__owner = owner
        self.__balance = 0

    def get_owner(self) -> str:
        """Возвращает имя владельца карты."""
        return self.__owner

    def get_balance(self) -> float:
        """Возвращает текущий баланс карты."""
        return self.__balance

    def add_money(self, amount: float) -> None:
        """Пополняет баланс карты."""
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше нуля!")

        self.__balance += amount
        print(f"Карта {self.__owner}: успешно пополнена на {amount} сом. Текущий баланс: {self.__balance} сом.")

    def pay_for_trip(self) -> None:
        """Оплачивает одну поездку."""
        if self.__balance < TRIP_COST:
            raise ValueError(
                f"Недостаточно средств на карте {self.__owner}! "
                f"Баланс: {self.__balance} сом, стоимость поездки: {TRIP_COST} сом."
            )

        self.__balance -= TRIP_COST
        print(f"Карта {self.__owner}: поездка оплачена ({TRIP_COST} сом). Остаток: {self.__balance} сом.")


# ==========================================
# Демонстрация работы программы
# ==========================================
if __name__ == "__main__":
    print("--- Создание карт ---")
    card1 = TransportCard("Айбек")
    card2 = TransportCard("Елена")

    print(f"Владелец карты 1: {card1.get_owner()}, начальный баланс: {card1.get_balance()} сом")
    print(f"Владелец карты 2: {card2.get_owner()}, начальный баланс: {card2.get_balance()} сом\n")

    print("--- Пополнение баланса ---")
    card1.add_money(50)
    card2.add_money(20)
    print()

    print("--- Оплата поездок ---")
    # Айбек делает 2 поездки (50 - 20 - 20 = 10)
    card1.pay_for_trip()
    card1.pay_for_trip()

    # Елена делает 1 поездку (20 - 20 = 0)
    card2.pay_for_trip()
    print()

    print("--- Демонстрация обработки ошибок (try/except) ---")

    # Ошибка 1: Попытка пополнить карту на нулевую или отрицательную сумму
    try:
        print("Попытка пополнить карту на -10 сом:")
        card1.add_money(-10)
    except ValueError as e:
        print(f"Ошибка: {e}\n")

    # Ошибка 2: Попытка оплатить поездку при недостаточном балансе
    try:
        print(f"Попытка оплаты картой Елены (баланс: {card2.get_balance()} сом):")
        card2.pay_for_trip()
    except ValueError as e:
        print(f"Ошибка: {e}\n")

    print("--- Финальное состояние карт ---")
    print(f"Владелец: {card1.get_owner()} | Итоговый баланс: {card1.get_balance()} сом")
    print(f"Владелец: {card2.get_owner()} | Итоговый баланс: {card2.get_balance()} сом")