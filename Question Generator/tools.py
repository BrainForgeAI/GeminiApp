from google.api_core import retry
import google.generativeai as genai
from google.generativeai.types import generation_types

# For convenience, a simple wrapper to let the SDK handle error retries
def generate_with_retry(model: genai.GenerativeModel, prompt: str) -> generation_types.GenerateContentResponse:
  return model.generate_content(prompt, request_options={'retry':retry.Retry()})
