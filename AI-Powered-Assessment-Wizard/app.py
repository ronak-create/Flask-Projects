from flask import Flask, render_template, request, jsonify
import os
from PIL import Image
import google.generativeai as genai
import re
import html
import json


app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configure API Key
genai.configure(api_key="AIzaSyAvswdOPVKHM1ew374flcLM_RHnpJFji6A")  # Replace with your actual key
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

def clean_text(text):
    """
    Clean and sanitize the generated text before sending to frontend.
    """
    if not text:
        return ""
    
    # Decode HTML entities
    text = html.unescape(text)
    
    # Remove any null bytes
    text = text.replace('\x00', '')
    
    # Replace multiple newlines with a single newline
    text = re.sub(r'\n\s*\n', '\n', text)
    
    # Remove leading/trailing whitespace
    text = text.strip()
    
    # Replace tabs with spaces
    text = text.replace('\t', '    ')
    
    # Remove any control characters except newlines
    text = ''.join(char for char in text if char == '\n' or char.isprintable())
    
    # Ensure proper JSON escaping
    text = text.replace('\\', '\\\\')
    text = text.replace('"', '\\"')
    
    return text

@app.route('/')
def upload_form():
    return render_template('index.html')

@app.route('/process_images', methods=['POST'])
def process_images():
    if 'images' not in request.files:
        return jsonify({'error': 'No images uploaded'}), 400

    images = request.files.getlist('images')
    uploaded_images = []

    for img in images:
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)
        img.save(img_path)
        uploaded_images.append(Image.open(img_path))

    # Define the prompt
    prompt = "Choose the correct answer. Give output in a JSON format like {1:'<answer>',2:'<answer>'}:"

    try:
        # Send prompt to the model
        response = model.generate_content([prompt] + uploaded_images)
        # Clean the generated text
        response = response.text
        cleaned_dict = json.loads(response.replace("```json\n", "").replace("```", ""))
        # Extract JSON from the cleaned text
        try:
            # Parse the cleaned text as JSON
            if not isinstance(cleaned_dict, dict):
                raise ValueError("Generated text is not in JSON format.")
        except Exception as parse_error:
            return jsonify({'error': f"Failed to parse JSON: {str(parse_error)}"}), 500
        return jsonify({'generated_text': cleaned_dict})
        
    except Exception as e:
        return jsonify({'error': f'Error processing request: {str(e)}'}), 500

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)