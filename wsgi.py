import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from app import app as application

#from app berarti : buka file app.py - baca isi di dalamnya
#import app : ambil objek flask dari file tersebut
#as application : agar apache bisa menjalankan flask
