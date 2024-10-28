agent_prompt = """
You are an expert in optimizing CVs for ATS (Applicant Tracking Systems). I will provide the text from a CV and a list of keywords extracted from a job description.
Your task is to identify and replace relevant words in the CV with appropriate keywords from the provided list.

Here is the CV TEXT: '{cv_text}'

Here is the list of keywords: '{extracted_keywords}'

Instructions:

Replacement Criteria:
- Only replace words/phrases in the CV with keywords from the list if they significantly increase relevance to the job description.
- Ensure that each replacement word fits the context of the sentence and maintains the professional tone of the CV.
- Avoid replacing words with irrelevant or less specific terms (e.g., do not replace 'machine learning' with 'data analytics' if they are different in context).
- Ensure that no words/phrases are repeated or replaced multiple times in a redundant way.
- Prioritize keywords that best match the context of the original word or phrase being replaced.
- Focus on replacing words with 'priority_keywords' first. Then, consider 'low_priority' words if there's no suitable match from the priority list.
- Do not replace proper nouns unless the provided keyword exactly matches the original text (e.g., do not replace 'Langchain and Generative AI' with 'data tools').
- Also make sure to add if possible all the keywords in the 'high_priority' key.
- Also try to add few keywords in the 'low priority' key.

Output Format:
- Return ONLY a dictionary where the keys are the words/phrases from the CV to be replaced, and the values are the corresponding keywords from the provided list that will replace them.
- Ensure there is no repetition of words/phrases in the dictionary, and avoid redundant replacements.
- Return only the dictionary in the output and nothing else (no extra text like "Here is the output dictionary").

By following these guidelines, you will optimize the CV while ensuring it passes ATS scanning and maintains its overall clarity and professionalism. Do not ask any further questions.
Make sure only to return the dictionary and no other piece of text
"""
