from gpiozero import LED, Button
from time import sleep, time
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
start_time = time()

# 按键触发函数
def pressed(button):
    global start_time
    reaction_time = round(time() - start_time, 3)
    
    if button.pin.number == 14:
        print(left_name + ' won the game')
    else:
        print(right_name + ' won the game')
    
    print('反应时间：' + str(reaction_time) + ' 秒')
    exit()

# 绑定按键事件
right_button.when_pressed = pressed
left_button.when_pressed = pressed

# 保持程序运行
sleep(30)
