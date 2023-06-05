

from pptx import Presentation

#import pptx
import openai
import chat_gpt_interface
import open_ai_query_builder
import read_from_powerpoint


def main():
    file_path = "C:/Users/shire/Downloads/le_chien.pptx"
    powerpoint_content = read_from_powerpoint.parse_all_power_point(file_path)
    prompt = open_ai_query_builder.build_prompt(powerpoint_content)
    responses = chat_gpt_interface.send_query(prompt)
    print(responses)





if __name__ == "__main__":
    main()
