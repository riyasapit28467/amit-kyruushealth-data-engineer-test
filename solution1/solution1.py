from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/popular_names'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/getPopularNames', methods=['GET'])
def get_popular_names():
    start_year = request.args.get('start_year', type=int)
    end_year = request.args.get('end_year', type=int)
    if (start_year is None or end_year is None) or (start_year > end_year):
        return jsonify({"error": "Please provide both valid start_year and end_year."}), 400
    # Log incoming parameters
    print(f"Received request with start_year: {start_year}, end_year: {end_year}")

    if start_year is None or end_year is None:
        return jsonify({"error": "Please provide both start_year and end_year."}), 400

    male_query = text("""
        SELECT name, SUM(occurrence) AS total_occurrence
        FROM users
        WHERE year >= :start_year AND year <= :end_year AND gender = 'M'
        GROUP BY name
        ORDER BY total_occurrence DESC
        LIMIT 1
    """)
    female_query = text("""
        SELECT name, SUM(occurrence) AS total_occurrence
        FROM users
        WHERE year >= :start_year AND year <= :end_year AND gender = 'F'
        GROUP BY name
        ORDER BY total_occurrence DESC
        LIMIT 1
    """)
    try:
        male_result = db.session.execute(male_query, {'start_year': start_year, 'end_year': end_year}).fetchone()
        female_result = db.session.execute(female_query, {'start_year': start_year, 'end_year': end_year}).fetchone()

        if male_result is None:
            return jsonify({"error": "No results found."}), 404

        response = f"M: {male_result[0]} F: {female_result[0] if female_result else 'No result'}"
        return response

    except Exception as e:
        print("Error occurred:", str(e))  # Log the detailed error
        return jsonify({"error": str(e)}), 500  # Return the error message

if __name__ == '__main__':
    app.run(debug=True)