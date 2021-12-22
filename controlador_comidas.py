from src.db import obtener_conexion

def insertar_comida(code, url, creator, created_t, created_datetime, last_modified_t, last_modified_datetime, product_name, ingredients_text, nutrition_grade_fr, enery_100g, fat_100g, saturated_fat_100g, carbohydrates_100g, sugars_100g, fiber_100g, proteins_100g, salt_100g, sodium_100g, vitamin_a_100g, vitamin_c_100g, calcium_100g, iron_100g, nutrition_score_fr_100g, nutrition_score_uk_100g):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO comidas(code, url, creator, created_t, created_datetime, last_modified_t, last_modified_datetime, product_name, ingredients_text, nutrition_grade_fr, energy_100g, fat_100g, `saturated-fat_100g`, carbohydrates_100g, sugars_100g, fiber_100g, proteins_100g, salt_100g, sodium_100g, `vitamin-a_100g`, `vitamin-c_100g`, calcium_100g, iron_100g, `nutrition-score-fr_100g`, `nutrition-score-uk_100g`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (code, url, creator, created_t, created_datetime, last_modified_t, last_modified_datetime, product_name, ingredients_text, nutrition_grade_fr, enery_100g, fat_100g, saturated_fat_100g, carbohydrates_100g, sugars_100g, fiber_100g, proteins_100g, salt_100g, sodium_100g, vitamin_a_100g, vitamin_c_100g, calcium_100g, iron_100g, nutrition_score_fr_100g, nutrition_score_uk_100g))
    conexion.commit()
    conexion.close()
    
def eliminar_comida(code):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM comidas WHERE code = %s", (code))
    conexion.commit()
    conexion.close()
    
def obtener_comidas():
    conexion = obtener_conexion()
    juegos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM comidas")
        juegos = cursor.fetchall()
    conexion.close()
    return juegos

def obtener_comidas_por_id(code):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM comidas WHERE code = %s", (code))
        juego = cursor.fetchone()
    conexion.close()
    return juego

def actualizar_comida(nombre, code):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE comidas SET product_name = %s WHERE code = %s", (nombre, code))
    conexion.commit()
    conexion.close()
    
# @app.route("/guardar_juego", methods["POST"])
# def guardar_juego():
#     nombre = request.form["nombre"]
#     descripcion = request.form["descripcion"]
#     precio = request.form["precio"]
#     controlador_juegos.insertar_juego(nombre, descripcion, precio)
#     # De cualquier modo, y si todo fue bien, redireccionar
#     return redirect("/juegos")

# print(insertar_comida("16087", "http://world-en.openfoodfacts.org/product/0000000016087/organic-salted-nut-mix-grizzlies", "usda-ndb-import", "1489055731", "2017-03-09 10:35:31", "1489055731", "2017-03-09 10:35:31", "Organic Salted Nut Mix", "Organic hazelnuts, organic cashews, organic walnuts almonds, organic sunflower oil, sea salt.", "d", 2540, 57.14, 5.36, 17.86, 3.57, 7.1, 17.86, 122.428, 0.482, 0, 0, 0.143, 0.00514, 12, 12))