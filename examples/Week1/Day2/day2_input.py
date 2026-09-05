from openmechanicalai import calculate_output_speed
speed=float(input("Enter the input speed in RPM: "))
gear_ratio=float(input("Enter the gear ratio: "))
output_speed = calculate_output_speed(speed, gear_ratio)
print(f"The output speed is: {output_speed:.2f} RPM")
