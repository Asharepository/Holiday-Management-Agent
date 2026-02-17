from autogen_agentchat.agents import AssistantAgent
from holiday_management.models.gpt_model import model_client

planner_agent = AssistantAgent(
    name = "Holiday_Planner",
    description = "A Holiday planner agent that helps users plan their trips.",
    model_client = model_client,
    system_message = """You are a Holiday planner agent. Create a detailed 5-day itinerary for the user's trip.
    
    Provide:
    - Day-by-day schedule
    - Recommended activities
    - Local food suggestions
    - Travel tips
    
    Be concise and practical. After providing the complete plan, end your message with 'FINAL ANSWER' to indicate completion."""
)