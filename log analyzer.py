import re
import google.generativeai as genai
import os

genai.configure(api_key='Your-API-Key')

def analyze_logs(log_data):
    """
    Analyze system logs and convert them to layman terms with issue identification
    """
    # Preprocess the logs to remove sensitive data (optional)
    cleaned_logs = re.sub(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', '[IP Address]', log_data)
    
    # Prepare the prompt for the AI
    prompt = f"Analyze the following system logs and explain in simple terms what happened, identifying any issues:\n\n{cleaned_logs}"
    
    try:
        # Call OpenAI's GPT to process the logs
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            prompt
        )
        # Output the AI's response
        return response.text
    
    except Exception as e:
        return f"Error analyzing logs: {str(e)}"

# Example system log (you can replace this with actual log data)
log_example = """
Oct 10 10:12:32 myserver kernel: [Hardware Error]: CPU:0 Machine Check Exception: 0 Bank 4: b200000000070f0f
Oct 10 10:12:32 myserver kernel: [Hardware Error]: TSC 0 ADDR ffffffff814c005a
Oct 10 10:12:32 myserver kernel: [Hardware Error]: PROCESSOR 2:300f00000001f07 PROCESSOR_VENDOR_ID 20
Oct 10 10:12:32 myserver kernel: [Hardware Error]: This is a fatal error. Shutting down the system.
"""

# Analyze the logs
result = analyze_logs(log_example)
print(result)
