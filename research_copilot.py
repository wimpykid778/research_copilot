#!/usr/bin/env python3
"""
Entry point script for Research Co-Pilot.
This script allows running the application from the root directory.

Usage:
    python research_copilot.py --topic "Your Research Topic"
    python research_copilot.py --pdf-folder pdfs_downloaded/
"""

import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run main
from src.main import main

if __name__ == "__main__":
    main()
