# 1. รับค่า text จากผู้ใช้
# 2. รับค่าอักขระที่ต้องการค้าหาจากผู้ใช้
# 3. แสดงผลจำนวนของอักขระในข้อความ

# ตัวอย่างผล run
# Insert Your Text: Boonchoo jitnupong
# Character to find: o
# 5 letter 'o' found in 'Boonchoo jitnupong'


"""
 print("\n=== ITERATING THROUGH STRING ===")
count = 0
Text = input("Insert your Text: ")
char = input("character to find: ")
for letter in Text:
    if letter == char:
        count += 1
print(f"{count} letters '{char}' found in '{Text}'")

"""

# เขียน Progaram ตรวจสอบความแข็งแรงของ Password
# นิยามของ strong password คือ ยาวกว่า 8 ตัว, มีอักขระ'@' 1 ตัว, มีตัวเลข, มีตัวอกษร
#
# ตัวอย่างหน้าจอ
# Insert your password: Boonchoo
# Your password is not strong
#
# Insert your password: test@123
# Your password is very strong

"""
 password = input("Isert your password: ")
lenght = len(password)
words = password.split('@')

if len(words) > 1 and password.count('@') == 1:
    left = words[0].isalnum()
    right = words[1].isalnum()
else:
    left = False;
    right = False;

if lenght >= 8 and len(words) == 2 and left and right == True:
    print("Your password is strong")
else:
    print("Your password is not strong")
    
"""
"""My"""

