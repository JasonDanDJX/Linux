//LED正极接gpio0即17号引脚
#include <wiringPi.h>
void main()
{
        wiringPiSetup();
        pinMode(0,OUTPUT);
        digitalWrite(0,HIGH);
        delay(500);
        digitalWrite(0,LOW);

}

