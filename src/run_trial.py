from psyflow import TrialUnit
from functools import partial

def run_trial(win, kb, settings, condition, stim_bank, trigger_sender, trigger_bank):
    """
    Run a single MID trial sequence (fixation → cue → anticipation → target → feedback).
    See full docstring above...
    """

    trial_data = {"condition": condition}
    make_unit = partial(TrialUnit, win=win, triggersender=trigger_sender)

    make_unit(unit_label='movie').add_stim(stim_bank.get("movie")) \
        .show(duration=settings.movie_duration, onset_trigger=trigger_bank.get("movie_onset")) \
        .to_dict(trial_data)


    return trial_data

