import ujson
import enums
import servos
import motor
import sys

# esp32cam中，板子上的 GPIO = PIN
# GPIO 2/12/13/14/15 支持 PWM 输出因此被用于电机驱动相关的设计中
# GPIO 4 也支持 PWM 输出，是本设计中灯光（开发板自带）的控制口

def detail(topic, msg):
    # 解析报文
    json_data = ujson.loads(msg)
    print(json_data)
    event = json_data.get("event")
    data = json_data.get("data")
    # 处理事件
    if event == enums.STOP:
        print("退出")
        sys.exit(0)
    if event == enums.TURN:
        servos.s_17g.set_angle(data)
    elif event == enums.RUN:
        motor.run_percent(data)
    elif event == enums.LIGHT:
        print()
