from flask import Flask, jsonify, request
import game_controller
from db import create_tables

app = Flask(__name__)