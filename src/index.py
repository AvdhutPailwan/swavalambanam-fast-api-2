# uvicorn index:app --reload

from dotenv import load_dotenv
from fastapi import FastAPI

from routes.interest_based_learning import interest_based_learning_router
# , UploadFile, File
# from fastapi.responses import JSONResponse
# import shutil
# import uuid
from routes.note import note
from routes.question_and_answer_chatbot import question_and_answer_chatbot_router
from routes.quiz import quiz
from routes.know_your_rights import know_your_right_router

load_dotenv()

app = FastAPI()

# app.include_router(note, prefix="/notes")
app.include_router(interest_based_learning_router, prefix="/interest_based_learning")
app.include_router(question_and_answer_chatbot_router, prefix="/question_and_answer_chatbot")
app.include_router(quiz, prefix="/quiz")
app.include_router(know_your_right_router, prefix="/know_your_right")

# @app.post("/upload/audio/")
# async def upload_audio_file(audio_file: UploadFile = File(...)):
#     try:
#         # Create a unique filename
#         file_extension = audio_file.filename.split(".")[-1]
#         file_id = str(uuid.uuid4())
#         file_path = f"../public/uploads/audio/{file_id}.{file_extension}"
#
#         # Save the uploaded file
#         with open(file_path, "wb") as buffer:
#             shutil.copyfileobj(audio_file.file, buffer)
#
#         # Construct the URL to access the uploaded file
#         base_url = "http://127.0.0.1:8000"  # Replace with your actual domain
#         file_url = f"{base_url}/{file_path}"
#
#         return JSONResponse(content={"file_url": file_url}, status_code=200)
#
#     except Exception as e:
#         return JSONResponse(content={"error": f"Failed to upload: {e}"}, status_code=500)
