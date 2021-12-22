from flask import Flask, render_template, request, redirect
import controlador_comidas

app = Flask(__name__)

@app.route("/guardar_comida", methods=["POST"])
def guardar_juego():
    code = request.form["code"]
    url = request.form["url"]
    creator = request.form["creator"]
    created_t = request.form["created_t"]
    created_datetime = request.form["created_datetime"]
    last_modified_t = request.form["last_modified_t"]
    last_modified_datetime = request.form["last_modified_datetime"]
    product_name = request.form["product_name"]
    ingredients_text = request.form["ingredients_text"]
    nutrition_grade_fr = request.form["nutrition_grade_fr"]
    enery_100g = request.form["enery_100g"]
    fat_100g = request.form["fat_100g"]
    saturated_fat_100g = request.form["saturated_fat_100g"]
    carbohydrates_100g = request.form["carbohydrates_100g"]
    sugars_100g = request.form["sugars_100g"]
    fiber_100g = request.form["fiber_100g"]
    proteins_100g = request.form["proteins_100g"]
    salt_100g = request.form["salt_100g"]
    sodium_100g = request.form["sodium_100g"]
    vitamin_a_100g = request.form["vitamin_a_100g"]
    vitamin_c_100g = request.form["vitamin_c_100g"]
    calcium_100g = request.form["calcium_100g"]
    iron_100g = request.form["iron_100g"]
    nutrition_score_fr_100g = request.form["nutrition_score_fr_100g"]
    nutrition_score_uk_100g = request.form["nutrition_score_uk_100g"]
    
    controlador_comidas.insertar_comida(code, url, creator, created_t, created_datetime, last_modified_t, last_modified_datetime, product_name, ingredients_text, nutrition_grade_fr, enery_100g, fat_100g, saturated_fat_100g, carbohydrates_100g, sugars_100g, fiber_100g, proteins_100g, salt_100g, sodium_100g, vitamin_a_100g, vitamin_c_100g, calcium_100g, iron_100g, nutrition_score_fr_100g, nutrition_score_uk_100g)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/get_comidas")

@app.route("/get_comidas")
def get_comidas():
    comidas = controlador_comidas.obtener_comidas()
    # De cualquier modo, y si todo fue bien, redireccionar
    return render_template("personas.html", comidas = comidas)

@app.route("/")
def prueba():
    return "Hola"

@app.route("/eliminar_comida", methods=["POST"])
def borrar_comida():
    controlador_comidas.eliminar_comida(request.form["code"])
    return redirect("/get_comidas")

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)