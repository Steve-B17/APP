import streamlit as st
st.set_page_config(page_title="Wind Forecasting",layout="wide")

def main():
    # Create a sidebar with navigation options
    st.sidebar.title("Navigation")
    pages = ["Home","Mission", "Predictors", "Tech", "About Us", "Contact Us", "Blog"]
    selected_page = st.sidebar.radio("Go to", pages)

    # Render the selected page content
    if selected_page == "Home":
        render_home_page()
    elif selected_page == "Mission":
        render_mission_page()
    elif selected_page == "Predictors":
        render_predictors_page()
    elif selected_page == "Tech":
        render_tech_page()
    elif selected_page == "About Us":
        render_about_us_page()
    elif selected_page == "Contact Us":
        render_contact_us_page()
    elif selected_page == "Blog":
        render_blog_page()

def render_mission_page():
    st.title("Our Mission")
    st.write("""
	- Optimizing Clean Energy Utilization: Our mission is to optimize the utilization of wind and solar power through advanced forecasting, ensuring efficient and reliable clean energy production.

	- Enhancing Grid Stability: We aim to enhance the stability and reliability of power grids by providing accurate predictions of energy production from renewable sources.

	- Empowering Informed Decision-Making: Our project is committed to empowering energy consumers and decision-makers with precise information on expected wind and solar power generation, facilitating informed choices.

	- Advancing Renewable Energy Technologies: We are dedicated to advancing renewable energy technologies by developing cutting-edge forecasting models, pushing the boundaries of prediction accuracy.

	- Contributing to a Sustainable Future: Through collaboration and innovation, our mission is to contribute to a sustainable future, reducing dependence on fossil fuels and mitigating the environmental impact of energy production.
""")

def render_home_page():
    st.title("Our Project: Power Prediction for a Sustainable Tomorrow")

    st.write("Welcome to our innovative project at PSG College of Technology! Our team of six students is dedicated to revolutionizing the way we harness renewable energy. Our primary focus is on developing advanced power prediction models for wind and solar energy sources. By leveraging cutting-edge technologies such as artificial intelligence and machine learning, we aim to enhance the accuracy and efficiency of forecasting, ensuring optimal utilization of these clean energy resources.")

    st.write("Our project delves into the intricacies of predicting power generation, offering insights into the future of sustainable energy. Through innovative approaches and a passion for environmental responsibility, we strive to contribute to a greener tomorrow. Join us on this exciting journey towards a more sustainable and eco-friendly future. Explore the possibilities, stay informed, and be a part of our mission to create a cleaner and brighter world through the power of technology.")

def render_predictors_page():
    st.title("Choose your Source")
    
    # Create a dropdown menu for predictors
    predictor_choice = st.selectbox("Select Predictor", ["Wind", "Solar"])

    # Redirect to a new page based on the selected choice
    if st.button("Go to Selected Predictor"):
        if predictor_choice == "Wind":
            render_wind_page()
        elif predictor_choice == "Solar":
            render_solar_page()

def render_wind_page():
    st.title("Wind Predictions")
    st.write("Wind predictions for the next 48 hours are shown below")

def render_solar_page():
    st.title("Solar Predictions")
    st.write("Solar predictions for the next 48 hours are shown below")

def render_tech_page():
    st.title("Latest Technological Advancements in our Domain")
    st.write("""
In recent years, the field of renewable energy forecasting, encompassing wind and solar power prediction, has experienced remarkable advancements driven by cutting-edge technologies. The integration of artificial intelligence and machine learning has notably improved the accuracy of prediction models by analyzing extensive datasets and intricate environmental variables. Concurrently, the use of sophisticated weather and climate models, coupled with advancements in remote sensing technologies and satellite imagery, contributes to a more nuanced understanding of atmospheric conditions. The Internet of Things facilitates real-time data acquisition, allowing for immediate adjustments in forecasting models based on evolving factors. Additionally, the synergy of data analytics, cloud computing, and advancements in smart grid technologies is shaping a more resilient and adaptive renewable energy landscape, promising optimized energy production and grid integration. Stay informed through ongoing research and industry developments to stay abreast of the latest breakthroughs in this dynamic field.
""")

def render_about_us_page():
    st.title("Get to know us")
    st.write("Welcome to PSG College of Technology's Power Prediction Team! We are a group of six dedicated students based in Coimbatore, India, pursuing our education at PSG College of Technology. Our passion lies in the realm of renewable energy, and we have come together to explore and harness the potential of wind and solar power. Committed to advancing sustainable solutions, our team focuses on power prediction through innovative forecasting methods. By leveraging cutting-edge technologies and our collective expertise, we aim to contribute to the efficient utilization of renewable resources for a greener and more sustainable future. Join us on this journey as we delve into the exciting world of wind and solar forecasting to power a cleaner and brighter tomorrow.")

def render_contact_us_page():
    st.title("Contact Us")
    st.write("""
We appreciate your interest and encourage you to get in touch with us. Feel free to reach out using the following contact information:

Email:
22n2xx@psgtech.ac.in

For General Inquiries contact: +91 XXXXXXXXXX

For any questions, collaboration opportunities, or to connect with PSG College of Technology's Power Prediction Team, please use the provided email address or contact number. We look forward to hearing from you and engaging with our community. Thank you for your interest!""")

def render_blog_page():
    st.title("Exploring the Future of Renewable Energy Forecasting")
    st.write("""
Welcome to our blog, where we delve into the fascinating world of renewable energy forecasting and power prediction. In our latest post, we explore the transformative impact of artificial intelligence and machine learning on enhancing the accuracy of wind and solar power predictions. Discover how these advanced technologies analyze vast datasets and intricate environmental factors to optimize energy production. We also delve into the role of sophisticated weather and climate models, shedding light on their contribution to more precise forecasting. Additionally, join us as we discuss the real-time adaptability enabled by Internet of Things (IoT) devices and the integration of cloud computing for processing extensive datasets. Our blog aims to keep you informed about the latest technological trends, industry insights, and research breakthroughs that are shaping the future of renewable energy. Stay tuned for more updates as we navigate the evolving landscape of sustainable energy solutions.
""")

if __name__ == "__main__":
    main()

