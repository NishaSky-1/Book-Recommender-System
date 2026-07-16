from flask import Flask, render_template, request

app = Flask(__name__)

book_list = [
    'Harry Potter and the Philosopher\'s Stone',
    'The Hobbit',
    'To Kill a Mockingbird',
    'The Great Gatsby',
    '1984',
    'The Catcher in the Rye'
    'Timeline'
]

# Home page
@app.route('/')
def index():
    return render_template('index.html', book_list=book_list)

# Recommendation page
@app.route('/recommed', methods=['POST'])
def recommend():
    selected_book = request.form.get('book')

    # Abhi ke liye dummy recommendation. Baad me asli logic lagaenge
    recommendations = [
        'Book 1 similar to ' + selected_book,
        'Book 2 similar to ' + selected_book,
        'Book 3 similar to ' + selected_book
    ]

    return render_template('index.html',
                           book_list=book_list,
                           recommendations=recommendations,
                           selected_book=selected_book)

if __name__ == '__main__':
    app.run(debug=True)