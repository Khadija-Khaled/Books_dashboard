from flask import Flask, render_template, request
import pandas as pd

from dashboard import routes
from dashboard.routes import app