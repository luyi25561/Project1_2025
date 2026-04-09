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

# 初始化双方分数为0
left_score = 0
right_score = 0

# -------------------------- 新增：无限循环（自动重开） --------------------------
while True:
    # 每局开始显示当前比分
    print(f"\n===== 新一局开始 =====")
    print(f"当前比分：{left_name} {left_score} 分 | {right_name} {right_score} 分")

# 游戏开始
led.on()
sleep(uniform(5, 10))
led.off()

# 按键触发函数
def pressed(button):
global left_score, right_score
    if button.pin.number == 14:
        print(left_name + ' won the game')
left_score += 1  # 左玩家加分

    else:
        print(right_name + ' won the game')
right_score += 1  # 右玩家加分
    exit()

# 绑定按键事件
right_button.when_pressed = pressed
left_button.when_pressed = pressed
# 新增：每局结束后等待1.5秒，再开下一局，避免误触
    sleep(1.5)
