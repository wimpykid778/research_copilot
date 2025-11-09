"""
SummarizerAgent: Uses OpenAIAgent to summarize text.
Stub for assignment structure.
"""


class SummarizerAgent:
    def __init__(self, openai_agent):
        self.openai_agent = openai_agent

    def summarize(self, text, metadata=None):
        """
        Summarize the given text using the OpenAIAgent.
        Returns a structured summary (dict or string).
        """
        prompt = (
            "Summarize the following research paper text in a structured format: "
            "- Main contributions\n- Methods\n- Key findings\n- Limitations\n- Citation (if available)\n"
            "Text:\n" + (text[:4000] if text else "")  # Truncate for token safety
        )
        try:
            summary = self.openai_agent.handle_message(prompt)
            return {"summary": summary, "metadata": metadata}
        except Exception as e:
            print(f"Error summarizing text: {e}")
            return {"summary": "", "metadata": metadata}
