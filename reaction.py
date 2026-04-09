# 快速反应游戏 - 优化前完整代码
from gpiozero import LED, Button
from time import sleep
from random import uniform

# 设置硬件引脚
led = LED(4)
left_button = Button(14)
right_button = Button(15)

# 输入玩家名字
left_name = input('left player name is ')
right_name = input('right player name is ')

# 游戏开始
led.on()
sleep(uniform(5, 10))
led.off()

# 按键触发函数
def pressed(button):
    if button.pin.number == 14:
        print(left_name + ' won the game')
    else:
        print(right_name + ' won the game')
    exit()

# 绑定按键事件
right_button.when_pressed = pressed
left_button.when_pressed = pressed