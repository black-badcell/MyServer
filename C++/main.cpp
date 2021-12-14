#include <ctime>
#include <iostream>
#include <string>

int countAngle(int h, int m) {
    int angle = abs((h % 12) * 30 - m * 6);
    return std::min(angle, 360 - angle);
}

int getAngle() {
    std::time_t t = std::time(0);
    std::tm* now = std::localtime(&t);

    return countAngle(now->tm_hour, now->tm_min);
}

int getDefinedAngle(std::string time) {
    int hour = std::stoi(time.substr(0, time.find(':')));
    int minute = std::stoi(time.substr(time.find(':') + 1));

    return countAngle(hour, minute);
}