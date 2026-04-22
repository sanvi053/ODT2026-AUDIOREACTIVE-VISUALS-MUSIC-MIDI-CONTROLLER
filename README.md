# Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
Audio Reactive Music MIDI Controller 

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| Manasvi D. | Electronics and Coding  | Physical Presentation  | Circuit Building  |
| Sanvi T. | Software manipulation  | Creating initial testing versions  | Musical understanding ` |

## 1.3 Project Title
Audio Reactive Music MIDI Controller 

## 1.4 One-Line Pitch
A MIDI Controller made from scratch that can help you create music using looping tracks and then see it corresponding to audio reactive visuals.  `

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
Our project is an interactive music-making experience where users create and explore their own sound using a custom MIDI controller. They can switch between instruments, layer beats, and experiment with rhythms in an intuitive way, with no prior musical experience needed. The controller interfaces with Ableton Live, enabling real-time sound generation and flexible music creation. 

What makes it engaging is the instant audio-visual feedback: as users build their beats, their music is visualized in real time, making the process both satisfying and immersive. The project combines a custom MIDI controller, Ableton Live for music production, and TouchDesigner for dynamic visuals, blending physical interaction, sound, and visuals into a playful creative system. 

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
This project places the user in the role of a DJ or live music performer, where their beats are paired with dynamic, captivating visuals to create a mini concert experience. It builds an immersive and playful environment where users feel in control of their performance and creative output. The experience encourages them to return, experiment with new beats, and discover how each change transforms the visuals in real time. 

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
We are designing this project as if we were a small design studio making an interactive experience for exhibition visitors to experiment with.  

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| Ed Sheeran Looping Pedal Live performances.   | `[Link or title]` |Borrowed how he adds different tracks live to create a musical experience  |
|Live Audio-reactive visuals   | `[Link or title]` |The act of live music controlling visuals |

## 3.2 Original Twist
What makes your project original?

**Response:**  
Combining live sets with visuals is not a common concept, and we decided to make music looping more accessible to non-professional artists.  

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
Press instrument button → Press same button again to activate loop recording → Press the keynotes to create beat → Press another instrument [if you want to add] → Repeat same steps → Once done creating the beat, press instrument buttons to clear recorded beat 

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | Exhibition visitors  |
| Age range | 12+|
| Solo or multiplayer |Solo|
| Expected duration of one round |3-4min|
| What should the player feel? |Immersed, creative, accomplished |
| Is explanation required before use? |Yes|

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:**  The player begins in front of a dormant visual display, with a custom music control unit placed on the table. 
2. **Start:** The interaction begins by creating the first looping track.
3. **First Action:** The player selects instruments using dedicated buttons to activate individual tracks.
4. **Main Interaction:** Beats and melodies are built layer by layer, with each track looping continuously in real time.
5. **System Response:** The audio plays and evolves through loops while the visuals dynamically respond and adapt to the sound. 
6. **Win / Lose / End Condition:** The session concludes once the complete music composition is formed, and the visuals fully respond to the final output.
7. **Reset:** A new round begins by clearing all active loops, allowing the user to start a fresh composition. 

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `[Rule 1]`
- `[Rule 2]`
- `[Rule 3]`
- `[Rule 4]`

---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

Music track is completed and looping 
The visuals react to the music in real time 

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

One instrument track (ex. Piano) sends musical notes through buttons, and a basic visual reacts to them.  

## 5.3 Stretch Features
What features are nice to have but not essential?

Multiple instrument tracks (beyond the base instrument) 
Adding audio effects to beats created, i.e. reverb, delay, auto filter, etc. 
More advanced or detailed visual reactions in Touch Designer 
---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

Electronics-based 
Mechanical 
Sound-based 
Screen/UI-based 
Fabricated structure
Installation / tabletop experience 
Other: Audioreactive Visuals 

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
When the user presses a button on the physical controller, the input is detected through an ESP32 running MicroPython in Thonny, using a BLE Keyboard library. This input is sent as keyboard signals to the computer. In Ableton Live, each sound or function is mapped to specific keyboard keys, so the received input triggers the corresponding instrument or sound. 

The system works on a simple mapping flow: physical button → ESP32 → keyboard signal → Ableton Live → audio output. The result is real-time sound generation based on user interaction 

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
|ESP32 / Controller | Processing  |Transmits input messages to output components  |
|LED / Sound / Display | Output  |LED- loop recording indicator; Sound- created music track; Display- Visual presentation of music track | 
|Mechanical Assembly  |Physical Action |NA|
---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length |9 in.|
| Width |7 in. |
| Height |3 in.|
| Estimated weight |500 gm |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [ ] Linkages
- [ ] Hinges
- [ ] Shafts
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [ ] Sliders
- [ ] Levers
- [ ] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`[Write here]`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`[Write here]`

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `[Fusion 360 / Tinkercad / other]` | `[Link or screenshot]` | `[What did you validate?]` |
| `[Tool]` | `[Link or screenshot]` | `[What did you validate?]` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`[Write here]`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
|[ESP32] | 1 |Main controller|
|Push Button| 13 |Controlling the musical notes/beats and initiating/creating the loop|
|LED | 1 |Indicates if the loop recording has started|

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
Buttons are connected various pins on ESP-32 
LED Bulb connected to ESP32 

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source |USB|
| Voltage required |3V|
| Current concerns |Low power consumption overall, but unstable USB connections or insufficient power supply from some ports may cause intermittent disconnections of the ESP32. |
| Safety concerns |Accidentally soldering buttons incorrectly and damaging ESP-32 |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
|MicroPython Thonny |Thonny-Running Code and ESP32 |
|Ableton Live |MIDI controller outputs and instrumental track loop arrangement |
|Touchdesigner |Connecting music track components to visual manipulations |
|Adobe Illustrator |Used to create precise vector design files for laser cutting the MIDI controller setup|
|Rhino |Used to create precise vector design files for laser cutting the MIDI controller setup|

## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
The software logic governs how the controller initializes, processes user inputs, and communicates with external software such as Ableton Live and TouchDesigner. 

 

Startup Behavior: 
When the system is powered on, the ESP32 initializes all GPIO pins for input (buttons) and output (LEDs). The Bluetooth module is activated, and the device begins advertising itself as a wireless input controller. Default states are assigned to all buttons and LEDs to ensure no unintended signals are sent during initialization. 

 

Input Handling: 
The system continuously scans the state of each button using a loop. Each button is configured with a pull-up resistor, meaning a press is detected when the signal changes from HIGH to LOW. The current state is compared with the previous state to detect valid press events (edge detection), preventing repeated triggering while a button is held down. 

 

Decision Logic: 
Based on the detected input, the system determines the appropriate action. For example: 

A single button press triggers a specific key or command.  

Sequential presses (such as first press, second press) are tracked using state variables.  

Conditional logic is used to control LED behavior (e.g., blinking sequence, steady ON state). 
This ensures that each interaction produces a predictable and controlled response.  

 

Output Behavior: 
Outputs are handled in two ways: 

Digital Output (LEDs): LEDs provide visual feedback based on system state, such as blinking during active phases or remaining ON to indicate a stable state.  

Software Output (Input Signals): The ESP32 sends keyboard/MIDI-like signals via Bluetooth, which are received by Ableton Live to trigger sounds, loops, or effects.  

 

Communication Logic: 
The controller communicates wirelessly via Bluetooth Low Energy (BLE). Input signals are transmitted as keyboard or MIDI messages. Ableton Live processes these inputs to generate audio, which is then routed internally to TouchDesigner using virtual audio drivers. This enables synchronized audio-visual output. 

 

Reset Behavior: 
The system resets under two conditions: 

Manual reset (power cycle): All states return to default, and Bluetooth reconnects.  

Logical reset: Certain interaction sequences (e.g., repeated button cycles) reset LED patterns and input states to prevent unintended looping or stuck states.  

This ensures stable operation during continuous use. 

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
`[Upload image and link here]`

## 10.4 Pseudocode
INITIALIZE Bluetooth keyboard with name "ESPMIDIMS" 

  

INITIALIZE LED as OUTPUT 

  

INITIALIZE performance buttons (A–L) as INPUT with pull-up resistors 

STORE last state of each performance key as HIGH 

  

INITIALIZE 4 control buttons as INPUT with pull-up resistors 

STORE last state of each control button as HIGH 

SET control state of each button = 0 

  

DEFINE control actions as: 

    Button 1 → [q, n, m] 

    Button 2 → [r, 2, 3] 

    Button 3 → [i, 4, 5] 

    Button 4 → [b, 6, 7] 

  

PRINT "Controller Ready" 

  

  

FUNCTION blink_LED: 

    REPEAT 4 times: 

        TURN LED ON 

        WAIT 0.5 seconds 

        TURN LED OFF 

        WAIT 0.5 seconds 

    TURN LED ON (stay ON) 

  

  

LOOP forever: 

  

    IF Bluetooth is connected: 

  

        // ------------------------- 

        // PERFORMANCE KEYS 

        // ------------------------- 

        FOR each key in performance keys: 

  

            READ current state 

  

            IF key is PRESSED (LOW) AND last state was NOT PRESSED (HIGH): 

                SEND corresponding key via Bluetooth 

                WAIT 40 ms 

  

            UPDATE last state 

  

  

        // ------------------------- 

        // CONTROL BUTTONS 

        // ------------------------- 

        FOR each control button (index i): 

  

            READ current state 

  

            IF button is PRESSED (LOW) AND last state was HIGH: 

  

                WAIT 50 ms (debounce) 

  

                IF still PRESSED: 

  

                    IF control state == 1: 

                        CALL blink_LED 

  

                    SELECT action from CONTROL_ACTIONS using control state 

                    SEND action via Bluetooth 

  

                    UPDATE control state: 

                        (state = (state + 1) mod 3) 

  

                    PRINT which button and action sent 

  

                    WAIT 150 ms 

  

            UPDATE last control state 

  

    WAIT 20 ms

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [ ] Yes
- [ ] No

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`[Write here]`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[Bluetooth connect button]` | `[Purpose]` |
| `[Score display]` | `[Purpose]` |
| `[Control button / slider / label]` | `[Purpose]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Step 1]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `[ESP32]` | `1` | `Yes` | `No` | `0` | `[Spec]` | `[Reason]` |
|Push Buttons|13|No (not the kind we needed) |Yes|Rs. 400| Not producing click sound when pressed  |Smoother interaction than provided push buttons|
|LED Bulb |1|Yes|0| `[Spec]` | `[Reason]` |
|Jumper Wire|35|No|0| `[Spec]` | `[Reason]` |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
We chose MDF for the base structure because it is strong, stable, and cost-effective compared to 3D printing large parts. It is easier to laser cut for flat structural components and provides good rigidity to hold the electronics securely. 

We used push buttons instead of more complex input components like rotary encoders or touch sensors because they are simple, reliable, and provide clear tactile feedback, making the interaction more intuitive for users. 

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
|Push Buttons |Push Buttons  | NA (Nimesh Electronics)  |10th March |Received|


## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | Rs. 400|
| Mechanical parts |NA|
| Fabrication materials |NA|
| Purchased extras |NA|
| Contingency |Rs.150|
| **Total** |Rs.550|

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
NA

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
Team Working Strategy 

The project is executed through a collaborative approach where responsibilities are divided based on individual strengths, while still allowing overlap for support and flexibility. 

 

Task Division: 

Tasks are primarily divided according to expertise. Manasvi leads electronics and coding, focusing on circuit building and implementing the core logic. Sanvi leads software-related work, handling interaction with Ableton Live and TouchDesigner, along with initial testing and musical mapping. 

Both members support each other in secondary roles to ensure continuity and shared understanding of the system. 

 

Decision Making: 

Decisions are made collaboratively through discussion and testing. Ideas are evaluated based on functionality, user experience, and feasibility. In case of differing opinions, small prototypes or trials are created to test outcomes, and the most effective solution is selected. 

 

Progress Tracking: 

Progress is monitored through regular check-ins and testing sessions. Each module (electronics, coding, software integration) is tested individually and then combined to evaluate overall system performance. Milestones are set for key stages such as input detection, sound triggering, and audio-visual synchronization. 

 

Handling Delays: 

If a task is delayed, responsibilities are adjusted temporarily. The support owner assists in completing the pending task to maintain workflow continuity. Simpler alternatives or workarounds are also considered to avoid blocking the overall progress of the project. 

 

Documentation Maintenance: 

Documentation is primarily managed by Sanvi, with support from Manasvi. All stages of the project, including concept development, circuit design, code logic, and testing outcomes, are recorded regularly. Updates are made alongside development to ensure accuracy and completeness, rather than being compiled at the end. 

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `[Finalize concept]` | `[Name]` | `2` | `[Date]` | `None` | `To Do` |
| T2 | `[Complete BOM]` | `[Name]` | `1` | `[Date]` | `T1` | `To Do` |
| T3 | `[Test electronics]` | `[Name]` | `2` | `[Date]` | `T1` | `To Do` |
| T4 | `[Build structure]` | `[Name]` | `4` | `[Date]` | `T1` | `To Do` |
| T5 | `[Write control code]` | `[Name]` | `4` | `[Date]` | `T3` | `To Do` |
| T6 | `[Integrate system]` | `[Name]` | `4` | `[Date]` | `T4, T5` | `To Do` |
| T7 | `[Playtest]` | `[Name]` | `2` | `[Date]` | `T6` | `To Do` |
| T8 | `[Refine and document]` | `[Name]` | `3` | `[Date]` | `T7` | `To Do` |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | Sanvi |Manasvi |
| Electronics |Manasvi |Sanvi |
| Coding |Manasvi |Sanvi |
| Software (Ableton Live & Touchdesigner) |Sanvi| Manasvi|
| Testing |Both|Both |
| Documentation |Sanvi  |Manasvi |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [ ] Idea finalized
- [ ] Core interaction decided
- [ ] Sketches made
- [ ] BOM completed
- [ ] Purchase needs identified
- [ ] Key uncertainty identified
- [ ] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [ ] Electronics tests completed
- [ ] CAD / structure planning completed
- [ ] App UI started if needed
- [ ] Mechanical concept tested
- [ ] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [ ] Physical body built
- [ ] Electronics integrated
- [ ] Code connected to hardware
- [ ] App connected if required
- [ ] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [ ] Technical bugs reduced
- [ ] Playtesting completed
- [ ] Improvements made
- [ ] Documentation completed
- [ ] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 2 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 3 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 4 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `[Example: Bluetooth disconnects]` | `Technical` | `Medium` | `High` | `[Fallback interaction / simplify connection flow]` | `[Name]` |
| `[Example: Structure breaks during play]` | `Mechanical` | `Medium` | `High` | `[Reinforce joints / change material]` | `[Name]` |
| `[Risk]` | `[Technical / Material / Time / Gameplay]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |
| `[Risk]` | `[Type]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`[Write here]`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `[Bluetooth connection]` | `[Method]` | `[What counts as success?]` |
| `[Mechanism movement]` | `[Method]` | `[What counts as success?]` |
| `[Sensor behavior]` | `[Method]` | `[What counts as success?]` |
| `[App communication]` | `[Method]` | `[What counts as success?]` |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `[Method]` |
| Is the interaction satisfying? | `[Method]` |
| Do players want another turn? | `[Method]` |
| Is the challenge balanced? | `[Method]` |
| Is the response clear and immediate? | `[Method]` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `[Date]` | `[Describe issue]` | `[Technical / Mechanical / UI / Gameplay]` | `[What you did]` | `[Worked / Partly / Failed]` | `[Next step]` |
| `[Date]` | `[Describe issue]` | `[Type]` | `[What you did]` | `[Result]` | `[Next step]` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`[Write here]`

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.

Example:
```md



```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | `[Date]` | `[Describe]` | `[Reason]` |
| `v2` | `[Date]` | `[Describe]` | `[Reason]` |
| `v3` | `[Date]` | `[Describe]` | `[Reason]` |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[Write here]`

## 18.2 What Works Well
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.3 What Still Needs Improvement
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[Write here]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[Write here]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Write here]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[Write here]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[Write here]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [ ] Team details are complete
- [ ] Project description is complete
- [ ] Inspiration sources are included
- [ ] Player journey is written
- [ ] Sketches are added
- [ ] BOM is complete
- [ ] Purchase list is complete
- [ ] Budget summary is complete
- [ ] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [ ] Code flowchart is added
- [ ] Task breakdown is complete
- [ ] Weekly logs are updated
- [ ] Risk register is complete
- [ ] Testing log is updated
- [ ] Playtesting notes are included
- [ ] Build photos are included
- [ ] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
