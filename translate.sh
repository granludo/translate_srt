#!/bin/bash

# Check if the target language is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <target_language>"
    exit 1
fi

target_language="$1"

# Loop through all .srt files in the current directory
for file in *.srt; do
    # Check if the file exists and is a regular file
    if [ -f "$file" ]; then
        # Generate the output filename by adding "-cat.srt" before the extension
        output_file="${file%.srt}-cat.srt"
        
        echo "Translating $file to $output_file"
        
        # Call the Python script with the appropriate arguments
        python3 translate_srt.py "$file" "$output_file" --target_language "$target_language"
    fi
done

echo "Translation complete for all .srt files."
