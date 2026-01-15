from flask import Flask, render_template, send_file
import pymysql
import os

app = Flask(__name__)

def buat_koneksi():
	return pymysql.connect(
		user = "root",
		password = "B1smill4h",
		host = "localhost",
		db = "new_project",
		port = 3306,
		charset = "utf8mb4"
	)

@app.route("/test")
def static_test():
	return send_file('templates/index.html')


@app.route("/")
def index():
	try:
		conn = buat_koneksi()
		cur = conn.cursor()
		cur.execute("SELECT * FROM alFatihah")
		baris = cur.fetchall()
		conn.close()
	#	status = "KONEKSI BERHASIL"

		return render_template("index.html", verses=baris)
	
	except pymysql.Error as e:
		return f"Error database {e}"