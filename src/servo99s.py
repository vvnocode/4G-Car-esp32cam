# 99s舵机
from machine import Pin, PWM

# 定义舵机参数
angle_min = 0  # 最小角度
angle_max = 120  # 最大角度
neutral_pulse_width = 1500  # 中立点脉冲宽度（微秒）
frequency = 300  # PWM频率（赫兹）
width_min = 0.5  # 最低脉冲宽度 毫秒
width_max = 2.5  # 最低脉冲宽度 毫秒
period = 1000 / 300.0  # 脉冲周期 毫秒

pwm_pin = Pin(14, Pin.OUT)  # 使用GPIO15作为PWM输出引脚
pwm = PWM(pwm_pin, freq=frequency)
pwm_range = 1023

angle_left = 0  # 最左边角度，和结构有关，固定
angle_wright = 0  # 最左边角度，和结构有关，固定

left_max = 5430
middle = 4650
right_max = 3590


def turn(scale):
    if scale > left_max:
        scale = left_max
    elif scale < right_max:
        scale = right_max
    turn_scale = int(scale)
    pwm.duty_u16(turn_scale)


# 百分比转向
def turn_percent(percent):
    if not isinstance(percent, int) or percent == 0:
        print("回正")
        turn(middle)
    # 左
    elif percent < 0:
        print("左")
        turn((left_max - middle) * (-percent) / 100 + middle)
    # 右
    else:
        print("右")
        turn(middle - (middle - right_max) * percent / 100)
