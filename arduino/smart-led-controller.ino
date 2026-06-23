void setup() {
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);

  Serial.begin(9600);
}

void loop() {

  if (Serial.available()) {

    char command = Serial.read();

    switch(command) {

      case 'A':
        digitalWrite(8, HIGH);
        break;

      case 'a':
        digitalWrite(8, LOW);
        break;

      case 'B':
        digitalWrite(9, HIGH);
        break;

      case 'b':
        digitalWrite(9, LOW);
        break;

      case 'C':
        digitalWrite(10, HIGH);
        break;

      case 'c':
        digitalWrite(10, LOW);
        break;
    }
  }
}