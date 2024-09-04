import google.generativeai as genai
import os
import glob

# Configure the Google Generative AI API key
genai.configure(api_key='Your_API_key') #use your google  gemini API key.

def read_template(file_path):
    """Read the content of a YAML template file."""
    if not os.path.isfile(file_path):
        print(f"Error: The path '{file_path}' is not a valid file or does not exist.")
        return None
    
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except PermissionError:
        print(f"Error: Permission denied for file '{file_path}'.")
        return None
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return None

def combine_templates(templates):
    """Combine multiple templates using the LLM."""
    prompt = "Given the following CloudFormation templates, combine them into a single template, ensuring no duplicate or common code:\n\n"
    
    for i, template in enumerate(templates):
        prompt += f"Template {i+1}:\n{template}\n\n"
    
    prompt += "Combined Template:"
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    combined_template = response.text.strip()
    return combined_template

def main(input_directory):
    templates = []
    # Get all YAML files in the input directory
    yaml_files = glob.glob(os.path.join(input_directory, "*.yml"))
    
    for file_path in yaml_files:
        template_content = read_template(file_path)
        if template_content:
            templates.append(template_content)
    
    if templates:
        combined_template = combine_templates(templates)
        
        output_file = os.path.join(input_directory, "combined_template.yml")
        
        try:
            with open(output_file, 'w') as file:
                file.write(combined_template)
            print(f"Combined template generated and written to '{output_file}'")
        except Exception as e:
            print(f"Error writing to file '{output_file}': {e}")
    else:
        print("No templates were found in the specified directory.")

if __name__ == "__main__":
    input_directory = input("Enter the directory path containing YAML template files: ")
    main(input_directory)
