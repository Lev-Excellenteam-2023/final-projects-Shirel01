

from pptx import Presentation
import asyncio
#import pptx
import openai
import chat_gpt_interface
import json_utils
import prompt_builder
import read_from_powerpoint


async def process_slide(slides):

    tasks = await asyncio.gather (*[asyncio.create_task(chat_gpt_interface.send_query (slide))for slide in slides])
    return tasks


def main():
    file_path = "C:/Users/shire/Downloads/le_chien.pptx"
    presentation = Presentation(file_path)
    powerpoint_content = read_from_powerpoint.parse_all_power_point(file_path)
    response = asyncio.run(process_slide(powerpoint_content))
    json_utils.save_to_json(response, "res.json")
    return response
if __name__ == "__main__":
    main()


