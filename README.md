# 🐉 Dragon AI Analysis Template

A template repository for creating AI-powered analysis tools with Gradio interfaces and multi-provider API support.

## 🚀 Quick Start

1. **Use this template** by clicking the "Use this template" button on GitHub
2. **Clone your new repository**
3. **Run the setup script** to customize for your use case:
   ```bash
   python setup_dragon.py
   ```
4. **Install dependencies and run**:
   ```bash
   pip install -r requirements.txt
   python dragon_[yourtype]_gradio.py
   ```

## 🎨 Built-in Variants

This template has been used to create:

- **🔍 Dragonsight** - Image analysis (purple/gold theme, port 7860)
- **🎵 Dragonsong** - Audio analysis (teal/cyan theme, port 7861)
- **📄 DragonScript** - Document analysis (green/lime theme, port 7862)
- **🧬 DragonLab** - Data analysis (blue/indigo theme, port 7863)

## 🏗️ Architecture

### Core Components

- **Dragon[Type] Class** - Main analysis engine with multi-provider support
- **Multi-API Integration** - Ollama, OpenAI, Google, Anthropic, and others
- **Intelligent Fallbacks** - Graceful degradation when APIs fail
- **Comprehensive Logging** - JSONL format with metadata extraction
- **Color-Coded UI** - Distinct themes for easy identification

### Key Features

- **🔄 Hot-swappable Models** - Switch between providers in real-time
- **📊 Rich Logging** - Track all analyses with searchable history
- **🎨 Themed Interface** - Color-coded for multi-app environments
- **🚀 Public Sharing** - Built-in Gradio sharing capabilities
- **🔧 Environment-based Config** - API keys via environment variables

## 🎨 Color Schemes

Each Dragon variant uses a unique color scheme:

| Variant | Primary | Secondary | Accent | Port |
|---------|---------|-----------|--------|------|
| Dragonsight (Image) | `#2d1b69` | `#4c1d95` | `#facc15` | 7860 |
| Dragonsong (Audio) | `#0f4c75` | `#2d6a4f` | `#40e0d0` | 7861 |
| DragonScript (Document) | `#064e3b` | `#065f46` | `#10b981` | 7862 |
| DragonLab (Data) | `#1e3a8a` | `#1e40af` | `#3b82f6` | 7863 |

## 📝 Creating Your Own Dragon

### Option 1: Interactive Setup

```bash
python setup_dragon.py
```

The setup script will ask you:
- Dragon name and type
- Data type being analyzed
- API providers to include
- Color scheme preferences
- Port number

### Option 2: Manual Configuration

1. Copy `dragon_template.py` to `dragon[yourtype]_gradio.py`
2. Replace all placeholder variables (see Placeholders section below)
3. Update `CLAUDE.md` with your specific documentation
4. Customize the color scheme in the CSS section

## 🔧 Template Placeholders

When customizing the template, replace these placeholders:

### Basic Configuration
- `{{TYPE}}` - Display name (e.g., "sight", "song", "script")
- `{{type}}` - Lowercase version for filenames
- `{{DATA_TYPE}}` - What you're analyzing (e.g., "Image", "Audio", "Document")
- `{{data_type}}` - Lowercase version
- `{{DESCRIPTION}}` - Brief description of your tool

### Class and Methods
- `{{CLASS_SUFFIX}}` - Class suffix (e.g., "Eye", "Ear", "Reader")
- `{{instance}}` - Instance variable name
- `{{method_suffix}}` - Method name suffix

### API Configuration
- `{{MODEL_KEYWORDS}}` - List of keywords to identify relevant models
- `{{DEFAULT_MODEL}}` - Fallback model name
- `{{OPENAI_MODELS}}` - List of OpenAI model options
- `{{GOOGLE_MODELS}}` - List of Google model options

### UI Configuration
- `{{EMOJI}}` - Emoji for your Dragon type
- `{{PRIMARY_COLOR}}`, `{{SECONDARY_COLOR}}`, `{{ACCENT_COLOR}}` - Color scheme
- `{{PORT}}` - Unique port number
- `{{ANALYZE_BUTTON}}` - Text for main action button

### Data Flow
- `{{input_param}}`, `{{output_param}}` - Parameter names
- `{{INPUT_LABEL}}`, `{{OUTPUT_LABEL}}` - UI labels
- `{{GRADIO_COMPONENT}}` - Gradio component type
- `{{DEFAULT_PROMPT}}` - Default analysis prompt

## 🌟 Examples of New Dragons

### DragonScript (Document Analysis)
```python
# Analyzes PDFs, Word docs, text files
# APIs: OpenAI GPT, Claude, Google Document AI
# Color: Green/lime theme
# Port: 7862
```

### DragonLab (Data Analysis)
```python
# Analyzes CSV, JSON, database files
# APIs: OpenAI Code Interpreter, Claude, custom analytics
# Color: Blue/indigo theme  
# Port: 7863
```

### DragonCode (Code Analysis)
```python
# Analyzes source code files
# APIs: OpenAI Codex, Claude, GitHub Copilot API
# Color: Orange/amber theme
# Port: 7864
```

### DragonVision (Video Analysis)
```python
# Analyzes video files
# APIs: OpenAI Vision, Google Video Intelligence
# Color: Red/rose theme
# Port: 7865
```

## 📚 Documentation

Each Dragon variant should include:
- `CLAUDE.md` - Development guidance for Claude Code
- `README.md` - User documentation
- `requirements.txt` - Python dependencies
- `.gitignore` - Exclude environments and logs

## 🤝 Contributing

1. Fork this template repository
2. Create your Dragon variant
3. Test thoroughly
4. Submit a PR with your variant as an example
5. Update this README with your Dragon's details

## 📄 License

Copyright © 2025 Seed13 Productions. All rights reserved.

## 🐉 Dragon Family

Join the growing family of Dragon AI tools! Each one specializes in a different type of analysis while sharing the same robust, proven architecture.