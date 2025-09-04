from pyngrok import ngrok
import time
import os

# Set auth token
ngrok.set_auth_token("30foccVxqRN0htkGWdBF1PXhvGm_B6sYQEB8pBE34xuLsKMv")

# Kill existing tunnels
for tunnel in ngrok.get_tunnels():
    ngrok.disconnect(tunnel.public_url)

# Kill any running Streamlit instance
os.system("pkill streamlit")

# Start Streamlit app
os.system("streamlit run main.py &> /dev/null &")

# Wait a bit
time.sleep(3)

# Start tunnel
public_url = ngrok.connect(8501)
print("🔗 Your Streamlit app is live at:", public_url)