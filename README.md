# Cloud_Microservices_automation
This script is useful for situations where you have multiple CloudFormation templates that you want to merge into a single file while ensuring that there is no duplicate or conflicting code. The use of a LLM helps in intelligently combining the templates by understanding the context and structure of the YAML files.

This script automates the process of combining multiple YAML template files (specifically CloudFormation templates) into a single template, using a Large Language Model (LLM) from Google Generative AI.

Here's a breakdown of what the script does:

1. Configuration:
The script starts by configuring the Google Generative AI API with an API key using the genai.configure(api_key=...) function. This allows the script to interact with Google's Generative AI model.
2. Reading YAML Templates:
The read_template(file_path) function reads the content of a given YAML template file. It handles cases where the file does not exist, where there are permission issues, or other exceptions when attempting to read the file.
3. Combining Templates:
The combine_templates(templates) function creates a prompt that includes the content of all the provided YAML templates and asks the LLM to combine them into a single template. It sends this prompt to the LLM (in this case, Google's "gemini-pro" model) and receives the combined template as a response.
4. Main Process:
The main(input_directory) function:
Searches the specified directory for all files with a .yml extension.
Reads the content of each file and stores it in a list.
If templates are found, it uses the combine_templates function to combine them into one.
The combined template is then written to a new file named combined_template.yml in the same directory.
5. Execution:
When the script is executed, it prompts the user to input the directory path containing the YAML files.
The script then processes all YAML files in that directory and generates a combined template.
