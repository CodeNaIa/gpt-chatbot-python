"""
Módulo principal do chatbot
"""
from .core import ChatBot
from .config import load_config

__all__ = ["ChatBot", "load_config"] 