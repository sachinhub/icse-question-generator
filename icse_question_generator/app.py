from flask import Flask, render_template, jsonify, request
from icse_question_generator.knowledge_base.chemistry_kb import ChemistryKnowledgeBase
from icse_question_generator.generator.chemistry_generator import ChemistryGenerator
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_questions', methods=['POST'])
def generate_questions():
    try:
        data = request.get_json()
        num_questions = int(data.get('num_questions', 5))
        
        # Initialize the knowledge base and generator
        kb = ChemistryKnowledgeBase()
        generator = ChemistryGenerator(kb)
        
        # Get all available chapters
        chapters = list(kb.chapters.keys())
        
        # Generate questions
        questions = []
        for _ in range(num_questions):
            # Randomly select a chapter
            chapter_num = random.choice(chapters)
            chapter = kb.chapters[chapter_num]
            
            # Generate a question
            question = generator.generate_question(chapter)
            
            # Format the question for display
            formatted_question = {
                'text': question.text,
                'type': question.type,
                'marks': question.marks,
                'chapter': chapter.title,
                'correct_answer': question.correct_answer
            }
            
            # Add options for multiple choice questions
            if question.type == 'multiple_choice':
                formatted_question['options'] = question.options
            
            questions.append(formatted_question)
        
        return jsonify({
            'success': True,
            'questions': questions
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True) 