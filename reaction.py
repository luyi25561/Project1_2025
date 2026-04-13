from gpiozero import LED, Button
from time import sleep, time
from random import uniform

# 硬件定义
led = LED(4)
left_button = Button(14)
right_button = Button(15)

# 玩家名称
left_name = input('left player name is ')
right_name = input('right player name is ')

# 计分
left_score = 0
right_score = 0

# 记录开始时间
start_time = 0

def pressed(button):
    global left_score, right_score, start_time
    
    # 计算反应时间
    reaction_time = round(time() - start_time, 3)
    
    # 判断获胜者并加分
    if button.pin.number == 14:
        print(left_name + ' won the game!')
        left_score += 1
    else:
        print(right_name + ' won the game!')
        right_score += 1
    
    # 显示成绩与反应时间
    print('Reaction time: ' + str(reaction_time) + ' seconds')
    print('Current Score -- ' + left_name + ': ' + str(left_score) + ' | ' + right_name + ': ' + str(_right_score))
    
    # 下一轮准备
    print('\nNext round starting... Get ready!\n')
    led.on()
    sleep(uniform(5, 10))
    led.off()
    start_time = time()
    print('GO!')

# 绑定按键
right_button.when_pressed = pressed
left_button.when_pressed = pressed

# 游戏开始
print('Game starting... Get ready!')
led.on()
sleep(uniform(5, 10))
led.off()
start_time = time()
print('GO!')

# 保持程序运行
while True:
    sleep(1)
