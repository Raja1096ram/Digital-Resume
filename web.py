import streamlit as st
##from streamlit_option_menu import option_menu
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="My Website",page_icon="")

#--- General Settings 
page_Title = "Digital CV | Raghupathi Ramjee R"
NAME = "Raghupathi Ramjee R" 
DESCRIPTION = "A Data Analyst from Tech Sigram Pvt Ltd."
EMAIL = "ramjee1096@gmail.com"
CONTACT_NO = "8870897498"
SOCIAL_MEDIA = {
    "LinkedIn":"https://www.linkedin.com/in/raghupathi-ramjee-r-46985921b",
    "YouTube":"https://www.youtube.com/@Raghupathiramjee"
}
PROJECTS ={
    "SALES DASHBOARD- Created Sales Dashboard for Grocery, Furnitures, homelane ":"https://youtu.be/NY5omlkK32g",
    "INVENTORY DASHBOARD - Created Inventry Dashboard for Furnitures ":"https://app.powerbi.com/reportEmbed?reportId=94722cb0-91f4-4ef5-8f66-7cf3ccbf0923&autoAuth=true&ctid=9c384e49-1c62-441a-a0cf-d1bfb2fedbc8",
}

## Path Settings
current_dir = Path(__file__).parent if"__file__" in locals() else Path.cwd()
css_file = current_dir / "Style"/ "main.css"
resume_file = current_dir / "Assets" / "Ramjee.docx"
profile_pic = current_dir/ "Assets" / "rrr.jpeg"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# -- Hero Section --
##st.header(page_Title)
col1,col2 = st.columns(2,gap="large")
with col1:
    st.image(profile_pic,width=200)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📫",EMAIL)
    st.write("☏", CONTACT_NO)
    st.download_button(
        label="Download Resume",
        data= PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
  

#--- Socail Link ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

#--- Career Summary
st.write("#")
st.subheader("Career Summary:")
st.write(
    """
- ✔️ Over one year Experience in developing Power BI Applications.
- ✔️ Analyze the Data to Dumping Data and Connection With Databases like Oracle DB, MySQL DB, SQL Server, MariaDB, OData feed etc…
- ✔️ Created Power BI scorecards, dashboards using stack bars, bar graphs, scattered plots, geographical maps, Gauge charts using how me functionality.
- ✔️ Optimized data collection procedures and generated reports on a weekly, monthly, and quarterly basics.
- ✔️ Worked on Custom Visualizations like multi slicer, Hierarchy slicer, Parameters and Field Parameter.
- ✔️ Worked on DAX expressions like filters, Aggregate, Mathematical Functions, Date and Time Functions, Time Intelligent etc.
- ✔️ Convert the Report and Dashboard into Mobile View.
- ✔️ Imported the Table by the SQL Query.
- ✔️ Worked on Auto Refresh and Incremental Refresh.
- ✔️ Created New Calculated Column and Measure using DAX Expression.
- ✔️ Comfortable in working with filters/calculated columns/measures/relationships and transformations of Edit Query section.
- ✔️ Published/shared the reports by creating Content Pack/Sharing the pbix
- ✔️ Strong hands-on experience implementing dash boarding, data visualizations, and analytics using Power BI.
- ✔️ Used advanced Microsoft Excel to create pivot tables and pivot reporting, as well as use VLOOKUP function.
"""
)
# --- Technical Skills---
st.write("#")
st.subheader("Technical Skills:")
st.write(
    """
  - 📊  Data Visulization : Power BI, MS Excel
  - 🗄️  Database	       : SQL Server, MySQL.
  - 👩‍💻  Programming 	     : RStudio,Python(Streamlit,Pandas).
  - 📚  Web Application  :  HTML, CSS
    """
)
# ---Work Experience:---
st.write("#")
st.subheader("Work Experience:")
st.write("Power BI Analysis | TechSigaram Pvt Ltd, Tenkasi, Tamil Nadu.")
st.write(" [MAY/2021 to Current]")
st.write(
    """
- ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts.
- ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase.
- ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
- ►	Involved in creating a dual-axis bar chart with multiple measures.
- ► A proper Data gateway connectivity which is crucial for the Power BI Service Auto-Schedule Refresh.
- ► A Proper Manage Roles and View Roles with a UPN show users name and use it in RLS.
- ► Worked on live Database in ERP Software like Sales, Productions, Purchases, Inventory Modules.
- ► Optimized data collection procedures and generated reports on a weekly, monthly, and quarterly basis.
    """
)
#--- Projects & Accomplishments ---
st.write('\n')
st.subheader(" Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


## py -m streamlit run web.py"""