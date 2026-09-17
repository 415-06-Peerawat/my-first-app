import streamlit as st

# 📌 ตั้งค่าพื้นหลังสีขาว ตัวอักษรสีดำ
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFFFFF !important;
    }
    h1, h2, h3, h4, h5, h6, p, label, span, div {
        color: #000000 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("☕ Koffeeba Cafe - แอปพลิเคชันคำนวณราคาสินค้าและส่วนลด")

# 1. กรอกจำนวนสินค้าแต่ละรายการ
st.subheader("🛒 เลือกจำนวนสินค้า")
col1, col2 = st.columns(2)

with col1:
    qty_americano = st.number_input("Americano (75 บาท):", min_value=0, value=0)
    qty_cappuccino = st.number_input("Cappuccino (80 บาท):", min_value=0, value=0)
    qty_flat_white = st.number_input("Flat White (85 บาท):", min_value=0, value=0)

with col2:
    qty_cream_brulee = st.number_input("Cream Brulee (213 บาท):", min_value=0, value=0)
    qty_croissant = st.number_input("Croissant (130 บาท):", min_value=0, value=0)
    qty_honey_lemon = st.number_input("Honey Lemon Cold Brew (170 บาท):", min_value=0, value=0)

# 2. คำนวณราคารวม
total_price = (qty_americano * 75) + (qty_cappuccino * 80) + (qty_flat_white * 85) + \
              (qty_cream_brulee * 213) + (qty_croissant * 130) + (qty_honey_lemon * 170)

# รวมยอดเฉพาะสินค้าที่ราคาไม่เกิน 200 บาท (สำหรับคิดส่วนลด 15%)
eligible_15_discount = (qty_americano * 75) + (qty_cappuccino * 80) + (qty_flat_white * 85) + \
                       (qty_croissant * 130) + (qty_honey_lemon * 170)

# 3. คำนวณส่วนลดตามเงื่อนไข (If-Else)
if total_price >= 300:
    discount = total_price * 0.30  # ซื้อครบ 300 บาท ลด 30%
elif total_price >= 200:
    discount = eligible_15_discount * 0.15  # ซื้อครบ 200 บาท ลด 15% (ไม่รวมของเกิน 200 บาท)
else:
    discount = 0.0

net_price = total_price - discount

# แสดงผลคำนวณราคารวม
st.divider()
st.header(f"• ราคารวมทั้งหมด: **{total_price:.2f}** บาท")
st.header(f"• ส่วนลดที่ได้รับ: **{discount:.2f}** บาท")
st.header(f"• ราคาสุทธิที่ต้องจ่าย: **{net_price:.2f}** บาท")

# 4. รับเงินจากลูกค้าและคำนวณเงินทอน
st.divider()
received = st.number_input("กรอกจำนวนเงินที่รับจากลูกค้า (บาท):", min_value=0.0, value=0.0, step=10.0)

if net_price > 0:
    if received >= net_price:
        change = received - net_price
        st.header(f"• เงินทอน: **{change:.2f}** บาท")
    else:
        shortage = net_price - received
        st.header(f"• จำนวนเงินยังไม่พอ (ขาดอีก **{shortage:.2f}** บาท)")

st.divider()
st.write("นายพีระวัฒน์ ไชยวงค์ เลขที่6 ม.4/15")
