from pro_filer.actions.main_actions import show_details  # NOQA
from datetime import date
import os


def test_show_details_with_inexistent_file(capsys):
    context_mock = {"base_path": "/inexistent_dir/inexistent_file.py"}

    show_details(context_mock)
    captured = capsys.readouterr()

    assert captured.out == "File 'inexistent_file.py' does not exist\n"


def test_show_details_default_message(capsys, tmp_path):
    file_name = "temp"

    temp_dir = tmp_path / file_name
    temp_dir.mkdir()
    temp_path = str(temp_dir)  # pegando o path do temp_dir

    context_mock = {"base_path": temp_path}

    show_details(context_mock)  # função a ser testada

    captured = capsys.readouterr().out.split(
        "\n"
    )  # saída dos prints divididos por linha

    _, file_extension = os.path.splitext(
        file_name
    )  # pegando a extensão do arquivo

    py_mod_date = date.fromtimestamp(
        os.path.getmtime(temp_path)
    )  # pegando a data de modificação do arquivo

    assert captured[0] == f"File name: {file_name}"
    assert captured[1] == f"File size in bytes: {os.path.getsize(temp_path)}"
    assert (
        captured[2]
        == f"File type: {'directory' if os.path.isdir(temp_path) else 'file'}"
    )
    assert (
        captured[3] == f"File extension: {file_extension or '[no extension]'}"
    )
    assert captured[4] == f"Last modified date: {py_mod_date}"
