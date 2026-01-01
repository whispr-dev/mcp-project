"""streamlit minimal app.

Run:
  streamlit run streamlit_app_demo.py
"""

def main():
    try:
        import streamlit as st
    except Exception as e:
        print("Missing dependency or import failed:", e); return
    st.title("sm0l streamlit")
    n = st.slider("n", 1, 10, 3)
    st.write([i*i for i in range(1, n+1)])

if __name__ == "__main__":
    main()
