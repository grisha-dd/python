# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод. Задачу
# можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.
from tkinter import Tk, Canvas, Frame, BOTH, Button


class TrafficLight(Frame):

    def __init__(self):
        super().__init__()
        self.__color = -1

        self.master.title("Светофор")
        self.pack(fill=BOTH, expand=1)

        self.window = Canvas(self)
        self.window.create_rectangle(100, 390, 200, 70, fill="black")
        r_light = self.window.create_oval(110, 160, 190, 80, fill="grey")
        y_light = self.window.create_oval(110, 270, 190, 190, fill="grey")
        g_light = self.window.create_oval(110, 380, 190, 300, fill="grey")
        self.light_list = [r_light, y_light, g_light, y_light]
        self.color_list = ["red", "yellow", "green", "yellow"]

        self.window.pack(fill=BOTH, expand=1)

        startButton = Button(self, text="Поехали!", command=self.running)
        startButton.place(x=40, y=20)

        quitButton = Button(self, text="Остановить", command=self.quit)
        quitButton.place(x=200, y=20)

    def running(self):
        self.__color = (self.__color + 1) % 4
        self.window.itemconfig(self.light_list[self.__color], fill=self.color_list[self.__color])
        self.window.itemconfig(self.light_list[self.__color - 1], fill="grey")
        if self.__color == 1 or self.__color == 3:
            self.window.after(2000, self.running)
        else:
            self.window.after(7000, self.running)


def main():
    root = Tk()
    TrafficLight()
    root.geometry('300x400')
    root.mainloop()


if __name__ == '__main__':
    main()
