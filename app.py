import streamlit as st

st.set_page_config(page_title="Portfolio", layout="centered")

# Function to display a project
def display_project(title, description, image_path, github_link, live_link):
    st.subheader(title)
    st.image(image_path, use_column_width=True)
    st.write(description)
    github_markdown = f"[GitHub]({github_link})"
    live_link_markdown = f"[Live Link]({live_link})" if live_link else ""
    st.markdown(f"{github_markdown} {'| ' + live_link_markdown if live_link else ''}")
    st.write("---")

def display_certification(name, issuer, issue_date, cert_link):
    st.subheader(name)
    st.write(f"Issuer: {issuer}")
    st.write(f"Issue Date: {issue_date}")
    st.markdown(f"[View Certificate]({cert_link})")
    st.write("---")


button_style = '''
    <style>
        .button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-align: center;
            display: inline-block;
            font-size: 16px;
            margin-top: 20px;
            text-decoration: none;
            border-radius: 4px;
            transition: background-color 0.3s ease;
            cursor: pointer;
        }
        .button:hover {
            background-color: #45a049;
        }
        .spaced {
            margin-left: 10px; 
        }
    </style>
'''

st.title("My Portfolio")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "About Me", "Skills", "Projects", "Certifications"])

with tab1:
    col1, _, col2 = st.columns((1, 0.1, 2))
    with col1:
        st.image("images/p1.jpg", width=450, use_column_width=True)
    with col2:
        st.markdown(button_style, unsafe_allow_html=True)
        st.markdown('<div class="spaced"><h2>Hi There,<br>I\'m Dhruv Patel</h2><marquee><h7>I\'m a Data Scientist/Machine Learning Engineer</h7></marquee>', unsafe_allow_html=True)

        st.write("### Connect with me")
        st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DhruvPatel1409) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dhruv-patel-9a4755252) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox)")

        with open("dhruv resume.pdf", "rb") as file:
            btn = st.download_button(
                label="Download CV",
                data=file,
                file_name="dhruv resume.pdf",
                mime="application/pdf"
            )

with tab2:
    st.subheader("About Me")

    st.write("""
            👋 Hello! I am **Patel Dhruv Nishesh**, a passionate and driven individual specializing in Data Science, Data Analysis, Machine Learning, and Deep Learning. I am committed to leveraging my analytical skills to uncover actionable insights and contribute to the success of a forward-thinking organization as a data science intern.

            🎓 I hold a **Bachelor of Engineering in Information Technology** from Gujarat Technological University, Gujarat, India, graduating in May 2024 with a **CGPA of 8.99**. My academic journey has equipped me with the technical knowledge and problem-solving abilities essential for tackling complex data challenges.

            🔍 I have hands-on experience in building predictive models, performing comprehensive data analyses, and utilizing various data manipulation techniques. My proficiency in Python, SQL, and various data visualization tools allows me to extract meaningful insights from large datasets.

            📬 Feel free to reach out to me for collaboration, networking, or just a chat about the latest in tech!
        """)
    st.subheader("EDUCATION")
    st.write("""
                - Bachelor of Engineering (INFORMATION TECHNOLOGY) \n
                - Gujarat Technological University, Gujarat, India\n
                - May 2024\n
                - CGPA: 8.99 """)
    st.subheader("EXPERIENCE")
    st.write("""
            **Machine Learning Engineer**  
            Technowire Data Science Limited, January 2024 - March 2024, Ahmedabad, Gujarat

            During my tenure at TechnoWire Data Science Limited, I contributed significantly to several projects focused on data analysis and machine learning applications.

            - My responsibilities included data preprocessing, feature engineering, model development, and evaluation.
            - I collaborated with cross-functional teams to interpret findings and generate actionable insights for clients.
            - Additionally, I actively participated in refining data science methodologies and exploring emerging technologies to enhance project efficiency and effectiveness.
        """)

with tab3:
    st.subheader("Skills")

    st.subheader("Major Skills :rocket:")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image("images/python.png", width=50)
        st.write("**Python**")
    with col2:
        st.image("images/tableau.png", width=50)
        st.write("**Tableau**")
    with col3:
        st.image("images/sql.png", width=50)
        st.write("**SQL**")
    with col4:
        st.image("images/postgresql.png", width=50)
        st.write("**PostGRE SQL**")
    with col5:
        st.image("images/docker.webp", width=59)
        st.write("**Docker**")

        # Python Libraries
    st.subheader("Python Libraries Known :computer:")
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col1:
        st.image("images/numpy.png", width=50)
        st.write("**Numpy**")
    with col2:
        st.image("images/pandas.png", width=50)
        st.write("**Pandas**")
    with col3:
        st.image("images/seaborn.png", width=50)
        st.write("**Seaborn**")
    with col4:
        st.image("images/plotly.png", width=50)
        st.write("**Plotly**")
    with col5:
        st.image("images/matplotlib.png", width=50)
        st.write("**Matplotlib**")
    with col6:
        st.image("images/sklearn.png", width=50)
        st.write("**Sci-kit Learn**")

    with col7:
        st.image("images/tensorflow.png", width=50)
        st.write("**Tensorflow**")

        # Front End Skills
    st.subheader("Front End Skills Known :art:")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("images/html.png", width=50)
        st.write("**HTML**")
    with col2:
        st.image("images/css.png", width=50)
        st.write("**CSS**")
    with col3:
        st.image("images/bootstrap.png", width=50)
        st.write("**Bootstrap**")

    with col4:
        st.image("images/js.png", width=50)
        st.write("**JS**")

        # Soft Skills
    st.subheader("Soft Skills :bulb:")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image("images/hardworking.png", width=50)
        st.write("**Hardworking**")
    with col2:
        st.image("images/promotion.png", width=50)
        st.write("**Ambitious**")
    with col3:
        st.image("images/curious.png", width=50)
        st.write("**Intellectually Curious**")
    with col4:
        st.image("images/fast.png", width=50)
        st.write("**Quick Learner**")
    with col5:
        st.image("images/brain.png", width=50)
        st.write("**Creative Thinker**")

with tab4:
    st.subheader("Projects")
    col1, col2 = st.columns(2)

    projects = [
            {
                "title": "CUSTOMER CHURN PREDICTION",
                "description": "My customer churn prediction project leverages machine learning algorithms to analyze historical customer data and predict the likelihood of customer attrition. By utilizing features such as customer demographics, transaction history, and engagement metrics, our model identifies patterns and behaviors indicative of potential churn. Through predictive analytics, we aim to proactively identify at-risk customers and implement targeted retention strategies, thereby minimizing customer loss and maximizing revenue. By continuously refining our predictive models and adapting to evolving customer behaviors, we strive to enhance customer satisfaction and foster long-term relationships, ultimately driving sustainable business growth.",
                "image_path": "images/cc.png",
                "github_link": "https://github.com/DhruvPatel1409/Customer-Churn-Prediction",
                "live_link": " https://customer-churn-prediction-hbdj2zr4wzfemujd7rbbny.streamlit.app/"
            },
            {
                "title": "RAILWAY RESERVATION SYSTEM",
                "description": "My railway reservation system project, built using Streamlit and SQL, offers a seamless platform for users to manage their train bookings efficiently. With features such as adding trains, viewing train schedules, searching for available trains, booking tickets, and canceling reservations, our system simplifies the entire ticketing process. Users can easily search for trains based on their preferences, view detailed information about train routes and timings, and book tickets hassle-free. The system also allows for easy cancellation of tickets, providing flexibility to users in case of changes in travel plans. By leveraging Streamlit's intuitive interface and SQL database management, we ensure a smooth and user-friendly experience for both passengers and administrators, thereby enhancing the efficiency and reliability of railway ticketing services.",
                "image_path": "images/Railway-Reservation-System.jpg",
                "github_link": "https://github.com/DhruvPatel1409/Railway-Reservation-System",
                "live_link": "https://railway-reservation-system-w4wph3xmvnywbfimkjdwvw.streamlit.app/"
            },
            {
                "title": "FAKE NEWS DETECTOR",
                "description": "My fake news detector project harnesses the power of machine learning and natural language processing to combat the spread of misinformation. By leveraging advanced ML algorithms and NLP techniques, our system analyzes the linguistic patterns and semantic cues present in news articles to distinguish between genuine and fake news. Through feature extraction and sentiment analysis, the model identifies key indicators of deceptive content, such as sensationalism, biased language, and factual inaccuracies. By providing users with a reliable tool to verify the authenticity of news sources, we empower individuals to make informed decisions and combat the proliferation of misinformation in the digital age.",
                "image_path": "images/Fake-News.png",
                "github_link": "https://github.com/DhruvPatel1409/Fake-News-Detector",
                "live_link": "https://fake-news-detector-lvjxmvsakkrnrkkeqfxlpd.streamlit.app/"
            },
            {
                "title": "LAPTOP PRICE PREDICTOR",
                "description": "My  laptop price predictor project harnesses the power of machine learning algorithms to accurately estimate the price of laptops based on various features and specifications. By analyzing a diverse dataset of laptops encompassing attributes such as processor speed, RAM capacity, storage size, display resolution, and graphics card type, our model learns to identify patterns and correlations that influence laptop prices. Through advanced regression techniques and feature engineering, we have developed a robust predictive model capable of providing users with reliable price estimates for laptops of different configurations.",
                "image_path": "images/laptop price.jpg",
                "github_link": "https://github.com/DhruvPatel1409/Laptop-Price-Predictor",
                "live_link": " https://laptop-price-predictor-caiybugemhsskg59wmnvjk.streamlit.app/"
            },
            {
                "title": "CHATBOT",
                "description": "My  chatbot, powered by machine learning algorithms, offers users a personalized and interactive conversational experience. Leveraging natural language processing (NLP) techniques, my chatbot is trained on large datasets of conversations to understand and respond to user queries effectively. With each interaction, the chatbot learns and improves its responses, adapting to the user's preferences and language nuances over time. Whether it's providing customer support, answering frequently asked questions, or engaging users in casual conversation, my chatbot enhances user engagement and satisfaction.",
                "image_path": "images/chatbot.webp",
                "github_link": "https://github.com/DhruvPatel1409/Chatbot",
                "live_link": "https://chatbot-uwuxfazxuzbzcc8bzrz4et.streamlit.app/"
            },
            {
                "title": "HOUSE PRICE PREDICTION SYSTEM",
                "description": "My  house price prediction project utilizes cutting-edge machine learning techniques to forecast property prices accurately. By leveraging a rich dataset containing key features such as location, square footage, number of bedrooms and bathrooms, amenities, and historical sales data, our model learns intricate patterns and relationships within the housing market. Through advanced regression algorithms and feature engineering, we have developed a robust predictive model capable of providing precise estimates of house prices in various neighborhoods and markets.",
                "image_path": "images/home.jpeg",
                "github_link": "https://github.com/DhruvPatel1409/House-Price-Prediction",
                "live_link": " https://house-price-prediction-rdk9lx53wjssvsnyctszat.streamlit.app/"
            },
            {
                "title": "IMDB-Reviews-Sentiment-Analysis",
                "description": "My IMDB Reviews Sentiment Analysis project aims to leverage NLP techniques to perform sentiment analysis on a dataset of movie reviews. By analyzing the textual data, the project seeks to accurately classify each review as positive or negative, aiding in understanding public opinion about various movies. By analyzing the linguistic patterns and semantic nuances in the text, our system identifies the underlying sentiment expressed in each review. Through advanced feature extraction techniques and machine learning algorithms, the model discerns key indicators of sentiment, such as emotional tone, word choice, and context",
                "image_path": "images/imdb.png",
                "github_link": "https://github.com/DhruvPatel1409/IMDB-Reviews-Sentiment-Analysis",
                "live_link": " https://imdb-reviews-sentiment-analysis-7pjurhvwfgogahfkg9tz4l.streamlit.app/"
            },
            {
                "title": "MULTIPLE DISEASE PREDICTION SYSTEM",
                "description": "My  chatbot, powered by machine learning algorithms, offers users a personalized and interactive conversational experience. Leveraging natural language processing (NLP) techniques, my chatbot is trained on large datasets of conversations to understand and respond to user queries effectively. With each interaction, the chatbot learns and improves its responses, adapting to the user's preferences and language nuances over time. Whether it's providing customer support, answering frequently asked questions, or engaging users in casual conversation, my chatbot enhances user engagement and satisfaction.",
                "image_path": "images/disease.jpeg",
                "github_link": "https://github.com/DhruvPatel1409/Multiple-Disease-Prediction-System",
                "live_link" : ""
            },
            {
                "title": "COVID 19 ANALYSIS",
                "description": "My Exploratory Data Analysis (EDA) on the COVID-19 dataset involved a thorough examination of various key aspects, including trends in daily new cases, recoveries, and fatalities across different regions and time periods. Visualizations like line charts, bar graphs, and heatmaps were employed to identify patterns and correlations, such as the impact of government interventions on case numbers and the relationship between population density and infection rates. Additionally, demographic factors like age and comorbidities were analyzed to understand their influence on mortality rates.",
                "image_path": "images/c19.jpeg",
                "github_link": "https://github.com/DhruvPatel1409/covid19-analysis",
                "live_link" : ""
            },
            {
                "title": "EDA ON WOMEN CLOTHING REVIEWS",
                "description": "My Exploratory Data Analysis (EDA) on the Women Clothing Reviews dataset involved examining various aspects of customer feedback to derive meaningful insights. Key areas of focus included analyzing the distribution of ratings, identifying the most commonly reviewed product categories, and assessing the sentiment of customer reviews. Visualizations such as bar charts and word clouds were used to highlight trends in customer preferences and common themes in positive and negative feedback. This analysis aimed to inform business strategies by identifying areas for improvement in product quality and customer satisfaction.",
                "image_path": "images/cloth.jpg",
                "github_link": "https://github.com/DhruvPatel1409/EDA-on-women-E-Commerce-Clothing-Reviews",
                "live_link" : ""
            },
            {
                "title": "BITCOIN PRICE PREDICTION",
                "description": "My Bitcoin Price Prediction project utilizes advanced time series analysis techniques to forecast the future price movements of Bitcoin. By analyzing historical price data, our project aims to uncover underlying patterns and trends that influence Bitcoin's price dynamics over time. Leveraging methodologies such as ARIMA (AutoRegressive Integrated Moving Average), LSTM (Long Short-Term Memory) networks, or Prophet, the model learns from past price fluctuations to make predictions about future trends. Through comprehensive data preprocessing, feature engineering, and model training, our system captures complex relationships within Bitcoin's price history. This enables us to provide valuable insights into potential price movements, aiding investors, traders, and cryptocurrency enthusiasts in making informed decisions.",
                "image_path": "images/BTC-price.png",
                "github_link": "https://github.com/DhruvPatel1409/Bitcoin-Price-Prediction",
                "live_link" : ""
            }
            
        ]

    for i, project in enumerate(projects):
        if i % 2 == 0:
            with col1:
                display_project(
                    project["title"],
                    project["description"],
                    project["image_path"],
                    project["github_link"],
                    project["live_link"]
                )
        else:
            with col2:
                display_project(
                    project["title"],
                    project["description"],
                    project["image_path"],
                    project["github_link"],
                    project["live_link"]
                )

with tab5:
    st.subheader("Certifications")
        
    certifications = [
            {
                "name": "Learn python by doing real world projects from scratch ",
                "issuer": "Udemy",
                "issue_date": "May 2024",
                "cert_link": "https://www.udemy.com/certificate/UC-279f4d03-f9df-47b0-908a-bccb551a2b9a/"
            },
            {
                "name": "Python for data science and ML : zero to hero",
                "issuer": "Udemy",
                "issue_date": "March 2023",
                "cert_link": "https://www.udemy.com/certificate/UC-bede24b0-6d8b-4a6f-b528-ff406464cd06/"
            },
            {
                "name": "Machine learning using python",
                "issuer": "Udemy",
                "issue_date": "January 2024",
                "cert_link": "https://www.udemy.com/certificate/UC-40dfb7f7-e395-4479-85e4-f189db1b7c28/"
            },
            {
                "name": "Machine Learning basics in hindi - Regression analysis",
                "issuer": "Udemy",
                "issue_date": "August 2023",
                "cert_link": "https://www.udemy.com/certificate/UC-25504ac6-22de-4aca-9732-8dbf4308c7e2/"
            },
            {
                "name": "Seaborn - Mastering data visualisation with seaborn",
                "issuer": "Udemy",
                "issue_date": "November 2023",
                "cert_link": "https://www.udemy.com/certificate/UC-13a09141-84a6-4112-8aec-599d3b012597/"
            },
            {
                "name": "Statistics and Hypothesis Testing for Data Science",
                "issuer": "Udemy",
                "issue_date": "May 2024",
                "cert_link": "https://www.udemy.com/certificate/UC-fe8ed573-a649-429c-b260-593ee4bd4a31/"
            },
            {
                "name": "Complete Railway Reservation System Using Sqlite and Streamlit",
                "issuer": "Udemy",
                "issue_date": "March 2024",
                "cert_link": "https://www.udemy.com/certificate/UC-d6d99728-5579-4fd4-9c32-79c450b6560f/"
            },
            {
                "name": "CHATBOT USING MACHINE LEARNING ",
                "issuer": "Udemy",
                "issue_date": "April 2024",
                "cert_link": "https://www.udemy.com/certificate/UC-72cd0aa2-331e-420a-94db-93c83bc98e19/"
            }
        ]
        
    for cert in certifications:
        display_certification(
            cert["name"],
            cert["issuer"],
            cert["issue_date"],
            cert["cert_link"]
        )

    st.markdown("Made by Dhruv Patel")