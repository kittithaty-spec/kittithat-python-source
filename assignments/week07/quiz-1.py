"""
    สร้าง class Rectangle โดยกำหนดให้
    - มี attribute ชื่อ length และ width ที่เก็บข้อมูลความยาวและความกว้างของสี่เหลี่ยม
    - มี method ชื่อ get_area() ที่คืนค่าพื้นที่ของสี่เหลี่ยม
    - มี method ชื่อ get_perimeter() ที่คืนค่ารอบรูปของสี่เหลี่ยม
"""

class Rectangle:
<<<<<<< HEAD
=======

>>>>>>> upstream/main
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to get the area
    def get_area(self):
        return self.length * self.width

    # Method to get the perimeter
    def get_perimeter(self):
<<<<<<< HEAD
        return f"Perimeter = {self.length} * {self.width} = {2 * (self.length + self.width)}"

=======
        return 2 * (self.length + self.width)
>>>>>>> upstream/main

rect = Rectangle(10, 5)
print(rect.get_area())       # Should print 50
print(rect.get_perimeter())  # Should print 30

<<<<<<< HEAD
"""
วงกลม
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pei =3.141

    # Method to get the area ปรับสูตรพท.วงกลม
    def get_area(self):
        area_Circle = self.pei * self.radius ** 2
        return f"คืนค่าพท.วงกลม: {area_Circle}"
    
    # Method to get the perimeter ปรับสูตรเส้นรอบวง

    def get_perimeter(self):
        perimeter = 2 * (self.pei * self.radius)
        return f"คืนค่าความยาวรอบรูป: {perimeter}"


myCircle = Circle(5)
print(myCircle.get_area())      
print(myCircle.get_perimeter())  
=======


"""
สร้างคลาส Circle ที่ประยุกต์ใช้คลาส Rectangle
ในการคำนวณ พท. และเส้นรอบรูปได้
"""

class Circle:

    # circle ต้องใช้ข้อมูลอะไรบ้าง เพื่อคำนวณ พท. และเส้นรอบรูป
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to get the area สูตรเดิมได้ไหม?
    def get_area(self):
        return self.length * self.width

    # Method to get the perimeter สูตรเดิมได้มั้ย?
    def get_perimeter(self):
        return 2 * (self.length + self.width)
    
myCircle = Circle(....)
print(myCircle.get_area())
print(myCircle.get_perimeter())
>>>>>>> upstream/main
