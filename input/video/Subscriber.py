import paho.mqtt.client as mqtt 
import camera

SERVER_HOST = '192.168.0.10'
BROKER_HOST = '218.38.254.30'
PORT = 5000
door_topic='door/#'

# 브로커 접속 시도 결과 처리 콜백 함수
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    if rc == 0:
        client.subscribe(door_topic)  # 연결 성공시 토픽 구독 신청
    else:
        print('연결 실패 : ', rc)


# 관련 토픽 메세지 수신 콜백 함수
def on_message(client, userdata, msg):
    print('111111111111')
    print(msg.topic+" "+str(msg.payload))
    print('2222222222222')

    if msg.payload == b'on':
        camera.camera(SERVER_HOST, PORT)

if __name__ == '__main__':
    print('start sub...')
    # 1. MQTT 클라이언트 객체 인스턴스화
    client = mqtt.Client()

    # 2. 관련 이벤트에 대한 콜백 함수 등록
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        # 3. 브로커 연결
        client.connect(BROKER_HOST)

        # 4. 메세지 루프 - 이벤트 발생시 해당 콜백 함수 호출됨
        client.loop_forever()

    except Exception as err:
        print('에러 : %s' % err)
