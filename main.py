from flet import (
    Page, 
    FilePickerResultEvent,
    FilePicker,
    AlertDialog, 
    Text,
    ElevatedButton,
    Container,
    app,
    icons,
    Column,
    alignment,
    )


from pathlib import Path
import time


import paths_settings
from automatic_tagging import AutomaticTagging



def main(page: Page):
    page.title = "mp3 & flac tagger"
    page.window_center()
    page.window_height, page.window_width = 300, 500
    page.window_max_height, page.window_max_width = 300, 500
    page.scroll = True


    def choose_file(e: FilePickerResultEvent):
        def close_dialog(event):
            dialog.open = False
            page.update()

        at = AutomaticTagging(
            str(
                Path(e.files[0].path)
            )
        )

        start = time.time()

        dialog = AlertDialog(
            title= Text(value= paths_settings.TAGGING, size= 15),
            modal= True,
        )
        page.dialog = dialog
        dialog.open = True
        page.update()
        
        for nr, (file, title, file_format) in enumerate(zip(at.music_files, at.titles, at.music_files_formats), start= 1):
            dialog.clean()
            
            progress_proc = round(100 * (int(nr) / int(at.len_of_music_files)), 2)

            dialog.content = Text(
                    value= f"{str(nr).zfill(len(str(at.len_of_music_files)))}/{at.len_of_music_files}. {title}\n{paths_settings.PROGRESS}: {progress_proc}%"
                )

            dialog.update()
            
            at.tag_music_file(nr, file, title, file_format)

        end = time.time()
        time_delta = end - start

        dialog.clean()
        dialog.content = Text(
            value= paths_settings.TIME_DELTA.format(time_delta)
        )
        dialog.actions = [
            ElevatedButton(
                text= Text(value= paths_settings.CLOSE).value,
                on_click= close_dialog
            )
        ]
        dialog.update()


    pick_file = FilePicker(
        on_result= choose_file
    )
    choosen_file = Text()
    page.overlay.append(pick_file)

    page.add(
        Container(
            padding= 5,
            height= 50,
            width= 490,
        ),

        Container(
            ElevatedButton(
                text= Text(value= paths_settings.CHOOSE_FILE).value,
                on_click= lambda _: pick_file.pick_files(
                    allowed_extensions= ["txt"],
                ),
                icon= icons.UPLOAD_FILE,
            ),
            padding= 5,
            height= 50,
            width= 490,
        ),

        Container(
            ElevatedButton(
                text= Text(value= paths_settings.SOURCE_CODE).value,
                icon= icons.OPEN_IN_BROWSER,
            ),
            padding= 5,
            height= 50,
            width= 490,
            url= "https://github.com/skrzypa/mp3_flac_tag",
        ),
        
        Container(
            padding= 5,
            height= 50,
            width= 490,
        ),
    ),


app(target= main)