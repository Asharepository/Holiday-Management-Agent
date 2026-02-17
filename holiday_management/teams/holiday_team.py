from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import MaxMessageTermination
from holiday_management.agents.planner import planner_agent
from holiday_management.agents.researcher import reseacher_agent

# RoundRobin team with max 4 messages (2 turns per agent)
team = RoundRobinGroupChat(
    participants=[reseacher_agent, planner_agent],
    termination_condition=MaxMessageTermination(max_messages=4)
)


