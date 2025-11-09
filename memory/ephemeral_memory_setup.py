"""
EphemeralMemory setup for assignment.
Provides a shared memory interface for agents to store and retrieve context/results.
"""

from moya.tools.ephemeral_memory import EphemeralMemory

# Example usage:
# To store a message or result:
# EphemeralMemory.store_message(thread_id, sender, content)
#
# To retrieve a thread summary:
# summary = EphemeralMemory.get_thread_summary(thread_id)

# If you want to configure a custom memory repository:
# from moya.memory.file_system_repo import FileSystemRepository
# EphemeralMemory.memory_repository = FileSystemRepository(base_path="/path/to/memory")
