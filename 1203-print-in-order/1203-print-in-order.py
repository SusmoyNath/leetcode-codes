from threading import Lock

class Foo:
    def __init__(self):
        self.lock2 = Lock()
        self.lock3 = Lock()
        self.lock2.acquire()  # Lock second()
        self.lock3.acquire()  # Lock third()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.lock2.release()  # Unlock second()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.lock2.acquire()  # Wait until first() is done
        printSecond()
        self.lock3.release()  # Unlock third()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.lock3.acquire()  # Wait until second() is done
        printThird()
