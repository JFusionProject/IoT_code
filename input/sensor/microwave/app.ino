#include <MqttCom.h>
#include <Sensor.h>


const char *ssid = "TECH2_2G";
const char *password = "tech21234!";
const char *server =  "172.30.1.14";
// const char *ssid = "TECH2_2G";
// const char *password = "tech21234!";
// const char *server =  "172.30.1.107";
const char *pub_topic = "input/lift/wave";

MqttCom com(ssid, password);
Sensor sensor(D6);

void publishWorking() {
  com.publish("input/lift/work", "working on");
}

ICACHE_RAM_ATTR void publish_sensor(){
  com.publish(pub_topic, "close");
}


void setup()
{
  Serial.begin(115200);
  com.init(server);                         // publish만 실행
  com.setInterval(30000, publishWorking);   // 센서 작동 확인
  sensor.setCallback(publish_sensor);       // 센서 감지 시 콜백
}

void loop()
{
  com.run();
  sensor.attachInterrupt(publish_sensor, RISING);
}