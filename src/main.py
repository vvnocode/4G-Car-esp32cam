import wifi
import mqtt
import udpclient


def main():
    # 联网
    wifi.do_connect()

    udpclient.send_udp()

    # mqtt
    mqtt.subscribe()


if __name__ == "__main__":
    main()
