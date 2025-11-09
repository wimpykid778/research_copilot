"""
CLI entrypoint for the research co-pilot assignment.
Stub for assignment structure.
"""


import argparse
import os
import sys
from agents.pdf_miner_agent import PDFMinerAgent
from agents.pdf_parser_agent import PDFParserAgent
from agents.summarizer_agent import SummarizerAgent
from agents.synthesizer_agent import SynthesizerAgent
from agents.survey_writer_agent import SurveyWriterAgent
from orchestrator import ResearchCopilotOrchestrator

# Import OpenAIAgent from MOYA (user must configure API key)
from moya.agents.openai_agent import OpenAIAgent, OpenAIAgentConfig

def main():
    parser = argparse.ArgumentParser(description="Research Co-Pilot: Multi-agent research survey generator")
    parser.add_argument('--topic', type=str, help='Research topic to mine papers for (uses arXiv)')
    parser.add_argument('--pdf-folder', type=str, help='Folder containing PDF files to process')
    parser.add_argument('--output', type=str, default='mini_survey.txt', help='Output file for the mini-survey')
    parser.add_argument('--openai-api-key', type=str, default=None, help='OpenAI API key (or set OPENAI_API_KEY env var)')
    args = parser.parse_args()

    # Set up OpenAIAgent
    api_key = args.openai_api_key or os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("OpenAI API key required. Use --openai-api-key or set OPENAI_API_KEY env var.")
        sys.exit(1)
    openai_agent = OpenAIAgent(OpenAIAgentConfig(
        agent_name="openai_agent",
        description="LLM agent for summarization, synthesis, and survey writing",
        api_key=api_key,
        model_name="gpt-4o",
        agent_type="ChatAgent",
        is_streaming=False
    ))

    # Set up agents
    pdf_miner = PDFMinerAgent(args.topic, download_dir="pdfs_downloaded")
    pdf_parser = PDFParserAgent()
    summarizer = SummarizerAgent(openai_agent)
    synthesizer = SynthesizerAgent(openai_agent)
    survey_writer = SurveyWriterAgent(openai_agent)

    # Set up orchestrator
    orchestrator = ResearchCopilotOrchestrator(
        pdf_miner, pdf_parser, summarizer, synthesizer, survey_writer
    )

    # Run workflow
    survey = orchestrator.run(topic=args.topic, pdf_folder=args.pdf_folder)
    if survey:
        with open(args.output, 'w') as f:
            f.write(survey)
        print(f"Mini-survey written to {args.output}")
    else:
        print("No survey generated.")

if __name__ == "__main__":
    main()
