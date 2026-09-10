# กำหนดชื่อร้าน
print("=== ยินดีต้อนรับสู่ร้าน Panda Cafe ===")

# 1. สินค้าอย่างน้อย 4 รายการ (รับข้อมูลตัวเลข)
print("กรุณากรอกราคาสินค้าทั้ง 4 รายการ:")
item1 = float(input("- ราคาสินค้าชิ้นที่ 1: "))
item2 = float(input("- ราคาสินค้าชิ้นที่ 2: "))
item3 = float(input("- ราคาสินค้าชิ้นที่ 3: "))
item4 = float(input("- ราคาสินค้าชิ้นที่ 4: "))

# 2. คำนวณราคารวมทั้งหมด
total_price = item1 + item2 + item3 + item4
print(f"\nราคารวมทั้งหมด: {total_price:.2f} บาท")

# 3. กำหนดเกณฑ์ส่วนลด (If-Else) อย่างน้อย 2 เงื่อนไข
# เงื่อนไขที่ 1: ซื้อครบ 500 บาท ลด 10%
# เงื่อนไขที่ 2: ซื้อครบ 300 บาท ลด 5%
discount = 0
if total_price >= 500:
    discount = total_price * 0.10
    print(">> โปรโมชั่น: ซื้อครบ 500 บาท รับส่วนลด 10%")
elif total_price >= 300:
    discount = total_price * 0.05
    print(">> โปรโมชั่น: ซื้อครบ 300 บาท รับส่วนลด 5%")
else:
    print(">> โปรโมชั่น: ไม่มียอดถึงเกณฑ์รับส่วนลด")

# 4. เช็กเงื่อนไขและยอดเงินที่ต้องจ่ายจริง
net_to_pay = total_price - discount
print(f"ส่วนลดที่ได้รับ: {discount:.2f} บาท")
print(f"ยอดเงินที่ต้องจ่ายจริง: {net_to_pay:.2f} บาท")

# 5. รับเงินจากลูกค้าและคำนวณเงินทอน
received_money = float(input("\nรับเงินจากลูกค้า (บาท): "))

if received_money >= net_to_pay:
    change = received_money - net_to_pay
    print(f"เงินทอน: {change:.2f} บาท")
    print("=== ขอบคุณที่ใช้บริการ ===")
else:
    shortfall = net_to_pay - received_money
    print(f"ยอดเงินไม่เพียงพอ ขาดอีก {shortfall:.2f} บาท")
