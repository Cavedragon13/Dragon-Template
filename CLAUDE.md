# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with the Dragon Template repository.

## Template Overview

This is a **template repository** for creating AI-powered analysis tools using the Dragon architecture. The template provides a complete foundation for building Gradio-based applications with multi-provider API support.

## Using This Template

### Quick Setup
```bash
# After creating a new repository from this template:
git clone your-new-dragon-repo
cd your-new-dragon-repo

# Run the interactive setup
python setup_dragon.py

# Install dependencies
pip install -r requirements.txt

# Launch your custom Dragon
python dragon[yourtype]_gradio.py
```

### Template Structure

**Core Files:**
- `dragon_template.py` - Main template with placeholder variables
- `setup_dragon.py` - Interactive configuration script
- `requirements.txt` - Base Python dependencies
- `README.md` - Template documentation

**Generated Files (after setup):**
- `dragon[type]_gradio.py` - Your customized Dragon application
- `CLAUDE.md` - Variant-specific documentation
- `.gitignore` - Tailored exclusions

## Architecture Patterns

### Dragon Class Structure
Every Dragon follows this pattern:
1. **Initialization** - API keys, configuration
2. **Model Discovery** - Dynamic provider detection  
3. **Multi-API Methods** - `try_[provider]_[type]()` functions
4. **Intelligent Fallbacks** - Graceful degradation
5. **Comprehensive Logging** - JSONL with metadata
6. **Gradio Interface** - Themed, responsive UI

### Color Coding System
Each Dragon variant uses a unique color scheme for easy identification:
- **Dragonsight** (Image): Purple/Gold - Port 7860
- **Dragonsong** (Audio): Teal/Cyan - Port 7861  
- **DragonScript** (Document): Green/Lime - Port 7862
- **DragonLab** (Data): Blue/Indigo - Port 7863
- **DragonCode** (Code): Orange/Amber - Port 7864

### Template Variables

When customizing, replace these key placeholders:

**Basic Configuration:**
- `{{TYPE}}` / `{{type}}` - Dragon variant name
- `{{DATA_TYPE}}` / `{{data_type}}` - Data being analyzed
- `{{DESCRIPTION}}` - Tool description
- `{{EMOJI}}` - Dragon emoji identifier

**Technical Configuration:**
- `{{CLASS_SUFFIX}}` - Class name suffix (Eye, Ear, Reader, etc.)
- `{{PORT}}` - Unique port number
- `{{MODEL_KEYWORDS}}` - Model discovery keywords
- `{{DEFAULT_MODEL}}` - Fallback model name

**UI Configuration:**
- `{{PRIMARY_COLOR}}`, `{{SECONDARY_COLOR}}`, `{{ACCENT_COLOR}}` - Color scheme
- `{{GRADIO_COMPONENT}}` - Input component type
- `{{INPUT_LABEL}}`, `{{OUTPUT_LABEL}}` - UI labels

## Development Guidelines

### Creating New Dragons

1. **Use setup_dragon.py** for guided configuration
2. **Choose unique colors** to distinguish from existing Dragons
3. **Use sequential port numbers** (7860, 7861, 7862, ...)
4. **Follow naming conventions** (DragonType, dragon_type, etc.)
5. **Include comprehensive logging** with domain-specific metadata

### API Integration Pattern

Each Dragon should support:
- **Local processing** (Ollama) as primary option
- **Cloud APIs** as fallbacks with environment-based configuration
- **Intelligent fallback chains** when providers fail
- **Consistent error handling** and user feedback

### Testing New Variants

Before publishing:
1. Test with multiple API providers
2. Verify fallback chains work correctly
3. Test logging and export functionality
4. Ensure UI theming is distinct and functional
5. Update documentation with your variant

## Template Maintenance

When updating the template:
1. **Preserve placeholder structure** - Don't break `{{VARIABLE}}` format
2. **Update all variants** - Test changes across existing Dragons
3. **Version control** - Tag template releases
4. **Document changes** - Update this CLAUDE.md with new features

## Known Dragon Variants

Update this list when creating new Dragons:

- **🔍 Dragonsight** - Image analysis (Dragonsight_Gradio repo)
- **🎵 Dragonsong** - Audio analysis (in development)
- **📄 DragonScript** - Document analysis (planned)
- **🧬 DragonLab** - Data analysis (planned)
- **💻 DragonCode** - Code analysis (planned)

## Development Commands

```bash
# Test the template setup process
python setup_dragon.py

# Create a specific Dragon type manually
cp dragon_template.py dragontest_gradio.py
# Then manually replace placeholders

# Validate template structure
python -m py_compile dragon_template.py
python -m py_compile setup_dragon.py
```

This template enables rapid creation of specialized AI analysis tools while maintaining architectural consistency and code quality across the Dragon family.