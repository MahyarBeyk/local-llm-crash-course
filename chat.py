# In terminal: pip insall ctransformers

from typing import List  # For being able to use in history
from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained(
    "zoltanctoth/orca_mini_3B-GGUF", model_file="orca-mini-3b.q4_0.gguf"
)

# prompt = "The name of the capital of canada is"
# print(prompt + llm(prompt))

# prompt = "The name of the capital of canada is"
# for word in llm(prompt, stream=True): # stream = جریان، گذار کلمه به کلمه
#    print(word)

# prompt = "The name of the capital of canada is"
# for word in llm(prompt, stream=True): # stream = جریان، گذار کلمه به کلمه
#    print(word, end="", flush=True) # end="": با یک رشته خالی تمام شود نه با خط بعدی  flush=True: هر کلمه که تولید شد ظاهر شود
# print() # در آخر، یک خط ایجاد کن


# def get_prompt(instruction: str) -> str:
#    system = "You are an AI assistant that gives helpful answers. You answer the questions in a short and concise way."
#    prompt = f"### System:\n{system}\n\n### User:\n{instruction}\n\n### Response:\n"  # Prompt format of the model on Huggingface. Because this model is trained in this way
#    print(prompt)  # For debugging
#    return prompt
# question = "Which city is the capital of Canada?"
# for word in llm(get_prompt(question), stream=True):  # stream = جریان، گذار کلمه به کلمه
#    print(word, end="", flush=True)  # end="": با یک رشته خالی تمام شود نه با خط بعدی  flush=True: هر کلمه که تولید شد ظاهر شود
# print()  # در آخر، یک خط ایجاد کن

# def get_prompt(instruction: str) -> str:
#     system = "You are an AI assistant that gives helpful answers. You answer the questions in a short and concise way."
#     prompt = f"### System:\n{system}\n\n### User:\n{instruction}\n\n### Response:\n"  # Prompt format of the model on Huggingface. Because this model is trained in this way
#     print(prompt)  # For debugging
#     return prompt
# question = "Which city is the capital of Canada?"
# for word in llm(get_prompt(question), stream=True):  # stream = جریان، گذار کلمه به کلمه
#     print(word, end="", flush=True)  # end="": با یک رشته خالی تمام شود نه با خط بعدی  flush=True: هر کلمه که تولید شد ظاهر شود
# print()  # در آخر، یک خط ایجاد کن
# question = "And which is of the United States?"
# for word in llm(get_prompt(question), stream=True):  # stream = جریان، گذار کلمه به کلمه
#     print(word, end="", flush=True)  # end="": با یک رشته خالی تمام شود نه با خط بعدی  flush=True: هر کلمه که تولید شد ظاهر شود
# print()  # در آخر، یک خط ایجاد کن


def get_prompt(instruction: str, history: List[str] = None) -> str:  # None if there were not any list of history
    system = "You are an AI assistant that gives helpful answers. You answer the questions in a short and concise way."
    prompt = f"###System:\n{system}\n\n### User:\n"
    if history is not None:
        prompt += f"This is the conversation history: {''.join(history)}. Now answer the question: "  # Coding in NLP way by speaking. ''.join(history) is for changing type of hisory to str
    prompt += f"{instruction}\n\n### Response:\n"  # Prompt format of the model on Huggingface. Because this model is trained in this way
    print(prompt)  # For debugging
    return prompt


history = []  # First, we have no histories
question = "Which city is the capital of Canada?"
answer = ""  # For collecting the answer
for word in llm(get_prompt(question), stream=True):  # stream = جریان، گذار کلمه به کلمه
    answer += word  # collecting the answer
    print(word, end="", flush=True)  # end="": با یک رشته خالی تمام شود نه با خط بعدی  flush=True: هر کلمه که تولید شد ظاهر شود
print()  # در آخر، یک خط ایجاد کن
history.append(answer)  # Using answers as history
question = "And which is of the United States?"
for word in llm(get_prompt(question, history), stream=True):  # stream = جریان، گذار کلمه به کلمه And using history value for applying history
    print(word, end="", flush=True)  # end="": با یک رشته خالی تمام شود نه با خط بعدی  flush=True: هر کلمه که تولید شد ظاهر شود
print()  # در آخر، یک خط ایجاد کن
