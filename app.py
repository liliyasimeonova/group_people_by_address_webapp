import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, send_file
from io import StringIO
from unidecode import unidecode

app = Flask(__name__)


def process_data(data):
    df = pd.read_csv(StringIO(data))
    df['Address'] = df['Address'].apply(lambda x: unidecode(
        x.strip()))
    df['AddressKey'] = df['Address'].apply(
        lambda x: x.split(' ')[0]).replace("Shipka", "ul.")
    grouped_data = df.groupby('AddressKey')['Name'].apply(
        lambda x: ', '.join(sorted(x))).reset_index()
    return grouped_data[['AddressKey', 'Name']]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    if 'file' in request.files:
        file = request.files['file']
        data = file.read().decode('utf-8')
    elif 'data' in request.form:
        data = request.form['data']
    else:
        return redirect(url_for('index'))

    grouped_data = process_data(data)

    result_text = ''
    for _, group in grouped_data.groupby('AddressKey'):
        names = ', '.join(group['Name'])
        result_text += f"{names}\n"

    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(result_text)

    return render_template('result.html', result=result_text)


@app.route('/download')
def download():
    return send_file('output.txt', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
