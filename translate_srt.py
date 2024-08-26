import re
import os
import json
import argparse
import openai
from openai import OpenAI
from tqdm import tqdm

# Function to translate text using OpenAI's GPT-4 model
def translate_text(text, source_language, target_language):
    try:
        client = OpenAI(api_key=openai.api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"You are a professional translator. Translate the following subtitles from {source_language} to {target_language}. Maintain the original formatting, line breaks, and numbering. Each subtitle block is separated by a blank line."},
                {"role": "user", "content": text}
            ]
        )
        translated_text = response.choices[0].message.content.strip()
        return translated_text
    except Exception as e:
        print(f"Error in translation: {e}")
        return text  # Return original text if translation fails

# Function to translate an entire SRT file
def translate_srt(input_file, output_file, source_language, target_language, batch_size=50):
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split the content into subtitle blocks
    subtitle_blocks = re.split(r'\n\n', content.strip())

    translated_blocks = []
    for i in tqdm(range(0, len(subtitle_blocks), batch_size), desc="Translating subtitles"):
        batch = subtitle_blocks[i:i+batch_size]
        batch_text = '\n\n'.join(batch)
        translated_batch = translate_text(batch_text, target_language, source_language)
        translated_blocks.extend(translated_batch.split('\n\n'))

    # Write the translated blocks to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(translated_blocks))

# Set up OpenAI API key
def setup_api_key():
    # Get the absolute path of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to mykey.json
    key_file_path = os.path.join(current_dir, '..', 'mykey.json')

    # Read the API key from the JSON file
    with open(key_file_path, 'r') as f:
        key_data = json.load(f)
        openai.api_key = key_data['key']

# Main function to handle command-line arguments and run the translation
def main():
    parser = argparse.ArgumentParser(description='Translate SRT subtitles')
    parser.add_argument('input_file', help='Path to the input SRT file')
    parser.add_argument('output_file', help='Path to the output SRT file')
    parser.add_argument('--target_language', default='catalan', help='Target language for translation (default: catalan)')
    parser.add_argument('--source_language', default='english', help='Source language of the subtitles (default: english)')

    args = parser.parse_args()

    setup_api_key()
    translate_srt(args.input_file, args.output_file, args.source_language, args.target_language)
    print(f"Translation complete. Output saved to {args.output_file}")

if __name__ == "__main__":
    main()