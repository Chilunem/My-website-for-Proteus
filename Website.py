import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

#the step below is attempting to load a lottie animation from a url


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#the step below is the link to the lottie animation which is a submarine animation


LottieAnimation= "https://app.lottiefiles.com/share/6749dee3-896a-459f-8bc0-3bb9fb899775" 

# ----- HEADER SECTION
with st.container():
    st.subheader("Proteus")
    st.title("I am an autonomous underwater vehicle startup")
    st.write("I am a startup that is developing an autonomous underwater vehicle")
    st.write("www.x.com/proteusML")

# ----- USE CASES SECTION
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Use cases for Proteus")
        st.write("##")
        st.write(
        """
        **🌊 AQUACULTURE & FISHERIES**
        - Fish Farm Health Monitoring
        - Net Integrity Inspection
        - Automated Feed Optimization
        - Autonomous Sea Lice Management
        - Genetic Stock Monitoring
        
        **🏗️ INFRASTRUCTURE & UTILITIES**
        - Swimming Pool Inspection
        - Dam & Reservoir Inspection
        - Water Treatment Plant Monitoring
        - Underwater Pipeline Inspection
        - Submarine Power Cable Inspection
        - Bridge & Pier Foundation Assessment
        
        **🌍 ENVIRONMENTAL & CONSERVATION**
        - Coral Reef Health Monitoring
        - Invasive Species Detection
        - Water Quality Assessment
        - Plastic Pollution Mapping & Collection
        - Microplastics & Chemical Contaminant Detection
        - Marine Protected Area Enforcement
        
        **🔬 SCIENTIFIC RESEARCH**
        - Marine Biology Observation Platform
        - Underwater Archaeological Survey
        - Oceanographic Data Collection
        - Deep Sea Exploration
        - Hydrothermal Vent & Extremophile Research
        - Climate Change Baseline Monitoring
        
        **⚓ MARITIME & NAVAL**
        - Hull Inspection & Cleaning
        - Port & Harbor Surveying
        - Marina & Yacht Maintenance
        - Autonomous Port Security
        - Mine Countermeasures
        - Submarine Cable Installation & Maintenance
        
        **🏭 INDUSTRIAL & COMMERCIAL**
        - Quarry & Mine Water Management
        - Cooling Water Intake Monitoring
        - Industrial Tank & Reservoir Inspection
        - Offshore Wind Farm Foundation Inspection
        - Subsea Oil & Gas Infrastructure
        - Rare Earth Mineral Exploration
        
        **🚨 EMERGENCY & DISASTER RESPONSE**
        - Flood Assessment & Mapping
        - Underwater Search & Recovery
        - Dam Failure Prevention
        - Disaster Reconnaissance
        - Aircraft/Shipwreck Recovery Support
        
        **🎬 ENTERTAINMENT & MEDIA**
        - Underwater Photography/Videography
        - Virtual Reef Tours
        - Underwater Sports Coverage
        - Marine Life Behavioral Research Filming
        
        **🔮 MOONSHOT / TRANSFORMATIONAL**
        - Ocean Internet-of-Things (IoT) Network
        - Autonomous Underwater Construction
        - Submarine Carbon Capture Monitoring
        - Marine Genetic Library
        - Underwater Data Centers
        - Planetary Defense - Asteroid Ocean Impact Monitoring
        """)
    with right_column:
        st.lottie(LottieAnimation, height=300, key="submarine ")
    
        
        
        # inserted a photo of a craft that appeard to be a maritime vehicle

# To run this code, use: streamlit run Website.py