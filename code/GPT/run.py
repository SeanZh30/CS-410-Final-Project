import openai
import pandas as pd


openai.api_key = "YOUR_API_KEY"

def load_prompt_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        prompt_template = file.read()
    return prompt_template

def detect_spam_and_calculate_accuracy(csv_file, text_column, label_column, output_file, prompt_file):
    
    prompt_template = load_prompt_from_file(prompt_file)

    data = pd.read_csv(csv_file)
    data['Predicted_Label'] = ""

    correct_predictions = 0  
    total_samples = 0       

    for index, row in data.iterrows():
        if index == 100:
            break
        text = row[text_column]
        true_label = row[label_column]
        prompt = prompt_template.replace("{text}", text)

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert spam email detector."},
                    {"role": "user", "content": prompt}
                ]
            )
            predicted_label = response['choices'][0]['message']['content'].strip().strip('"').strip("'")
            print(f"Predicted label for row {index}: {predicted_label}")
            if predicted_label not in ["0", "1"]:
                print(f"Unexpected response for row {index}: {predicted_label}")
                predicted_label = "-1"  

            data.at[index, 'Predicted_Label'] = int(predicted_label)

            if int(predicted_label) == int(true_label):
                correct_predictions += 1

            total_samples += 1

        except Exception as e:
            print(f"Error processing row {index}: {e}")
            data.at[index, 'Predicted_Label'] = -1 

    accuracy = correct_predictions / 100 if total_samples > 0 else 0
    print(f"Accuracy: {accuracy:.2%}")

    data.to_csv(output_file, index=False)
    print(f"Spam detection results saved to {output_file}")
    return accuracy

csv_file = "./spam_ham_dataset.csv"
text_column = "text"
label_column = "label_num"  
output_file = "./out_spam_ham_dataset.csv" 
prompt_file = "./fewshot.prompt"  

accuracy = detect_spam_and_calculate_accuracy(csv_file, text_column, label_column, output_file, prompt_file)
print(f"Final Accuracy: {accuracy:.2%}")
