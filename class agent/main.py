import os
import asyncio
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner
import chainlit as cl

load_dotenv()

@cl.on_chat_start
async def start():
    MODEL_NAME = "gemini-2.0-flash"
    API_KEY = os.getenv("GEMINI_API_KEY")

    # Set up Gemini API client
    external_client = AsyncOpenAI(
        api_key=API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    model = OpenAIChatCompletionsModel(
        model=MODEL_NAME,
        openai_client=external_client
    )

    cl.user_session.set("chat_history", [])

    teacher = Agent(
        name="math teacher",
        instructions="You are a helpful math teacher.",
        model=model
    )

    cl.user_session.set("agent", teacher)

    await cl.Message(content="Welcome to the MATH TEACHER FRIDAY agent!").send()


@cl.on_message
async def main(message: cl.Message):
    msg = await cl.Message(content="Thinking or Processing your query...").send()

    teacher = cl.user_session.get("agent")
    history = cl.user_session.get("chat_history")
    history.append({"role": "user", "content": message.content})

    result = await Runner.run(starting_agent=teacher, input=history)

    msg.content = result.final_output
    await msg.update()

    cl.user_session.set("chat_history", result.to_input_list())

    print(result.final_output)

#  result = await Runner.run(starting_agent=teacher, input="tell me the answer of 10 + 10")



 # MODEL_NAME = "gemini-2.0-flash"
    # API_KEY = os.getenv("GEMINI_API_KEY")

    # # Set up Gemini API client
    # external_client = AsyncOpenAI(
    #     api_key=API_KEY,
    #     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    # )

    # Set up the model using OpenAI-style interface
#  model = OpenAIChatCompletionsModel(
#         model=MODEL_NAME,
#         openai_client=external_client
#     )

    # Define the agent
#  teacher = Agent(
#         name="math teacher",
#         instructions="You are a helpful math teacher.",
#         model=model
#     )

    # Run the agent using the runner






# import os
# from dotenv import load_dotenv
# from agents import AsyncOpenAI,OpenAIChatCompletionsModel,Agent,Runner,set_tracing_disabled,function_tool
# import asyncio
# load_dotenv()
# def main():
#  MODEL_NAME = "gemini-2.0-flash"
#  API_KEY = os.getenv("GEMINI_API_KEY")

# external_client = AsyncOpenAI(
#         api_key= API_KEY,
#         base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
#     )
# model = OpenAIChatCompletionsModel(
#          model=MODEL_NAME,
#          openai_client=external_client,
#     )
# teacher = Agent(
#         name = "math teacher",
#         instructions= f"You are a helpful math teacher .",
#         model=model,
        
#     )
# result= awaitRunner.run(starting_agent=teacher,input="tell me the answer of 10 +10")
# print(result.final_output)
# # def main():
# #     print("Hello from class-agent!")


# if __name__ == "__main__":
#   asyncio.run(  main())
