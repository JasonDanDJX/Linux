//LED������gpio0��17������
#include <stdio.h>
#include <wiringPi.h>
int main(void)
{
	int i;
	wiringPiSetup();
	pinMode(0,OUTPUT);
	for(i = 0;i < 10;i++)
	{
		digitalWrite(0,HIGH);delay(500);
		digitalWrite(0,LOW);delay(500);
	}
}
