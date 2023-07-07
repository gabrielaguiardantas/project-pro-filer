from pro_filer.actions.main_actions import find_duplicate_files  # NOQA

import pytest


def test_find_duplicate_files_default_output(tmp_path):
    # criação do diretório temporário
    temp_dir = tmp_path / "temp"
    temp_dir.mkdir()

    # criação dos arquivos que serão usados no teste
    temp_file_1 = temp_dir / "temp_file_1.txt"
    temp_file_1.write_text("same file content")
    temp_file_2 = temp_dir / "temp_file_2.txt"
    temp_file_2.write_text("same file content")
    temp_file_3 = temp_dir / "temp_file_3.txt"
    temp_file_3.write_text("diferent file content")

    # criação do mock do context
    mock_context = {
        "all_files": [str(temp_file_1), str(temp_file_2), str(temp_file_3)]
    }

    # chamada da função
    result = find_duplicate_files(mock_context)

    # asserção esperada
    assert result == [(str(temp_file_1), str(temp_file_2))]


def test_find_duplicate_files_with_inexistent_file(tmp_path):
    # criação do diretório temporário
    temp_dir = tmp_path / "temp"
    temp_dir.mkdir()

    # criação dos arquivos que serão usados no teste
    temp_file_1 = temp_dir / "temp_file_1.txt"
    temp_file_1.write_text("same file content")

    # criação do mock do context
    mock_context = {
        "all_files": [str(temp_file_1), f"{str(temp_dir)}/inexistent_file.py"]
    }

    # asserção esperada
    with pytest.raises(ValueError):
        # chamada da função
        find_duplicate_files(mock_context)
