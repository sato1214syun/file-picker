"""Utility functions for selecting file(files) or directory and extracting path."""

import tkinter as tk
from pathlib import Path
from tkinter import filedialog as tk_file_dialog


def init_window(func):  # noqa: ANN001, ANN201
    """デコレータ."""

    def wrapper(*arg, **kwargs):  # noqa: ANN202
        """選択ウィンドウの初期化."""
        # ファイル選択ダイアログの表示
        root = tk.Tk()
        root.withdraw()
        # Make it almost invisible - no decorations, 0 size, top left corner.
        root.overrideredirect(boolean=True)
        root.geometry("0x0+0+0")
        root.deiconify()
        root.lift()
        root.focus_force()

        result = func(*arg, **kwargs)

        root.destroy()
        return result

    return wrapper


@init_window
def pick_file(
    file_type: list[tuple[str, str]] | None = None,
    init_dir: Path | None = Path(__file__).parent,
) -> Path:
    """ファイル選択ウィンドウで選択したファイルパスを返す.

    Args:
        file_type (list[tuple[str, str]] | None, optional): File type restriction.
        Defaults to None.
        init_dir (Path | None, optional): Initial open directory.
        Defaults to Path(__file__).parent.

    Returns:
        Path: 選択したファイルのパス
    """
    # file_typeの初期化
    if file_type is None:
        file_type = [("すべてのファイル", "*")]

    # 初期表示ディレクトリの設定
    initial_dir = None if init_dir is None else str(init_dir)

    file_path = tk_file_dialog.askopenfilename(
        filetypes=file_type,
        initialdir=initial_dir,
    )
    return Path(file_path)


@init_window
def pick_files(
    file_type: list[tuple[str, str]] | None = None,
    init_dir: Path | None = Path(__file__).parent,
) -> list[Path]:
    """ファイル選択ウィンドウで選択したファイルパスを返す(複数選択可).

    Args:
        file_type (list[tuple[str, str]] | None, optional): File type restriction.
        Defaults to None.
        init_dir (Path | None, optional): Initial open directory.
        Defaults to Path(__file__).parent.

    Returns:
        Path: 選択したファイルのパス
    """
    # file_typeの初期化
    if file_type is None:
        file_type = [("すべてのファイル", "*")]

    # 初期表示ディレクトリの設定
    initial_dir = None if init_dir is None else str(init_dir)

    # 画面表示
    file_paths = tk_file_dialog.askopenfilenames(
        filetypes=file_type,
        initialdir=initial_dir,
    )
    return [Path(path) for path in file_paths]


@init_window
def pick_dir(init_dir: Path | None = Path(__file__).parent) -> Path:
    """ファイル選択ウィンドウで選択したディレクトリパスを返す.

    Args:
        init_dir (Path | None, optional): Initial open directory.
        Defaults to Path(__file__).parent.

    Returns:
        Path: 選択したディレクトリのパス
    """
    # 初期表示ディレクトリの設定
    initial_dir = None if init_dir is None else str(init_dir)

    dir_path = tk_file_dialog.askdirectory(initialdir=initial_dir)
    return Path(dir_path)
