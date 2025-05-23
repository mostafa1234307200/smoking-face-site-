import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter

def simulate_smoking_effect(image):
    image = ImageEnhance.Brightness(image).enhance(0.7)
    image = ImageEnhance.Contrast(image).enhance(1.5)
    image = image.filter(ImageFilter.GaussianBlur(radius=1))
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return image

st.set_page_config(page_title="تأثير التدخين", layout="centered")
st.title("كيف سيكون شكلك بعد 20 سنة من التدخين؟")
st.write("ارفع صورة لوجهك وسنُظهر لك التأثيرات المحتملة للتدخين بشكل فني.")

uploaded_file = st.file_uploader("اختر صورة (jpg أو png):", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="الصورة الأصلية", use_column_width=True)

    if st.button("تطبيق تأثير التدخين"):
        output = simulate_smoking_effect(image)
        st.image(output, caption="بعد 20 سنة من التدخين", use_column_width=True)
