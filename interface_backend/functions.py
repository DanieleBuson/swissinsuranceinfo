import pandas as pd
import re
import openai
import environ

env = environ.Env()
environ.Env.read_env()

openai.api_key = env('OPENAI_SECRET_KEY')



def summarize_text(question, text):

    string = f"""Based on the following information, please provide a concise answer in the form of an FAQ response, limited to 180 tokens. Do not include additional or circumstantial text. 

            Question: {question}

            Context: {text}

            Please provide a direct answer, completing the response within 180 tokens."""

    # This function takes a string and returns a summary using OpenAI's GPT model.
    try:
        response = openai.Completion.create(
          engine="text-davinci-003",  # You may choose a different model as needed
          prompt=string,
          max_tokens=180  # Adjust as needed
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print("Error during OpenAI API call:", e)
        return ""

def read_and_concat_csv(file_path):

    text = ""
    csv_file = pd.read_csv(file_path)
    for i in csv_file.index: 
        text += csv_file.loc[i, 'content']

    return {
        'df': csv_file,
        'cleaned_text': text
    }

def cleaning_text(question): 

    return re.sub(r'[^a-zA-Z,;.:!? ]', '', question.lower())

def give_an_answer(question, file_path):

    cleaned_question = cleaning_text(question)
    dict_csv = read_and_concat_csv(file_path)
    answer = summarize_text(cleaned_question, dict_csv['cleaned_text'])
    cleaned_answer = cleaning_text(answer)
    return {
        'question': cleaned_question,
        'answer': cleaned_answer
    }

def create_update_csv(file_path, question, answer):
    
    # Read the CSV file into a DataFrame
    csv_file = pd.read_csv(file_path)

    # Create a new row with the question and answer
    new_row = pd.DataFrame({'Question': [question], 'Answer': [answer]})

    # Concatenate the new row to the DataFrame
    csv_file = pd.concat([csv_file, new_row], ignore_index=True)

    # Update the CSV file with the modified DataFrame
    csv_file.to_csv(file_path, index=False)

def similarity_score(qaa_df_path, question):
    
    qaa_df = pd.read_csv(qaa_df_path)
    cleaned_question = cleaning_text(question)
    cleaned_question_list = cleaned_question.split(" ")

    temp_df = pd.DataFrame()
    
    for i in qaa_df.index:
        df_question = cleaning_text(qaa_df.loc[i, 'Question'])
        df_question_list = df_question.split(" ")
        score = 0
        for word in cleaned_question_list:
    
            if word in df_question_list:
                score += df_question_list.count(word)/len(df_question_list)
    
        temp_df.loc[i, 'Question'] = qaa_df['Question'].loc[i]
        temp_df.loc[i, 'Answer'] = qaa_df['Answer'].loc[i]
        temp_df.loc[i, 'Score'] = score
    
    sorted_df = temp_df.sort_values(by='Score', ascending=False).reset_index(drop=True)
    
    return {
        'question1': sorted_df.loc[0, 'Question'],
        'answer1': sorted_df.loc[0, 'Answer'],
        'question2': sorted_df.loc[1, 'Question'],
        'answer2': sorted_df.loc[1, 'Answer'],
        'question3': sorted_df.loc[2, 'Question'],
        'answer3': sorted_df.loc[2, 'Answer'],
        'question4': sorted_df.loc[3, 'Question'],
        'answer4': sorted_df.loc[3, 'Answer'],
    }

            
            