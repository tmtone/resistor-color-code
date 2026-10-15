import sys

# digit value for each color (bands 1, 2, and 3 on 5-band resistors)
DIGITS = {
    "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
    "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9,
}

# multiplier band
MULTIPLIER = {
    "black": 1, "brown": 10, "red": 100, "orange": 1000,
    "yellow": 10000, "green": 100000, "blue": 1000000,
    "gold": 0.1, "silver": 0.01,
}

# tolerance band in percent
TOLERANCE = {
    "brown": 1, "red": 2, "green": 0.5, "blue": 0.25,
    "violet": 0.1, "gray": 0.05, "gold": 5, "silver": 10,
}


def normalize(color):
    """lowercase, no extra spaces, grey works too"""
    color = color.strip().lower()
    return color.replace("grey", "gray")


def calculate(colors):
    """returns (ohms, tolerance in %)"""
    if len(colors) not in (4, 5):
        raise ValueError("enter 4 or 5 colors")

    *digit_bands, multi_band, tol_band = colors

    number = 0
    for color in digit_bands:
        if color not in DIGITS:
            raise ValueError(f"'{color}' isnt a valid digit band")
        number = number * 10 + DIGITS[color]

    if multi_band not in MULTIPLIER:
        raise ValueError(f"'{multi_band}' isnt a valid multiplier band")
    if tol_band not in TOLERANCE:
        raise ValueError(f"'{tol_band}' isnt a valid tolerance band")

    value = number * MULTIPLIER[multi_band]
    return value, TOLERANCE[tol_band]


def pretty(ohms):
    """470 -> '470 Ω', 4700 -> '4.7 kΩ', 1000000 -> '1 MΩ'"""
    if ohms >= 1000000:
        return f"{ohms / 1000000:g} MΩ"
    if ohms >= 1000:
        return f"{ohms / 1000:g} kΩ"
    return f"{ohms:g} Ω"


def main():
    raw = input("Colors (e.g. yellow violet brown gold): ")
    colors = [normalize(c) for c in raw.split()]

    try:
        value, tolerance = calculate(colors)
    except ValueError as err:
        print(f"Error: {err}")
        sys.exit(1)

    low = value * (1 - tolerance / 100)
    high = value * (1 + tolerance / 100)
    print(f"Value: {pretty(value)} ±{tolerance} %")
    print(f"Allowed: {pretty(low)} to {pretty(high)}")

    measured_raw = input("Measured value in ohms (Enter to skip): ").strip()
    if measured_raw:
        measured = float(measured_raw.replace(",", "."))
        if low <= measured <= high:
            print(f"{pretty(measured)} is within tolerance.")
        else:
            print(f"{pretty(measured)} is NOT within tolerance.")


if __name__ == "__main__":
    main()
