# TODO: make interest based learning router
# TODO: make interest based learning learning pickle file
# TODO: in routes pass arguments to predictions and return the prediction result for the above
# TODO: MongoDB connection
# TODO: Mongo schema models
# TODO: Deployment on render
# import os
#
# from dotenv import load_dotenv
# from fastapi import FastAPI, Request
# from pymongo import MongoClient
#
# load_dotenv()
#
# # MONGODB DATABASE CONNECTION
# connection = MongoClient(os.getenv("MONGODB_URI"))
# if connection:
#     print("Connected Successfully!")
# else:
#     print("Something went wrong while connection!")
# # ------------------------------------------------------------------------------------------------------
#
# app = FastAPI()
#
#
# @app.get("/", description="This is the home route")
# def home(req: Request):
#     return req.base_url
#
# # @app.route("/interest_based_learning/")
