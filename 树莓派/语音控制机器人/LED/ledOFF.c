//LED������gpio0��17������
#include <wiringPi.h>
void main()
{
        wiringPiSetup();
        pinMode(0,OUTPUT);
        digitalWrite(0,HIGH);
        delay(500);
        digitalWrite(0,LOW);

}

