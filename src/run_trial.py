from psyflow import StimUnit
from functools import partial

def run_trial(win, kb, settings, condition, stim_bank, trigger_sender):

    trial_data = {"condition": condition}
    make_unit = partial(StimUnit, win=win, kb=kb, triggersender=trigger_sender)

    make_unit(unit_label='movie').add_stim(stim_bank.get("movie")) \
        .show(duration=settings.movie_duration, 
              onset_trigger=settings.triggers.get("movie_onset"),
              offset_trigger=settings.triggers.get("movie_offset")) \
        .to_dict(trial_data)


    return trial_data

