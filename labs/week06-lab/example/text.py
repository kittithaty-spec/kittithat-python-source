def get_circle_info(radius):
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

print("Circle calculations:")
radius = 5
area, circumference = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()

"""
เขียน Function แปลงหน่วยสกุลเงิน ที่แปลจาก
THB <-> USD 1 USD = 32 THB

โดยใช้ชื่อและการใช้งาน
Function convert_currency(100, "USD)
"""
def THB_to_USD(USD):
    THB = USD / 32
    return THB

def USD_to_THB(THB):
    USD = THB * 32
    return USD

def THB_to_JPY(JPY):
    THB = (JPY / 22) * 100
    return THB

def JPY_to_THB(THBJ):
    JPY = THBJ/100 * 22
    return JPY

def convert_currency(a, b):
    if b == "USD":
        result = THB_to_USD(a)
        return f"{a} THB = {result:.2f} USD"
    elif b == "THB":
        result = USD_to_THB(a)
        return f"{a} USD = {result:.2f} THB"
    elif b == "JPY":
            result = JPY_to_THB(a)
            return f"{a} JPY = {result:.2f} THB"
    elif b == "THBJ":
            result = THB_to_JPY(a)
            return f"{a} THB = {result:.2f} JPY"
print("convert currency:")
print(convert_currency(100, "USD"))
print(convert_currency(100, "THB"))
print(convert_currency(100, "THBJ"))
print(convert_currency(100, "JPY"))
