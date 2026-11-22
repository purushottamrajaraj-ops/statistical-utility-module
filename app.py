import streamlit as st
import statistics_module as sm
import math
import os
import matplotlib.pyplot as plt
from collections import Counter
import csv
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Page Configuration
st.set_page_config(
    page_title="Stat Tool",
    page_icon="📊",
    layout="wide"
)

# Demo Login Details
USERNAME = "student"
PASSWORD = "1234"

# Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# LOGIN PAGE
def login_page():
    if os.path.exists("logo.png"):
     st.image("logo.png", width=180)

    st.markdown(
        "<h1 style='text-align:center;'>📊 STAT TOOL</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;'>"
        "Custom Statistical Utility Module"
        "</p>",
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.subheader("Login to Continue")

        username = st.text_input("Username")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("LOGIN", use_container_width=True):

            if username == USERNAME and password == PASSWORD:

                st.session_state.logged_in = True
                st.rerun()

            else:
                st.error("Invalid Username or Password")

        st.info(
            "Demo Username: student\n\n"
            "Demo Password: 1234"
        )


# MAIN DASHBOARD
def dashboard():
    if os.path.exists("logo.png"):
        st.image("logo.png", width=180)

    st.title("📊 Statistical Dashboard")

    st.write(
        "Welcome to Custom Statistical Utility Module"
    )

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.rerun()

    st.sidebar.title("STAT TOOL")

    st.sidebar.write("Statistical Analysis System")

    st.header("Enter Your Data")

    user_input = st.text_input(
        "Enter numbers separated by spaces",
        placeholder="Example: 10 20 30 40 50"
    )

    if st.button("CALCULATE", use_container_width=True):

        try:

            numbers = list(map(float, user_input.split()))

            if not numbers:
                st.error("Please enter some numbers.")

            elif not all(math.isfinite(x) for x in numbers):
                st.error("Please enter valid finite numbers.")

            else:

                st.success("Calculation Completed Successfully!")

                mean = sm.calculate_mean(numbers)
                median = sm.calculate_median(numbers)
                mode = sm.calculate_mode(numbers)
                variance = sm.calculate_variance(numbers)
                std = sm.calculate_std(numbers)

                q1, q2, q3 = sm.calculate_quartiles(numbers)

                st.subheader("Statistical Results")

                col1, col2, col3 = st.columns(3)

                col1.metric("Mean", round(mean, 2))
                col2.metric("Median", median)
                col3.write("**Mode**")
                col3.write(mode)

                col4, col5, col6 = st.columns(3)

                col4.metric("Variance", round(variance, 2))
                col5.metric("Standard Deviation", round(std, 2))
                col6.metric("Range", max(numbers) - min(numbers))

                st.subheader("Quartile Analysis")

                qcol1, qcol2, qcol3 = st.columns(3)

                qcol1.metric("Q1", q1)
                qcol2.metric("Q2", q2)
                qcol3.metric("Q3", q3)

                st.metric(
                    "Interquartile Range",
                    sm.calculate_iqr(numbers)
                )
                # CSV DOWNLOAD

                st.subheader("Download CSV Report")

                csv_data = io.StringIO()

                csv_writer = csv.writer(csv_data)

                csv_writer.writerow([
                    "Statistical Measure",
                    "Result"
                ])

                csv_writer.writerow(["Mean", mean])
                csv_writer.writerow(["Median", median])
                csv_writer.writerow(["Mode", mode])
                csv_writer.writerow(["Variance", variance])
                csv_writer.writerow(["Standard Deviation", std])
                csv_writer.writerow(["Maximum", max(numbers)])
                csv_writer.writerow(["Minimum", min(numbers)])
                csv_writer.writerow(["Total Values", len(numbers)])
                csv_writer.writerow(["Total Sum", sum(numbers)])
                csv_writer.writerow(["Range", max(numbers) - min(numbers)])
                csv_writer.writerow(["Q1", q1])
                csv_writer.writerow(["Q2", q2])
                csv_writer.writerow(["Q3", q3])
                csv_writer.writerow(["IQR", sm.calculate_iqr(numbers)])

                st.download_button(
                    label="DOWNLOAD CSV",
                    data=csv_data.getvalue(),
                    file_name="statistical_report.csv",
                    mime="text/csv"
                )
                # PDF DOWNLOAD

                st.subheader("Download PDF Report")

                pdf_buffer = io.BytesIO()

                pdf = canvas.Canvas(pdf_buffer, pagesize=A4)

                width, height = A4

                pdf.setFont("Helvetica-Bold", 18)

                pdf.drawString(
                    50,
                    height - 50,
                    "CUSTOM STATISTICAL UTILITY MODULE"
               )

                pdf.setFont("Helvetica", 12)

                y = height - 100

                pdf_results = [
                    f"Input Data: {numbers}",
                    f"Mean: {mean}",
                    f"Median: {median}",
                    f"Mode: {mode}",
                    f"Variance: {variance}",
                    f"Standard Deviation: {std}",
                    f"Maximum: {max(numbers)}",
                    f"Minimum: {min(numbers)}",
                    f"Total Sum: {sum(numbers)}",
                    f"Total Values: {len(numbers)}",
                    f"Range: {max(numbers)-min(numbers)}",
                    f"Quartile Q1: {q1}",
                    f"Quartile Q2: {q2}",
                    f"Quartile Q3: {q3}",
                    f"IQR: {sm.calculate_iqr(numbers)}"
                ]

                for item in pdf_results:

                    pdf.drawString(50, y, item)

                    y -= 30

                pdf.save()

                pdf_buffer.seek(0)

                st.download_button(
                   label="DOWNLOAD PDF REPORT",
                   data=pdf_buffer,
                   file_name="statistical_report.pdf",
                   mime="application/pdf"
                )

              
                st.subheader("Additional Information")

                st.write("**Input Data:**", numbers)

                st.write("**Total Values:**", len(numbers))

                st.write("**Total Sum:**", sum(numbers))

                st.write("**Maximum:**", max(numbers))

                st.write("**Minimum:**", min(numbers))

                st.write("**Ascending Order:**", sorted(numbers))

                st.write(
                    "**Descending Order:**",
                    sorted(numbers, reverse=True)
                )

                st.subheader("Data Visualization")

                frequency = Counter(numbers)

                labels = list(frequency.keys())
                values = list(frequency.values())

                chart_col1, chart_col2 = st.columns(2)

                # BAR GRAPH
                with chart_col1:

                   st.write("### Bar Graph")

                   fig1, ax1 = plt.subplots()

                   ax1.bar(
                       [str(x) for x in labels],
                       values
                   )

                   ax1.set_xlabel("Values")
                   ax1.set_ylabel("Frequency")
                   ax1.set_title("Data Frequency")

                   st.pyplot(fig1)

                   plt.close(fig1)


                # PIE CHART
                with chart_col2:

                    st.write("### Pie Chart")

                    fig2, ax2 = plt.subplots()

                    ax2.pie(
                        values,
                        labels=[str(x) for x in labels],
                        autopct="%1.1f%%",
                        startangle=90
                   )

                    ax2.set_title("Data Distribution")

                    st.pyplot(fig2)

                    plt.close(fig2)

        except ValueError:

            st.error(
                "Invalid Input! Enter numbers separated by spaces."
            )


# APPLICATION CONTROL
if st.session_state.logged_in:

    dashboard()

else:

    login_page()