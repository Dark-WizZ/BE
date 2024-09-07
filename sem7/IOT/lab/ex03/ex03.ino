// INPUT = 0; OUTPUT = 1; LOW = 0; HIGH = 1;
int echoPin = 3;
int trigPin = 2;
int buzzer = 8;
int led1 = 13;
int led2 = 12;
float distance;
void setup() {
  pinMode(trigPin, 1);
  pinMode(echoPin, 0);
  Serial.begin(115200);
  pinMode(buzzer, 1);
  pinMode(led1, 1);
  pinMode(led2, 1);
  Serial.println("Distance Measure Program: ");
}


void loop() {
  digitalWrite(trigPin, 0);
  delayMicroseconds(2);
  digitalWrite(trigPin, 1);
  delayMicroseconds(10);
  digitalWrite(trigPin, 0);
  distance  = pulseIn(echoPin, 1) * 0.034 / 2;
  Serial.println("Distance: " + String(distance) + " cm");
  digitalWrite(led1, 0);
  digitalWrite(led2, 0);
  digitalWrite(buzzer, 0);

  if(distance <= 10){
    Serial.println("very close");
    digitalWrite(led2, 1);    
    digitalWrite(buzzer, 1);
  }else if(distance <= 50){
    Serial.println("Near Range");
    digitalWrite(led1, 1);    
  }else{
    Serial.println("Far Range");
  }

  delay(500);
}
