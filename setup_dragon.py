#!/usr/bin/env python3
"""
Dragon Template Setup Script
Copyright © 2025 Seed13 Productions. All rights reserved.

Interactive setup script to customize the Dragon template for your specific use case.
"""

import os
import json
import re
from pathlib import Path


class DragonSetup:
    def __init__(self):
        self.config = {}
        self.template_file = "dragon_template.py"
        self.claude_template = "CLAUDE_template.md"
        
        # Predefined color schemes
        self.color_schemes = {
            "purple": {
                "PRIMARY_COLOR": "#2d1b69",
                "SECONDARY_COLOR": "#4c1d95", 
                "ACCENT_COLOR": "#facc15",
                "FOOTER_COLOR": "#a855f7",
                "BUTTON_1_COLOR": "#ef4444",
                "BUTTON_1_COLOR_DARK": "#dc2626",
                "BUTTON_2_COLOR": "#fbbf24",
                "BUTTON_2_COLOR_DARK": "#f59e0b"
            },
            "teal": {
                "PRIMARY_COLOR": "#0f4c75",
                "SECONDARY_COLOR": "#2d6a4f",
                "ACCENT_COLOR": "#40e0d0", 
                "FOOTER_COLOR": "#7dd3fc",
                "BUTTON_1_COLOR": "#0ea5e9",
                "BUTTON_1_COLOR_DARK": "#0284c7",
                "BUTTON_2_COLOR": "#06b6d4",
                "BUTTON_2_COLOR_DARK": "#0891b2"
            },
            "green": {
                "PRIMARY_COLOR": "#064e3b",
                "SECONDARY_COLOR": "#065f46",
                "ACCENT_COLOR": "#10b981",
                "FOOTER_COLOR": "#6ee7b7",
                "BUTTON_1_COLOR": "#059669",
                "BUTTON_1_COLOR_DARK": "#047857",
                "BUTTON_2_COLOR": "#10b981",
                "BUTTON_2_COLOR_DARK": "#059669"
            },
            "blue": {
                "PRIMARY_COLOR": "#1e3a8a",
                "SECONDARY_COLOR": "#1e40af",
                "ACCENT_COLOR": "#3b82f6",
                "FOOTER_COLOR": "#93c5fd",
                "BUTTON_1_COLOR": "#2563eb",
                "BUTTON_1_COLOR_DARK": "#1d4ed8",
                "BUTTON_2_COLOR": "#3b82f6",
                "BUTTON_2_COLOR_DARK": "#2563eb"
            },
            "red": {
                "PRIMARY_COLOR": "#7f1d1d",
                "SECONDARY_COLOR": "#991b1b",
                "ACCENT_COLOR": "#f87171",
                "FOOTER_COLOR": "#fca5a5",
                "BUTTON_1_COLOR": "#dc2626",
                "BUTTON_1_COLOR_DARK": "#b91c1c",
                "BUTTON_2_COLOR": "#ef4444",
                "BUTTON_2_COLOR_DARK": "#dc2626"
            }
        }
    
    def welcome(self):
        print("🐉 Welcome to Dragon Template Setup!")
        print("=" * 50)
        print("This script will help you create a custom Dragon AI analysis tool.")
        print("Answer the questions below to configure your Dragon variant.\n")
    
    def get_basic_config(self):
        """Get basic configuration from user"""
        print("📝 Basic Configuration")
        print("-" * 20)
        
        # Dragon name and type
        dragon_name = input("Enter your Dragon name (e.g., 'Script', 'Lab', 'Code'): ").strip()
        if not dragon_name:
            dragon_name = "Custom"
        
        # Data type
        data_type = input("What type of data will this analyze? (e.g., 'Document', 'Video', 'Code'): ").strip()
        if not data_type:
            data_type = "Data"
        
        # Description
        description = input(f"Brief description of Dragon{dragon_name}: ").strip()
        if not description:
            description = f"AI-powered {data_type.lower()} analysis tool"
        
        # Emoji
        emoji = input(f"Choose an emoji for Dragon{dragon_name} (e.g., 📄, 🎬, 💻): ").strip()
        if not emoji:
            emoji = "🐉"
        
        self.config.update({
            "TYPE": dragon_name,
            "type": dragon_name.lower(),
            "DATA_TYPE": data_type,
            "data_type": data_type.lower(),
            "DESCRIPTION": description,
            "EMOJI": emoji,
            "CLASS_SUFFIX": self.suggest_class_suffix(dragon_name, data_type),
            "instance": dragon_name.lower(),
        })
    
    def suggest_class_suffix(self, dragon_name, data_type):
        """Suggest a class suffix based on dragon name and data type"""
        suggestions = {
            "sight": "Eye", "vision": "Eye", "image": "Eye",
            "song": "Ear", "audio": "Ear", "sound": "Ear", 
            "script": "Reader", "document": "Reader", "text": "Reader",
            "lab": "Analyst", "data": "Analyst", "stats": "Analyst",
            "code": "Coder", "dev": "Coder", "program": "Coder"
        }
        
        # Check dragon name first
        for key, suffix in suggestions.items():
            if key in dragon_name.lower():
                return suffix
        
        # Check data type
        for key, suffix in suggestions.items():
            if key in data_type.lower():
                return suffix
        
        return "Processor"  # Default
    
    def get_api_config(self):
        """Get API configuration"""
        print("\n🔌 API Configuration")
        print("-" * 20)
        
        # Default model
        default_model = input("Default Ollama model name (e.g., 'llava', 'whisper', 'codellama'): ").strip()
        if not default_model:
            default_model = "llama2"
        
        # Model keywords for discovery
        keywords_input = input("Keywords to identify relevant models (comma-separated): ").strip()
        if keywords_input:
            keywords = [f"'{k.strip()}'" for k in keywords_input.split(',')]
        else:
            keywords = ["'llama'", "'chat'"]
        
        # OpenAI models
        openai_input = input("OpenAI models to include (comma-separated, or 'none'): ").strip()
        if openai_input.lower() == 'none':
            openai_models = "[]"
        elif openai_input:
            openai_models = [f"'openai:{m.strip()}'" for m in openai_input.split(',')]
        else:
            openai_models = ["'openai:gpt-4', 'openai:gpt-3.5-turbo'"]
        
        self.config.update({
            "DEFAULT_MODEL": default_model,
            "MODEL_KEYWORDS": f"[{', '.join(keywords)}]",
            "OPENAI_MODELS": str(openai_models) if isinstance(openai_models, list) else openai_models,
            "GOOGLE_MODELS": "['google:gemini-pro']",  # Default
            "method_suffix": self.config["type"],
            "DEFAULT_OPENAI_MODEL": "gpt-4",
            "TIMEOUT_SECONDS": "60",
            "API_TIMEOUT": "30"
        })
    
    def get_ui_config(self):
        """Get UI configuration"""
        print("\n🎨 UI Configuration")
        print("-" * 20)
        
        # Color scheme
        print("Available color schemes:")
        for i, (name, _) in enumerate(self.color_schemes.items(), 1):
            print(f"{i}. {name.title()}")
        
        while True:
            try:
                choice = input("Choose a color scheme (1-5): ").strip()
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= len(self.color_schemes):
                        scheme_name = list(self.color_schemes.keys())[choice - 1]
                        color_config = self.color_schemes[scheme_name]
                        break
                elif choice.lower() in self.color_schemes:
                    color_config = self.color_schemes[choice.lower()]
                    break
                print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")
        
        # Port
        base_port = 7860
        suggested_port = base_port + len([f for f in os.listdir('.') if f.startswith('dragon') and f.endswith('.py')])
        port = input(f"Port number (suggested: {suggested_port}): ").strip()
        if not port.isdigit():
            port = str(suggested_port)
        
        # Gradio component
        component_map = {
            "image": ("Image", "pil", "height=300"),
            "audio": ("Audio", "filepath", "show_label=True"),
            "file": ("File", "file", ""),
            "text": ("Textbox", "text", "lines=5")
        }
        
        data_lower = self.config["data_type"]
        if data_lower in component_map:
            comp, comp_type, comp_params = component_map[data_lower]
        else:
            comp, comp_type, comp_params = "File", "file", ""
        
        self.config.update(color_config)
        self.config.update({
            "PORT": port,
            "GRADIO_COMPONENT": comp,
            "GRADIO_TYPE": comp_type,
            "COMPONENT_PARAMS": comp_params,
            "INPUT_LABEL": f"📁 Upload {self.config['DATA_TYPE']} File",
            "OUTPUT_LABEL": f"📜 {self.config['DATA_TYPE']} Analysis",
            "ANALYZE_BUTTON": f"🔍 Analyze {self.config['DATA_TYPE']}",
            "TAB_ICON": "🔍"
        })
    
    def get_data_flow_config(self):
        """Get data processing configuration"""
        print("\n⚡ Data Flow Configuration")
        print("-" * 20)
        
        # Input/output parameters
        input_param = input("Input parameter name (e.g., 'image_data', 'audio_file'): ").strip()
        if not input_param:
            input_param = f"{self.config['type']}_data"
        
        output_param = input("Output parameter name (e.g., 'description', 'transcription'): ").strip()
        if not output_param:
            output_param = "analysis_result"
        
        # Default prompt
        default_prompt = input("Default analysis prompt: ").strip()
        if not default_prompt:
            default_prompt = f"Analyze this {self.config['data_type']} in detail."
        
        # Metadata descriptors
        descriptors_input = input("Relevant descriptors for metadata (comma-separated): ").strip()
        if descriptors_input:
            descriptors = [f"'{d.strip()}'" for d in descriptors_input.split(',')]
        else:
            descriptors = ["'data'", "'content'", "'information'"]
        
        self.config.update({
            "input_param": input_param,
            "output_param": output_param,
            "DEFAULT_PROMPT": default_prompt,
            "METADATA_DESCRIPTORS": f"[{', '.join(descriptors)}]",
            "FILE_EXTENSION": self.suggest_file_extension(),
            "input_data": f"{input_param}_encoded",
            "output_var": "result",
            "input_key": self.config["type"],
            "output_key": output_param.replace('_', ''),
            "input_component": f"{self.config['type']}_input",
            "output_component": f"{output_param}_output",
            "OUTPUT_COLUMN": output_param.title(),
            "OUTPUT_TYPE": output_param.replace('_', ' ').title(),
            "result_key": "result"
        })
    
    def suggest_file_extension(self):
        """Suggest file extension based on data type"""
        extensions = {
            "image": "jpg", "audio": "wav", "video": "mp4",
            "document": "pdf", "text": "txt", "code": "py",
            "data": "csv"
        }
        
        data_lower = self.config["data_type"]
        for key, ext in extensions.items():
            if key in data_lower:
                return ext
        return "txt"
    
    def finalize_config(self):
        """Add remaining configuration values"""
        # API endpoints (placeholders)
        self.config.update({
            "OPENAI_ENDPOINT": "https://api.openai.com/v1/chat/completions",
            "GOOGLE_ENDPOINT": "https://api.google.com/v1/analyze",
            "API_TYPE": "CLOUD",
            "SERVICE_NAME": "API"
        })
    
    def replace_placeholders(self, content):
        """Replace all placeholders in content with config values"""
        for key, value in self.config.items():
            placeholder = f"{{{{{key}}}}}"
            content = content.replace(placeholder, str(value))
        return content
    
    def create_dragon_file(self):
        """Create the customized dragon file"""
        if not os.path.exists(self.template_file):
            print(f"❌ Template file {self.template_file} not found!")
            return False
        
        # Read template
        with open(self.template_file, 'r', encoding='utf-8') as f:
            template_content = f.read()
        
        # Replace placeholders
        customized_content = self.replace_placeholders(template_content)
        
        # Write new file
        output_file = f"dragon{self.config['type']}_gradio.py"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(customized_content)
        
        print(f"✅ Created {output_file}")
        return True
    
    def create_requirements(self):
        """Create requirements.txt file"""
        requirements = [
            "gradio>=5.42.0",
            "pandas",
            "requests", 
            "Pillow",  # For image processing
            "pathlib"
        ]
        
        # Add data-type specific requirements
        data_lower = self.config["data_type"]
        if "audio" in data_lower:
            requirements.extend(["librosa", "soundfile", "pydub"])
        elif "image" in data_lower:
            requirements.append("opencv-python")
        elif "document" in data_lower:
            requirements.extend(["PyPDF2", "python-docx"])
        
        with open("requirements.txt", 'w') as f:
            f.write('\n'.join(requirements))
        
        print("✅ Created requirements.txt")
    
    def create_gitignore(self):
        """Create .gitignore file"""
        gitignore_content = f"""# Virtual Environment
dragon{self.config['type']}_env/

# Log files
*.log
*.jsonl

# Data files (temporary processing)
temp_{self.config['type']}/

# Python cache
__pycache__/
*.py[cod]
*$py.class
*.so

# IDE files
.vscode/
.idea/
*.swp
*.swo

# OS files
.DS_Store
Thumbs.db

# Temporary files
*.tmp
*.temp"""
        
        with open(".gitignore", 'w') as f:
            f.write(gitignore_content)
        
        print("✅ Created .gitignore")
    
    def create_claude_md(self):
        """Create CLAUDE.md file"""
        claude_content = f"""# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Running the Application
```bash
# Activate virtual environment (if not already active)
source dragon{self.config['type']}_env/bin/activate

# Install dependencies (if needed)
pip install -r requirements.txt

# Run the main application
python dragon{self.config['type']}_gradio.py
```

The application will launch on `http://localhost:{self.config['PORT']}` with public sharing enabled by default.

## Architecture Overview

### Core Components

**Dragon{self.config['CLASS_SUFFIX']} Class (dragon{self.config['type']}_gradio.py:22-400)**
- Main application class handling all AI {self.config['data_type']} analysis
- Supports multiple {self.config['data_type']} providers: Ollama, OpenAI, Google, and others
- Implements intelligent fallback chain if primary model fails
- Manages API keys through environment variables

**Key Methods:**
- `get_available_models()` - Dynamically discovers available {self.config['data_type']} models
- `analyze_{self.config['type']}()` - Main analysis function that routes requests to appropriate API
- `try_*_{self.config['type']}()` methods - Individual API implementations for each provider
- `log_analysis()` - Comprehensive logging with {self.config['data_type'].lower()} metadata extraction

### Data Flow
1. {self.config['DATA_TYPE']} upload → Processing
2. Model selection → Route to appropriate API handler  
3. API response → Analysis with metadata extraction
4. Results display → Update logs table

### Color Scheme
**Dragon{self.config['TYPE']}**: {self.config['PRIMARY_COLOR']} theme (port {self.config['PORT']})
- Easily identifiable when running multiple Dragon apps

### Environment Variables
```bash
# Optional API keys (application detects what's available)
OPENAI_API_KEY=your_key
GOOGLE_CLOUD_API_KEY=your_key
```

## Development Notes

- Application requires Ollama running locally on port 11434 for local models
- Gradio interface auto-launches on port {self.config['PORT']}
- Dependencies are defined in requirements.txt
- All API provider integrations use direct REST API calls"""
        
        with open("CLAUDE.md", 'w', encoding='utf-8') as f:
            f.write(claude_content)
        
        print("✅ Created CLAUDE.md")
    
    def run_setup(self):
        """Run the complete setup process"""
        try:
            self.welcome()
            self.get_basic_config()
            self.get_api_config()
            self.get_ui_config()
            self.get_data_flow_config()
            self.finalize_config()
            
            print(f"\n🔧 Creating Dragon{self.config['TYPE']} files...")
            print("-" * 40)
            
            success = self.create_dragon_file()
            if success:
                self.create_requirements()
                self.create_gitignore()
                self.create_claude_md()
                
                print(f"\n🎉 Dragon{self.config['TYPE']} setup complete!")
                print(f"📁 Generated files:")
                print(f"   - dragon{self.config['type']}_gradio.py")
                print(f"   - requirements.txt")
                print(f"   - .gitignore")
                print(f"   - CLAUDE.md")
                print(f"\n🚀 Next steps:")
                print(f"   1. pip install -r requirements.txt")
                print(f"   2. python dragon{self.config['type']}_gradio.py")
                print(f"   3. Open http://localhost:{self.config['PORT']}")
            else:
                print("❌ Setup failed. Please check the template file exists.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Setup cancelled by user.")
        except Exception as e:
            print(f"\n❌ Setup failed with error: {e}")


if __name__ == "__main__":
    setup = DragonSetup()
    setup.run_setup()