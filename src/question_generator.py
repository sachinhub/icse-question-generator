from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class QuestionGenerator:
    def __init__(self, llm):
        self.llm = llm
        self.question_prompt = PromptTemplate(
            input_variables=["material", "num_questions"],
            template="""
            You are an expert ICSE Class 7 teacher. Based on the following course material, 
            generate {num_questions} diverse and challenging questions that test different 
            levels of understanding (remembering, understanding, applying, analyzing, evaluating).

            Course Material:
            {material}

            Generate questions that:
            1. Cover different topics from the material
            2. Include various question types (MCQ, short answer, long answer)
            3. Test different cognitive levels
            4. Are appropriate for Class 7 students
            5. Include clear instructions and context

            Format each question with:
            - Question number
            - Question type
            - Marks allocation
            - Clear instructions
            - Any necessary context or diagrams

            Questions:
            """
        )

    def generate(self, material, num_questions=10):
        """Generate questions based on the course material"""
        chain = LLMChain(llm=self.llm, prompt=self.question_prompt)
        response = chain.run(material=material, num_questions=num_questions)
        
        # Split the response into individual questions
        questions = [q.strip() for q in response.split('\n\n') if q.strip()]
        return questions 