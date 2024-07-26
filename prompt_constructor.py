from config import Config

def construct_prompt(history):
    config = Config()
    if config.use_history_context_option == 1:
        message = "Write using the following messages as context/inspiration: " + history + " Here is your prompt/context: " + config.prompt
    elif config.use_history_context_option == 2:
        message = config.prompt
    behaviour = "Your persona is: " + config.persona + ". Use/sound like the following behaviour: " + config.use_behaviour + ". Avoid the following behaviour: " + config.avoid_behaviour + ". It's crucial that you respond in 200 characters or less, and AVOID writing something similar to previous replies."

    return message, behaviour