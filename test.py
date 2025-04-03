#GITHUB CODE 

import streamlit as st
import pandas as pd
import datetime
import os


    # Page Configuration
st.set_page_config(
        page_title="MSR-R25-Daily Islamic Duas",
        page_icon="🕌",
        layout="wide"
    )
def main():
    
    st.snow()
    # Function to display a dua card - moved to top of main()
    def display_dua(title, arabic, transliteration, translation, source=""):
        source_html = f'<div class="source-text"><strong>Source:</strong> {source}</div>' if source else ''
        st.markdown(f"""
        <div class="dua-card">
            <h3 class="dua-title">{title}</h3>
            <div class="arabic-text">{arabic}</div>
            <div class="transliteration-text">
                <strong>Transliteration:</strong><br>
                {transliteration}
            </div>
            <div class="translation-text">
                <strong>Translation:</strong><br>
                {translation}
            </div>
            {source_html}
        </div>
        """, unsafe_allow_html=True)

   
    
    
    # Create a dictionary of all duas
    duas = {
        "Testimony of Faith": {
            "title": "Testimony of Faith (Shahadah)",
            "arabic": "أَشْهَدُ أَنْ لَا إِلَـهَ إِلاَّ اللّهُ وَحْدَهُ لَا شَريـكَ لَـهُ وَأَشْهَدُ أَنَّ مُحَمَّـداً عَبْـدُهُ وَرَسُـولُـهُ",
            "transliteration": "Ashhadu an la ilaha illal-lahu wahdahu la shareeka lah, wa-ashhadu anna Muhammadan AAabduhu warasooluh",
            "translation": "I bear witness that none has the right to be worshipped except Allah, alone without partner, and I bear witness that Muhammad is His slave and Messenger"
        },
        "After Completing Ablution": {
            "title": "Dua After Completing Ablution (Wudu)",
            "arabic": "أَشْهَدُ أَنْ لَا إِلَـهَ إِلاَّ اللّهُ وَحْدَهُ لَا شَريـكَ لَـهُ وَأَشْهَدُ أَنَّ مُحَمَّـداً عَبْـدُهُ وَرَسُـولُـهُ",
            "transliteration": "Ashhadu an la ilaha illal-lahu wahdahu la shareeka lah, wa-ashhadu anna Muhammadan AAabduhu warasooluh",
            "translation": "I bear witness that none has the right to be worshipped except Allah, alone without partner, and I bear witness that Muhammad is His slave and Messenger"
        },
        "Upon Completing Ablution - 3": {
            "title": "Upon Completing Ablution (Third Dua)",
            "arabic": "سُبْحـَانَكَ اللَّهُـمَّ وَبِحَمْدِكَ، أَشْهَـدُ أَنْ لاَ إِلَهَ إِلاَّ أَنْتَ، أَسْتَغْفِرُكَ وَأَتُوبُ إِلَـيْكَ",
            "transliteration": "Subhanakal-lahumma wabihamdika ashhadu an la ilaha illa anta astaghfiruka wa-atoobu ilayk",
            "translation": "How perfect You are O Allah, and I praise You, I bear witness that none has the right to be worshipped except You, I seek Your forgiveness and turn in repentance to You"
        },
        "When In Anger": {
            "title": "Seeking Refuge from Anger",
            "arabic": "اَعُوْذُ بِاللهِ مِنَ الشَّيْطَانِ الرَّجِيْمِ",
            "transliteration": "A'oozu Bil'laahi Minash Shaitaanir Rajeem",
            "translation": "I seek refuge in Al'laah from Shaitaan the cursed"
        },
        "Before Meal": {
            "title": "Before Meal",
            "arabic": "بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيْمِ",
            "transliteration": "Bismil laahir Rahmaanir Raheem",
            "translation": "Al'laah's Name we begin with, The Compassionate, Most Merciful"
        },
        "After Meal": {
            "title": "After Meal",
            "arabic": "اَلْحَمْدُ للهِ الَّذِىْ اَطْعَمَنَا وَسَقَاناَ وَجَعَلَناَ مِنَ الْمُسْلِمِيْنَ",
            "transliteration": "Alhumdu lil laahil Lazee At'amana Wa Saqaana Wa Ja'alana Minal Muslimeen",
            "translation": "All Praise is due to Al'laah, who has blessed us with food and drink and made us from amongst the Believers (Muslims)"
        },
        "Entering Home": {
            "title": "Entering Home",
            "arabic": "بِسْمِ اللَّهِ وَلَجْنَا، وَبِسْمِ اللَّهِ خَرَجْنَا، وَعَلَى رَبِّنَا تَوَكَّلْنَا",
            "transliteration": "Bismillahi walajna, wa bismillahi kharajna, wa 'ala rabbina tawakkalna",
            "translation": "In the name of Allah we enter, in the name of Allah we leave, and upon our Lord we rely"
        },
        "Entering And Leaving Home": {
            "title": "Entering And Leaving Home",
            "arabic": "بِسْمِ اللهِ تَوَكَّلْتُ عَلىَ اللهِ وَلاَ حَوْلَ وَلاَ قُوَّةَ اِلاَّ بِاللهِ ط",
            "transliteration": "Bismil laahi Tawak'kaltu Alal laahi Wa Laa Hawla Wa Laa Quw'wata il'la bil'laah",
            "translation": "Al'laah's Name we begin with, I place my (full) trust in Al'laah and there is no Might and Power except with Al'laah."
        },
        "While Traveling": {
            "title": "While Traveling",
            "arabic": "سُبْحَنَ الَّذِىْ سَخَّرَلَنَا هَذَا وَ مَا كُنَّا لَهُ مُقْرِنِيْنْ وَ اِنَّا اِلَى رَبِّنَا لَمُنْقَلِبُوْنْ",
            "transliteration": "Subhaanal lazee Sakh'khara Lana Haaza Wa Maa Kun'na Lahu Muqrineen. Wa In'na ilaa Rab'bina La Munqaliboon",
            "translation": "Glory be to Al'laah who has given us control over this (mode of transport) and without his Grace we would not have been able to control it and undoubtedly we are to return towards our Lord."
        },
        "Entering Mosque": {
            "title": "When Entering the Mosque",
            "arabic": "اللّهُـمَّ افْتَـحْ لي أَبْوابَ رَحْمَتـِك",
            "transliteration": "Allaahum-maf-Tahlee Abwaaba Rahmatika",
            "translation": "O Allaah, open the doors of Your Mercy for me"
        },
        "Leaving Mosque": {
            "title": "When Leaving the Mosque",
            "arabic": "اللّهُـمَّ إِنّـي أَسْأَلُكَ مِـنْ فَضْـلِك",
            "transliteration": "Allaahum-ma In-nee As`aluka Min Fadhlika",
            "translation": "O Allaah, I seek of You Your Grace"
        },
        "When Sneezing": {
            "title": "Person who Sneezes should say",
            "arabic": "الْحَمْدُ لِلَّهِ",
            "transliteration": "Alhamdulillah",
            "translation": "Thanks and all praise be to Allah"
        },
        "Responding to Sneezing": {
            "title": "Person who hears should respond",
            "arabic": "يَرْحَمُكَ اللَّهُ",
            "transliteration": "Yar Hamoo kall Lah",
            "translation": "May Allah have mercy on you"
        },
        "Azaan Dua": {
            "title": "Dua After Azaan (Dua-e-Adhan)",
            "arabic": "اَللّٰہُمَّ رَبَّ ھٰذِہِ الدَّعْوَةِ التَّآمَّةِ وَالصَّلٰوةِ الْقَآئِمَةِ اٰتِ مُحَمَّدَنِ الْوَسِیْلَةَ وَالْفَضِیْلَةَوَالدَّرَجَتَہ الرَّفِیٌعَتَہ وَابْعَثْہُ مَقَامًا مَّحْمُوْدَنِ الَّذِیْ وَعَدْتَّہ وَر زُکنا شَفاعَتَھُ یَوٌمَ الٌقِیٰمَتہِ اِنَّکَ لَا تُخٌلِفُ الٌمِیٌعَاد",
            "transliteration": "Allaahumma Rabba Haazihid Da-vaatitaammati Vassalaatil Kaimati Aati Muhamm-da-nilavasee Lata Val Fazee-la-ta Vadd-ra-ja Tarrafee-a-ta Vab-asahu Maqaamam Mhamoo Da-nil-lazee Va Attahoo Varjukna Shafa A-ta-hu Yaumal Qiyaamati Inn-qa La Tusliphul Miaadi",
            "translation": "O Allah! O God, please grant Hazrat Muhammad Sallallahu Alaihi Wasallam the Lord of this complete call and constant prayer, greatness and high status and make him stand in the place of Mahmood which you promised him and make us blessed with his intercession on the Day of Judgment. Surely you do not break your promise"
        },
        "Durood Ibrahim": {
            "title": "Durood Ibrahim (Salawat)",
            "arabic": "اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ، وَعَلَى آلِ مُحَمَّدٍ، كَمَا صَلَّيْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ، اللَّهُمَّ بَارِكْ عَلَى مُحَمَّدٍ، وَعَلَى آلِ مُحَمَّدٍ، كَمَا بَارَكْتَ عَلَى إِبْرَاهِيمَ، وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ",
            "transliteration": "Allaahumma salli 'ala Muhammad wa 'ala Aali Muhammad kama salayta 'ala Ibrahim wa 'ala aali Ibraaheem innaka hameedun majeed, Allahumma baarik 'ala Muhammad wa 'ala Aali Muhammad kama baarakta 'ala Ibrahim wa ála aali Ibraaheem innaka hameedun majeed",
            "translation": "O Allah! Send Your Mercy on Muhammad and on the family of Muhammad, as You sent Your Mercy on Abraham and on the family of Abraham, for You are the Most Praise-worthy, the Most Glorious. O Allah! Send Your Blessings on Muhammad and the family of Muhammad, as You sent your Blessings on Abraham and on the family of Abraham, for You are the Most Praise-worthy, the Most Glorious."
        }
    }
    
    st.info("بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (Bismillah-ir-Rahman-ir-Raheem), meaning 'In the name of Allah, the Most Gracious, the Most Merciful.'")
    st.info("https://www.youtube.com/@msr-islam")
    
    # st.markdown("<h3 style='color: #088856;'>Ramadan Schedule</h3>", unsafe_allow_html=True)

    # st.info("Ramadan 2025 will begin on the evening of March 1st and end on March 31st or April 1st depending on the sighting of the moon.")
    #  Sectionhttps://github.com/login/device
    st.markdown("<h2 class='section-header'>Islamic Educational Videos</h2>", unsafe_allow_html=True)
        
        # Method 2: Using Local Video Files
    st.markdown("<h3 style='color: #088856;'>Educational Content</h3>", unsafe_allow_html=True)
    with st.expander(" Trending Islamic Videos"):
        # Get all MP4 files in the current directory
            current_dir = os.path.dirname(os.path.abspath(__file__))
            video_files = [f for f in os.listdir(current_dir) if f.endswith('.mp4')]

            if not video_files:
                st.warning("No video files (.mp4) found in the current directory. Please ensure your videos are in the same folder as this script.")
                st.info("Expected location: " + current_dir)
            else:
                # Create columns
                cols = st.columns(3)  # Changed to 3 columns for better visibility

                # Display videos with error handling
                for idx, video_name in enumerate(video_files):
                    try:
                        with cols[idx % 3]:  # Use modulo to cycle through columns
                            video_path = os.path.join(current_dir, video_name)
                            if os.path.exists(video_path):
                                st.write(f"Loading video: {video_name}")
                                video_file = open(video_path, 'rb')
                                video_bytes = video_file.read()
                                st.video(video_bytes)
                                video_file.close()
                            else:
                                st.error(f"Video file not found: {video_name}")
                    except Exception as e:
                        st.error(f"Error loading video {video_name}: {str(e)}")
            
    st.subheader("Search for a Dua")
   
    search_query = st.text_input("Search Duas", placeholder="Type to search duas...", label_visibility="collapsed")


    if search_query:
        # Filter duas based on search query
        filtered_duas = {
            k: v for k, v in duas.items() 
            if search_query.lower() in k.lower() 
            or search_query.lower() in v['translation'].lower() 
            or search_query.lower() in v['transliteration'].lower()
        }
        
        if filtered_duas:
            for key, dua in filtered_duas.items():
                st.markdown(f"<h2 class='section-header'>{key}</h2>", unsafe_allow_html=True)
                display_dua(
                    dua['title'],
                    dua['arabic'],
                    dua['transliteration'],
                    dua['translation'],
                    dua.get('source', '')
                )
        else:
            st.warning("No duas found matching your search.")
    else:
        # Enhanced styling for better visual appeal
        st.markdown("""
            <style>
            /* Modern Islamic Theme */
            :root {
                --primary-color: #088856;
                --secondary-color: #1a5f7a;
                --accent-color: #FFF940;
                --text-dark: #2E2E5C;
                --text-light: #ffffff;
                --shadow: 0 8px 16px rgba(0,0,0,0.1);
                --gradient: linear-gradient(135deg, var(--secondary-color) 0%, var(--primary-color) 100%);
            }

            /* Enhanced Card Design */
            .dua-card {
                background: #ffffff;
                padding: 2.5rem;
                border-radius: 25px;
                margin: 2rem 0;
                box-shadow: var(--shadow);
                border: 1px solid rgba(8, 136, 86, 0.1);
                transition: all 0.3s ease;
                position: relative;
                overflow: hidden;
            }

            .dua-card::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 5px;
                background: var(--gradient);
            }

            .dua-card:hover {
                transform: translateY(-8px);
                box-shadow: 0 15px 30px rgba(0,0,0,0.15);
            }

            /* Enhanced Typography */
            .dua-title {
                font-size: 1.8rem;
                color: var(--primary-color);
                margin-bottom: 2rem;
                font-weight: 700;
                letter-spacing: -0.5px;
                position: relative;
                padding-bottom: 1rem;
            }

            .dua-title::after {
                content: '';
                position: absolute;
                bottom: 0;
                left: 0;
                width: 50px;
                height: 3px;
                background: var(--gradient);
                border-radius: 2px;
            }

            /* Enhanced Arabic Text */
            .arabic-text {
                font-family: 'Amiri', 'Traditional Arabic', serif;
                font-size: 2.2rem;
                text-align: right;
                color: #006400;
                direction: rtl;
                padding: 2rem;
                background: linear-gradient(to right, #f8f9fa, #ffffff);
                border-radius: 20px;
                margin: 1.5rem 0;
                line-height: 2;
                position: relative;
            }

            /* Enhanced Transliteration & Translation */
            .transliteration-text, .translation-text {
                padding: 1.5rem;
                margin: 1.5rem 0;
                border-radius: 15px;
                line-height: 1.8;
                position: relative;
            }

            .transliteration-text {
                background: linear-gradient(to right, #f8f9fa, #ffffff);
                color: #4B0082;
                font-size: 1.2rem;
                border-left: 4px solid var(--secondary-color);
            }

            .translation-text {
                background: linear-gradient(to right, #ffffff, #f8f9fa);
                color: var(--text-dark);
                font-size: 1.2rem;
                border-right: 4px solid var(--primary-color);
            }

            /* Enhanced Section Headers */
            .section-header {
                font-size: 2.2rem;
                color: var(--primary-color);
                text-align: center;
                padding: 2rem;
                background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
                border-radius: 20px;
                margin: 3rem 0;
                font-weight: 700;
                letter-spacing: -0.5px;
                box-shadow: var(--shadow);
                position: relative;
                overflow: hidden;
            }

            .section-header::before {
                content: '🕌';
                position: absolute;
                right: 20px;
                top: 50%;
                transform: translateY(-50%);
                font-size: 2rem;
                opacity: 0.2;
            }

            /* Enhanced Info Boxes */
            .stInfo {
                background: linear-gradient(135deg, #f0f7ff 0%, #e6f3ff 100%);
                padding: 1.5rem;
                border-radius: 15px;
                border-left: 5px solid var(--primary-color);
                margin: 1.5rem 0;
            }

            /* Enhanced Tables */
            .dataframe {
                border-radius: 15px;
                overflow: hidden;
                box-shadow: var(--shadow);
                border: none;
            }

            .dataframe th {
                background: var(--gradient);
                color: var(--text-light);
                padding: 15px;
            }

            .dataframe td {
                padding: 12px;
                border-bottom: 1px solid #eee;
            }

            /* Enhanced Footer */
            .footer {
                text-align: center;
                padding: 3rem;
                color: var(--text-dark);
                font-size: 1rem;
                margin-top: 4rem;
                background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
                border-radius: 20px;
                box-shadow: var(--shadow);
            }
            </style>
        """, unsafe_allow_html=True)

        # Main Title
        st.markdown("""
            <div class="title-container">
                <h1 class="main-title"> Daily Islamic Duas 🕌 </h1>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="dua-card">
                <div class="translation-text">
                    <strong>Important Note:</strong><br>
                    Islam has put great stress on five times a day prayers in general and saying the prayers in the mosque in particular. 
                    Therefore, a practicing Muslim enters and exits a mosque five times a day where he submits to Allah Almighty and 
                    indulges in His prayer. It is imperative that a Muslim knows and understands the importance of being in the mosque 
                    and recites particular Duas on respective actions.
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.title("Hadith: A House in Paradise - 12 Rak'aat")

        st.write("### Structure of Sunnah Prayers:")

        # Create a table for better understanding
        
        
       
        st.write("#### Prayer Schedule")
        data = {
                "Prayer Time": ["Fajr (Dawn)", "Duhr (Noon)", "Maghrib (Sunset)", "Isha (Night)"],
                "Before Prayer": ["2 rak'aat", "4 rak'aat", "-", "-"],
                "After Prayer": ["-", "2 rak'aat", "2 rak'aat", "2 rak'aat"]
            }
        st.table(data)
            
        st.write("**Total: 12 Rak'aat**")
        st.write("*Whoever preserves in performing these 12 units of prayers from the Sunnah, Allah will build a house for them in paradise.*")

        # Add Islamic Daily Practices Section
        st.markdown("<h2 class='section-header'>Islamic Daily Practices</h2>", unsafe_allow_html=True)
        
        # --- 30-Day Challenge Table ---
        st.markdown("<h3 style='color: #088856;'>30-Day Islamic Challenge</h3>", unsafe_allow_html=True)
        
        challenge_data = [
            ["1", "Tahajjud (2x2 Raka'at)"],
            ["2", "Take a bath before Fajr"],
            ["3", "Pray the two Sunnah of Fajr"],
            ["4", "Pray your 5 daily Salah on time"],
            ["5", "Morning Adhkaar"],
            ["6", "Read Quran before Sunrise"],
            ["7", "Make Sadaqah every day, even just $1"],
            ["8", "Dhuha prayer (2x2 Raka'at)"],
            ["9", "Pray Dhuhr, Asr, Fajr & Isha on time"],
            ["10", "Fast Monday & Thursday"],
            ["11", "Evening Adhkaar"],
            ["12", "Make dua every day in your Sujood"],
            ["13", "Surah Mulk every night"],
            ["14", "Read last verse of Al-Baqarah before going to sleep"],
            ["15", "Read Surah Al-Kahf on every Friday"],
            ["16", "Istighfar every day"],
            ["17", "Forgive everyone before sleep"],
            ["18", "Recite Ayatul Kursi after every Fard prayer"],
            ["19", "Understand the meaning of the Quran & duas you make in Salah"]
        ]

        df_challenge = pd.DataFrame(challenge_data, columns=["Day", "Challenge"])
        st.table(df_challenge)

        # --- Life-Changing Prayers ---
        st.markdown("<h3 style='color: #088856;'>Life-Changing Prayers</h3>", unsafe_allow_html=True)

        prayer_data = [
            ["*Tahajjud Prayer*", "Before Fajr (Last third of the night)", "2 Raka'at + dua in Sujood & at the end", "Deep connection with Allah & spiritual elevation"],
            ["*Al-Duha Prayer*", "15-20 min after sunrise", "2 Raka'at", "Immense blessings & sustenance"],
            ["*Al-Tawbah Prayer*", "Anytime", "2 Raka'at", "Seeking forgiveness & spiritual purification"],
            ["*Al-Istikhara Prayer*", "Anytime, but after Isha", "2 Raka'at", "Divine guidance in decision making"]
        ]

        df_prayers = pd.DataFrame(prayer_data, columns=["Prayer", "When", "How", "Benefits"])
        st.table(df_prayers)

        # Add styling for tables (optional)
        st.markdown("""
            <style>
            .dataframe {
                font-size: 1.1rem;
                margin: 1rem 0;
                border-radius: 10px;
                overflow: hidden;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            .dataframe th {
                background-color: #088856;
                color: white;
                padding: 12px;
            }
            .dataframe td {
                padding: 10px;
                background-color: #f8f9fa;
            }
            </style>
        """, unsafe_allow_html=True)

        # Powerful Midnight & Sujood Dua Section
        st.markdown("<h2 class='section-header'>Powerful Dua (Midnight & Sujood)</h2>", unsafe_allow_html=True)
        
        display_dua(
            "First Part - Powerful Midnight & Sujood Dua",
            "لَا إِلٰهَ إِلَّا ٱللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ، لَهُ ٱلْمُلْكُ وَلَهُ ٱلْحَمْدُ، وَهُوَ عَلَىٰ كُلِّ شَىْءٍ قَدِيرٌ",
            "Laa ilaaha illallahu wahdahu laa shareeka lahu, lahul-mulku wa lahul-hamdu, wa huwa 'alaa kulli shay'in qadeer",
            "There is no deity worthy of worship except Allah alone, who has no partner. His is the dominion and His is the praise, and He is able to do all things."
        )

        display_dua(
            "Second Part - Powerful Midnight & Sujood Dua",
            "سُبْحَانَ ٱللَّهِ، وَٱلْحَمْدُ لِلَّهِ، وَلَا إِلٰهَ إِلَّا ٱللَّهُ، وَٱللَّهُ أَكْبَرُ، وَلَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِٱللَّهِ ٱلْعَلِيِّ ٱلْعَظِيمِ، رَبِّ ٱغْفِرْ لِي",
            "SubhanAllahi, wal hamdulillahi, wala ilaha illallah, wallahu akbar, wala hawla wala quwwata illa billah, Al Aliyil Azeem, Rabbi ighfirli",
            "Glory be to Allah, and all praise is for Allah, and there is no deity except Allah, and Allah is the Greatest, and there is no power nor might except with Allah, the Most High, the Most Great. My Lord, forgive me."
        )

        # Add custom CSS for video sizing
        st.markdown("""
            <style>
            /* Custom styling for videos */
            .stVideo {
                width: 100%;
                max-width: 600px;  /* Adjust this value to change width */
                height: auto;
                max-height: 337px;  /* Adjust this value to change height */
                margin: 0 auto;
            }
            
            /* For iframe videos (YouTube) */
            .stVideo > div {
                width: 100%;
                max-width: 600px;  /* Same as above */
                height: 337px;     /* Same as above */
                margin: 0 auto;
            }
            
            .st > div > iframe {
                width: 100%;
                height: 100%;
            }
            </style>
        """, unsafe_allow_html=True)

        

        # Sections with Duas
        st.markdown("<h2 class='section-header'>When In Anger</h2>", unsafe_allow_html=True)
        display_dua(
            "Seeking Refuge from Anger",
            "اَعُوْذُ بِاللهِ مِنَ الشَّيْطَانِ الرَّجِيْمِ",
            "A'oozu Bil'laahi Minash Shaitaanir Rajeem",
            "I seek refuge in Al'laah from Shaitaan the cursed"
           
        )

        st.markdown("<h2 class='section-header'>Before and After Meals</h2>", unsafe_allow_html=True)
        display_dua(
            "Before Meal",
            "بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيْمِ",
            "Bismil laahir Rahmaanir Raheem",
            "Al'laah's Name we begin with, The Compassionate, Most Merciful"
            ""
        )

        display_dua(
            "After Meal",
            "اَلْحَمْدُ للهِ الَّذِىْ اَطْعَمَنَا وَسَقَاناَ وَجَعَلَناَ مِنَ الْمُسْلِمِيْنَ",
            "Alhumdu lil laahil Lazee At'amana Wa Saqaana Wa Ja'alana Minal Muslimeen",
            "All Praise is due to Al'laah, who has blessed us with food and drink and made us from amongst the Believers (Muslims)"
        )

        # Add more sections as needed...
        display_dua(
            "Entering Home",
            "بِسْمِ اللَّهِ وَلَجْنَا، وَبِسْمِ اللَّهِ خَرَجْنَا، وَعَلَى رَبِّنَا تَوَكَّلْنَا",
            "Bismillahi walajna, wa bismillahi kharajna, wa 'ala rabbina tawakkalna",    
            "In the name of Allah we enter, in the name of Allah we leave, and upon our Lord we rely"

        )

        display_dua(
            "Entering And Leaving Home",

        " بِسْمِ اللهِ تَوَكَّلْتُ عَلىَ اللهِ وَلاَ حَوْلَ وَلاَ قُوَّةَ اِلاَّ بِاللهِ ط",

        "Bismil laahi Tawak'kaltu Alal laahi Wa Laa Hawla Wa Laa Quw'wata il'la bil'laah",
        "Al'laah's Name we begin with, I place my (full) trust in Al'laah and there is no Might and Power except with Al'laah."
        )
        display_dua(
            "While Traveling",


        "سُبْحَنَ الَّذِىْ سَخَّرَلَنَا هَذَا وَ مَا كُنَّا لَهُ مُقْرِنِيْنْ وَ اِنَّا اِلَى رَبِّنَا لَمُنْقَلِبُوْنْ ",
        " Subhaanal lazee Sakh'khara Lana Haaza Wa Maa Kun'na Lahu Muqrineen. Wa In'na ilaa Rab'bina La Munqaliboon",
        "Glory be to Al'laah who has given us control over this (mode of transport) and without his Grace we would not have been able to control it and undoubtedly we are to return towards our Lord.Traveling is also an activity, which people undertake on daily basis. No matter how small a distance is or whatever means of traveling is to be adopted, there is always a concern of safety with traveling. Therefore, it is imperative that a person asks for the protection and safety of Allah Almighty.")

        
        display_dua(
            "When Entering the Mosque",
            "اللّهُـمَّ افْتَـحْ لي أَبْوابَ رَحْمَتـِك",
            "Allaahum-maf-Tahlee Abwaaba Rahmatika",
            "O Allaah, open the doors of Your Mercy for me"
            
        )

        display_dua(
            "When Leaving the Mosque",
            "اللّهُـمَّ إِنّـي أَسْأَلُكَ مِـنْ فَضْـلِك",
            "Allaahum-ma In-nee As`aluka Min Fadhlika",
            "O Allaah, I seek of You Your Grace"
           
        )
        # Sneezing Section
        st.markdown("<h2 class='section-header'>When Sneezing</h2>", unsafe_allow_html=True)

        display_dua(
            "Person who Sneezes should say",
            "الْحَمْدُ لِلَّهِ",
            "Alhamdulillah",
            "Thanks and all praise be to Allah"
            ""
        )

        display_dua(
            "Person who hears should respond",
            "يَرْحَمُكَ اللَّهُ",
            "Yar Hamoo kall Lah",
            "May Allah have mercy on you"
        )
        st.markdown("""
            <div class="dua-card">
                <div class="translation-text">
                    <strong>About Sneezing:</strong><br>
                    Although most of the activities undertaken by us in our daily routine are intentional, there are few unintentional 
                    things as well that happen to us every day. One of such things is the act of sneezing. The revival of breath after 
                    a sneeze is also a blessing of Allah Almighty and a Muslim ought to say thanks for it. Moreover, besides the person 
                    who sneezes, the other person who witnesses the sneeze must also respond to the Dua made by the sneezer.
                </div>
            </div>
        """, unsafe_allow_html=True)

        

        

        # --- Morning & Evening Adhkaar & Duas ---
        st.markdown("<h2 class='section-header'>Morning & Evening Adhkaar & Duas</h2>", unsafe_allow_html=True)
        
        st.markdown("""
            <div class="dua-card">
                <div class="translation-text">
                    Recite these supplications in the morning and evening for protection, blessings, and peace.
                </div>
            </div>
        """, unsafe_allow_html=True)

        # --- Adhkaar List ---
        adhkaar_data = [
            ["Surah Ikhlas, Falaq, Nas", "3x"],
            ["Bismillahilladhi la yadhurru (بِسْمِ اللَّهِ الَّذِي لَا يَضُرُّ...)", "3x (Protection from harm)"],
            ["A'udhu bikalimatillahi", "3x"],
            ["Hasbiyallahu laa ilaha illa huwa tawakkaltu alayhi wa huwa rabbul arshil azeem (حَسْبِيَ اللَّهُ لَا إِلَهَ إِلَّا هُوَ...)", "7x (For worries)"],
            ["Subhanallahi wabihamdihi adada khalqihi wa rida nafsihi wa zinata arshihi wa midada kalimatihi", "3x"],
            ["La ilaha illallahu wahdahu la sharika lahu, lahul mulku walahul hamdu wahuwa ala kulli shay'in qadeer", "100x (Every morning)"],
            ["Subhanallahi wa bihamdihi", "100x"],
            ["Allahummaghfirli warhamni wahdini wa 'afini warzuqni", "1x"],
            ["Subhanallah, Alhamdulillah, Allahu Akbar", "Repeatedly"],
            ["Surah Ikhlas before and after Fajr/Duhr/Asr/Maghrib/Isha", "100x"],
            ["Allahu noorus samawati wal ardh", "100x"]
        ]

        # Convert to DataFrame and display
        df_adhkaar = pd.DataFrame(adhkaar_data, columns=["Dhikr / Dua", "Repetitions & Purpose"])
        st.table(df_adhkaar)

        # --- Additional Duas Section ---
        st.markdown("<h3 style='color: #088856;'>Additional Duas for Protection & Peace</h3>", unsafe_allow_html=True)

        # Dua for Protection
        display_dua(
            "Dua for Protection (Every Morning & Evening)",
            "بِسْمِ اللَّهِ الَّذِي لَا يَضُرُّ مَعَ اسْمِهِ شَيْءٌ فِي الْأَرْضِ وَلَا فِي السَّمَاءِ وَهُوَ السَّمِيعُ الْعَلِيمُ",
            "Bismillahi-lladhi la yadhurru ma'as-mihi shay'un fil-ardi wa la fis-sama'i wa huwa-s-Sami'ul-Alim",
            "In the name of Allah, with whose name nothing can cause harm in the earth or in the heavens, and He is the All-Hearing, the All-Knowing."
        )

        # Dua to Fix All Worries
        display_dua(
            "Dua to Fix All Worries",
            "حَسْبِيَ اللَّهُ لَا إِلَهَ إِلَّا هُوَ عَلَيْهِ تَوَكَّلْتُ وَهُوَ رَبُّ الْعَرْشِ الْعَظِيمِ",
            "Hasbiyallahu laa ilaha illa huwa 'alayhi tawakkaltu wa huwa Rabbul 'arshil 'azeem",
            "Allah is sufficient for me. There is none worthy of worship but Him. I rely on Him alone. He is the Lord of the Majestic Throne."
        )

        # Closing Note for Morning & Evening Adhkaar
        st.markdown("""
            <div class="dua-card">
                <div class="translation-text">
                    <strong>Note:</strong><br>
                    May Allah bless you and accept your supplications. Keep your dhikr consistent for spiritual growth and tranquility.
                </div>
            </div>
        """, unsafe_allow_html=True)

        # --- Duas for Fasting Section ---
        st.markdown("<h2 class='section-header'>Duas for Fasting</h2>", unsafe_allow_html=True)

        # Dua for Starting Fast (Suhoor)
        display_dua(
            "Dua for Starting Fast (Suhoor)",
            "نَوَيْتُ صَوْمَ غَدٍ مِنْ شَهْرِ رَمَضَانَ",
            "Nawaitu sawma ghadin min shahri Ramadana",
            "I intend to keep the fast for tomorrow in the month of Ramadan"
        )

        # Dua for Breaking Fast (Iftar)
        display_dua(
            "Dua for Breaking Fast (Iftar)",
            "اللَّهُمَّ إِنِّي لَكَ صُمْتُ وَبِكَ آمَنْتُ وَعَلَى رِزْقِكَ أَفْطَرْتُ",
            "Allahumma inni laka sumtu wa bika amantu wa 'ala rizqika aftartu",
            "O Allah, I fasted for You and I believe in You and I break my fast with Your sustenance"
        )


        # Dua During Fasting
        display_dua(
            "Dua While Fasting",
            "اللَّهُمَّ إِنِّي أَسْأَلُكَ بِرَحْمَتِكَ الَّتِي وَسِعَتْ كُلَّ شَيْءٍ أَنْ تَغْفِرَ لِي",
            "Allahumma inni as'aluka bi-rahmatika allati wasi'at kulla shay'in an taghfira li",
            "O Allah, I ask You by Your mercy which encompasses all things, that You forgive me"
        )

        # Additional Information Card
        st.markdown("""
            <div class="dua-card">
                <div class="translation-text">
                    <strong>Important Times for Making Dua While Fasting:</strong><br>
                    • At the time of breaking fast (Iftar)<br>
                    • During the last third of the night<br>
                    • While fasting (the dua of a fasting person is not rejected)<br>
                    • During the last 10 nights of Ramadan<br>
                    • During Laylatul Qadr (Night of Power)
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Add a section for Important Duas
        st.markdown("<h2 class='section-header'>Important Duas</h2>", unsafe_allow_html=True)
        
        # Display Testimony of Faith
        display_dua(
            duas["Testimony of Faith"]["title"],
            duas["Testimony of Faith"]["arabic"],
            duas["Testimony of Faith"]["transliteration"],
            duas["Testimony of Faith"]["translation"],
            "Muslim 1:209"  # Adding the source
        )
        
        # Display After Completing Ablution
        display_dua(
            duas["After Completing Ablution"]["title"],
            duas["After Completing Ablution"]["arabic"],
            duas["After Completing Ablution"]["transliteration"],
            duas["After Completing Ablution"]["translation"],
            "Source: IslamicFinder.org - Masnoon Duas"  # Adding the source
        )

        # Display Upon Completing Ablution - 3
        display_dua(
            duas["Upon Completing Ablution - 3"]["title"],
            duas["Upon Completing Ablution - 3"]["arabic"],
            duas["Upon Completing Ablution - 3"]["transliteration"],
            duas["Upon Completing Ablution - 3"]["translation"]
        )

        # Display Durood Ibrahim
        st.markdown("<h2 class='section-header'>Durood Ibrahim</h2>", unsafe_allow_html=True)
        display_dua(
            duas["Durood Ibrahim"]["title"],
            duas["Durood Ibrahim"]["arabic"],
            duas["Durood Ibrahim"]["transliteration"],
            duas["Durood Ibrahim"]["translation"]
        )

        # Add Benefits of Salaat section before the footer
        with st.expander("Benefits of sending Salaat upon the Prophet ﷺ"):
            st.markdown("""
            Imaam Ibnul-Qayyim -rahimahullaah, in his book "Jalaa·ul-Afhaam fee Fadlis-Salaati was-Salaam 'alaa khayril anaam (صلى الله عليه و سلم)", mentions benefits arising from sending salaat upon Allaah's Messenger ﷺ:

            1. Compliance with the Command of Allaah-the Perfect and Most High. [i.e. in Aayah 65 of Sooratul-Ahzaab].

            2. Conformity with Him- He the Perfect- in sending salaat upon him, even though the two forms of salaat are different.

            3. Conformity with the Angels in it.

            4. Attaining ten salawaat from Allaah by the person who sends salaat upon him once.

            5. That he is raised by ten levels.

            6. That he has ten good deeds written for him.

            7. That ten sins are erased from him.

            8. That it is to be hoped that his supplication will be responded to if he precedes it with that.

            9. It is a means to attain his (صلى الله عليه و سلم) Intercession.

            10. It is a means for forgiveness of sins.

            11. It is a cause for Allaah to suffice the servant with regard to whatever concerns him.

            12. It is a means for the person to gain nearness to him (صلى الله عليه و سلم) on the Day of Resurrection.

            13. It is a cause for the fulfillment of your needs.

            14. It is a cause for Allaah to send salaat upon the person, and for the salaat of His Angels upon him.

            15. It is a cleansing (zakaat) and purification for the person.

            16. It is a cause for the Prophet (صلى الله عليه و سلم) to respond to the one who sends salaat and salaam upon him.

            17. It is a cause of good for the gathering.

            18. It repels from the person the description of being a miser.

            19. He becomes saved from being supplicated against.

            20. It puts its companion upon the path to Paradise.

            21. It saves from the stench of a gathering wherein Allaah and His Messenger are not mentioned.

            22. It is a means for the completion of speech begun with praise of Allaah.

            23. It takes the servant away from coarseness.

            24. It is a cause for Allaah to bestow favourable praise upon the one who sends salaat upon him.

            25. It is a cause of blessing for the one who sends salaat.

            26. It is a means for attaining the Mercy of Allaah.

            27. It is a means to perpetuate his love of the Messenger (صلى الله عليه و سلم).

            28. It is a cause of his loving that person.

            29. It is a means for the guidance of the person and for his heart to have life.

            30. It fulfils the slightest part of his right.

            31. It comprises remembrance of Allaah and thankfulness to Him.

            32. The person's salaat upon him is supplication (du'aa) to his Lord.
            """)

        # Add 99 Names of Allah section before the footer
        with st.expander("99 Names of Allah (Al Asma Ul Husna)"):
            st.markdown("""
            The first pillar of imaan (faith) in Islam is Belief in Allah. As Muslims, we believe in Allah according to His beautiful names and attributes, which have been revealed in the Holy Quran for our understanding. Allah has mentioned His names repeatedly in the Quran, primarily to help us comprehend His essence and nature. Learning and memorizing the names of Allah are essential steps toward understanding the true way to believe in Him. There is nothing more sacred and blessed than gaining this understanding and living by these names.

            **How can we worship, love, fear, and trust our Lord, the Almighty Allah, if we do not know who He truly is?**

            Allah says in the Quran:
            > "And to Allah belong the best names, so invoke Him by them." (Quran 7:180)
            
            > "Allah—there is no deity except Him. To Him belong the best names." (Quran 20:8)
            
            > "He is Allah, the Creator, the Inventor, the Fashioner; to Him belong the best names." (Quran 59:24)

            **Prophet Muhammad (ﷺ) said:**
            > "Allah has ninety-nine names, one hundred minus one, and whoever knows them will enter Paradise."
            (Sahih Bukhari 54:23)

            **Abu Huraira reported that Allah's Messenger (ﷺ) said:**
            > "There are ninety-nine names of Allah; he who commits them to memory will enter Paradise. Verily, Allah is Odd (He is one, and it is an odd number), and He loves odd numbers."
            (Sahih Muslim Book 48 Hadith 5)
            """)
              # Add Audio Section before the names table
            st.markdown("""
            <h3 style='color: #088856; text-align: center; margin: 20px 0;'>Listen to the 99 Names of Allah</h3>
            """, unsafe_allow_html=True)

            # Create columns for audio files
            audio_col1 = st.columns(1)

            with audio_col1:
                st.markdown("""
                <div style='background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin: 10px 0;'>
                    <h4 style='color: #088856; text-align: center;'>Arabic Recitation</h4>
                </div>
                """, unsafe_allow_html=True)
                
                # Add your Arabic audio file
                try:
                    audio_file_arabic = open('99_names_arabic.mp3', 'rb')
                    audio_bytes = audio_file_arabic.read()
                    st.audio(audio_bytes, format='audio/mp3')
                except FileNotFoundError:
                    st.warning("Arabic audio file not found. Please add '99_names_arabic.mp3' to the folder.")


            # Create a DataFrame for the 99 names
            names_data = {
                "#": list(range(1, 100)),
                "Arabic": [
                    "ٱلرَّحْمَٰنُ", "ٱلرَّحِيمُ", "ٱلْمَلِكُ", "ٱلْقُدُّوسُ", "ٱلسَّلَامُ", "ٱلْمُؤْمِنُ", "ٱلْمُهَيْمِنُ", "ٱلْعَزِيزُ", "ٱلْجَبَّارُ", "ٱلْمُتَكَبِّرُ",
                    "ٱلْخَٰلِقُ", "ٱلْبَارِئُ", "ٱلْمُصَوِّرُ", "ٱلْغَفَّارُ", "ٱلْقَهَّارُ", "ٱلْوَهَّابُ", "ٱلْرَّزَّاقُ", "ٱلْفَتَّاحُ", "ٱلْعَلِيمُ", "ٱلْقَابِضُ",
                    "ٱلْبَاسِطُ", "ٱلْخَافِضُ", "ٱلْرَّافِعُ", "ٱلْمُعِزُّ", "ٱلْمُذِلُّ", "ٱلسَّمِيعُ", "ٱلْبَصِيرُ", "ٱلْحَكَمُ", "ٱلْعَدْلُ", "ٱللَّطِيفُ",
                    "ٱلْخَبِيرُ", "ٱلْحَلِيمُ", "ٱلْعَظِيمُ", "ٱلْغَفُورُ", "ٱلشَّكُورُ", "ٱلْعَلِيُّ", "ٱلْكَبِيرُ", "ٱلْحَفِيظُ", "ٱلْمُقيِتُ", "ٱلْحَسِيبُ",
                    "ٱلْجَلِيلُ", "ٱلْكَرِيمُ", "ٱلْرَّقِيبُ", "ٱلْمُجِيبُ", "ٱلْوَاسِعُ", "ٱلْحَكِيمُ", "ٱلْوَدُودُ", "ٱلْمَجِيدُ", "ٱلْبَاعِثُ", "ٱلْشَّهِيدُ",
                    "ٱلْحَقُّ", "ٱلْوَكِيلُ", "ٱلْقَوِيِيُ", "ٱلْمَتِينُ", "ٱلْوَلِيُ", "ٱلْحَمِيدُ", "ٱلْمُحْصِي", "ٱلْمُبْدِئُ", "ٱلْمُعِيدُ", "ٱلْمُحْيِي",
                    "ٱلْمُمِيتُ", "ٱلْحَيِّيُ", "ٱلْقَيُّومُ", "ٱلْوَاجِدُ", "ٱلْمَاجِدُ", "ٱلْوَاحِدُ", "ٱلْأَحَدُ", "ٱلصَّمَدُ", "ٱلْقَادِرُ", "ٱلْمُقْتَدِرُ",
                    "ٱلْمُقَدِّمُ", "ٱلْمُؤَخِّرُ", "ٱلْأوَّلُ", "ٱلْآخِرُ", "ٱلظَّٰهِرُ", "ٱلْبَاطِنُ", "ٱلْوَالِي", "ٱلْمُتَعَالِي", "ٱلْبَرُّ", "ٱلتَّوَابُ",
                    "ٱلْمُنْتَقِمُ", "ٱلْعَفُوُ", "ٱلْرَّؤُوفُ", "مَالِكُ ٱلْمُلْكُ", "ذُوالْجَلاَلِ وَالإكْرَامِ", "ٱلْمُقْسِطُ", "ٱلْجَامِعُ", "ٱلْغَنيُّ", "ٱلْمُغْنِيُ", "ٱلْمَانِعُ",
                    "ٱلضَّٰرَ", "ٱلنَّافِعُ", "ٱلْنُورُ", "ٱلْهَادِي", "ٱلْبَدِيعُ", "ٱلْبَاقِي", "ٱلْوَارِثُ", "ٱلرَّشِيدُ", "ٱلصَّبُورُ"
                ],
                "Transliteration": [
                    "Ar-Rahmaan", "Ar-Raheem", "Al-Malik", "Al-Quddus", "As-Salaam", "Al-Mu'min", "Al-Muhaymin", "Al-Azeez", "Al-Jabbaar", "Al-Mutakabbir",
                    "Al-Khaaliq", "Al-Baari'", "Al-Musawwir", "Al-Ghaffaar", "Al-Qahhaar", "Al-Wahhaab", "Ar-Razzaaq", "Al-Fattah", "Al-'Aleem", "Al-Qaabid",
                    "Al-Baasit", "Al-Khaafidh", "Ar-Raafi'", "Al-Mu'izz", "Al-Muzil", "As-Samee'", "Al-Baseer", "Al-Hakam", "Al-'Adl", "Al-Lateef",
                    "Al-Khabeer", "Al-Haleem", "Al-'Azeem", "Al-Ghafoor", "Ash-Shaakoor", "Al-'Alee", "Al-Kabeer", "Al-Hafeedh", "Al-Muqeet", "Al-Hasib",
                    "Al-Jaleel", "Al-Kareem", "Ar-Raqeeb", "Al-Mujeeb", "Al-Waasi'", "Al-Hakeem", "Al-Wadud", "Al-Majeed", "Al-Baa'ith", "As-Shaheed",
                    "Al-Haqq", "Al-Wakeel", "Al-Qawiyy", "Al-Mateen", "Al-Walee", "Al-Hameed", "Al-Muhsee", "Al-Mubdi'", "Al-Mu'id", "Al-Muhyee",
                    "Al-Mumeet", "Al-Hayy", "Al-Qayyoom", "Al-Waajid", "Al-Maajid", "Al-Waahid", "Al-Ahad", "As-Samad", "Al-Qaadir", "Al-Muqtadir",
                    "Al-Muqaddim", "Al-Mu'akhkhir", "Al-Awwal", "Al-Aakhir", "Az-Zaahir", "Al-Baatin", "Al-Waalee", "Al-Muta'ali", "Al-Barr", "At-Tawwaab",
                    "Al-Muntaqim", "Al-'Afuww", "Ar-Ra'ooof", "Maalik-al-Mulk", "Thul-Jalaali wal-Ikraam", "Al-Muqsiṭ", "Al-Jaami'", "Al-Ghaniyy", "Al-Mughniyy", "Al-Maani'",
                    "Ad-Dhaarr", "An-Naafi'", "An-Noor", "Al-Haadi", "Al-Badee'", "Al-Baaqi", "Al-Waarith", "Ar-Rasheed", "Al-Saboor"
                ],
                "Meaning": [
                    "The Most or Entirely Merciful", "The Bestower of Mercy", "The King and Owner of Dominion", "The Pure", "The Perfection and Giver of Peace", 
                    "The One Who gives Emaan and Security", "The Guardian, The Witness, The Overseer", "The All Mighty", "The Compeller, The Restorer", "The Supreme, The Majestic",
                    "The Creator, The Maker", "The Originator", "The Fashioner", "The All- and Oft-Forgiving", "The Subduer, The Ever-Dominating", 
                    "The Giver of Gifts", "The Provider", "The Opener, The Judge", "The All-Knowing, The Omniscient", "The Withholder",
                    "The Extender", "The Reducer, The Abaser", "The Exalter, The Elevator", "The Honourer, The Bestower", "The Dishonourer, The Humiliator",
                    "The All-Hearing", "The All-Seeing", "The Judge, The Giver of Justice", "The Utterly Just", "The Subtle One, The Most Gentle",
                    "The Acquainted, The All-Aware", "The Most Forbearing", "The Magnificent, The Supreme", "The Forgiving, The Exceedingly Forgiving", "The Most Appreciative",
                    "The Most High, The Exalted", "The Greatest, The Most Grand", "The Preserver, The All-Heedful and All-Protecting", "The Sustainer", "The Reckoner",
                    "The Majestic", "The Most Generous, The Most Esteemed", "The Watchful", "The Responsive One", "The All-Encompassing, the Boundless",
                    "The All-Wise", "The Most Loving", "The Most Glorious", "The Infuser of New Life", "The All Observing Witness",
                    "The Absolute Truth", "The Trustee, The Disposer of Affairs", "The All-Strong", "The Firm, The Steadfast", "The Protecting Associate",
                    "The Praiseworthy", "The All-Enumerating", "The Originator", "The Restorer", "The Giver of Life",
                    "The Creator of Death", "The Ever Living", "The Self-Subsisting", "The Perceiver", "The Illustrious",
                    "The One", "The Unique", "The Eternal", "The All Powerful", "The All Determiner",
                    "The Expediter", "The Delayer", "The First", "The Last", "The Manifest",
                    "The Hidden", "The Governor", "The Self Exalted", "The Source of All Goodness", "The Ever-Pardoning",
                    "The Avenger", "The Pardoner", "The Most Kind", "Master of the Kingdom", "Possessor of Majesty and Honor",
                    "The Equitable", "The Gatherer", "The Self-Sufficient", "The Enricher", "The Preventer",
                    "The Creator of Harm", "The Creator of Good", "The Light", "The Guide", "The Incomparable",
                    "The Everlasting", "The Inheritor", "The Guide to the Right Path", "The Most Patient"
                ]
            }
            
            df = pd.DataFrame(names_data)

            # Apply custom styling to the DataFrame
            st.markdown("""
                <style>
                .names-table {
                    font-size: 1.1rem;
                    background-color: #f8f9fa;
                    border-radius: 10px;
                    overflow: hidden;
                    margin: 1rem 0;
                }
                .names-table th {
                    background-color: #088856;
                    color: white;
                    padding: 12px;
                    text-align: center;
                }
                .names-table td {
                    padding: 10px;
                    border-bottom: 1px solid #dee2e6;
                }
                .arabic-name {
                    font-family: 'Traditional Arabic', serif;
                    font-size: 1.5rem;
                    color: #006400;
                    text-align: right;
                    direction: rtl;
                }
                .transliteration {
                    color: #4B0082;
                    font-style: italic;
                }
                .meaning {
                    color: #2E2E5C;
                }
                </style>
            """, unsafe_allow_html=True)

            # Display the table with custom formatting
            st.markdown(
                df.style
                .set_properties(**{
                    'background-color': '#f8f9fa',
                    'border-color': '#dee2e6'
                })
                .format({
                    'Arabic': lambda x: f'<div class="arabic-name">{x}</div>',
                    'Transliteration': lambda x: f'<div class="transliteration">{x}</div>',
                    'Meaning': lambda x: f'<div class="meaning">{x}</div>'
                })
                .to_html(), 
                unsafe_allow_html=True
            )

            

        # Footer
        st.markdown("""
            <div class="footer">
                Made with ❤️ for the Muslim Ummah<br>
                <small>May Allah accept our prayers & Grant us Jannah - Ameen</small>
                    <small>Remember me in your duas 🤲 for getting success here and hereafter - MS Rakha 💚 </small>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
