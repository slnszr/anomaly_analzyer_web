# Anomaly Analyzer Web

An intelligent, AI-powered network anomaly detection system built with **Flask**, **Scapy**, and **Cohere API**.  
This web-based application captures real-time network packets and detects anomalous behavior based on packet size using a machine learning model and language model inference.

---

##  Features

-  Real-time packet size monitoring
-  Anomaly detection using Cohere AI
-  User login and session management
-  Dashboard with packet prediction results
-  Web-based interface with Flask

---
## How Anomaly Detection Works
The `network_sniffer_cohere_API.py` module performs real-time network traffic monitoring using **Scapy**, a powerful packet manipulation library. Captured packets are analyzed based on their size and are initially labeled as either *normal* or *anomalous* using a local statistical thresholding approach (e.g., mean and standard deviation of packet sizes).

To enhance the detection reliability, the system integrates with the **Cohere AI API**, which provides a second-layer assessment based on large language model inference. This hybrid approach enables both rule-based and AI-driven anomaly detection.

Due to API rate limitations, only the first 10 packets are evaluated through the Cohere API during each run. This ensures cost efficiency while still leveraging the strengths of a modern language model for verification.

The system is particularly useful for lightweight anomaly detection in small-scale environments or educational settings where limited API usage is acceptable.

When executed via `python3 app.py`, the application launches a Flask-based web interface that serves as a lightweight anomaly detection platform.

The backend utilizes a previously trained statistical model based on historical network traffic data. This model was trained using captured packet size distributions and identifies anomalies by comparing incoming input against calculated thresholds (e.g., mean ± standard deviation).

Users can manually input packet sizes through the web interface to simulate real-time traffic. Upon submission, the application evaluates the input and returns a prediction of whether the packet is *normal* or *anomalous*.

In addition to this local prediction, the first few inputs (up to 10 due to API constraints) are also sent to the **Cohere AI API** for verification using a language model-based reasoning process. This hybrid mechanism combines fast statistical inference with intelligent validation to improve reliability and interpretability.


##  Installation

1. **Clone this repository**
```bash
git clone https://github.com/YOUR_USERNAME/anomaly_analyzer_web.git
cd anomaly_analyzer_web

## Set up a virtual environment
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

##Install dependencies
pip install -r requirements.txt

##Set up environment variables
Create a .env file based on the provided .env.example:
COHERE_API_KEY=your-cohere-api-key
FLASK_SECRET_KEY=your-secret-key

## Run the app locally
cd network_sniffer
python3 app.py
