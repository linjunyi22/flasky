from . import config
from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)
app.config.from_object(config)
