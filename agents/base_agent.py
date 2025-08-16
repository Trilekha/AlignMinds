from typing import Dict, Any
import json
import os
from openai import OpenAI


class BaseAgent:
    def __init__(self, name: str, instructions: str):
        self.name = name
        self.instructions = instructions
        
        # Initialize Ollama client with minimal parameters to avoid conflicts
        try:
            self.ollama_client = OpenAI(
                base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1"),
                api_key=os.getenv("OLLAMA_API_KEY", "ollama")
            )
            print(f"✅ {self.name}: Successfully initialized Ollama client")
        except Exception as e:
            print(f"❌ Error initializing Ollama client for {self.name}: {str(e)}")
            raise

    async def run(self, messages: list) -> Dict[str, Any]:
        """Default run method to be overridden by child classes"""
        raise NotImplementedError("Subclasses must implement run()")

    def _query_ollama(self, prompt: str) -> str:
        """Query Ollama model with the given prompt"""
        try:
            response = self.ollama_client.chat.completions.create(
                model="llama3.2",
                messages=[
                    {"role": "system", "content": self.instructions},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=2000,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"❌ Error querying Ollama model 'llama3.2': {str(e)}")
            print(f"   Make sure Ollama is running: ollama serve")
            print(f"   Make sure model is available: ollama pull llama3.2")
            raise

    def _parse_json_safely(self, text: str) -> Dict[str, Any]:
        """Safely parse JSON from text, handling potential errors"""
        try:
            # Remove any markdown code blocks first
            if "```json" in text:
                start = text.find("```json") + 7
                end = text.find("```", start)
                if end != -1:
                    text = text[start:end].strip()
            elif "```" in text:
                start = text.find("```") + 3
                end = text.find("```", start)
                if end != -1:
                    text = text[start:end].strip()
            
            # Try to find JSON-like content between curly braces
            start = text.find("{")
            end = text.rfind("}")
            if start != -1 and end != -1:
                json_str = text[start : end + 1]
                return json.loads(json_str)
            return {"error": "No JSON content found", "raw_text": text}
        except json.JSONDecodeError as e:
            return {"error": f"Invalid JSON content: {str(e)}", "raw_text": text}
