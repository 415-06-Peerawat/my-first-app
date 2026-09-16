# ----------------------------------------------------
# 📌 1. กำหนดข้อมูลเมนูและราคา
# ----------------------------------------------------
menu = {
    "Americano": 75,
    "Cappuccino": 80,
    "Flat White": 85,
    "Cream Brulee": 213,
    "Croissant": 130,
    "Honey Lemon Cold Brew": 170,
}

print("===================================")
print(" ☕ Koffeeba Cafe - Smart Shop")
print("===================================")
print("--- รายการเมนู ---")
for item, price in menu.items():
    print(f"- {item}: {price} บาท")
print("-----------------------------------\n")

# ----------------------------------------------------
# 📌 2. รับข้อมูลจำนวนสินค้าจากผู้ใช้
# ----------------------------------------------------
qty_americano = int(input("รับ Americano (75 ฿) กี่แก้ว: ") or 0)
qty_cappuccino = int(input("รับ Cappuccino (80 ฿) กี่แก้ว: ") or 0)
qty_flat_white = int(input("รับ Flat White (85 ฿) กี่แก้ว: ") or 0)
qty_cream_brulee = int(input("รับ Cream Brulee (213 ฿) กี่ชิ้น: ") or 0)
qty_croissant = int(input("รับ Croissant (130 ฿) กี่ชิ้น: ") or 0)
qty_honey_lemon = int(input("รับ Honey Lemon Cold Brew (170 ฿) กี่แก้ว: ") or 0)

# ----------------------------------------------------
# 📌 3. คำนวณราคารวม
# ----------------------------------------------------
orders = [
    (qty_americano, menu["Americano"]),
    (qty_cappuccino, menu["Cappuccino"]),
    (qty_flat_white, menu["Flat White"]),
    (qty_cream_brulee, menu["Cream Brulee"]),
    (qty_croissant, menu["Croissant"]),
    (qty_honey_lemon, menu["Honey Lemon Cold Brew"]),
]

total_price = 0
eligible_for_15 = 0  # ยอดรวมสินค้าที่ราคาไม่เกิน 200 บาท

for qty, price in orders:
    subtotal = qty * price
    total_price += subtotal
    # เช็กเงื่อนไข: สินค้าที่ราคา <= 200 บาท เท่านั้นที่จะนำไปคิดส่วนลด 15%
    if price <= 200:
        eligible_for_15 += subtotal

# ----------------------------------------------------
# 📌 4. เช็กเงื่อนไขส่วนลด (If-Else)
# ----------------------------------------------------
discount = 0.0

if total_price >= 300:
    discount = total_price * 0.30  # ซื้อครบ 300 บาท ลด 30%
elif total_price >= 200:
    discount = (
        eligible_for_15 * 0.15
    )  # ซื้อครบ 200 บาท ลด 15% (ไม่นับชิ้นเกิน 200)

net_price = total_price - discount

# ----------------------------------------------------
# 📌 5. แสดงผลสรุปยอดเงิน รับเงิน และคำนวณเงินทอน
# ----------------------------------------------------
print("\n===================================")
print("🧾 สรุปยอดชำระเงิน")
print("===================================")
print(f"ราคารวมทั้งหมด    : {total_price:,.2f} บาท")
print(f"ส่วนลดที่ได้รับ      : {discount:,.2f} บาท")
print(f"ยอดรวมสุทธิ       : {net_price:,.2f} บาท")
print("-----------------------------------")

received_money = float(input("รับเงินจากลูกค้า (บาท): ") or 0)

if received_money >= net_price:
    change = received_money - net_price
    print(f"เงินทอน           : {change:,.2f} บาท")
    print("===================================")
    print("🎉 ขอบคุณที่ใช้บริการ Koffeeba Cafe!")
else:
    missing = net_price - received_money
    print(f"❌ เงินไม่พอ! ยังขาดอีก {missing:,.2f} บาท")
