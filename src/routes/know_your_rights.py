# import joblib
# from fastapi import APIRouter, Body
#
# from config.db import db
# from utils.absolute_root import root_path
#
# know_your_right_router = APIRouter()
#
# # load know_your_right_model
# model = joblib.load(root_path + '/public/ml_models/model.pkl')
# vectorizer = joblib.load(root_path + '/public/ml_models/vectorizer.pkl')
#
#
# @know_your_right_router.post("/", tags=["Know Your Rights"])
# def know_your_rights(context: str = Body(...)):
#     act = model.predict(vectorizer.transform([context]))
#     act_name = act.tolist()[0]
#     act_obj = db.rights.find_one({"ACT": act_name})
#     return {
#         "act": act_name,
#         "description": act_obj["Description"] | ""
#     }
