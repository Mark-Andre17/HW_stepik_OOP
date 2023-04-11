# В этом задании создайте класс банковского счёта, который имеет два атрибута:
#
# * owner - владелец
# * balance - баланс
#
# и два метода:
#
# * deposit - внести средства
# * withdraw - снять средства
#
# Дополнительное условие - сумма снятия не должна превышать доступный баланс.
#
# Создайте экземпляр класса, сделайте несколько внесений и снятий средств, а также проверьте, что баланс счёта не
# может уходить в минус при снятии средств.

class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def add_deposit(self, deposit):
        self.balance = self.balance + deposit
        return f'Пополнение сделано'

    def get_withdraw(self, money):
        if self.balance < money:
            return f'Снять наличные невозможно'
        else:
            self.balance = self.balance - money
            return f'Вы сняли {money}. На счете осталось {self.balance}'

    def __str__(self):
        return f'Владелец счета: {self.owner}\nБаланс счета: {self.balance}'



