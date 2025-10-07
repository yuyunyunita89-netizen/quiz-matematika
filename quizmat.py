import streamlit as st
import random

# Fungsi untuk membuat soal matematika
def generate_question():
    a = random.randint(0, 200)
    b = random.randint(1, 200)
    operation = random.choice(["+", "-", "*", "/"])

    if operation == "+":
        correct_answer = a + b
    elif operation == "-":
        correct_answer = a - b
    elif operation == "*":
        correct_answer = a * b
    elif operation == "/":
        correct_answer = round(a / b, 2)

    question_str = f"{a} {operation} {b}"
    return question_str, correct_answer

# Inisialisasi session state
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.question = None
    st.session_state.answer = None
    st.session_state.last_result = ""
    st.session_state.new_question = True

st.title("🧮 Teka-Teki Matematika 0-200")
st.write("Masukkan jawabanmu di bawah. Tekan 'Soal Baru' untuk lanjut. Ketik jawaban desimal dengan titik (.)")

# Jika perlu soal baru, generate
if st.session_state.new_question or st.session_state.question is None:
    st.session_state.question, st.session_state.answer = generate_question()
    st.session_state.new_question = False

# Tampilkan soal
st.subheader(f"Soal: {st.session_state.question}")

# Input jawaban
user_input = st.text_input("Jawabanmu:", key="answer_input")

# Tombol periksa jawaban
if st.button("Periksa Jawaban"):
    try:
        user_answer = float(user_input)
        st.session_state.total += 1
        if abs(user_answer - st.session_state.answer) < 0.01:
            st.success("✅ Benar!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Salah. Jawaban yang benar adalah {st.session_state.answer}")
    except ValueError:
        st.warning("Masukkan angka yang valid!")

# Tampilkan skor
st.info(f"Skor kamu: {st.session_state.score} dari {st.session_state.total} soal.")

# Tombol untuk soal baru
if st.button("Soal Baru"):
    st.session_state.new_question = True
    st.experimental_rerun()

# Tombol reset
if st.button("Reset Permainan"):
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.question = None
    st.session_state.answer = None
    st.session_state.new_question = True
    st.experimental_rerun()
