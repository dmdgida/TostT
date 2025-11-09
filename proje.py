from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def veritabani_baglanti():
    return sqlite3.connect("menuu.db")

@app.route("/")
def anasayfa():
    conn = veritabani_baglanti()
    kategoriler = conn.execute("SELECT * FROM kategoriler").fetchall()
    conn.close()
    return render_template("index.html", kategoriler=kategoriler)

@app.route("/ekle", methods=["GET", "POST"])
def add_item():
    conn = veritabani_baglanti()
    cursor = conn.cursor()
    kategoriler = cursor.execute("SELECT name FROM kategoriler").fetchall()
    
    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        category = request.form.get("category")
        description = request.form.get("description")
        image = request.form.get("image")

        if not name or not price or not category:
            return "Eksik veri gönderildi!", 400

        try:
            price = float(price)
        except ValueError:
            return "Fiyat geçerli bir sayı olmalı!", 400

        cursor.execute("INSERT INTO menuu (name, price, category, description, image) VALUES (?, ?, ?, ?, ?)",
                       (name, price, category, description, image))
        conn.commit()
        conn.close()

        return redirect(url_for("anasayfa"))

    conn.close()
    return render_template("ekle.html", kategoriler=kategoriler)
    
@app.route("/kategori-ekle", methods=["POST"])
def kategori_ekle():
    name = request.form.get("name")
    image = request.form.get("image") or "default.jpg"

    conn = veritabani_baglanti()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kategoriler WHERE name = ?", (name,))
    var_mi = cursor.fetchone()

    if var_mi:
        conn.close()
        return "❌ Bu kategori zaten var! Başka bir isim gir.", 400
    cursor.execute("INSERT INTO kategoriler (name, image) VALUES (?, ?)", (name, image))
    conn.commit()
    conn.close()

    return redirect(url_for("anasayfa"))

@app.route("/kategori/<kategori_adi>")
def kategori_sayfasi(kategori_adi):
    conn = veritabani_baglanti()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menuu WHERE category = ?", (kategori_adi,))
    yemekler = cursor.fetchall()
    conn.close()

    return render_template("1menü.html", yemekler=yemekler, kategori_adi=kategori_adi)

@app.route("/sil", methods=["GET", "POST"])
def sil():
    kategori = request.args.get("kategori") 

    with veritabani_baglanti() as conn:
        cursor = conn.cursor()

        if request.method == "POST":
            yemek_id = request.form.get("id")
            if yemek_id:
                cursor.execute("DELETE FROM menuu WHERE id = ?", (yemek_id,))
                conn.commit()

        if kategori:
            cursor.execute("SELECT id, name, price, category FROM menuu WHERE category = ?", (kategori,))
        else:
            cursor.execute("SELECT id, name, price, category FROM menuu")

        yemekler = cursor.fetchall()

        cursor.execute("SELECT name FROM kategoriler")
        kategoriler = cursor.fetchall()

    return render_template("sil.html", yemekler=yemekler, kategoriler=kategoriler, secili_kategori=kategori)

@app.route("/kategori-sil", methods=["POST"])
def kategori_sil():
    kategori_adi = request.form.get("kategori_adi")
    if not kategori_adi:
        return "Kategori seçmediniz!", 400
    
    conn = veritabani_baglanti()
    cursor = conn.cursor()

    # Önce o kategoriye ait ürünleri de silebiliriz (opsiyonel)
    cursor.execute("DELETE FROM menuu WHERE category = ?", (kategori_adi,))
    # Sonra kategoriyi sil
    cursor.execute("DELETE FROM kategoriler WHERE name = ?", (kategori_adi,))
    
    conn.commit()
    conn.close()

    return redirect(url_for("sil"))  

@app.route("/1menü.html")
def menu_sayfasi1():
    conn = sqlite3.connect("menuu.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menuu WHERE category = '1menü'")
    yemekler = cursor.fetchall()
    conn.close()
    return render_template("1menü.html", yemekler=yemekler)

@app.route("/2menü.html")
def menu_sayfasi2():
    conn = sqlite3.connect("menuu.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menuu WHERE category = '2menü'")
    yemekler = cursor.fetchall()
    conn.close()
    return render_template("2menü.html", yemekler=yemekler)

@app.route("/3menü.html")
def menu_sayfasi3():
    conn = sqlite3.connect("menuu.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menuu WHERE category = '3menü'")
    yemekler = cursor.fetchall()
    conn.close()
    return render_template("3menü.html", yemekler=yemekler)

@app.route("/4menü.html")
def menu_sayfasi4():
    conn = sqlite3.connect("menuu.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menuu WHERE category = '4menü'")
    yemekler = cursor.fetchall()
    conn.close()
    return render_template("4menü.html", yemekler=yemekler)

@app.route("/5menü.html")
def menu_sayfasi5():
    conn = sqlite3.connect("menuu.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menuu WHERE category = '5menü'")
    yemekler = cursor.fetchall()
    conn.close()
    return render_template("5menü.html", yemekler=yemekler)

@app.route("/6menü.html")
def menu_sayfasi6():
    conn = sqlite3.connect("menuu.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menuu WHERE category = '6menü'")
    yemekler = cursor.fetchall()
    conn.close()
    return render_template("6menü.html", yemekler=yemekler)

@app.route("/7menü.html")
def menu_sayfasi7():
    conn = sqlite3.connect("menuu.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menuu WHERE category = '7menü'")
    yemekler = cursor.fetchall()
    conn.close()
    return render_template("7menü.html", yemekler=yemekler)

@app.route("/8menü.html")
def menu_sayfasi8():
    conn = sqlite3.connect("menuu.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menuu WHERE category = '8menü'")
    yemekler = cursor.fetchall()
    conn.close()
    return render_template("8menü.html", yemekler=yemekler)

@app.route("/9menü.html")
def menu_sayfasi9():
    conn = sqlite3.connect("menuu.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menuu WHERE category = '9menü'")
    yemekler = cursor.fetchall()
    conn.close()
    return render_template("9menü.html", yemekler=yemekler)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)