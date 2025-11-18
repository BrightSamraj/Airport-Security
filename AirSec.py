import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Airport Security System", layout="wide")

st.title("🛫 Interactive Airport Security System Architecture")

# Tabs for high-level navigation
tabs = st.tabs(["🏠 Home", "🧱 Architecture", "🔍 Modules", "📈 Vendor Comparison", "🚀 Installation Simulation"])

# --- HOME TAB ---
with tabs[0]:
    st.header("Welcome to the Airport Security System Simulation App")
    st.markdown("""
    This application is designed to help you understand how modern airports secure themselves using:
    - Multiple security layers
    - Best-in-class security tools
    - Trusted vendors
    - Standard protocols and flows  
    All without installing anything physically. Perfect for classroom learning and demonstration!  
    """)

    if st.button("📜 Click to Learn: Why Layered Security Matters"):
        st.info("""
        Layered security follows the proven **Defense-in-Depth** approach,
        which ensures even if one layer fails, the system remains protected through additional layers.
        """)

    st.markdown("---")
    st.image("https://via.placeholder.com/900x350.png?text=Airport+Security+Flow+Animation")  # Replace with your image or gif


# --- SYSTEM ARCHITECTURE TAB ---
with tabs[1]:
    st.header("Airport Security System Architecture Overview")

    col1, col2 = st.columns(2)
    with col1:
        st.write("""
        🛡️ **Main Security Layers**:
        - Perimeter Security
        - Access Control
        - Passenger Screening
        - Baggage Screening
        - Command & Cybersecurity
        - AI-based Smart Surveillance
        - Immigration & Boarding Security
        """)

        if st.button("📊 View System Blueprint"):
            st.success("Displaying architecture diagram...")
            st.image("https://via.placeholder.com/900x600.png?text=Architecture+Diagram")  # Replace with real diagram

    with col2:
        st.write("### 🔁 Workflow Example")
        st.code("""
        Step 1: Perimeter breach detection → Alert Command Center
        Step 2: Block access via smart fences & entry points
        Step 3: Trigger alerts in monitoring systems
        Step 4: AI-based camera analysis validates incident
        Step 5: Security operations team responds
        """)

    st.markdown("---")
    st.write("Click automation-based icons to explore layers below:")

    if st.button("🔐 Go to Access Control"):
        st.session_state["goto"] = "Access Control"

# --- SECURITY MODULES TAB ---
with tabs[2]:
    st.header("🔍 Explore Security Modules")

    module = st.selectbox(
        "Choose a module to explore:",
        ["Perimeter & Entry Security", "Access Control", "Passenger & Baggage Screening", 
         "Cyber Command Center", "AI & IoT Surveillance", "Immigration & Boarding"])
    
    if module == "Perimeter & Entry Security":
        st.subheader("🔵 Perimeter & Entry-Level Security")

        with st.expander("🧰 Devices & Tools"):
            st.write("""
            - Fiber-optic intrusion detection sensors
            - Thermal + PTZ IP cameras
            - License Plate Recognition (LPR)
            - Vehicle barricades & bollards
            """)

        with st.expander("🏢 Top Vendors"):
            st.write(pd.DataFrame({
                "Vendor": ["Honeywell IntelliSense", "Senstar", "Hikvision", "Delta Scientific"],
                "Speciality": ["Fencing", "Detection Systems", "CCTV AI Cameras", "Barriers"]
            }))

        with st.expander("🧩 How It Works"):
            st.markdown("""
            - Cameras continuously monitor perimeter  
            - Sensors detect vibrations or anomalies  
            - Alerts pushed to command center via secure protocols  
            - LPR logs every vehicle entering or leaving  
            """)

        with st.expander("💻 Protocols & Network"):
            st.write("""
            - Protocols: ONVIF, RTSP, HTTPS  
            - Encryption: TLS 1.3  
            - Network: VLAN segmentation, WPA3 for WiFi  
            """)
        
    # Similar sections for other modules using conditionals
    if module == "Access Control":  # Sample of another section
        st.subheader("🔒 Access Control (Staff & Internal Zones)")
        
        with st.expander("🧰 Authentication Tools"):
            st.write("- RFID + Biometric Scanners\n- Smart Gates\n- MFA Badge Readers")

        with st.expander("🔑 Best Vendors"):
            st.write(pd.DataFrame({
                "Vendor": ["HID Global", "IDEMIA", "NEC", "ZKTeco"],
                "Strength": ["Smart Card Systems", "Biometric Fusion", "Face Recognition", "Affordable MFA"]
            }))

        if st.button("🎬 Watch Workflow Animation"):
            st.image("https://via.placeholder.com/800x300.png?text=Biometric+Flow+Animation")

        st.markdown("---")
        st.write("For a visual implementation guide → go to Installation Simulation")

# --- VENDOR COMPARISON TAB ---
with tabs[3]:
    st.header("📈 Vendor Comparison Dashboard")
    vendors = pd.DataFrame({
        "Vendor": ["Hikvision", "Smiths Detection", "Splunk", "NEC", "Fortinet", "BriefCam"],
        "Category": ["CCTV", "Baggage Screening", "SIEM", "Biometric", "Firewall", "AI Surveillance"],
        "Region": ["China", "USA", "USA", "Japan", "USA", "Israel"],
        "Certifications": ["ONVIF", "ICAO Compliant", "ISO 27001", "ISO 30107", "Common Criteria", "GDPR Compliant"]
    })

    filter_category = st.selectbox("Filter by Vendor Category", ["All"] + list(vendors["Category"].unique()))
    if filter_category != "All":
        st.write(vendors[vendors["Category"] == filter_category])
    else:
        st.write(vendors)

    st.markdown("---")
    st.info("Use this to compare who provides what at each layer of security.")

# --- INSTALLATION SIMULATION TAB ---
with tabs[4]:
    st.header("🚀 Installation & Setup Simulation")
    
    st.write("This section simulates how tools integrate into the architecture. No command execution, just conceptual learning.")

    tool = st.selectbox("Choose tool to simulate setup:", ["🎯 SIEM (Splunk)", "🛡️ IDS (Snort)", "🔥 Firewall (FortiGate)", "📹 CCTV Network (ONVIF)"])
    
    if tool == "🎯 SIEM (Splunk)":
        st.subheader("Install & Setup: Splunk SIEM")
        st.write("Splunk is a powerful log collector and intelligent event monitoring platform used in the central command center.")
        
        with st.expander("Installation Steps"):
            st.code("""
            1️⃣ Download .tgz installer for Linux  
            2️⃣ Extract and install:
                $ tar -xzf splunk-<version>.tgz
                $ ./splunk start
            3️⃣ Web UI:
                http://localhost:8000
            4️⃣ Add event sources:
                - Firewall logs
                - CCTV analytics
                - Identity access logs
            """)

        with st.expander("How Splunk Works"):
            st.markdown("""
            - Collects log data from devices  
            - Uses ML-based rules to detect anomalies  
            - Sends alerts to SOC / Command Center  
            """)

        st.image("https://via.placeholder.com/800x300.png?text=Splunk+Workflow+Diagram")  # Replace with actual diagram

    elif tool == "🛡️ IDS (Snort)":
        st.subheader("Snort IDS Setup Simulation")
        st.write("A powerful open-source intrusion detection tool used for detecting network-based attacks.")
        # Similar layout for Snort using expanders and images...

    # Add simulations for FortiGate Firewall & ONVIF-based CCTV similarly

