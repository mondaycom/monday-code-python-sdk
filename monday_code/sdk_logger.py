"""
Monday SDK Logging Utility

Add this to track SDK usage in your local development.
"""
import logging
from typing import Any, Callable

# Configure logging format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def log_sdk_usage(message: str):
    """Simple function to log SDK usage"""
    logging.info(f"📱 [Monday SDK] {message}")
