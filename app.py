from flask import Flask, render_template, request
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
	return render_template('templates/index.html')


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



@app.route("/tambahdata", methods=["GET", "POST"])
def tambah_data():
	if request.method == "POST":
		teksayat = request.form["ayat"]
		terjemah = request.form["terjemah"]

		conn = buat_koneksi()
		cur = conn.cursor()
		perintahquery = "INSERT INTO alFatihah (ayat, terjemah) VALUES (%s, %s)"
		cur.execute(perintahquery, (teksayat, terjemah))
		conn.commit()
		conn.close()

	return render_template("tambah_data.html")


@app.route("/tampilkandata")
def tampilkan_data():
	try:
		conn = buat_koneksi()
		cur = conn.cursor()
		cur.execute("SELECT * FROM alFatihah")
		baris = cur.fetchall()
		conn.close()

		return render_template("tampilkan_data.html", verses=baris)
	
	except pymysql.Error as e:
		return f"Error database {e}"