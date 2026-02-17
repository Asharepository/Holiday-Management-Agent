from autogen_agentchat.messages import TextMessage
from holiday_management.teams.holiday_team import team

async def main():
    task = TextMessage(content = "I want to plan a trip to Switzerland for 5 days. I want to visit the mountains and try some local food. Can you help me with that?")
    response = await team.run(task=task)

    for message in response.messages:
        print(f"{message.source} : {message.content}")


if __name__ == "__main__":
    asyncio.run(main())