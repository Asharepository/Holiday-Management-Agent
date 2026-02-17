from autogen_agentchat.agents import AssistantAgent
from holiday_management.models.gpt_model import model_client

reseacher_agent = AssistantAgent(
    name = "Holiday_Researcher",
    description = "A Holiday researcher agent that helps users research about their holiday destinations.",
    model_client = model_client,
    system_message = """You are a Holiday researcher agent. Provide essential information about the destination:
    
    - Best locations to visit
    - Local cuisine highlights
    - Weather and best time to visit
    - Cultural tips and customs
    
    Be concise and informative. After providing complete information, end your message with 'FINAL ANSWER'."""
)