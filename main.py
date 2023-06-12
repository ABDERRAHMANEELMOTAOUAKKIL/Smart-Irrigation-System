import random
import time

def read_moisture_sensor():
    # Simulate reading moisture level from the sensor
    # Replace this with your actual sensor reading code
    moisture_level = random.randint(0, 100)
    return moisture_level

def check_weather_conditions():
    # Simulate checking weather conditions
    # Replace this with your actual weather API or sensor integration
    weather_conditions = ['sunny', 'rainy', 'cloudy']
    current_weather = random.choice(weather_conditions)
    return current_weather

def irrigate():
    # Simulate irrigation process
    # Replace this with your actual irrigation mechanism control code
    print("Irrigation is running...")
    time.sleep(5)  # Simulate irrigation time
    print("Irrigation completed.")

def main():
    while True:
        moisture_level = read_moisture_sensor()
        current_weather = check_weather_conditions()

        print(f"Moisture Level: {moisture_level}")
        print(f"Weather Conditions: {current_weather}")

        if moisture_level < 50 and current_weather != 'rainy':
            irrigate()

        time.sleep(10)  # Delay between each iteration

if __name__ == '__main__':
    main()


