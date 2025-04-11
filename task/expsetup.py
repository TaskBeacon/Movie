import os
from psychopy import visual
from psychopy.hardware import keyboard
from datetime import datetime
from types import SimpleNamespace

def exp_setup(
    subdata,
    video_path="media",
    movie_name="presentch.mp4",
    win_size=(1920, 1080),
    bg_color='black',
    fullscr=True,
):
    """
    Initializes the PsychoPy window, video path, and keyboard input handler 
    for a single-movie naturalistic viewing task.

    Parameters
    ----------
    subdata : list
        Subject information (e.g., [sub_id, group, session]).
    video_path : str
        Folder where the movie is stored.
    movie_name : str
        Filename of the movie (e.g., 'clip01.mp4').
    win_size : tuple
        Window size.
    bg_color : str
        Background color.
    screen : int
        Screen index for multi-display setups.
    fullscr : bool
        Whether to run fullscreen.

    Returns
    -------
    win : visual.Window
        The PsychoPy window.
    kb : keyboard.Keyboard
        Keyboard object.
    settings : SimpleNamespace
        Experiment settings and metadata.
    """

    # Initialize window
    win = visual.Window(
        size=win_size,
        monitor="testMonitor",
        units="deg",
        screen=1,
        color=bg_color,
        fullscr=fullscr,
        gammaErrorPolicy='ignore'
    )

    # Initialize settings
    settings = SimpleNamespace()
    settings.video_path = video_path
    settings.movie_name = movie_name

    # Full path to the movie file
    movie_full_path = os.path.join(video_path, movie_name)
    if not os.path.isfile(movie_full_path):
        raise FileNotFoundError(f"Movie file not found: {movie_full_path}")
    
    settings.movie_file = movie_full_path

    # Output file
    dt_string = datetime.now().strftime("%H%M%d%m")
    settings.outfile = f"Subject{subdata[0]}_{dt_string}.csv"

    # Initialize keyboard
    kb = keyboard.Keyboard()

    return win, kb, settings
