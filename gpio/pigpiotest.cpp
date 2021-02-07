#include <stdio.h>
#include <pigpio.h>

int main(int argc, char *argv[])
{
	gpioInitialise();
	gpioTerminate();

	return 0;
}
