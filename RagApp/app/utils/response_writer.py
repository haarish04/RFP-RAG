import pandas as pd
import io

def write_response_to_excel(response_data: list) -> io.BytesIO:
    rows = []
    for item in response_data:
        question = item.get('question', '')
        llm_answer = item.get('LLM answer', '')
        matches = item.get('matches', [])
        row = {
            'Ouery': question,
            'LLM Response': llm_answer,
        }
        # Add each match as separate columns
        for i, match in enumerate(matches, start=1):
            match_question = match.get('metadata', {}).get('Question', '')
            match_answer = match.get('metadata', {}).get('Answer', '')
            row[f'Matched Question {i}'] = match_question
            row[f'Matched Answer {i}'] = match_answer
        rows.append(row)

    df = pd.DataFrame(rows)
    output = io.BytesIO()

    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Results')

    output.seek(0)
    return output