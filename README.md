# Movie Watching Task

| Field                | Value                        |
|----------------------|------------------------------|
| Name                 | Movie Watching Task |
| Version              | main (1.0)                          |
| URL / Repository     | https://github.com/TaskBeacon/Movie |
| Short Description    | A passive video-watching task with a centered movie clip for EEG studies |
| Created By           |Zhipeng Cao (zhipeng30@foxmail.com) |
| Date Updated         |2025/06/23   |
| PsyFlow Version      | 0.1.0       |
| PsychoPy Version     |2025.1.1     |
| Modality             | EEG         |

```{note}
The movie is not publicly available due to potential copyright issues.
```

## 1. Task Overview

The Movie Presentation Task is a naturalistic EEG paradigm where participants passively watch a centered movie clip on screen. Unlike full-screen video presentations, the movie is rendered at a fixed visual size while the background remains visible. This format preserves spatial context and minimizes abrupt visual transitions, supporting naturalistic stimulus presentation for continuous EEG data acquisition. No behavioral responses are required; only onset and offset triggers are logged for synchronization.

## 2. Task Flow

### Block-Level Flow

| Step                       | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| Load Config                | Load YAML-based task settings for subject info, stimuli, window, triggers   |
| Collect Subject Info       | Prompt for subject ID, name, age, and gender                                |
| Setup Triggers             | Configure serial trigger output via `loop://` or COM                        |
| Initialize Window/Input    | Create full-screen PsychoPy window and keyboard                            |
| Load Stimuli               | Load instructions and centered movie video; convert to voice               |
| Show Instructions          | Present visual and audio instructions; wait for spacebar                   |
| Countdown                  | Display a 3-second countdown before video starts                            |
| Movie Playback             | Show centered video stimulus with triggers on start and end                |
| Show Goodbye               | Display thank-you screen                                                    |
| Save Data                  | Save trial metadata in CSV format                                           |
| Close                      | Close serial port and PsychoPy session                                      |

### Trial-Level Flow

| Step             | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| Movie Presentation | Show `presentch.mp4` (22.1 × 12.4 deg) centered on screen for 204 seconds |
| Trigger Onset    | Send EEG trigger at video start (`movie_onset = 1`)                        |
| Trigger Offset   | Send EEG trigger at video end (`movie_offset = 2`)                         |
| Trial Logging    | Save trial condition, duration, and triggers                                |

### Other Logic

| Component         | Description                                                        |
|-------------------|--------------------------------------------------------------------|
| None              | No adaptive logic, dynamic trial structure, or stimulus randomization present |

This task is entirely passive and fixed across all participants.

## 3. Configuration Summary

### a. Subject Info

| Field       | Meaning                        |
|-------------|--------------------------------|
| subject_id  | Participant ID (101–999)       |
| subname     | Participant name (pinyin)      |
| age         | Age (5–60)                     |
| gender      | Gender (Male/Female)           |

### b. Window Settings

| Parameter             | Value         |
|-----------------------|---------------|
| size                  | [1920, 1080]  |
| units                 | deg           |
| screen                | 1             |
| bg_color              | black         |
| fullscreen            | True          |
| monitor_width_cm      | 60            |
| monitor_distance_cm   | 72            |

### c. Stimuli

| Name             | Type     | Description                                                     |
|------------------|----------|-----------------------------------------------------------------|
| movie            | movie    | `presentch.mp4`, centered at 22.1 × 12.4 deg (not full-screen)  |
| instruction_text | textbox  | Pre-task guidance with keypress to continue                     |
| good_bye         | textbox  | End-of-task thank-you message                                   |
| fixation         | text     | Central fixation (not used during movie playback)               |

### d. Timing

| Phase           | Duration (s) |
|------------------|--------------|
| movie            | 204          |

### e. Triggers

| Event           | Code |
|------------------|------|
| Experiment Start | 98   |
| Experiment End   | 99   |
| Block Start      | 100  |
| Block End        | 101  |
| Movie Onset      | 1    |
| Movie Offset     | 2    |

## 4. Methods

Participants engaged in a passive viewing task, during which they watched a 204-second movie clip (`The present`) presented at the center of the screen within a fixed visual angle (22.1 × 12.4 degrees). While the display window occupied the full screen, the movie itself was embedded within it rather than scaled to full-screen size. This design allows for reduced visual noise and stable peripheral context. Participants were instructed to remain still, focus on the screen, and minimize eye movements and blinking. No responses were required during the video. A trigger was sent at the start (`movie_onset`) and end (`movie_offset`) of the movie to synchronize EEG data collection. The experiment consisted of one block and one trial. 

## 5. References
>Alexander, L. M., Escalera, J., Ai, L., Andreotti, C., Febre, K., Mangone, A., ... & Milham, M. P. (2017). An open resource for transdiagnostic research in pediatric mental health and learning disorders. Scientific data, 4(1), 1-26.

>Shirazi, S. Y., Franco, A., Scopel Hoffmann, M., Esper, N. B., Truong, D., Delorme, A., ... & Makeig, S. (2024). HBN-EEG: The FAIR implementation of the Healthy Brain Network (HBN) electroencephalography dataset. bioRxiv, 2024-10.