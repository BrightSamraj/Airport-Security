import streamlit as st
import pandas as pd

st.set_page_config(page_title="Airport Security Architecture", layout="wide")

# Sidebar navigation
section = st.sidebar.radio(
    "Select Section",
    [
        "Home", "System Architecture", "Perimeter Security", 
        "Access Control", "Passenger Screening", "Baggage Handling",
        "Command & Cybersecurity", "AI & IoT Layer",
        "Immigration & Boarding", "Vendor Dashboard"
    ]
)

# Home Page
if section == "Home":
    st.title("Airport Security System Architecture")
    st.image("https://via.placeholder.com/1000x350.png?text=Airport+Security+Architecture")
    st.markdown("""
    ### Welcome!
    This interactive app presents a **conceptual design** of an Airport Security System using **layered defense**.  
    Explore each module to learn about:
    - Security objectives  
    - Best vendors and tools  
    - Protocols and network flow  
    - Integration methods  

    This architecture is built for teaching and simulation—not live deployments.
    """)

# System Architecture
elif section == "System Architecture":
    st.header("System Architecture Blueprint")
    st.image("https://via.placeholder.com/1000x550.png?text=Proposed+Architecture+Diagram")
    st.markdown("""
    ### Layered Design (Defense-in-Depth)
    - Perimeter Level  
    - Access Control & Staff Verification  
    - Passenger & Baggage Screening  
    - IoT & Smart Surveillance  
    - Command Center for Cybersecurity  
    - Emergency Management  
    """)

# Perimeter & Entry Security
elif section == "Perimeter Security":
    st.header("Perimeter and Entry-Level Security")
    st.subheader("Objective")
    st.write("Prevent unauthorized entry before any access to terminals.")

    st.subheader("Tools & Technologies")
    st.write("""
    - Fiber-optic intrusion detection sensors  
    - Thermal PTZ cameras  
    - License Plate Recognition (LPR)  
    - Vehicle barriers and bollards  
    """)

    st.subheader("Vendors")
    vendors = ["Honeywell IntelliSense", "Senstar", "Hikvision DarkFighterX", "Axis Communications", "Delta Scientific"]
    st.write(pd.DataFrame(vendors, columns=["Vendor Name"]))

    st.subheader("Protocols & Network Layer")
    st.write("""
    - PoE Gigabit LAN for cameras  
    - ONVIF for camera interoperability  
    - RTSP or HTTPS streaming  
    - WPA3 wireless security  
    """)

# Access Control
elif section == "Access Control":
    st.header("Staff Access Control")
    st.subheader("Objective")
    st.write("Prevent insider threats via biometric and smart card control.")

    st.subheader("Tools & Devices")
    st.write("""
    - RFID Smart Cards  
    - Biometric terminals: Fingerprint, Iris, Face  
    - Smart turnstiles with anti-tailgating  
    - Multi-factor authentication  
    """)

    st.subheader("Vendors")
    st.write(pd.DataFrame(["HID Global", "ZKTeco", "NEC NeoFace", "IDEMIA"], columns=["Vendor Name"]))

    st.subheader("Security Protocols")
    st.write("""
    - TLS 1.3-secured access panels  
    - LDAP integration  
    - Zero Trust Network Access (ZTNA)  
    """)

# Passenger Screening
elif section == "Passenger Screening":
    st.header("Passenger Screening (Security Checkpoint)")
    st.write("""
    - Walk-Through Detectors  
    - Full-Body Scanners  
    - Explosive Trace Detection (ETD)  
    - Carry-on X-ray Imaging  
    """)

    st.write(pd.DataFrame({
        "Device": ["WTMD", "Millimeter Wave Scanner", "ETD", "CT Bag Scanner"],
        "Vendor": ["Garrett", "L3 ProVision", "Smiths IonScan", "Leidos ClearScan"]
    }))

# Baggage Handling
elif section == "Baggage Handling":
    st.header("Baggage Handling & Screening")
    st.write("""
    - Level 1–5 Screening System  
    - RFID-based Track & Trace  
    - Baggage Reconciliation System  
    """)

    st.write(pd.DataFrame({
        "System": ["BHS", "RFID Tracking", "BRS"],
        "Vendor": ["Siemens Logistics", "Zebra Technologies", "SITA"],
        "Protocol": ["MQTT", "EPC Gen2", "REST APIs"]
    }))

# Command Center
elif section == "Command & Cybersecurity":
    st.header("Command Center & Cybersecurity")
    st.write("""
    The central security hub of the airport integrating:
    - SIEM
    - IDS/IPS
    - Firewalls
    - Event logging & response
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Tools")
        st.write("""
        - SIEM: Splunk, IBM QRadar  
        - IDS/IPS: Snort, Suricata  
        - Firewalls: FortiGate, Palo Alto  
        - Endpoint Security: CrowdStrike  
        """)
    with col2:
        st.subheader("Protocols")
        st.write("""
        - 802.1X Secure Auth  
        - AES-256 Encryption  
        - Zero Trust Architecture  
        """)

    st.image("https://via.placeholder.com/400.png?text=Command+Center+Diagram")

# AI & IoT Layer
elif section == "AI & IoT Layer":
    st.header("AI & IoT Layer (Smart Surveillance)")
    st.write("""
    - AI-based video analytics  
    - Behavior monitoring  
    - IoT sensors for environment  
    """)

    st.write(pd.DataFrame({
        "System": ["Analytics", "Sensors", "Gateway"],
        "Tools/Vendors": ["BriefCam / Avigilon", "Zigbee / LoRa sensors", "Cisco IR1101"],
        "Protocol": ["MQTT over TLS", "IPv6", "DTLS"]
    }))

# Immigration & Boarding
elif section == "Immigration & Boarding":
    st.header("Immigration, Boarding & Final Checks")
    st.write("""
    - Automated Border Control (ABC) gates  
    - Facial recognition boarding  
    - API/PNR data validation  
    """)

    st.write(pd.DataFrame({
        "System": ["ABC Gates", "FR Boarding", "API/PNR Sync"],
        "Vendor": ["Vision-Box", "NEC FacePass", "IATA Timatic"],
        "Integration": ["TLS 1.3", "OAuth2", "JSON API"]
    }))

# Vendor Dashboard
elif section == "Vendor Dashboard":
    st.header("Vendor Comparison Dashboard")
    st.write("Filter vendors by category to compare features, reliability, and reputation.")

    vendor_data = pd.DataFrame({
        "Vendor": ["Hikvision", "Smiths Detection", "Splunk", "NEC", "FortiGate", "BriefCam"],
        "Category": ["CCTV", "Baggage Screening", "SIEM", "Biometric", "Firewall", "AI Surveillance"],
        "Region": ["China", "USA", "USA", "Japan", "USA", "Israel"],
        "Certifications": ["ONVIF", "ICAO", "ISO 27001", "ISO 30107", "Common Criteria", "GDPR Compliant"]
    })

    category_filter = st.selectbox("Select Category", ["All"] + list(vendor_data["Category"].unique()))
    if category_filter != "All":
        st.write(vendor_data[vendor_data["Category"] == category_filter])
    else:
        st.write(vendor_data)
