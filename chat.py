# In terminal: pip insall ctransformers

import chainlit as cl
from typing import List  # For being able to use in history
from ctransformers import AutoModelForCausalLM

# llm = AutoModelForCausalLM.from_pretrained(
#    "zoltanctoth/orca_mini_3B-GGUF", model_file="orca-mini-3b.q4_0.gguf"
# )

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


# def get_prompt(instruction: str, history: List[str] = None) -> str:  # None if there were not any list of history
#     system = "You are an AI assistant that gives helpful answers. You answer the questions in a short and concise way."
#     prompt = f"###System:\n{system}\n\n### User:\n"
#     if history is not None:
#         prompt += f"This is the conversation history: {''.join(history)}. Now answer the question: "  # Coding in NLP way by speaking. ''.join(history) is for changing type of hisory to str
#     prompt += f"{instruction}\n\n### Response:\n"  # Prompt format of the model on Huggingface. Because this model is trained in this way
#     print(prompt)  # For debugging
#     return prompt
# history = []  # First, we have no histories
# question = "Which city is the capital of Canada?"
# answer = ""  # For collecting the answer
# for word in llm(get_prompt(question), stream=True):  # stream = جریان، گذار کلمه به کلمه
#     answer += word  # collecting the answer
#     print(word, end="", flush=True)  # end="": با یک رشته خالی تمام شود نه با خط بعدی  flush=True: هر کلمه که تولید شد ظاهر شود
# print()  # در آخر، یک خط ایجاد کن
# history.append(answer)  # Using answers as history
# question = "And which is of the United States?"
# for word in llm(get_prompt(question, history), stream=True):  # stream = جریان، گذار کلمه به کلمه And using history value for applying history
#     print(word, end="", flush=True)  # end="": با یک رشته خالی تمام شود نه با خط بعدی  flush=True: هر کلمه که تولید شد ظاهر شود
# print()  # در آخر، یک خط ایجاد کن

# ----------------------------------------------------------------------------------------------------------------------------
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ----------------------------------------------------------------------------------------------------------------------------
# For making Ui using chainlit:
# For running it, for python files we need in Terminal: chainlit run file.py
# And For avoiding of crtl+c everytime we chane our code and let chainli update itself authomaticly when we change our code
# In Terminal: chainlit run file.py -w
# ----------------------------------------------------------------------------------------------------------------------------
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ----------------------------------------------------------------------------------------------------------------------------

# def get_prompt(instruction: str, history: List[str] = None) -> str:  # None if there were not any list of history
#     system = "You are an AI assistant that gives helpful answers. You answer the questions in a short and concise way."
#     prompt = f"###System:\n{system}\n\n### User:\n"
#     if history is not None:
#         prompt += f"This is the conversation history: {''.join(history)}. Now answer the question: "  # Coding in NLP way by speaking. ''.join(history) is for changing type of hisory to str
#     prompt += f"{instruction}\n\n### Response:\n"  # Prompt format of the model on Huggingface. Because this model is trained in this way
#     print(prompt)  # For debugging
#     return prompt
# @cl.on_message
# async def on_message(message: cl.Message):
#     response = f"Hello, you just sent: {message.content}!"
#     await cl.Message(response).send()

# ----------------------------------------------------------------------------------------------------------------------------
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ----------------------------------------------------------------------------------------------------------------------------
# For changing Ui in chainlit page in Readme Tab, we must change the chainlit.md file
# For changing configs or settings of chainlit like name of bot or... , we must change config.toml file in .chainlit folder
# ----------------------------------------------------------------------------------------------------------------------------
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ----------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ----------------------------------------------------------------------------------------------------------------------------
# For using our LLM in chainlit
# ----------------------------------------------------------------------------------------------------------------------------
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ----------------------------------------------------------------------------------------------------------------------------

# def get_prompt(instruction: str, history: List[str] = None) -> str:  # None if there were not any list of history
#     system = "You are an AI assistant that gives helpful answers. You answer the questions in a short and concise way."
#     prompt = f"###System:\n{system}\n\n### User:\n"
#     if history is not None:
#         prompt += f"This is the conversation history: {''.join(history)}. Now answer the question: "  # Coding in NLP way by speaking. ''.join(history) is for changing type of hisory to str
#     prompt += f"{instruction}\n\n### Response:\n"  # Prompt format of the model on Huggingface. Because this model is trained in this way
#     print(prompt)  # For debugging
#     return prompt
# @cl.on_message
# async def on_message(message: cl.Message):
#     prompt = get_prompt(message.content)  # message.content for getting content of msg
#     response = llm(prompt)
#     await cl.Message(response).send()

# ----------------------------------------------------------------------------------------------------------------------------
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ----------------------------------------------------------------------------------------------------------------------------
# For calling our LLM model just when we started chating in chainlit, we must define llm global var in this environment except
# for just first line of our code
# Its details is in: chat life cycle in documentation
# This is a much better way to use llm var
# ----------------------------------------------------------------------------------------------------------------------------
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ----------------------------------------------------------------------------------------------------------------------------

# Delete defining llm var at the first line of our code and:
# @cl.on_chat_start
# def on_chat_start():
#     global llm  # For making it global to use in on_message func
#     llm = AutoModelForCausalLM.from_pretrained(
#         "zoltanctoth/orca_mini_3B-GGUF", model_file="orca-mini-3b.q4_0.gguf"
#     )

# ----------------------------------------------------------------------------------------------------------------------------
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ----------------------------------------------------------------------------------------------------------------------------
# For streaming response, we must:
# ----------------------------------------------------------------------------------------------------------------------------
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ----------------------------------------------------------------------------------------------------------------------------


# def get_prompt(instruction: str, history: List[str] = None) -> str:  # None if there were not any list of history
#     system = "You are an AI assistant that gives helpful answers. You answer the questions in a short and concise way."
#     prompt = f"###System:\n{system}\n\n### User:\n"
#     if history is not None:
#         prompt += f"This is the conversation history: {''.join(history)}. Now answer the question: "  # Coding in NLP way by speaking. ''.join(history) is for changing type of hisory to str
#     prompt += f"{instruction}\n\n### Response:\n"  # Prompt format of the model on Huggingface. Because this model is trained in this way
#     print(prompt)  # For debugging
#     return prompt
# @cl.on_message
# async def on_message(message: cl.Message):
#     msg = cl.Message(content="")  # At first, we send an empty msg for starting streaming
#     await msg.send()  # Send msg to user

#     prompt = get_prompt(message.content)  # message.content for getting content of msg
#     for word in llm(prompt, stream=True):
#         await msg.stream_token(word)  # stream_token makes our token to stream which is word
#     await msg.update()  # This updates msg for streaming

# ----------------------------------------------------------------------------------------------------------------------------
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ----------------------------------------------------------------------------------------------------------------------------
# For having history, we can not set a common var history because on this server me might have different users using this service
# and we must define history var personalized for every users.
# So we use user session in cl, which details is in user state in documentation of chainlit
# ----------------------------------------------------------------------------------------------------------------------------
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ----------------------------------------------------------------------------------------------------------------------------

# Delete defining llm var at the first line of our code and:
@cl.on_chat_start
def on_chat_start():
    cl.user_session.set("message_history", [])  # At first, we create our needed session which is message_history with value []
    global llm  # For making it global to use in on_message func
    llm = AutoModelForCausalLM.from_pretrained(
        "zoltanctoth/orca_mini_3B-GGUF", model_file="orca-mini-3b.q4_0.gguf"
    )


def get_prompt(instruction: str, history: List[str]) -> str:  # None if there were not any list of history # We delete  = None
    system = "You are an AI assistant that gives helpful answers. You answer the questions in a short and concise way."
    prompt = f"###System:\n{system}\n\n### User:\n"
    # if history is not None:
    if len(history) > 0:  # Because we have changed the history's first value from None to empty list []
        prompt += f"This is the conversation history: {''.join(history)}. Now answer the question: "  # Coding in NLP way by speaking. ''.join(history) is for changing type of hisory to str
    prompt += f"{instruction}\n\n### Response:\n"  # Prompt format of the model on Huggingface. Because this model is trained in this way
    # print(prompt)  # For debugging
    return prompt


@cl.on_message
async def on_message(message: cl.Message):
    user_message_history = cl.user_session.get("message_history")  # With this equality, when we change user_message_history value, authomaticly our message_history session will be changed and we are not forced to reset our session
    msg = cl.Message(content="")  # At first, we send an empty msg for starting streaming
    await msg.send()  # Send msg to user

    prompt = get_prompt(message.content, user_message_history)  # message.content for getting content of msg # We add history by user_message_history
    response = ""  # For using to collect and add prev response to user_message_history
    for word in llm(prompt, stream=True):
        await msg.stream_token(word)  # stream_token makes our token to stream which is word
        response += word
    await msg.update()  # This updates msg for streaming

    user_message_history.append(response)
