# SRT File Translator

By Marc Alier, @granludo  

This project provides a script to translate SRT subtitle files from English to a specified target language using OpenAI's GPT-4 model.

## Features

- Translates SRT files while maintaining original formatting and timing
- Supports batch translation for improved efficiency
- Command-line interface for easy use

## Requirements

- Python 3.6+
- OpenAI API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/srt-translator.git
   cd srt-translator
   ```

2. Install the required packages:
   ```
   pip install openai tqdm
   ```

3. Set up your OpenAI API key:
   Create a file named `mykey.json` in the parent directory of the script with the following content:
   ```json
   {
     "key": "your-openai-api-key-here"
   }
   ```

## Usage

To translate a single SRT file:

 python3 translate_srt.py <input_file> <output_file> --target_language <target_language>

To translate all SRT files in the current directory:

./translate.sh <target_language>


