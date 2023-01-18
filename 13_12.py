from threading import Thread, Condition, Lock
from time import sleep
from random import choice


class Writer(Thread):

    WRITING = .1 #Пишет 
    NOT_WRITE = 1 #Не пишет 

    def __init__(self, num_writer: int, text: str):
        super().__init__(name=num_writer)
        self.num_writer = num_writer
        self.text = text

    def run(self):
        global p, lock, сondition
        while True:
            lock.acquire()
            print('Писатель {0} сейчас будет писать: {1}'.format(self.num_writer, self.text))
            # lock.acquire()
            print('Писатель {0} начинает писать, убирает текст последнего писателя'.format(self.num_writer))
            p = ''
            for s in self.text:
                with сondition:
                    p += s
                    print('Писатель {0} пишет: {1}'.format(self.num_writer, p))
                    сondition.notify_all()    #разбудить все потоки, ожидающие этого условия.
                sleep(Writer.WRITING)
            print('Писатель {0} закончил писать: {1}'.format(self.num_writer, self.text))
            lock.release()
            sleep(Writer.NOT_WRITE)


class Reader(Thread):

    def __init__(self, num_writer: str):
        super().__init__(name=num_writer)
        self.num_writer = num_writer

    def run(self):
        global p, сondition
        while True:
            with сondition:
                сondition.wait() #подождать, пока не появится уведомление или пока не истечёт время ожидания.
                print('Читатель {0} читает: {1}'.format(self.num_writer, p))


READERS_NUMBER = 1
WRITERS_NUMBER = 5
TEXT = ['Красивое лучше, чем уродливое',
        'Явное лучше, чем неявное',
        'Простое лучше, чем сложное',
        'Сложное лучше, чем запутанное']

if __name__ == '__main__':
    lock = Lock()
    сondition = Condition(Lock()) #позволяют одному или нескольким потокам ждать, пока они не будут уведомлены другим потоком о его выполнении.
    for num in range(WRITERS_NUMBER):
        Writer(num, choice(TEXT)).start()
    for num in range(READERS_NUMBER):
        Reader(str(num)).start()
