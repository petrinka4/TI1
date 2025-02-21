# import chardet
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from algorytm import encryptFileContentColumn, decryptFileContentColumn, encryptFileContentVigenere, decryptFileContentVigenere
import os
app = FastAPI()

# Настроим CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешаем доступ с фронтенда
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/encrypt/column")
async def encrypt_column(key: str = Form(...), input_file: UploadFile = File(...)):

    content = await input_file.read()
    content_str = content.decode("utf-8")
    directory = "../firstLabResultf"
    if not os.path.exists(directory):
        os.makedirs(directory)
    try:
        result = str(encryptFileContentColumn(key, content_str))
        file_path = "../firstLabResultf/encryptedFileColumn.txt"
        with open(file_path, "wb") as file:
            file.write(result.encode("utf-8"))
    except:
        result = "key is longer then text"
    return {"result": result}


@app.post("/decrypt/column")
async def decrypt_column(key: str = Form(...), input_file: UploadFile = File(...)):
    directory = "../firstLabResultf"
    if not os.path.exists(directory):
        os.makedirs(directory)
    content = await input_file.read()
    content_str = content.decode("utf-8")
    try:
        result = decryptFileContentColumn(key, content_str)

        with open("../firstLabResultf/decryptedFileColumn.txt", "w", encoding="utf-8") as my_file:
            my_file.write(result)
    except:
        result = "key is longer then text"
    return {"result": result}


@app.post("/encrypt/vigenere")
async def encrypt_vigenere(key: str = Form(...), input_file: UploadFile = File(...)):

    content = await input_file.read()
    content_str = content.decode("utf-8")
    directory = "../firstLabResultf"
    if not os.path.exists(directory):
        os.makedirs(directory)
    try:
        result = str(encryptFileContentVigenere(key, content_str))
        file_path = "../firstLabResultf/encryptedFileVigenere.txt"
        with open(file_path, "wb") as file:
            file.write(result.encode("utf-8"))
    except:
        result = "key is longer then text"
    return {"result": result}


@app.post("/decrypt/vigenere")
async def decrypt_vigenere(key: str = Form(...), input_file: UploadFile = File(...)):
    content = await input_file.read()
    content_str = content.decode("utf-8")
    print(key)
    print(content_str)
    try:
        result = decryptFileContentVigenere(key, content_str)
        with open("../firstLabResultf/decryptedFileVigenere.txt", "w", encoding="utf-8") as my_file:
            my_file.write(result)
    except:
        result = "key is longer then text"
    return {"result": result}
