# รับชื่อจริงจากผู้ใช้
# นับจำนวนสระทั้งหมดในข้อความว่ามีกี่ตัว (a, e, i, o, u)
# โดยใช้ loop-for เท่านั้น
# e
Name = input("Enter your Name: ").lower()

vowels = 'aeiouAEIOU'

count = sum(1 for char in Name if char in vowels)

print(f"สระที่มี: {count}")
