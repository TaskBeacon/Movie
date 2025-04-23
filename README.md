# Naturalistic Movie Task – PsyFlow Version

This task presents a short naturalistic video (e.g., *"presentch.mp4"*) to participants in a controlled environment while recording neural or behavioral responses (e.g., EEG, fMRI, or eye tracking). It is implemented using the [PsyFlow](https://taskbeacon.github.io/psyflow/) framework.



## Task Overview

Participants are instructed to watch a short film clip passively. During the video presentation, no user response is required. After the video ends, the task concludes with a thank-you screen.

This task is particularly useful for naturalistic paradigms where spontaneous brain activity or subjective responses are analyzed post hoc.



## Task Flow

| Step        | Description |
|-|-|
| Instruction | A textbox presents task instructions in Chinese. The participant presses the **space bar** to begin. |
| Movie       | The movie (`presentch.mp4`) is presented for **204 seconds**, with triggers sent at onset and offset. |
| Goodbye     | A textbox thanks the participant and prompts for exit via **space bar**. |



## Configuration Summary

All key settings are stored in the `config.yaml` file. Here's a breakdown of relevant sections:

### Subject Info (`subinfo_fields`)
Participants are registered with:
- **Subject ID** (3-digit number from 101–999)
- **Session name** (e.g., Practice, Experiment)
- **Experimenter name**
- **Gender** (Male or Female)

These fields are localized to Chinese via `subinfo_mapping`.



### Window Settings (`window`)
- Resolution: `1920 × 1080`
- Units: `deg`
- Fullscreen: `True`
- Monitor: `testMonitor`
- Background color: `black`



### Stimuli (`stimuli`)
| Stimulus       | Type   | Notes |
|-|-|-|
| `general_instruction` | `textbox` | Instruction screen in Chinese |
| `movie`        | `movie` | File: `./assets/presentch.mp4`, size: `[1152, 648]` |
| `good_bye`     | `textbox` | End message in Chinese |
| `fixation`     | `text` | Not used in current task, but available |



### Timing (`timing`)
- `movie_duration`: `204` seconds


### Triggers (`triggers`)
The following triggers are sent via `TriggerSender`:
- **Experiment**: `exp_onset = 98`, `exp_end = 99`
- **Block**: `block_onset = 100`, `block_end = 101`
- **Movie**: `movie_onset = 1`, `movie_offset = 2`

These are typically used for synchronizing EEG or fMRI recordings.



## Running the Task

1. Make sure all dependencies are installed (see below).
2. Place the movie file in `./assets/presentch.mp4`.
3. Launch the experiment via:

```bash
python main.py
