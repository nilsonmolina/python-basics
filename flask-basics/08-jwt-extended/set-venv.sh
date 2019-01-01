#!/bin/sh
# CHECK IF VIRTUAL ENVIRONMENT EXISTS
if [ ! -d "./venv" ] ; then
    # CREATE & PREPARE VIRTUAL ENVIRONMENT
    python3 -m venv venv && # can also use: virtualenv venv
    . venv/bin/activate &&
    pip install --upgrade pip &&
    pip install flask-restful
    pip install flask-jwt
    pip install flask-sqlalchemy
    pip install pylint
    pip install pylint-flask
else
    # ACTIVATE VIRTUAL ENVIRONMENT
    . venv/bin/activate
fi

# -------------
# HELPFUL INFO
# -------------
# --- RUN THIS SCRIPT USING:
# source set-venv.sh

# --- RUN SERVER USING: 
# python app.py