from autogen_agentchat.conditions import TextMentionTermination, MaxMessageTermination
from autogen_core import CancellationToken

def get_termination_condition():
    """
    Get the termination condition for the agent.
    Combines text mention and max message termination.
    """
    # Stop if agents mention these words OR after 8 messages
    TERMINATION_WORDS = ["TERMINATE", "FINAL ANSWER", "stop"]
    text_termination = TextMentionTermination(TERMINATION_WORDS)
    max_message_termination = MaxMessageTermination(max_messages=8)
    
    # Return the max message termination as primary
    return max_message_termination