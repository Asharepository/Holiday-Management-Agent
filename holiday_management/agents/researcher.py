from auotogen_agentchat.agents import AssistantAgent
from holiday_management.models.get_mmodel import model_client

reseacher_agent = AssistantAgent(
    name = "Holiday_Researcher",
    description = "A Holiday researcher agent that helps users research about their holiday destinations.",
    model_client = model_client,
    system_message = "You are a Holiday researcher agent. Your task is to help users research about their holiday destinations by providing information about destinations, itineraries, and travel tips"
)