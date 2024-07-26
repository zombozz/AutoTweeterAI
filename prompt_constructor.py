from config import prompt, persona, use_behaviour, avoid_behaviour

def construct_prompt(history):

    message = "AVOID writing anything similar to these previous replies: " + history + " Here is your prompt/context: " + prompt
    behaviour = "Your persona is: " + persona + ". Use/sound like the following behaviour: " + use_behaviour + ". Avoid the following behaviour: " + avoid_behaviour + ". It's crucial that you respond in 200 characters or less, and AVOID writing something similar to previous replies."

    return message, behaviour