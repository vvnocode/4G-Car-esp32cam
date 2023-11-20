from machine import Pin, PWM


class Servo:
    def __init__(self, pin, frequency, min_us, max_us, min_angle, max_angle):
        # 创建一个PWM对象
        self.servo = PWM(Pin(pin, mode=Pin.OUT))

        # 舵机参数
        self.frequency = frequency  # 舵机的频率 300Hz
        self.period = 1000 * 1000 / self.frequency  # 舵机的周期 μs
        self.min_us = min_us  # 最小脉冲宽度 μs
        self.max_us = max_us  # 最大脉冲宽度 μs
        self.min_angle = min_angle  # 最小角度
        self.max_angle = max_angle  # 最大角度

        # 设置舵机的频率
        self.servo.freq(self.frequency)

    def set_angle(self, angle):
        # 将角度转换为脉冲宽度
        us = self.map_angle(angle, self.min_angle, self.max_angle, self.min_us, self.max_us)
        # 将脉冲宽度转换为duty
        duty = int(us / self.period * 1023)
        print("角度：{} 脉冲：{} 占空比：{} duty：{}".format(angle, us, us / self.period, duty))
        # 设置舵机的脉冲宽度
        self.servo.duty(duty)

    def map_angle(self, x, in_min, in_max, out_min, out_max):
        # 将一个数从一个范围映射到另一个范围
        return (x - in_min) / (in_max - in_min) * (out_max - out_min) + out_min
