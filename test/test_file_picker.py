"""file_picker.pyのテスト."""

from pathlib import Path

import file_picker as fp

TARGET = Path("test/__init__.py")


def test_file_picker() -> None:
    """テスト.ダイアログ表示時に__init__.pyやそのディレクトリを選択すること."""
    result = fp.pick_file([(TARGET.name, TARGET.name)], Path(__file__).parent)
    assert result.absolute() == Path(TARGET).absolute()  # noqa: S101

    result2 = fp.pick_files([(TARGET.name, TARGET.name)], Path(__file__).parent)
    assert result2[0].absolute() == Path(TARGET).absolute()  # noqa: S101

    result3 = fp.pick_dir(Path(__file__).parent)
    assert result3.absolute() == Path(TARGET).parent.absolute()  # noqa: S101
