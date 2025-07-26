A complete machine learning monitoring pipeline built with Python, FastAPI, Streamlit, and scikit-learn — wrapped in Docker.
>>>>How It Works
- Trains a classification model on the Iris dataset using RandomForestClassifier
- Serves predictions via a REST API using FastAPI
- Logs every prediction request (input + output) to SQLite
- Visualizes logs in real-time with a live Streamlit dashboard
- Fully containerized with Docker
>>>>Tech Stack
- Python
- scikit-learn
- FastAPI
- Streamlit
- SQLite
- joblib
- pandas
- Docker
>>>>Run Locally
- Train the model: python model/train_model.py
- Start the API: uvicorn api.app:app --reload
- Start the dashboard: streamlit run monitor/monitor.py
>>>>Run with Docker : 
: >docker build -t mlops-api .
 >docker run -p 8000:8000 mlops-api
>>>>Author
Built by Arios7069646873656D65
