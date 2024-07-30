import pathlib
import os
from prompts import summarize_prompt
import google.generativeai as genai


def load_syllabus(gemini_model: genai, path_to_file: str | pathlib.Path
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
    if not path_to_file and not file_name:
        raise ValueError("'path_to_file' and 'file_name' cannot both be None")
    elif path_to_file and file_name:
        raise ValueError("'path_to_file' and 'file_name' cannot both be passed as argummets")
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




     
    
    
    