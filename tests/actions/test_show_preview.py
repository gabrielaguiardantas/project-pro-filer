from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview_empty_files_and_dirs(capsys):
    mock_context = {"all_files": [], "all_dirs": []}

    show_preview(mock_context)
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"


def test_show_preview_correct_slice_results(capsys):
    mock_context = {
        "all_files": ["a", "b", "c", "d", "e", "f"],
        "all_dirs": ["a", "b", "c", "d", "e", "f"],
    }

    show_preview(mock_context)
    captured = capsys.readouterr()
    assert (
        captured.out.split("\n")[1]
        == "First 5 files: ['a', 'b', 'c', 'd', 'e']"
    )
    assert (
        captured.out.split("\n")[2]
        == "First 5 directories: ['a', 'b', 'c', 'd', 'e']"
    )
