"""
Configuration of vocabulary game server.
Generated Mon Oct 17 22:59:37 PDT 2016
Edit to fit development or deployment environment.

"""

PORT=5000
DEBUG = True  # Set to False for production use
secret_key="8d9546bcbc4d2184f793ed902cffa183"
success_at_count = 3  # How many matches before we declare victory? 
vocab="data/vocab.txt"  # CHANGE THIS to use another vocabulary file

