import streamlit as st

st.title("☕ Koffeeba Cafe")
st.write("แอปพลิเคชันคิดเงินและคำนวณส่วนลดประจำร้าน")

# ----------------------------------------------------
# 📌 1. กำหนดราคาสินค้าตามเมนู
# ----------------------------------------------------
prices = {
    "Americano": 75,
    "Cappuccino": 80,
    "Flat White": 85,
    "Cream Brulee": 213,
    "Croissant": 130,
    "Honey Lemon Cold Brew": 170
}

# ----------------------------------------------------
# 📌 2. ฟังก์ชัน MessageBox (Dialog) สำหรับแสดงใบเสร็จ
# ----------------------------------------------------
@st.dialog("🧾 สรุปใบเสร็จรับเงิน")
def show_receipt_dialog(total, discount, net, received):
    st.write(f"**💰 ยอดรวมสินค้าทั้งหมด:** {total:,.2f} บาท")
    st.write(f"**🏷️ ส่วนลดที่ได้รับ:** {discount:,.2f} บาท")
    st.write(f"**💵 ยอดที่ต้องชำระสุทธิ:** {net:,.2f} บาท")
    
    st.divider()
    
    st.write(f"**📥 รับเงินจากลูกค้า:** {received:,.2f} บาท")
    
    if received >= net:
        change = received - net
        st.success(f"**💸 เงินทอน:** {change:,.2f} บาท")
        st.balloons()
    else:
        st.error(f"❌ ถ้าไม่มีตังก็อย่าซื้อเยอะสิฟะ!!! {net - received:,.2f} บาท")

# ----------------------------------------------------
# 📌 3. ส่วนรับข้อมูลจากผู้ใช้ (UI)
# ----------------------------------------------------
st.header("📝 เลือกรายการสินค้า (ระบุจำนวน)")
col1, col2 = st.columns(2)

with col1:
    qty_americano = st.number_input(f"Americano ({prices['Americano']} ฿)", min_value=0, step=1)
    qty_cappuccino = st.number_input(f"Cappuccino ({prices['Cappuccino']} ฿)", min_value=0, step=1)
    qty_flat_white = st.number_input(f"Flat White ({prices['Flat White']} ฿)", min_value=0, step=1)

with col2:
    qty_cream_brulee = st.number_input(f"Cream Brulee ({prices['Cream Brulee']} ฿)", min_value=0, step=1)
    qty_croissant = st.number_input(f"Croissant ({prices['Croissant']} ฿)", min_value=0, step=1)
    qty_honey_lemon = st.number_input(f"Honey Lemon Cold Brew ({prices['Honey Lemon Cold Brew']} ฿)", min_value=0, step=1)

# ----------------------------------------------------
# 📌 4. คำนวณราคาทันทีขณะเลือกของ (Live Calculation)
# ----------------------------------------------------
total_price = 0
eligible_for_15_discount = 0

items_ordered = [
    (qty_americano, prices["Americano"]),
    (qty_cappuccino, prices["Cappuccino"]),
    (qty_flat_white, prices["Flat White"]),
    (qty_cream_brulee, prices["Cream Brulee"]),
    (qty_croissant, prices["Croissant"]),
    (qty_honey_lemon, prices["Honey Lemon Cold Brew"])
]

for qty, price in items_ordered:
    item_total = qty * price
    total_price += item_total
    
    # เงื่อนไข: สินค้าต้องราคาไม่เกิน 200 ถึงจะเข้าร่วมส่วนลด 15%
    if price <= 200:
        eligible_for_15_discount += item_total

# คำนวณเกณฑ์ส่วนลด (If-Else)
discount = 0
if total_price >= 300:
    discount = total_price * 0.30  # ซื้อครบ 300 บาทลด 30%
elif total_price >= 200:
    discount = eligible_for_15_discount * 0.15  # ซื้อครบ 200 บาทลด 15% (ไม่นับของที่ราคาเกิน 200)

net_price = total_price - discount

# ----------------------------------------------------
# 📌 5. แสดงผลคำนวณราคาแบบเรียลไทม์
# ----------------------------------------------------
st.divider()
st.subheader("🛒 สรุปยอดเงินคงเหลือชำระ")

m_col1, m_col2, m_col3 = st.columns(3)
m_col1.metric("ยอดรวมสินค้า", f"{total_price:,.2f} ฿")
m_col2.metric("ส่วนลดที่ได้รับ", f"{discount:,.2f} ฿")
m_col3.metric("ยอดรวมที่ต้องจ่ายสุทธิ", f"{net_price:,.2f} ฿")

# ----------------------------------------------------
# 📌 6. ชำระเงินและรับเงินทอน
# ----------------------------------------------------
st.divider()
st.header("💳 ชำระเงิน")
received_money = st.number_input("ใส่จำนวนเงินที่รับจากลูกค้า (บาท)", min_value=0.0, step=10.0)

if st.button("🖩 ชำระเงินและออกใบเสร็จ"):
    if total_price > 0:
        show_receipt_dialog(total_price, discount, net_price, received_money)
    else:
        st.warning("⚠️ กรุณาเลือกสินค้าอย่างน้อย 1 รายการก่อนชำระเงิน")
