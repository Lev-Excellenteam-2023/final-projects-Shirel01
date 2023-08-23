import os
import asyncio

from pptx import Presentation
from Explainer import read_from_powerpoint, json_utils, chat_gpt_interface


UPLOADS_FOLDER = os.getenv('UPLOADS_FOLDER_PATH')

OUTPUTS_FOLDER = os.getenv('OUTPUTS_FOLDER_PATH')

async def process_slide(slides):
    UPLOADS_FOLDER = os.environ.get("UPLOADS_FOLDER_PATH")
    tasks = await asyncio.gather (*[asyncio.create_task(chat_gpt_interface.send_query (slide))for slide in slides])
    return tasks

async def process_presentation(file_path):
    file_path = "C:/Users/shire/Downloads/le_chien.pptx"
    presentation = Presentation(file_path)
    powerpoint_content = read_from_powerpoint.parse_all_power_point(file_path)
    response = asyncio.run(process_slide(powerpoint_content))
    json_utils.save_to_json(response, "res.json")
    return response



async def process_new_files():
    while True:
        print("Checking for new files...")
        pptx_files = [file for file in os.listdir(UPLOADS_FOLDER)]

        for pptx_file in pptx_files:
            name_file = pptx_file
            print("name file: ", name_file)
            json_file = name_file + ".json"
            print("json_file: ", json_file)
            json_file_path = os.path.join(OUTPUTS_FOLDER, json_file)
            print("json_file_path: ", json_file_path)

            if not os.path.exists(json_file_path):
                presentation_path = os.path.join(UPLOADS_FOLDER, pptx_file)
                print(f"Processing file: {pptx_file}")
                await process_presentation(presentation_path, name_file)
                print(f"File processed: {pptx_file}")
                os.remove(os.path.join(UPLOADS_FOLDER, pptx_file))

        await asyncio.sleep(10)


if __name__ == "__main__":
    asyncio.run(process_new_files())


