def build_prompt(powerpoint_content_list: list[list[str]]) -> str:
    all_text = []

    for slide_list in powerpoint_content_list:
        all_text.extend(slide_list)

    prompt = "Explain these slides of PowerPoint: "
    prompt += ' '.join(all_text)

    return prompt


def build_prompt_for_single_slide(slide_content_list: list[str]) -> str:
    prompt = "Explain this slide of PowerPoint:\n"
    prompt += ''.join(slide_content_list)
    return prompt
