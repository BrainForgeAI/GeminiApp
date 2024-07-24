from google.api_core import retry
import google.generativeai as genai

# For convenience, a simple wrapper to let the SDK handle error retries
def generate_with_retry(model: genai.GenerativeModel, prompt: str):
  return model.generate_content(prompt, request_options={'retry':retry.Retry()})