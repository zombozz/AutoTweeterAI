from config import use_history_context_option, prompt, persona, use_behaviour, avoid_behaviour

def construct_prompt(history):
    if use_history_context_option == 1:
        message = "AVOID writing anything similar to these previous replies: " + history + " Here is your prompt/context: " + prompt
    elif use_history_context_option == 2:
        message = "Write using the following messages as context/inspiration: " + history + " Here is your prompt/context: " + prompt
    elif use_history_context_option == 3:
        message = prompt
    behaviour = "Your persona is: " + persona + ". Use/sound like the following behaviour: " + use_behaviour + ". Avoid the following behaviour: " + avoid_behaviour + ". It's crucial that you respond in 200 characters or less, and AVOID writing something similar to previous replies."

    return message, behaviour