"""
Chemistry question generator module for ICSE.
"""

from typing import List, Dict
from dataclasses import dataclass
from enum import Enum


class QuestionType(Enum):
    """Types of questions that can be generated."""
    MULTIPLE_CHOICE = "multiple_choice"
    FILL_IN_BLANKS = "fill_in_blanks"
    SHORT_ANSWER = "short_answer"
    LONG_ANSWER = "long_answer"
    DIAGRAM = "diagram"


@dataclass
class Question:
    """Data class representing a question."""
    question_type: QuestionType
    question_text: str
    options: List[str] = None
    correct_answer: str = None
    marks: int = 1


class ChemistryGenerator:
    """Class for generating chemistry questions."""

    def __init__(self):
        """Initialize the chemistry question generator."""
        self.atomic_numbers = {
            "hydrogen": 1,
            "helium": 2,
            "lithium": 3,
            "beryllium": 4,
            "boron": 5,
            "carbon": 6,
            "nitrogen": 7,
            "oxygen": 8,
            "fluorine": 9,
            "neon": 10
        }

    def generate_questions(self, num_questions: int = 10) -> List[Question]:
        """
        Generate a set of chemistry questions.
        
        Args:
            num_questions: Number of questions to generate
            
        Returns:
            List of Question objects
        """
        questions = []
        
        # Generate multiple choice questions
        questions.extend(self._generate_multiple_choice_questions(num_questions // 2))
        
        # Generate fill in the blanks questions
        questions.extend(self._generate_fill_in_blanks_questions(num_questions // 2))
        
        return questions

    def _generate_multiple_choice_questions(self, num: int) -> List[Question]:
        """Generate multiple choice questions about atomic structure."""
        questions = []
        
        # Sample question about atomic numbers
        questions.append(Question(
            question_type=QuestionType.MULTIPLE_CHOICE,
            question_text="The element with atomic number 3 is:",
            options=["Lithium", "Beryllium", "Boron", "Carbon"],
            correct_answer="Lithium",
            marks=1
        ))
        
        # Add more questions here...
        
        return questions[:num]

    def _generate_fill_in_blanks_questions(self, num: int) -> List[Question]:
        """Generate fill in the blanks questions about atomic structure."""
        questions = []
        
        # Sample question about atomic numbers
        questions.append(Question(
            question_type=QuestionType.FILL_IN_BLANKS,
            question_text="The atomic number of carbon is ______.",
            correct_answer="6",
            marks=1
        ))
        
        # Add more questions here...
        
        return questions[:num] 