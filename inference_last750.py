import requests
import json
import pandas as pd

# List to store the responses
response_list = []

# Define the headers for the request
headers = {
    "Content-Type": "application/json",
}

#This is just a placeholder. Replace it with your actual contents.
contents = []

# Open the json file and load its contents into a Python object
with open('GSPR9.5K/test.json', 'r') as f:
    data = json.load(f)

data = data[750:]

test_ground_truth = []
# Iterate over the instructions in the list
for instruction in data:
    # Get the instruction, input, and output
    contents.append("Instruction: " + instruction['instruction'])
    test_ground_truth.append(instruction['output'])

for content in contents:
    data = {
        "model": "test2",
        "messages": [{"role": "user", "content": content}]
    }

    # Make the POST request
    response = requests.post("http://localhost:10000/v1/chat/completions", headers=headers, data=json.dumps(data))

    # If the request was successful, append the response to the list
    if response.status_code == 200:
        response_list.append(response.json())
    else:
        print(f"Request for content {content} failed with status code {response.status_code}")

vicuna_8bit_outputs = []
for response in response_list:
    vicuna_8bit_outputs.append(response['choices'][0]['message']['content'])

df = pd.DataFrame({
    'output': test_ground_truth,
    'output_vicuna': vicuna_8bit_outputs
})

df.to_csv('output_8bit_last750.csv', index=False)