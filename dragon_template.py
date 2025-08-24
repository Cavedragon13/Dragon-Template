#!/usr/bin/env python3
"""
Dragon{{TYPE}} Gradio - AI {{DATA_TYPE}} Analysis Tool
Copyright © 2025 Seed13 Productions. All rights reserved.

{{DESCRIPTION}}
"""

import os
import json
import base64
import requests
import gradio as gr
import pandas as pd
from pathlib import Path
from datetime import datetime
import hashlib
import re
import io


class Dragon{{CLASS_SUFFIX}}:
    def __init__(self):
        self.ollama_url = "http://localhost:11434"
        # Add your API keys here
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
        self.google_api_key = os.getenv('GOOGLE_{{API_TYPE}}_API_KEY')
        # Add more API keys as needed
        self.log_file = Path("dragon{{type}}_logs.jsonl")
        
    def get_available_models(self):
        """Get list of available {{data_type}} processing models from all sources"""
        models = []
        
        # Get Ollama models
        try:
            response = requests.get(f"{self.ollama_url}/api/tags", timeout=5)
            if response.status_code == 200:
                ollama_models = response.json().get('models', [])
                model_names = [f"ollama:{m['name']}" for m in ollama_models]
                # Prioritize relevant models
                relevant_models = [m for m in model_names if any(k in m.lower() for k in {{MODEL_KEYWORDS}})]
                models.extend(relevant_models + [m for m in model_names if m not in relevant_models])
        except:
            models.append('ollama:{{DEFAULT_MODEL}}')
        
        # Add cloud APIs if keys are available
        if self.openai_api_key:
            models.extend({{OPENAI_MODELS}})
        
        if self.google_api_key:
            models.extend({{GOOGLE_MODELS}})
        
        # Add more providers as needed
        
        return models if models else ['ollama:{{DEFAULT_MODEL}}']
    
    def try_ollama_{{method_suffix}}(self, {{input_param}}, model, prompt):
        """Try Ollama for {{data_type}} processing"""
        try:
            ollama_model = model.replace('ollama:', '') if model.startswith('ollama:') else model
            
            payload = {
                "model": ollama_model,
                "prompt": prompt,
                "{{input_key}}": {{input_param}},  # Base64 encoded data
                "stream": False
            }
            
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json=payload,
                timeout={{TIMEOUT_SECONDS}}
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get('response', 'No {{output_type}} returned'), f'Ollama ({ollama_model})', None
            else:
                return None, None, f"Ollama failed: {response.status_code}"
                
        except Exception as e:
            return None, None, f"Ollama error: {str(e)}"
    
    def try_openai_{{method_suffix}}(self, {{input_param}}, model, prompt):
        """Try OpenAI API for {{data_type}} processing"""
        if not self.openai_api_key:
            return None, None, "OpenAI API key not found"
        
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.openai_api_key}"
            }
            
            openai_model = model.replace('openai:', '') if model.startswith('openai:') else '{{DEFAULT_OPENAI_MODEL}}'
            
            # Implement OpenAI-specific logic here
            payload = {
                "model": openai_model,
                # Add model-specific parameters
            }
            
            response = requests.post(
                "{{OPENAI_ENDPOINT}}",
                headers=headers,
                json=payload,
                timeout={{API_TIMEOUT}}
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get('{{result_key}}', 'No {{output_type}} returned'), f'OpenAI ({openai_model})', None
            else:
                return None, None, f"OpenAI failed: {response.status_code}"
                
        except Exception as e:
            return None, None, f"OpenAI error: {str(e)}"
    
    def try_google_{{method_suffix}}(self, {{input_param}}, model):
        """Try Google API for {{data_type}} processing"""
        if not self.google_api_key:
            return None, None, "Google API key not found"
            
        try:
            url = f"{{GOOGLE_ENDPOINT}}?key={self.google_api_key}"
            
            payload = {
                # Add Google-specific payload structure
            }
            
            response = requests.post(url, json=payload, timeout={{API_TIMEOUT}})
            
            if response.status_code == 200:
                result = response.json()
                # Process Google-specific response
                return "{{output_type}} result", 'Google {{SERVICE_NAME}}', None
            else:
                return None, None, f"Google {{SERVICE_NAME}} failed: {response.status_code}"
                
        except Exception as e:
            return None, None, f"Google {{SERVICE_NAME}} error: {str(e)}"
    
    def extract_{{type}}_metadata(self, {{output_param}}, file_path=None):
        """Extract metadata for {{data_type}} logging"""
        # Define relevant descriptors for your data type
        descriptors = {{METADATA_DESCRIPTORS}}
        
        content_lower = {{output_param}}.lower()
        tags = [desc for desc in descriptors if desc in content_lower]
        
        # Extract quoted content
        quoted_content = re.findall(r'"([^"]*)"', {{output_param}})
        
        # Generate filename suggestion
        clean_content = re.sub(r'[^\w\s-]', '', {{output_param}}.lower())
        words = clean_content.split()[:4]
        suggested_filename = '_'.join(words) + '.{{FILE_EXTENSION}}'
        
        return {
            'tags': list(set(tags)),
            'quoted_content': quoted_content,
            'suggested_filename': suggested_filename,
            'word_count': len({{output_param}}.split()),
            'char_count': len({{output_param}})
        }
    
    def log_analysis(self, file_path, {{output_param}}, model, api_used, prompt):
        """Log the {{data_type}} analysis"""
        try:
            # Calculate file hash if we have the path
            file_hash = None
            if file_path and Path(file_path).exists():
                with open(file_path, 'rb') as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
            
            metadata = self.extract_{{type}}_metadata({{output_param}}, file_path)
            
            log_entry = {
                'timestamp': datetime.now().isoformat(),
                'file_path': str(file_path) if file_path else 'uploaded_{{type}}',
                'file_name': Path(file_path).name if file_path else 'uploaded_{{type}}.{{FILE_EXTENSION}}',
                'file_hash': file_hash,
                'model_used': model,
                'api_used': api_used,
                'prompt': prompt,
                '{{output_key}}': {{output_param}},
                'metadata': metadata
            }
            
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(log_entry, ensure_ascii=False) + '\n')
                
            return True
        except Exception as e:
            print(f"Logging error: {e}")
            return False
    
    def get_recent_logs(self, limit=20):
        """Get recent logs for display"""
        try:
            if not self.log_file.exists():
                return pd.DataFrame()
                
            logs = []
            with open(self.log_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        logs.append(json.loads(line))
            
            recent_logs = logs[-limit:]
            
            df_data = []
            for log in reversed(recent_logs):  # Newest first
                df_data.append({
                    'Timestamp': log['timestamp'][:19].replace('T', ' '),
                    'File': log['file_name'],
                    'Model': log['model_used'],
                    'API': log['api_used'],
                    'Tags': ', '.join(log['metadata']['tags'][:5]),
                    '{{OUTPUT_COLUMN}}': log['{{output_key}}'][:100] + '...' if len(log['{{output_key}}']) > 100 else log['{{output_key}}']
                })
            
            return pd.DataFrame(df_data)
            
        except Exception as e:
            print(f"Error reading logs: {e}")
            return pd.DataFrame()
    
    def analyze_{{type}}(self, {{input_param}}, model, prompt):
        """Main analysis function for Gradio"""
        if {{input_param}} is None:
            return "❌ Please upload a {{data_type}} file", "", pd.DataFrame()
        
        try:
            # Handle different input types
            file_path = None
            if isinstance({{input_param}}, str):
                # File path from Gradio
                file_path = {{input_param}}
                with open({{input_param}}, 'rb') as f:
                    {{input_data}} = base64.b64encode(f.read()).decode('utf-8')
            elif hasattr({{input_param}}, 'name'):
                # File object
                file_path = {{input_param}}.name
                with open({{input_param}}.name, 'rb') as f:
                    {{input_data}} = base64.b64encode(f.read()).decode('utf-8')
            else:
                # Raw data
                {{input_data}} = base64.b64encode({{input_param}}).decode('utf-8')
            
            if not prompt.strip():
                prompt = "{{DEFAULT_PROMPT}}"
            
            # Route to appropriate API based on model selection
            {{output_var}}, api_used, error = None, None, None
            
            if model.startswith('ollama:'):
                {{output_var}}, api_used, error = self.try_ollama_{{method_suffix}}({{input_data}}, model, prompt)
            elif model.startswith('openai:'):
                {{output_var}}, api_used, error = self.try_openai_{{method_suffix}}({{input_data}}, model, prompt)
            elif model.startswith('google:'):
                {{output_var}}, api_used, error = self.try_google_{{method_suffix}}({{input_data}}, model)
            else:
                # Default to Ollama
                {{output_var}}, api_used, error = self.try_ollama_{{method_suffix}}({{input_data}}, model, prompt)
            
            # Fallback chain if primary method fails
            if not {{output_var}}:
                fallback_methods = [
                    ('ollama:{{DEFAULT_MODEL}}', self.try_ollama_{{method_suffix}}),
                ]
                
                for fallback_model, fallback_method in fallback_methods:
                    if fallback_model != model:
                        {{output_var}}, api_used, error = fallback_method({{input_data}}, fallback_model, prompt)
                        if {{output_var}}:
                            break
            
            if {{output_var}}:
                # Log the result
                self.log_analysis(file_path, {{output_var}}, model, api_used, prompt)
                
                # Get updated logs
                logs_df = self.get_recent_logs(5)
                
                return {{output_var}}, f"✨ Analysis complete using {api_used}", logs_df
            else:
                return f"❌ Analysis failed: {error}", "❌ All {{data_type}} APIs failed", pd.DataFrame()
                
        except Exception as e:
            return f"❌ Error: {str(e)}", "❌ Analysis failed", pd.DataFrame()


# Initialize the dragon
dragon_{{instance}} = Dragon{{CLASS_SUFFIX}}()

# Custom CSS for {{type}}-themed dragon interface
css = """
.gradio-container {
    background: linear-gradient(135deg, {{PRIMARY_COLOR}}, {{SECONDARY_COLOR}}) !important;
}

h1 {
    color: {{ACCENT_COLOR}} !important;
    text-align: center !important;
}

.footer {
    text-align: center !important;
    color: {{FOOTER_COLOR}} !important;
    font-size: 12px !important;
}

/* Button styling with {{type}} theme */
button[data-testid="component-button"] {
    font-weight: bold !important;
    border: none !important;
    transition: all 0.2s ease !important;
}

/* {{TYPE}}-specific button colors */
button:has-text("{{ANALYZE_BUTTON}}"), button[aria-label*="Analyze"] {
    background: linear-gradient(45deg, {{BUTTON_1_COLOR}}, {{BUTTON_1_COLOR_DARK}}) !important;
    color: white !important;
    font-size: 16px !important;
}

button:has-text("🔄 Refresh Models"), button[aria-label*="Refresh"] {
    background: linear-gradient(45deg, {{BUTTON_2_COLOR}}, {{BUTTON_2_COLOR_DARK}}) !important;
    color: white !important;
}
"""

# Create Gradio interface for Dragon{{TYPE}}
with gr.Blocks(css=css, title="{{EMOJI}} Dragon{{TYPE}}") as demo:
    gr.Markdown("# {{EMOJI}} Dragon{{TYPE}}")
    
    with gr.Tabs():
        with gr.TabItem("{{TAB_ICON}} Analyze"):
            with gr.Row():
                with gr.Column(scale=1):
                    # {{DATA_TYPE}} input
                    {{input_component}} = gr.{{GRADIO_COMPONENT}}(
                        label="{{INPUT_LABEL}}", 
                        type="{{GRADIO_TYPE}}",
                        {{COMPONENT_PARAMS}}
                    )
                    
                    # Model selection
                    model_dropdown = gr.Dropdown(
                        choices=dragon_{{instance}}.get_available_models(),
                        value=dragon_{{instance}}.get_available_models()[0] if dragon_{{instance}}.get_available_models() else "{{DEFAULT_MODEL}}",
                        label="🤖 Model",
                        interactive=True
                    )
                    
                    # Refresh models button
                    refresh_btn = gr.Button("🔄 Refresh Models", size="sm")
                    
                    # Custom prompt
                    prompt_input = gr.Textbox(
                        label="📝 Custom Prompt",
                        placeholder="{{DEFAULT_PROMPT}}",
                        value="{{DEFAULT_PROMPT}}",
                        lines=2
                    )
                    
                    # Analyze button
                    analyze_btn = gr.Button("{{ANALYZE_BUTTON}}", variant="primary", size="lg")
                
                with gr.Column(scale=1):
                    # Results
                    status_output = gr.Textbox(label="🔮 Status", interactive=False)
                    {{output_component}} = gr.Textbox(
                        label="{{OUTPUT_LABEL}}", 
                        lines=10,
                        max_lines=15,
                        interactive=False
                    )
            
            # Quick logs preview
            gr.Markdown("## 📝 Recent Analysis (Quick View)")
            logs_output = gr.Dataframe(
                headers=["Timestamp", "File", "Model", "API", "Tags"],
                label="Last 5 Analyses",
                interactive=False
            )
        
        with gr.TabItem("📊 Detailed Logs"):
            gr.Markdown("### 🗂️ Complete {{DATA_TYPE}} Analysis History")
            
            # Detailed logs table
            detailed_logs = gr.Dataframe(
                headers=["Time", "File", "Model", "Tags", "Word Count"],
                label="Click a row to see full details",
                interactive=True
            )
            
            # Full output display
            full_output = gr.Textbox(
                label="Complete {{OUTPUT_TYPE}}",
                lines=8,
                interactive=False
            )
    
    # Footer
    gr.Markdown("---")
    gr.Markdown("<center><i>Powered by Ollama with cloud {{data_type}} API fallbacks</i></center>")
    gr.Markdown("*Copyright © 2025 Seed13 Productions. All rights reserved.*", elem_classes="footer")
    
    # Event handlers
    def refresh_models():
        new_models = dragon_{{instance}}.get_available_models()
        current_value = new_models[0] if new_models else "ollama:{{DEFAULT_MODEL}}"
        return gr.Dropdown(choices=new_models, value=current_value)
    
    # Wire up events
    refresh_btn.click(refresh_models, outputs=model_dropdown)
    
    analyze_btn.click(
        dragon_{{instance}}.analyze_{{type}},
        inputs=[{{input_component}}, model_dropdown, prompt_input],
        outputs=[{{output_component}}, status_output, logs_output]
    )
    
    # Load initial logs
    demo.load(lambda: dragon_{{instance}}.get_recent_logs(5), outputs=logs_output)

if __name__ == "__main__":
    print("{{EMOJI}} Dragon{{TYPE}} Gradio - Copyright © 2025 Seed13 Productions")
    print("=" * 60)
    print("Starting Dragon{{TYPE}} with public sharing enabled...")
    print("🌐 This will create a temporary public URL you can share!")
    print("🔒 Your {{data_type}} files are processed locally, only the interface is shared")
    print("=" * 60)
    
    # Launch the interface with sharing enabled
    demo.launch(
        server_name="0.0.0.0",
        server_port={{PORT}},  # Unique port for each Dragon variant
        share=True,
        show_error=True,
        favicon_path=None
    )