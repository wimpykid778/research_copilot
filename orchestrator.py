"""
Orchestrator and workflow logic for the research co-pilot assignment.
Stub for assignment structure.
"""


import os
from memory.ephemeral_memory_setup import EphemeralMemory

class ResearchCopilotOrchestrator:
    def __init__(self, pdf_miner, pdf_parser, summarizer, synthesizer, survey_writer):
        self.pdf_miner = pdf_miner
        self.pdf_parser = pdf_parser
        self.summarizer = summarizer
        self.synthesizer = synthesizer
        self.survey_writer = survey_writer

    def run(self, topic=None, pdf_folder=None, thread_id="default-thread"):
        """
        Main workflow:
        1. (Optional) Use PDFMinerAgent to download PDFs if topic is provided.
        2. Use PDFParserAgent to extract text from PDFs.
        3. Use SummarizerAgent to summarize each paper.
        4. Use SynthesizerAgent to synthesize insights/gaps.
        5. Use SurveyWriterAgent to generate the mini-survey.
        """
        # Step 1: Get PDF file paths
        if topic:
            print(f"Mining PDFs for topic: {topic}")
            pdf_paths = self.pdf_miner.mine_pdfs()
        elif pdf_folder:
            pdf_paths = [os.path.join(pdf_folder, f) for f in os.listdir(pdf_folder) if f.lower().endswith('.pdf')]
        else:
            print("No topic or PDF folder provided.")
            return None
        if not pdf_paths:
            print("No PDFs found.")
            return None

        # Step 2: Parse PDFs
        parsed_texts = []
        for pdf_path in pdf_paths:
            print(f"Parsing {pdf_path}")
            text = self.pdf_parser.parse_pdf(pdf_path)
            EphemeralMemory.store_message(thread_id, "parser", f"Parsed {pdf_path}")
            parsed_texts.append({"pdf_path": pdf_path, "text": text})

        # Step 3: Summarize each paper
        summaries = []
        for parsed in parsed_texts:
            print(f"Summarizing {parsed['pdf_path']}")
            summary = self.summarizer.summarize(parsed["text"], metadata={"pdf_path": parsed["pdf_path"]})
            EphemeralMemory.store_message(thread_id, "summarizer", f"Summarized {parsed['pdf_path']}")
            summaries.append(summary)

        # Step 4: Synthesize insights/gaps
        print("Synthesizing cross-paper insights and gaps")
        synthesis = self.synthesizer.synthesize(summaries)
        EphemeralMemory.store_message(thread_id, "synthesizer", "Synthesized insights and gaps")

        # Step 5: Generate mini-survey
        print("Generating mini-survey")
        survey = self.survey_writer.write_survey(synthesis, summaries)
        EphemeralMemory.store_message(thread_id, "survey_writer", "Generated mini-survey")

        return survey
