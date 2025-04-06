"""
Knowledge base for ICSE Class 7 Chemistry based on Bharati Bhawan and Selina textbooks.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
import random


@dataclass
class Chapter:
    """Data class representing a chapter in the textbook."""
    number: int
    title: str
    topics: List[str]
    key_concepts: List[str]
    important_formulas: Optional[List[str]] = None
    content: Dict[str, str] = field(default_factory=dict)  # Initialize with empty dict


class ChemistryKnowledgeBase:
    """Knowledge base for ICSE Class 7 Chemistry."""

    def __init__(self):
        """Initialize the chemistry knowledge base."""
        self.chapters = self._initialize_chapters()
        self.question_templates = self._initialize_question_templates()

    def _initialize_chapters(self) -> Dict[int, Chapter]:
        """Initialize the chapters with their content."""
        chapters = {
            1: Chapter(
                number=1,
                title="Elements and Compounds",
                topics=[
                    "Classification of matter",
                    "Elements and their properties",
                    "Compounds and their properties",
                    "Differences between elements and compounds",
                    "Atoms and molecules"
                ],
                key_concepts=[
                    "Elements are pure substances made of one type of atom",
                    "Compounds are substances made of two or more elements chemically combined",
                    "Atoms are the smallest particles of an element",
                    "Molecules are groups of atoms bonded together"
                ],
                content={
                    "Classification of matter": "Matter can be classified into pure substances and mixtures. Pure substances include elements and compounds, while mixtures can be homogeneous or heterogeneous.",
                    "Elements and their properties": "Elements are pure substances made of one type of atom. They cannot be broken down into simpler substances by chemical means. Examples include hydrogen, oxygen, and carbon.",
                    "Compounds and their properties": "Compounds are substances formed when two or more elements are chemically combined in a fixed ratio. They have properties different from their constituent elements.",
                    "Differences between elements and compounds": "Elements are pure substances made of one type of atom, while compounds are made of two or more elements chemically combined. Elements cannot be broken down, while compounds can be decomposed into their elements.",
                    "Atoms and molecules": "Atoms are the smallest particles of an element, while molecules are groups of atoms bonded together. Molecules can be of the same element (like O2) or different elements (like H2O)."
                }
            ),
            2: Chapter(
                number=2,
                title="Physical and Chemical Changes",
                topics=[
                    "Physical changes",
                    "Chemical changes",
                    "Differences between physical and chemical changes",
                    "Examples of physical and chemical changes"
                ],
                key_concepts=[
                    "Physical changes are reversible and do not form new substances",
                    "Chemical changes are irreversible and form new substances",
                    "Physical changes involve changes in state or form",
                    "Chemical changes involve changes in composition"
                ],
                content={
                    "Physical changes": "Physical changes are changes in the physical properties of a substance without changing its chemical composition. They are usually reversible. Examples include melting of ice, boiling of water, and tearing of paper.",
                    "Chemical changes": "Chemical changes result in the formation of new substances with different properties. They are usually irreversible. Examples include burning of paper, rusting of iron, and cooking of food.",
                    "Differences between physical and chemical changes": "Physical changes are reversible and do not form new substances, while chemical changes are irreversible and form new substances. Physical changes involve changes in state or form, while chemical changes involve changes in composition.",
                    "Examples of physical and chemical changes": "Physical changes: melting ice, boiling water, dissolving salt. Chemical changes: burning wood, rusting iron, cooking food."
                }
            ),
            3: Chapter(
                number=3,
                title="Atomic Structure",
                topics=[
                    "Structure of an atom",
                    "Atomic number and mass number",
                    "Electronic configuration",
                    "Valency"
                ],
                key_concepts=[
                    "Atoms consist of protons, neutrons, and electrons",
                    "Atomic number is the number of protons",
                    "Mass number is the sum of protons and neutrons",
                    "Valency is the combining capacity of an atom"
                ],
                content={
                    "Structure of an atom": "An atom consists of a nucleus containing protons and neutrons, with electrons orbiting around it. Protons are positively charged, neutrons are neutral, and electrons are negatively charged.",
                    "Atomic number and mass number": "The atomic number is the number of protons in an atom's nucleus. The mass number is the sum of protons and neutrons. For example, carbon has atomic number 6 and mass number 12.",
                    "Electronic configuration": "Electronic configuration describes how electrons are arranged in an atom's shells. For example, oxygen has electronic configuration 2,6, meaning 2 electrons in the first shell and 6 in the second.",
                    "Valency": "Valency is the combining capacity of an atom. It is determined by the number of electrons in the outermost shell. For example, oxygen has valency 2 as it needs 2 more electrons to complete its outer shell."
                }
            ),
            4: Chapter(
                number=4,
                title="Language of Chemistry",
                topics=[
                    "Chemical symbols",
                    "Chemical formulas",
                    "Chemical equations",
                    "Valency and radicals",
                    "Balancing chemical equations"
                ],
                key_concepts=[
                    "Chemical symbols are abbreviations for elements",
                    "Chemical formulas represent the composition of compounds",
                    "Chemical equations show chemical reactions",
                    "Valency is the combining capacity of an element",
                    "Radicals are groups of atoms that behave as a single unit"
                ],
                content={
                    "Chemical symbols": "Chemical symbols are one or two-letter abbreviations used to represent elements. For example, H for Hydrogen, O for Oxygen, and Na for Sodium. The first letter is always capitalized, and if there's a second letter, it's lowercase.",
                    "Chemical formulas": "Chemical formulas represent the composition of compounds using symbols and numbers. For example, H2O for water (2 hydrogen atoms and 1 oxygen atom), CO2 for carbon dioxide, and NaCl for sodium chloride.",
                    "Chemical equations": "Chemical equations represent chemical reactions using symbols and formulas. They show reactants on the left and products on the right, separated by an arrow. For example: 2H2 + O2 → 2H2O",
                    "Valency and radicals": "Valency is the combining capacity of an element. Common valencies: H(1), O(2), N(3), C(4). Radicals are groups of atoms that behave as a single unit, like OH- (hydroxide), SO4 2- (sulfate), and NO3- (nitrate).",
                    "Balancing chemical equations": "Balancing chemical equations ensures the same number of atoms of each element on both sides. For example: 2H2 + O2 → 2H2O is balanced (4 H atoms and 2 O atoms on both sides)."
                },
                important_formulas=[
                    "Water: H2O",
                    "Carbon dioxide: CO2",
                    "Sodium chloride: NaCl",
                    "Hydrogen peroxide: H2O2",
                    "Ammonia: NH3",
                    "Sulfuric acid: H2SO4",
                    "Nitric acid: HNO3",
                    "Hydrochloric acid: HCl"
                ]
            )
        }
        return chapters

    def _initialize_question_templates(self) -> Dict[str, List[str]]:
        """Initialize templates for generating different types of questions."""
        return {
            "mcq": [
                "Which of the following is {topic}?",
                "What is the correct definition of {topic}?",
                "Which statement about {topic} is true?",
                "Identify the {topic} from the following:",
                "Choose the correct statement about {topic}:"
            ],
            "short": [
                "Define {topic}.",
                "What is {topic}?",
                "Give two examples of {topic}.",
                "State two properties of {topic}.",
                "Explain {topic} in one sentence."
            ],
            "long": [
                "Explain {topic} in detail.",
                "Describe the importance of {topic}.",
                "Compare and contrast {topic} with {related_topic}.",
                "Discuss the properties and uses of {topic}.",
                "Explain how {topic} affects our daily life."
            ]
        }

    def generate_question(self, chapter: Chapter) -> Tuple[str, str, str, int, Optional[List[str]]]:
        """Generate a random question from a chapter."""
        # Randomly select question type with weighted probability
        question_types = ["mcq", "short", "long"]
        weights = [0.4, 0.3, 0.3]  # 40% MCQ, 30% short, 30% long
        question_type = random.choices(question_types, weights=weights)[0]

        # Select a random topic from either topics or key concepts
        if random.random() < 0.7:  # 70% chance of using a topic
            topic = random.choice(chapter.topics)
        else:  # 30% chance of using a key concept
            topic = random.choice(chapter.key_concepts)

        # Get content for the topic
        content = chapter.content.get(topic, "")
        if not content:
            # If no specific content, use a general description
            content = f"{topic} is an important concept in chemistry. It involves various properties and characteristics that are fundamental to understanding chemical processes."

        # Generate question based on type
        if question_type == "mcq":
            template = random.choice(self.question_templates["mcq"])
            question_text = template.format(topic=topic)
            
            # Generate options from content
            options = self._generate_mcq_options(content, topic)
            answer = options[0]  # First option is always correct
            
            return question_text, answer, "mcq", 1, options
            
        elif question_type == "short":
            template = random.choice(self.question_templates["short"])
            question_text = template.format(topic=topic)
            answer = self._generate_short_answer(content)
            
            return question_text, answer, "short", 2, None
            
        else:  # long answer
            template = random.choice(self.question_templates["long"])
            related_topics = [t for t in chapter.topics if t != topic]
            related_topic = random.choice(related_topics) if related_topics else topic
            question_text = template.format(
                topic=topic,
                related_topic=related_topic
            )
            answer = self._generate_long_answer(content)
            
            return question_text, answer, "long", 5, None

    def _generate_mcq_options(self, content: str, correct_topic: str) -> List[str]:
        """Generate options for MCQ questions."""
        # Extract key points from content
        key_points = [p.strip() for p in content.split('.') if p.strip()]
        
        # Use the first key point as correct answer
        correct_answer = key_points[0] if key_points else correct_topic
        
        # Generate incorrect options from other topics
        other_topics = []
        for chapter in self.chapters.values():
            for topic, content in chapter.content.items():
                if topic != correct_topic:
                    points = [p.strip() for p in content.split('.') if p.strip()]
                    other_topics.extend(points)
        
        # Select 3 random incorrect options
        incorrect_options = random.sample(other_topics, 3) if len(other_topics) >= 3 else other_topics
        
        # Combine and shuffle options
        options = [correct_answer] + incorrect_options
        random.shuffle(options)
        
        return options

    def _generate_short_answer(self, content: str) -> str:
        """Generate a short answer from content."""
        # Extract the main points
        points = [p.strip() for p in content.split('.') if p.strip()]
        return '. '.join(points[:2]) + '.' if points else "This concept is important in chemistry."

    def _generate_long_answer(self, content: str) -> str:
        """Generate a long answer from content."""
        # Format the content into a proper answer
        points = [p.strip() for p in content.split('.') if p.strip()]
        return '\n'.join([f"- {point}" for point in points]) if points else "This concept has significant importance in chemistry."

    def get_chapter(self, chapter_number: int) -> Optional[Chapter]:
        """Get a specific chapter by its number."""
        return self.chapters.get(chapter_number)

    def get_all_chapters(self) -> List[Chapter]:
        """Get all chapters in the textbook."""
        return list(self.chapters.values())

    def get_topics_by_chapter(self, chapter_number: int) -> Optional[List[str]]:
        """Get topics covered in a specific chapter."""
        chapter = self.get_chapter(chapter_number)
        return chapter.topics if chapter else None

    def get_key_concepts_by_chapter(self, chapter_number: int) -> Optional[List[str]]:
        """Get key concepts from a specific chapter."""
        chapter = self.get_chapter(chapter_number)
        return chapter.key_concepts if chapter else None 