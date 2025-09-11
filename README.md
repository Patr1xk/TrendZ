# TrendSpotter Malaysia – L'Oréal Datathon Prototype

## 🎯 Overview
This project is an AI-powered prototype to **identify and forecast emerging beauty trends in Malaysia** across social media.  
It enables L'Oréal Malaysia to:
- Detect **early-stage trends** from hashtags, keywords, audio snippets, and influencers.  
- Track **which demographics** (Gen Z, Millennials, etc.) are driving them.  
- Relate each trend to **L'Oréal’s product portfolio** (e.g., skincare, Indian makeup, hair care).  
- Predict **when trends start to decay**, helping optimize campaign timing.  
- Provide **actionable dashboards + AI chatbot insights** for marketing and product teams.  
- Suggest **new trend opportunities** (e.g., Hari Merdeka-inspired makeup).  

---

## 🛠️ System Architecture
1. **Data Collection & Wrangling**
   - Source: Provided dataset (hashtags, keywords, audio features).  
   - Enrichment: Map hashtags → topics + influencers (Malaysia-based).  
   - Geo-filter: Malaysia-only social trends.  

2. **Trend Detection (Multimodal)**
   - **Text embeddings** (keywords, hashtags) using HuggingFace models.  
   - **Audio embeddings** (snippets → music/speech classification).  
   - **Influencer signal**: Track Malaysia KOLs driving trends.  

3. **Forecasting & Lifecycle Modeling**
   - Use Prophet/LSTM to model trend adoption curve.  
   - Identify **growth → peak → decay phases**.  
   - Flag when it’s “too late to hop on.”  

4. **Segmentation**
   - Demographics: Gen Z, Millennials.  
   - Thematic: Beauty, Lifestyle, Health, Fashion.  
   - Local Focus: Malaysia-specific segments (Malay, Chinese, Indian communities).  

5. **Product Relevance Engine**
   - Match trends → L'Oréal Malaysia product lines.  
   - Examples:  
     - *Indian makeup festival trend* → Promote L'Oréal foundation shades for deeper tones.  
     - *Skincare #GlassSkin* → Relate to L'Oréal hydrating serums.  
   - Provides **direct marketing hooks**.  

6. **Trend Opportunity Generator**
   - Scan Malaysia calendar (e.g., Hari Merdeka, Deepavali, Raya).  
   - Suggest **proactive trend creation** ideas for L'Oréal campaigns.  

7. **Dashboard (Stakeholder View)**
   - **Trend Radar**: Heatmap of active vs emerging vs decaying trends.  
   - **Lifecycle Curves**: Trend popularity over time.  
   - **Segment & Influencer Insights**: Which KOLs/audiences drive each trend.  
   - **Product Mapping**: Which L'Oréal products tie into this trend.  
   - **AI Chatbot**: Button → Popup → Prompt → On-demand insights (“Which product to push for this skincare trend?”).  

---

## ⚙️ Tools & Stack
- **Data Pipeline**: Python (pandas, scikit-learn, librosa for audio)  
- **Modeling**: HuggingFace Transformers, Prophet/LSTM for forecasting  
- **Orchestration**: Prefect (or Airflow if time permits)  
- **Dashboard**: Streamlit (with chatbot popup), alternative: Power BI  
- **Storage**: PostgreSQL / local CSVs (for hackathon scale)  
- **Chatbot**: LangChain + OpenAI API (insight generation)  

---

## 🚀 WOW Factors
- **Multimodal detection**: Text + audio + influencer tracking.  
- **Malaysia-only focus**: Local KOLs + localized holiday-driven trends.  
- **Product Mapping Engine**: Trend → Direct L'Oréal Malaysia product line recommendation.  
- **Trend Lifecycle Forecasting**: Early warning for decay.  
- **AI Chatbot Insights**: Interactive “Ask TrendSpotter” button on dashboard.  
- **Trend Opportunity Generator**: Suggests future trend creation (Hari Merdeka makeup, Deepavali skincare glow).  

---

## 📊 Example Dashboard Layout
### Page 1 – Overview
- KPI Cards: Total Trends Detected, Active Trends, Emerging Trends, Decaying Trends  
- Trend Radar Heatmap  

### Page 2 – Trend Details
- Lifecycle curve of selected trend  
- Key hashtags + audio snippets driving trend  
- Segment & Influencer breakdown  
- **Product Match**: Suggested L'Oréal products  

### Page 3 – Forecasting & Alerts
- 7-day forecast of trend growth/decay  
- Alerts: “⚠️ Skincare trend #GlassSkin is nearing saturation”  
- **AI Chatbot Button** → popup for Q&A insights  

### Page 4 – Trend Opportunities
- Calendar-based suggestions (Hari Merdeka, Deepavali, Raya, Christmas)  
- “Potential campaign trend” ideas tied to L'Oréal Malaysia products  

---

## 📂 Project Structure
trendspotter-malaysia/
│── data/ # Raw + processed datasets
│── notebooks/ # EDA and prototyping
│── src/
│ ├── data_pipeline/ # ETL scripts
│ ├── models/ # ML models (detection, forecasting, product mapping)
│ ├── dashboard/ # Streamlit app + chatbot popup
│── README.md # Documentation

Wireframe Flow (with your 4 add-ons)
[ Social Data (hashtags, audio, influencers - Malaysia only) ]
                │
                ▼
       [ Data Wrangling & ETL ]
                │
                ▼
       [ Multimodal Trend Detection ]
       (Text + Audio + Influencer signals)
                │
                ▼
       [ Forecasting & Lifecycle Modeling ]
       (Prophet / LSTM → Growth/Decay curve)
                │
                ▼
       [ Product Mapping Engine ]
       (Trend → L'Oréal product lines)
                │
                ▼
       [ Trend Opportunity Generator ]
       (Malaysia holidays → new campaign ideas)
                │
                ▼
   ┌─────────────────────────────────────┐
   │           Dashboard (Streamlit)     │
   │  - Trend Radar (heatmap)            │
   │  - Lifecycle Curves                 │
   │  - Segment & Influencer Insights    │
   │  - Product Recommendations          │
   │  - Trend Opportunity Suggestions    │
   │  - AI Chatbot Popup for insights    │
   └─────────────────────────────────────┘