from kivy.app import App
from kivy.uix.button import Button
from winsound import Beep
import time

class MainApp(App):
    def Birthday(self):
        frequency = [392, 392, 440, 392, 523, 494,
                     392, 392, 440, 392, 587, 523,
                     392, 392, 784, 659, 523, 494, 440,
                     698, 698, 659, 523, 587, 523]
        delay = [375, 125, 500, 500, 500, 1000,
                 375, 125, 500, 500, 500, 1000,
                 375, 125, 500, 500, 500, 500, 1000,
                 375, 125, 500, 500, 500, 1000, ]
        for i in range(0, 25):
            Beep(frequency[i], delay[i])

    def run(self):
        name = input("亲，请告诉我你叫啥呗\n")

        age = int(input("名字都告诉我了，年龄也告诉我呗:\n"))

        time.sleep(1)
        print("接下来就是见证奇迹的时刻")
        time.sleep(3)
        for i in range(1, 667):
            print("{}个生日快乐！！！".format(i))
            time.sleep(0.01)

        print("我写了666个生日快乐来祝福你亲")
        time.sleep(3)
        print("这个程序可能略显简陋。。。")
        time.sleep(3)
        print("祝 {} 岁的 婷婷 永远开心快乐!".format(age / 2))
        time.sleep(3)
        print("岁数少一倍，快乐翻一倍哦亲~ ~ ~")
        time.sleep(3)
        print("为你献上最美的祝福亲~ ~ ~")
        time.sleep(3)

        ch = input("这份生日礼物还算满意嘛？输入y或n告诉我(注意大小写哦\n")
        while ch == 'Y' or ch == 'N':
            print("就知道你调皮，不是说了注意大小写嘛?给我重新输")
            ch = input()

        if ch == 'y':
            print("这么容易就满足啦？")
            time.sleep(3)
            print("快带上你的耳机")
            for i in range(1, 4):
                print(i)
                time.sleep(1)
        else:
            print("这你还不满足？")
            time.sleep(2)
            print("算啦算啦你是老大都依你，带上你的耳机")
        time.sleep(3)
        print("戴好了吗？那我放了哦~ ~ ~")
        while True:
            MainApp().Birthday()


MainApp().run()




