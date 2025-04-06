from flask import Flask, render_template, jsonify, request
from icse_question_generator.knowledge_base.chemistry_kb import ChemistryKnowledgeBase
import random

app = Flask(__name__)
kb = ChemistryKnowledgeBase()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_questions', methods=['POST'])
def generate_questions():
    try:
        num_questions = int(request.form.get('num_questions', 5))
        if num_questions < 1 or num_questions > 50:
            return jsonify({'error': 'Please enter a number between 1 and 50'}), 400

        # Get all chapters
        chapters = kb.get_all_chapters()
        questions = []
        
        for _ in range(num_questions):
            # Select a random chapter
            chapter = random.choice(chapters)
            
            # Generate a question from the chapter
            question_text, answer, question_type, marks, options = kb.generate_question(chapter)
            
            # Format the question for display
            formatted_question = {
                'text': question_text,
                'answer': answer,
                'type': question_type,
                'marks': marks,
                'chapter': chapter.title
            }
            
            # Add options for MCQ questions
            if question_type == 'mcq' and options:
                formatted_question['options'] = options
            
            questions.append(formatted_question)
        
        return jsonify({'questions': questions})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 