# Tech Stack Evaluation

## Project
[Morse Code Based Eye Blink]

## Functional Requirements
- FR1 — Eye Blink Detection: The system must detect eye blinks from a standard webcam and distinguish short blinks (dots) from long blinks (dashes).
- FR2 — Learning and Feedback: The system must provide Morse code lessons, practice exercises, and feedback to help users learn selected Morse code letters and numbers.
- FR3 — Progress Tracking: The system should display users' practice results so they can monitor their learning progress.


- NFR1 — Performance: The system should process blink inputs with minimal delay so users can practise comfortably.

- NFR2 — Cost and Accessibility: The system should work with a standard webcam and avoid requiring specialised hardware or expensive software.

## Options
- Option A: [for example: static website (HTML and JavaScript) on GitHub Pages]
- Option B: [for example: Python web app (Flask) with a database on a cloud host]
- Option C: [your own idea]

## Decision matrix
Weight: how important the criterion is for YOUR project (1 = low, 5 = high).
Score: how well each option does (1 = poor, 5 = excellent).
Weighted score = weight x score. Add them up for each option.

| Criterion                          | Weight | A score | B score | C score |
|------------------------------------|--------|---------|---------|---------|
| Fits my requirements               |        |         |         |         |
| Skills I already have              |        |         |         |         |
| Time to build before my deadline   |        |         |         |         |
| Free hosting and tools             |        |         |         |         |
| Performance and security needs     |        |         |         |         |
| Room to grow later                 |        |         |         |         |
| **Total (weighted)**               |        |         |         |         |

## Decision record
- **Context:** The project requires webcam-based eye blink detection, Morse code learning activities, immediate feedback and progress tracking. The selected technology stack should support computer vision while remaining affordable and manageable for a student project.

- **Decision:** Option A, using Python, OpenCV, MediaPipe, Flask, and SQLite, is the preferred technology stack based on the preliminary weighted scoring matrix.

- **Reasons:** Python supports computer vision development through OpenCV and MediaPipe. Flask can provide the web interface and connect the learning activities to the application's processing logic. SQLite provides a simple way to store learning progress without requiring a separate database server. The stack also allows the eye blink detection and learning components to be developed and tested separately.

- **Consequences:** The project can use a familiar Python development environment and a lightweight database. However, integrating webcam access with a Flask-based web interface requires additional work, including browser camera permissions and transferring or processing video frames.

- **Risks and next review:** Blink detection may be affected by lighting conditions, camera quality, head movement, and differences between users. The system must be tested with different users and environments. The webcam integration and response time should also be tested before finalising the architecture.
