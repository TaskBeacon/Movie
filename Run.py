from psyflow.screenflow import *
from task.expsetup import exp_setup
from task.expcontrol import exp_run
from psychopy import prefs
prefs.hardware['audioLib'] = ['sounddevice']

# Example subject info
subdata = ['144', '23', 'Male', 'Caucasian']

# Setup experiment with a specific movie
win, kb, settings = exp_setup(
    subdata=subdata,
    video_path='media',
    bg_color='gray',
    movie_name='presentch.mp4'
)

# Optional intro text for movie-watching
intro_text = (
    'In this task, you will watch a short movie clip.\n\n'
    'Please pay attention and remain still during the entire video.\n'
    'Press CTRL + Q if you need to quit early.\n\n'
    'Press SPACE to begin.'
)

show_instructions(win, intro_text=intro_text)
show_realtime_countdown(win)
exp_run(win, kb, settings, subdata)
show_goodbye(win)
