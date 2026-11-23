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
# PROFESSIONAL DARK THEME CSS

st.markdown("""
<style>

/* MAIN BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #080f20, #101b35, #0b1224);
    color: #f8fafc;
}

/* MAIN CONTENT */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111c35, #080f20);
    border-right: 1px solid #263b61;
}

/* SIDEBAR TEXT */
[data-testid="stSidebar"] * {
    color: #e2e8f0;
}

/* HEADINGS */
h1, h2, h3 {
    color: #f8fafc !important;
    font-weight: 700 !important;
}

/* PARAGRAPHS */
p, label {
    color: #dbeafe !important;
}

/* INPUT BOXES */
.stTextInput input {
    background-color: #17243d !important;
    color: white !important;
    border: 1px solid #385783 !important;
    border-radius: 10px !important;
}

/* INPUT FOCUS */
.stTextInput input:focus {
    border: 1px solid #38bdf8 !important;
    box-shadow: 0 0 10px #2563eb !important;
}

/* BUTTONS */
.stButton > button {
    background: linear-gradient(90deg, #2563eb, #06b6d4);
    color: white !important;
    border: none;
    border-radius: 10px;
    padding: 0.65rem 1rem;
    font-weight: 700;
    transition: 0.3s ease;
}

/* BUTTON HOVER */
.stButton > button:hover {
    background: linear-gradient(90deg, #1d4ed8, #0891b2);
    box-shadow: 0 0 18px #2563eb;
    transform: translateY(-2px);
}

/* RESULT METRIC CARDS */
[data-testid="stMetric"] {
    background: linear-gradient(145deg, #172944, #101d33);
    border: 1px solid #29476f;
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25);
}

/* METRIC LABEL */
[data-testid="stMetricLabel"] {
    color: #93c5fd !important;
}

/* METRIC VALUE */
[data-testid="stMetricValue"] {
    color: #38bdf8 !important;
    font-weight: 700;
}

/* SUCCESS MESSAGE */
[data-testid="stAlert"] {
    border-radius: 12px;
}

/* DOWNLOAD BUTTON */
.stDownloadButton > button {
    background: linear-gradient(90deg, #0f766e, #059669);
    color: white !important;
    border: none;
    border-radius: 10px;
    font-weight: bold;
}
/* LOGIN CARD */
[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(145deg, #172944, #101a2e) !important;
    border: 1px solid #29476f !important;
    border-radius: 18px !important;
    padding: 25px !important;
    box-shadow: 0 0 25px rgba(37, 99, 235, 0.15);
}

/* DIVIDER */
hr {
    border-color: #29476f;
}

/* RESPONSIVE MOBILE DESIGN */
@media (max-width: 768px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    h1 {
        font-size: 1.8rem !important;
    }
}

</style>
""", unsafe_allow_html=True)

# Demo Login Details
USERNAME = "student"
PASSWORD = "1234"

# Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False



# LOGIN PAGE
def login_page():

    st.write("")
    st.write("")
    st.write("")

    col1, col2, col3 = st.columns([1, 1.5, 1])

    with col2:

        with st.container(border=True):

            st.write("")

            if os.path.exists("logo.png"):

                st.image(
                    "logo.png",
                    width=150
                )

            st.markdown(
                """
                <h1 style="text-align:center; color:#38bdf8;">
                    STAT TOOL
                </h1>
                <p style="text-align:center; color:#94a3b8;">
                    CUSTOM STATISTICAL UTILITY MODULE
                </p>
                <hr>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                "<h2 style='text-align:center;'>Welcome Back!</h2>",
                unsafe_allow_html=True
            )

            st.markdown(
                "<p style='text-align:center;'>Login to access your dashboard</p>",
                unsafe_allow_html=True
            )

            st.write("")

            username = st.text_input(
                "Username",
                placeholder="Enter your username"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password"
            )

            st.write("")

            if st.button("LOGIN", use_container_width=True):

                if username.strip() == USERNAME and password.strip() == PASSWORD:

                    st.session_state.logged_in = True
                    st.rerun()

                else:

                    st.error("Invalid Username or Password")

            st.info(
                "Demo Username: student\n\n"
                "Demo Password: 1234"
            )

            st.markdown(
                """
                <p style="text-align:center; color:#64748b; font-size:12px;">
                    Statistical Analysis System
                </p>
                """,
                unsafe_allow_html=True
            )

# MAIN DASHBOARD
def dashboard():
        # CALCULATION HISTORY
    if "calculation_history" not in st.session_state:
        st.session_state.calculation_history = []

    # SIDEBAR DESIGN
    if os.path.exists("logo.png"):
        st.sidebar.image("logo.png", width=150)

    st.sidebar.title("STAT TOOL")

    st.sidebar.caption("Statistical Analysis System")

    st.sidebar.markdown("---")

    st.sidebar.markdown("### 🧭 Navigation")

    st.sidebar.markdown(
        """
        <div style="
            background:#172944;
            padding:15px;
            border-radius:12px;
            border:1px solid #385783;
            margin-bottom:10px;
        ">
            <p style="color:#38bdf8; font-weight:bold;">
                📊 Statistical Dashboard
            </p>
            <p style="color:#94a3b8; font-size:13px;">
                Calculate and analyze your data
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown(
        """
        <div style="
            background:#172944;
            padding:15px;
            border-radius:12px;
            border:1px solid #385783;
        ">
            <p style="color:#38bdf8; font-weight:bold;">
                ℹ️ About Project
            </p>
            <p style="color:#94a3b8; font-size:13px;">
                Learn about STAT TOOL and its features
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.markdown("---")

    if st.sidebar.button("🚪 LOGOUT", use_container_width=True):

        st.session_state.logged_in = False
        st.rerun()

    # DASHBOARD HEADER
    st.markdown(
        """
        <h1 style="color:#38bdf8;">
            📊 Statistical Dashboard
        </h1>
        <p style="color:#94a3b8; font-size:17px;">
            Analyze your numerical data with powerful statistical tools.
        </p>
        """,
        unsafe_allow_html=True
    )
    # ABOUT PROJECT SECTION

    with st.expander("ℹ️ About STAT TOOL - Project Information"):

        st.markdown("### 📊 Custom Statistical Utility Module")

        st.write(
            "STAT TOOL is a Python-based statistical analysis application "
            "designed to perform calculations and visualize numerical data."
        )

        st.markdown("### ✨ Key Features")

        st.markdown("""
        - Mean, Median and Mode Calculation
        - Variance and Standard Deviation
        - Quartile Analysis (Q1, Q2, Q3)
        - Interquartile Range (IQR)
        - Bar Graph and Pie Chart Visualization
        - CSV and PDF Export
        - Statistical Data Analysis
        """)

        st.markdown("### 🛠️ Technologies Used")

        st.write("Python, Streamlit, Matplotlib and ReportLab")

        st.markdown("### 🎓 Project Details")

        st.write("Course: B.Tech CSE")
        st.write("Semester: 3rd Semester")
        st.write("University: Brainware University, Kolkata")
        st.write("Developer: Purushottam")

    st.markdown("---")

        # DATA INPUT SECTION

    def load_sample_data():
        st.session_state.main_data_input = "10 20 30 40 50 60"

    def clear_input():
        st.session_state.main_data_input = ""

    with st.container(border=True):

        st.subheader("📥 Enter Your Data")

        st.write(
            "Enter numbers separated by spaces to calculate statistical measures."
        )

        user_input = st.text_input(
            "Your Numerical Data",
            placeholder="Example: 10 20 30 40 50",
            key="main_data_input"
        )

        st.caption("💡 Enter numbers separated by spaces.")

        sample_col, clear_col = st.columns(2)

        with sample_col:
            st.button(
                "📝 LOAD SAMPLE DATA",
                use_container_width=True,
                on_click=load_sample_data
            )

        with clear_col:
            st.button(
                "🗑️ CLEAR INPUT",
                use_container_width=True,
                on_click=clear_input
            )

        calculate_clicked = st.button(
            "🚀 CALCULATE RESULTS",
            use_container_width=True
        )

    if calculate_clicked:

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
                # SAVE CALCULATION HISTORY

                history_record = {
                    "Input Data": user_input,
                    "Mean": round(mean, 2),
                    "Median": median,
                    "Mode": mode_display if "mode_display" in locals() else str(mode),
                    "Variance": round(variance, 2),
                    "Standard Deviation": round(std, 2)
                }

                st.session_state.calculation_history.append(
                    history_record
                )

                # PREMIUM STATISTICAL RESULT CARDS

                st.markdown("---")

                st.markdown(
                    """
                    <h2 style="color:#38bdf8;">
                        📊 Statistical Results
                    </h2>
                    <p style="color:#94a3b8;">
                       Overview of calculated statistical measures
                    </p>
                    """,
                    unsafe_allow_html=True
                )

                mode_display = (
                    ", ".join(map(str, mode))
                    if isinstance(mode, (list, tuple, set))
                    else str(mode)
                )

                # FIRST ROW
                col1, col2, col3 = st.columns(3)

                col1.metric("📈 Mean", round(mean, 2))
                col2.metric("📊 Median", median)
                col3.metric("🔁 Mode", mode_display)

                # SECOND ROW
                col4, col5, col6 = st.columns(3)

                col4.metric("📉 Variance", round(variance, 2))
                col5.metric("📐 Standard Deviation", round(std, 2))
                col6.metric("↔️ Range", max(numbers) - min(numbers))

                # QUARTILE ANALYSIS
                st.markdown("---")

                st.markdown(
                   """
                   <h2 style="color:#38bdf8;">
                       📦 Quartile Analysis
                  </h2>
                   """,
                   unsafe_allow_html=True
                )

                qcol1, qcol2, qcol3 = st.columns(3)

                qcol1.metric("Q1 - First Quartile", q1)
                qcol2.metric("Q2 - Second Quartile", q2)
                qcol3.metric("Q3 - Third Quartile", q3)

                st.metric(
                    "📏 Interquartile Range (IQR)",
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

                            # PROFESSIONAL DATA VISUALIZATION

            st.markdown("---")

            st.markdown(
                """
                <h2 style="color:#38bdf8;">
                    📊 Data Visualization
                </h2>
                <p style="color:#94a3b8;">
                    Visual representation of your numerical data
                </p>
                """,
                unsafe_allow_html=True
            )

            frequency = Counter(numbers)

            labels = list(frequency.keys())
            values = list(frequency.values())

            chart_col1, chart_col2 = st.columns(2)
            # CALCULATION HISTORY SECTION

            st.markdown("---")

            st.markdown(
                    "<h2 style='color:#38bdf8;'>📜 Calculation History</h2>",
                    unsafe_allow_html=True
                )

            with st.expander("View Previous Calculations"):

                    if st.session_state.calculation_history:

                        st.dataframe(
                            st.session_state.calculation_history,
                            use_container_width=True
                        )

                        if st.button("🗑️ CLEAR HISTORY"):
                            st.session_state.calculation_history.clear()
                            st.rerun()

                    else:
                        st.info("No calculation history available.")

            # BAR GRAPH
            with chart_col1:
                with st.container(border=True):
                    st.markdown("### 📊 Bar Graph")

                    fig1, ax1 = plt.subplots(
                        figsize=(6, 4),
                        facecolor="#111c32"
                    )

                    ax1.set_facecolor("#111c32")

                    bars = ax1.bar(
                        [str(x) for x in labels],
                        values,
                        color="#3B82F6",
                        edgecolor="#38BDF8",
                        linewidth=1.5
                    )

                    ax1.set_xlabel("Values", color="white")
                    ax1.set_ylabel("Frequency", color="white")
                    ax1.set_title(
                        "Data Frequency",
                        color="#38BDF8",
                        fontsize=14
                    )

                    ax1.tick_params(colors="white")
                    ax1.grid(
                        axis="y",
                        linestyle="--",
                        alpha=0.2
                    )

                    for spine in ax1.spines.values():
                        spine.set_color("#385783")

                    st.pyplot(fig1)
                    plt.close(fig1)

            # PIE CHART
            with chart_col2:
                with st.container(border=True):
                    st.markdown("### 🥧 Pie Chart")

                    fig2, ax2 = plt.subplots(
                        figsize=(6, 4),
                        facecolor="#111c32"
                    )

                    ax2.set_facecolor("#111c32")

                    ax2.pie(
                        values,
                        labels=[str(x) for x in labels],
                        autopct="%1.1f%%",
                        startangle=90,
                        textprops={"color": "white"},
                        wedgeprops={
                            "edgecolor": "#111c32",
                            "linewidth": 2
                        }
                    )

                    ax2.set_title(
                        "Data Distribution",
                        color="#38BDF8",
                        fontsize=14
                    )

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

# PROFESSIONAL FOOTER

st.markdown("---")

st.markdown(
    "<h2 style='text-align: center;'>📊 STAT TOOL</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Custom Statistical Utility Module</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>B.Tech CSE | 3rd Semester</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Brainware University, Kolkata</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align: center; color: #38bdf8;'>Developed By: Purushottam</h4>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: #64748b;'>© 2026 STAT TOOL | Statistical Analysis System</p>",
    unsafe_allow_html=True
)

st.markdown("---")