import os
import pandas as pd
from psychopy import visual, event, core, logging
from datetime import datetime

def exp_run(win, kb, settings, subdata):
    """
    Runs a naturalistic movie-watching task for a single movie.

    Procedure:
        1. Optional fixation cross (settings.fixDuration)
        2. Play the .mp4 movie file using MovieStim3
        3. Record timing information and log
        4. Optional ITI (settings.ITI)

    Parameters
    ----------
    win : visual.Window
        The PsychoPy window object.
    kb : keyboard.Keyboard
        Keyboard object for response collection.
    settings : SimpleNamespace
        Contains experiment parameters including movie_file.
    subdata : list
        Subject info (used for logging/saving).
    """
    # Setup logging
    log_filename = settings.outfile.replace('.csv', '.log')
    logging.LogFile(log_filename, level=logging.DATA, filemode='a')
    logging.console.setLevel(logging.INFO)
    event.globalKeys.clear()
    event.globalKeys.add(key='q', modifiers=['ctrl'], func=core.quit)
    event.Mouse(visible=False)


    # Load and play movie
    movie_file = settings.movie_file
    logging.info(f"Starting movie: {os.path.basename(movie_file)}")
    movie = visual.MovieStim(win, filename=movie_file, size=win.size, flipVert=False, flipHoriz=False)

    movie_start = core.getTime()
    while movie.status != visual.FINISHED:
        movie.draw()
        win.flip()
        keys = event.getKeys()
        if 'escape' in keys:
            win.close()
            core.quit()
    movie_end = core.getTime()
    print("Movie time:", movie.getCurrentFrameTime())
    print("Wall time:", core.getTime())
    # Log viewing info
    df = pd.DataFrame([{
        "MovieName": os.path.basename(movie_file),
        "StartTime": movie_start,
        "EndTime": movie_end,
        "Duration": movie_end - movie_start
    }])
    df.to_csv(settings.outfile, index=False)

    with open(settings.outfile, 'a') as f:
        f.write('\n' + ','.join(subdata))

    logging.info("Movie presentation complete.")
