"""Quick test to verify Gemini integration"""
import os
from dotenv import load_dotenv

load_dotenv()

# Test if API key is loaded
google_key = os.getenv('GOOGLE_API_KEY')
print(f"API Key loaded: {google_key[:20]}..." if google_key else "No API key found")

# Test Gemini
if google_key:
    try:
        import google.generativeai as genai
        genai.configure(api_key=google_key)
        model = genai.GenerativeModel('gemini-pro')
        
        response = model.generate_content(
            "Say 'Gemini AI is working!' in one sentence.",
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=50,
                temperature=0.7,
            )
        )
        
        print(f"\n✅ Gemini Response: {response.text}")
        print("✅ Gemini integration is WORKING!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
else:
    print("❌ No API key found")
