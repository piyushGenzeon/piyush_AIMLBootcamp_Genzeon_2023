from flask import Flask, render_template, request
import PyPDF2
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Get the uploaded file from the request
    pdf_file = request.files['pdfFile']

    # Check if a file was uploaded
    if pdf_file:
        # Read the PDF file and extract its text
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        # Process the extracted text (e.g., pass it to the ML model for prediction)

        # Return the extracted text as a response or perform further processing

        return text

        # data = {'Text': [text]}
        # df = pd.DataFrame(data)

        # # Return the dataframe as a response or perform further processing
        #
        # return df.to_html(index=False)
    else:
        return "No file uploaded."

if __name__ == '__main__':
    app.run(debug=True)
