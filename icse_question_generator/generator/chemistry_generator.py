from dataclasses import dataclass
from typing import List, Optional, Dict, Tuple
import random


@dataclass
class Question:
    """Data class representing a generated question."""
    text: str
    type: str
    marks: int
    options: Optional[List[str]] = None
    correct_answer: Optional[str] = None


class ChemistryGenerator:
    """Generator for chemistry questions based on the knowledge base."""

    def __init__(self, knowledge_base):
        """Initialize the generator with a knowledge base."""
        self.kb = knowledge_base
        self._initialize_question_data()

    def _initialize_question_data(self):
        """Initialize data for generating questions."""
        self.element_data = {
            "Hydrogen": {"symbol": "H", "atomic_number": 1, "valency": 1, "type": "non-metal"},
            "Oxygen": {"symbol": "O", "atomic_number": 8, "valency": 2, "type": "non-metal"},
            "Carbon": {"symbol": "C", "atomic_number": 6, "valency": 4, "type": "non-metal"},
            "Nitrogen": {"symbol": "N", "atomic_number": 7, "valency": 3, "type": "non-metal"},
            "Sodium": {"symbol": "Na", "atomic_number": 11, "valency": 1, "type": "metal"},
            "Calcium": {"symbol": "Ca", "atomic_number": 20, "valency": 2, "type": "metal"},
            "Iron": {"symbol": "Fe", "atomic_number": 26, "valency": 3, "type": "metal"},
            "Helium": {"symbol": "He", "atomic_number": 2, "valency": 0, "type": "noble gas"},
            "Neon": {"symbol": "Ne", "atomic_number": 10, "valency": 0, "type": "noble gas"}
        }

    def generate_question(self, chapter) -> Question:
        """Generate a random question from the given chapter."""
        # Randomly select a question type with weighted probability
        question_type = random.choices(
            ['multiple_choice', 'short_answer', 'long_answer'],
            weights=[0.4, 0.4, 0.2]
        )[0]

        if question_type == 'multiple_choice':
            return self._generate_multiple_choice(chapter)
        elif question_type == 'short_answer':
            return self._generate_short_answer(chapter)
        else:
            return self._generate_long_answer(chapter)

    def _generate_multiple_choice(self, chapter) -> Question:
        """Generate a multiple choice question."""
        # Question types and their generation functions
        question_types = [
            self._generate_symbol_question,
            self._generate_atomic_number_question,
            self._generate_valency_question,
            self._generate_element_type_question
        ]

        # Randomly select a question type
        question_generator = random.choice(question_types)
        return question_generator()

    def _generate_symbol_question(self) -> Question:
        """Generate a question about chemical symbols."""
        element_name = random.choice(list(self.element_data.keys()))
        correct_symbol = self.element_data[element_name]["symbol"]
        
        # Generate wrong options
        other_symbols = [data["symbol"] for name, data in self.element_data.items() if name != element_name]
        wrong_options = random.sample(other_symbols, 3)
        
        options = wrong_options + [correct_symbol]
        random.shuffle(options)
        
        return Question(
            text=f"What is the chemical symbol for {element_name}?",
            type='multiple_choice',
            marks=1,
            options=options,
            correct_answer=correct_symbol
        )

    def _generate_atomic_number_question(self) -> Question:
        """Generate a question about atomic numbers."""
        element_name = random.choice(list(self.element_data.keys()))
        correct_number = self.element_data[element_name]["atomic_number"]
        
        # Generate wrong options
        other_numbers = [data["atomic_number"] for name, data in self.element_data.items() if name != element_name]
        wrong_options = random.sample(other_numbers, 3)
        
        options = [str(num) for num in wrong_options + [correct_number]]
        random.shuffle(options)
        
        return Question(
            text=f"What is the atomic number of {element_name}?",
            type='multiple_choice',
            marks=1,
            options=options,
            correct_answer=str(correct_number)
        )

    def _generate_valency_question(self) -> Question:
        """Generate a question about valency."""
        element_name = random.choice(list(self.element_data.keys()))
        correct_valency = self.element_data[element_name]["valency"]
        
        # Generate wrong options
        possible_valencies = [0, 1, 2, 3, 4]
        wrong_options = [v for v in possible_valencies if v != correct_valency][:3]
        
        options = [str(num) for num in wrong_options + [correct_valency]]
        random.shuffle(options)
        
        return Question(
            text=f"What is the valency of {element_name}?",
            type='multiple_choice',
            marks=1,
            options=options,
            correct_answer=str(correct_valency)
        )

    def _generate_element_type_question(self) -> Question:
        """Generate a question about element types."""
        element_name = random.choice(list(self.element_data.keys()))
        correct_type = self.element_data[element_name]["type"]
        
        options = ["metal", "non-metal", "noble gas", "metalloid"]
        
        return Question(
            text=f"Which type of element is {element_name}?",
            type='multiple_choice',
            marks=1,
            options=options,
            correct_answer=correct_type
        )

    def _generate_short_answer(self, chapter) -> Question:
        """Generate a short answer question."""
        topic = random.choice(list(chapter.content.keys()))
        content = chapter.content[topic]

        question_text = f"Define {topic.lower()}."
        
        return Question(
            text=question_text,
            type='short_answer',
            marks=2,
            correct_answer=content
        )

    def _generate_long_answer(self, chapter) -> Question:
        """Generate a long answer question."""
        topic = random.choice(list(chapter.content.keys()))
        content = chapter.content[topic]

        question_text = f"Explain {topic.lower()} in detail with examples."
        
        # Format the content into a proper answer
        answer = content
        
        return Question(
            text=question_text,
            type='long_answer',
            marks=5,
            correct_answer=answer
        ) 