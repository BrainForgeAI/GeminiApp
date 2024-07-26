from typing import TYPE_CHECKING
import pathlib
import os
from prompts import summarize_prompt

if TYPE_CHECKING:
    from google.generativeai import GenerativeModel

def load_syllabus_pdf(gemini_model: 'GenerativeModel', path_to_file: str | pathlib.Path
                      | os.PathLike = None, file_name: str = None):
    """
    Loads a PDF of a course syllabus and extracts a summary from it.
    
    :param gemini_model:
        Reference to a gemini model.
    :param path_to_file:
        Path to syllabus file, preferabally as a raw string.
    :param file_name:
        If you want to use a previously uploaded file, pass the name of the file, files/{name}.
    """
    if path_to_file and file_name:
        raise ValueError("Both 'path_to_file' and 'file_name' cannot both be passed as argummets")
    elif file_name:
        file_ref = genai.get_file(name=file_name)
    else:
        file_ref = genai.upload_file(path_to_file)
    
    response = gemini_model.generate_content(
                [file_ref, summarize_prompt])
    
    return response, response.text


# TODO: Method to get file path from user (E.g. from the game).
def get_file_path():
    raise NotImplementedError


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    import google.generativeai as genai
    import os
    
    genai.configure(api_key=os.environ["API_KEY"])
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    
    path = r"path_to_your_pdf"
    
    # Use this to get specific file
    ident = ""
    name = fr"files/{ident}"
    file_obj = genai.get_file(name=name)
    print(file_obj.name)

    res, res_txt = load_syllabus_pdf(gemini_model=model, file_name=file_obj.name)
    print(res_txt)


     
    
    
    