from pyngrok import ngrok, conf

conf.get_default().ngrok_path = r"D:\all past files\desktop f\All files\Passant Programming\ngrok.exe" 

# Ngrok authtoken from dashboard.ngrok.com
ngrok.set_auth_token("313v3vK8OOtMLrkfRhaRz8wquc4_6a5dz4eTsL9PtspdEjHng")

# Open a public URL tunnel to port 8501 (Streamlit default)
public_url = ngrok.connect(8501)
print("Public URL:", public_url)
print("App is live! Press Ctrl+C to stop.")

# Keep the tunnel open
import time
while True:
    time.sleep(1)


conf.get_default().ngrok_path = r"D:\ngrok\ngrok.exe"

