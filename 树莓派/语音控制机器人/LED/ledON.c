//LED������gpio0��17������
#include <wiringPi.h>
void main()
{
        wiringPiSetup();
        pinMode(0,OUTPUT);
	digitalWrite(0,LOW);
	delay(500);
	digitalWrite(0,HIGH);
 
}
