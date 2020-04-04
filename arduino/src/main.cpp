#include "SevSeg.h"

SevSeg sevseg;
int number;
const int UNINITIALIZED = 10000;

void setup()
{
	// Setup serial
	Serial.begin(9600);

	// Setup 4 digits - 7 segments display
	byte numDigits = 4;
	byte digitPins[] = {10, 11, 12, 13};
	byte segmentPins[] = {9, 2, 3, 5, 6, 8, 7, 4};

	bool resistorsOnSegments = true;
	byte hardwareConfig = COMMON_CATHODE;
	sevseg.begin(hardwareConfig, numDigits, digitPins, segmentPins, resistorsOnSegments);
	sevseg.setBrightness(90);

	number = UNINITIALIZED;
}
void loop()
{
	if (Serial.available() > 0)
	{
		String data = Serial.readStringUntil('\n');
		number = data.toInt();
	}
	sevseg.setNumber(number, 0);
	sevseg.refreshDisplay();
}
