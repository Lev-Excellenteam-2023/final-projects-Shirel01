

from pptx import Presentation
import asyncio
#import pptx
import openai
import chat_gpt_interface
import json_utils
import prompt_builder
import read_from_powerpoint


def process_slide(slide):
    slide_content = read_from_powerpoint.parse_slide(slide)
    prompt = prompt_builder.build_prompt_for_single_slide(slide_content)
    responses = chat_gpt_interface.send_query(prompt)
    res = chat_gpt_interface.extract_response(responses)
    return res

"""async def process_slides(slides):
    tasks = []

    for slide_content in slides:
        task = asyncio.to_thread(send_query, slide_content)
        tasks.append(task)

    responses = await asyncio.gather(*tasks)
    return responses"""
def main():
    file_path = "C:/Users/shire/Downloads/le_chien.pptx"
    presentation = Presentation(file_path)
    fullexplanation = []
    for slide in presentation.slides:
        response = process_slide(slide)
        fullexplanation.append(response)


    json_utils.save_to_json(fullexplanation, "res.json")


if __name__ == "__main__":
    main()
 #powerpoint_content = read_from_powerpoint.parse_all_power_point(file_path)
    #prompt = open_ai_query_builder.build_prompt(powerpoint_content)
    #responses = chat_gpt_interface.send_query(prompt)
    #res = chat_gpt_interface.extract_response(responses)
   # json_utils.save_to_json(res, "res.json")
