from machine import Pin, PWM
import time

# L298 参数
# PWM频率0-10KHz，限小脉宽10us
# 引脚从上到下
# 5V    5V
# EN1   EN2
# IN1   IN3
# IN2   IN4
# END   END
# ESP32CAM对应引脚
# EN1 -> IO12
# IN1 -> IO13
# EN2 -> IO15
# 改变方向必须刹车0.1秒以上

# 定义GPIO引脚
p_en1 = PWM(Pin(12, mode=Pin.OUT))
p_en1.freq(400)
p_in1 = Pin(13, mode=Pin.OUT)
p_in2 = Pin(15, mode=Pin.OUT)

# speed 0-1023
speed_max = 900
speed_current = 0
speed_add = 40

# 当前前进状态,0初始化;1前进;2后退;
run_status = 0


# 前进
def go(speed):
    run_check(1)
    p_in1.value(1)
    p_in2.value(0)
    duty = speed if speed < speed_max else speed_max
    print("前进 duty ", duty)
    p_en1.duty(duty)


# 后退
def back(speed):
    run_check(2)
    p_in1.value(0)
    p_in2.value(1)
    duty = speed if speed < speed_max else speed_max
    print("后退 duty ", duty)
    p_en1.duty(duty)


# 停止短暂
def stop_short():
    p_in1.value(0)
    p_in2.value(0)
    time.sleep_ms(300)


# 停止
def stop():
    p_in1.value(0)
    p_in2.value(0)


# 运行状态检测
def run_check(status):
    global run_status
    if run_status != status:
        stop_short()
    run_status = status


# 悬空
def space(ms):
    p_in1.value(1)
    p_in2.value(1)
    time.sleep_ms(ms)


# 前进加速
def go_speed_up():
    run_check(1)
    global speed_current
    speed_current += speed_add
    speed_current = speed_current if (0 < speed_current < speed_max) else (
        speed_max if speed_current > 0 else 0)
    go(speed_current)


# 前进减速
def go_slow_down():
    run_check(1)
    global speed_current
    speed_current -= speed_add
    speed_current = speed_current if (0 < speed_current < speed_max) else (
        speed_max if speed_current > 0 else 0)
    go(speed_current)


# 后退加速
def back_speed_up():
    run_check(2)
    global speed_current
    speed_current += speed_add
    speed_current = speed_current if (0 < speed_current < speed_max) else (
        speed_max if speed_current > 0 else 0)
    back(speed_current)


# 后退减速
def back_slow_down():
    run_check(2)
    global speed_current
    speed_current -= speed_add
    speed_current = speed_current if (0 < speed_current < speed_max) else (
        speed_max if speed_current > 0 else 0)
    back(speed_current)


# 百分比运动
def run_percent(percent):
    if not isinstance(percent, int) or percent == 0:
        print("空转")
        space(10)
    # 前进
    elif percent > 0:
        print("前进")
        go(int(speed_max * percent / 100))
    # 后退
    else:
        print("后退")
        back(int(- speed_max * percent / 100))
