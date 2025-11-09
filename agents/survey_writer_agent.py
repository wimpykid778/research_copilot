"""
SurveyWriterAgent: Uses OpenAIAgent to generate the final mini-survey with citations.
Stub for assignment structure.
"""


class SurveyWriterAgent:
    def __init__(self, openai_agent):
        self.openai_agent = openai_agent

    def write_survey(self, synthesis, summaries):
        """
        Generate a concise mini-survey (≤800 words) with inline citations using OpenAIAgent.
        Returns the survey as a string.
        """
        # Prepare context for the prompt
        joined_summaries = "\n\n".join(f"Paper {i+1}: {s['summary']}" for i, s in enumerate(summaries) if s.get('summary'))
        prompt = (
            "Write a concise mini-survey (≤800 words) on the following topic, synthesizing the provided insights and summaries. "
            "Include inline citations in the form [Paper 1], [Paper 2], etc.\n\n"
            f"Synthesis:\n{synthesis.get('synthesis', '')}\n\n"
            f"Summaries:\n{joined_summaries}\n\n"
            "The survey should be clear, well-structured, and highlight key trends, gaps, and future directions."
        )
        try:
            survey = self.openai_agent.handle_message(prompt)
            return survey
        except Exception as e:
            print(f"Error writing survey: {e}")
            return ""
