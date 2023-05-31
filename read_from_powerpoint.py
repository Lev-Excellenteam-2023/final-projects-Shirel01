from pptx import Presentation

class PowerPointReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse_slide(self, slide_number):
        presentation = Presentation(self.file_path)
        slide = presentation.slides[slide_number - 1]
        slide_content = []

        for shape in slide.shapes:
            if shape.has_text_frame:
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        slide_content.append(run.text)

        return slide_content
"""   
    def parse_all_power_point(self):
        presentation = Presentation(self.file_path)
        slides_content = []

        for i, slide in enumerate(presentation.slides):
            slide_content = self.parse_slide(i + 1)
            slides_content.append(slide_content)

        return slides_content
"""



