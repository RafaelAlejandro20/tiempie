#include <DHT.h>
#define DHTTYPE DHT11
#define DHTPIN 8

DHT dht(DHTPIN,DHTTYPE);
void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(9,OUTPUT);
}
void loop() {
  delay(1000);
  float hum = dht.readHumidity();
  float tem = dht.readTemperature(); 
  if(isnan(hum) || isnan(tem)){
    Serial.println("Error en el sensor");
    return;
  }
  Serial.print(tem);
  Serial.print(",");
  Serial.println(hum);
}
