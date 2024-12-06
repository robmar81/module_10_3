import threading
import random
import time


class Bank:
    def __init__(self, balance=500):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            a = random.randint(50, 500)
            self.lock.acquire()
            if self.balance >= 500 and self.lock == self.lock.locked():
                self.lock.release()
            self.balance += a
            self.lock.release()
            print(f'Пополнение: {a}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            b = random.randint(50, 500)
            print(f'Запрос на {b}')
            if b <= self.balance:
                with self.lock:
                    self.balance -= b
                print(f'Снятие: {b}. Баланс: {self.balance}')
                time.sleep(0.001)
            elif b > self.balance:
                print(f'Запрос отклонен, недостаточно средств')


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
