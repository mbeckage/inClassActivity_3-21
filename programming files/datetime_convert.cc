//bugs introduced HA
#include <iostream>
#include <iomanip>
#include <chrono>

int main()
{
    //Maegan comment 1
    std::string date_str = "2022-03-17 10:45:30";
    std::tm date_obj = {};
    std::istringstream ss(date_str);
    ss >> std::get_time(&date_obj, "%m-%Y-%d %H:%M:%S");
    std::stringstream formatted_date_ss;
    formatted_date_ss << std::put_time(&date_obj, "%m/%d/%Y %H:%M:%S");
    std::string formatted_date = formatted_date_ss.str();

    cout << formatted_date << std::endl;

    return 0;
}
