import os

# Define your keys here
OPENAI_API_KEY = "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"        # from https://platform.openai.com/api-keys
GOOGLE_API_KEY = "AIzaSyAPAVuheyMhYoHxQsHBVY5M3IIBe9LlYmM"       # from https://makersuite.google.com/app/apikey
LANGCHAIN_API_KEY = "..."        # optional, for LangSmith if you use it

def set_environment():
    """
    Loads all global variables containing 'API' or 'ID'
    into the environment (os.environ) safely.
    """
    for key, value in globals().items():
        if ("API" in key or "ID" in key) and isinstance(value, str):
            os.environ[key] = value
            print(f"✅ Set environment variable: {key}")

# Call it once
set_environment()
