def calculate_output_speed(input_speed, gear_ratio):
    """
    Calculate the output speed of a mechanical system based on input speed and gear ratio.

    Parameters:
    input_speed (float): The speed of the input shaft in RPM (revolutions per minute).
    gear_ratio (float): The ratio of the gears (output gear teeth / input gear teeth).

    Returns:
    float: The output speed in RPM.
    """
    if gear_ratio == 0:
        raise ValueError("Gear ratio cannot be zero.")
    
    output_speed = input_speed * gear_ratio
    return output_speed

import math
def calculate_output_torque(power, speed):
    """
    Calculate the output torque of a mechanical system based on power and speed.

    Parameters:
    power (float): The power in watts.
    speed (float): The speed in RPM (revolutions per minute).

    Returns:
    float: The output torque in Newton-meters (Nm).
    """
    if speed == 0:
        raise ValueError("Speed cannot be zero.")
    
    # Convert speed from RPM to radians per second
    speed_rad_per_sec = (speed * 2 * math.pi) / 60
    torque = power / speed_rad_per_sec
    return torque

def calculate_linear_speed(speed, diameter):
    """
    Calculate the linear speed of a point on the circumference of a rotating object.

    Parameters:
    speed (float): The rotational speed in RPM (revolutions per minute).
    diameter (float): The diameter of the rotating object in meters.

    Returns:
    float: The linear speed in meters per second (m/s).
    """
    if diameter <= 0:
        raise ValueError("Diameter must be greater than zero.")
    
    # Convert speed from RPM to revolutions per second
    speed_rps = speed / 60
    # Calculate circumference
    circumference = math.pi * diameter
    # Calculate linear speed
    linear_speed = speed_rps * circumference
    return linear_speed

def main():
    # Example usage of the functions
    input_speed = 1500  # RPM
    gear_ratio = 2.5
    power = 500  # Watts
    diameter = 0.5  # meters

    output_speed = calculate_output_speed(input_speed, gear_ratio)
    print(f"Output Speed: {output_speed} RPM")

    output_torque = calculate_output_torque(power, output_speed)
    print(f"Output Torque: {output_torque} Nm")

    linear_speed = calculate_linear_speed(output_speed, diameter)
    print(f"Linear Speed: {linear_speed} m/s")

if __name__ == "__main__":
    main()

