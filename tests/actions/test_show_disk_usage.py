from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from pro_filer.cli_helpers import _get_printable_file_path
import os


def test_show_disk_usage_with_empty_list(capsys):
    mock_context = {"all_files": []}

    show_disk_usage(mock_context)
    captured = capsys.readouterr()

    assert captured.out == "Total size: 0\n"


def test_show_disk_usage_correct_order(capsys, tmp_path):
    # criação do diretório temporário
    temp_dir = tmp_path / "temp"
    temp_dir.mkdir()

    # criação dos arquivos que serão usados no teste
    temp_file_1 = temp_dir / "temp_file_1.txt"
    temp_file_1.write_text("file that print firstttttttttttt")
    temp_file_2 = temp_dir / "temp_file_2.txt"
    temp_file_2.write_text("file that print second")

    # criação do mock do context
    mock_context = {"all_files": [str(temp_file_1), str(temp_file_2)]}

    # criação das informações que serão usadas para asserções
    total_size = sum(
        os.path.getsize(file) for file in mock_context["all_files"]
    )
    percentage_per_file = int(os.path.getsize(temp_file_1) / total_size * 100)

    # chamada da função a ser testada
    show_disk_usage(mock_context)

    # captura dos prints que serão lançados pela função, já divididos por linha
    captured = capsys.readouterr().out.split("\n")

    # verificando se a asserção bate com a mensagem default
    assert (
        captured[0]
        == f"'{_get_printable_file_path(str(temp_file_1))}'"
        + f":        {os.path.getsize(temp_file_1)} ({percentage_per_file}%)"
    )
