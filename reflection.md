# PawPal+ Project Reflection

## 1. System Design

- Add and manage pet care tasks, including duration and priority.
- Generate a daily care plan that fits available time and owner constraints.
- Review the schedule with clear task order and reasoning for choices.

**a. Initial design**

I designed four classes: Owner, Pet, Task, and Scheduler. Owner stores information about the pet owner and manages multiple pets. Pet stores information about an individual pet and its tasks. Task represents a specific pet care activity with scheduling information and completion status. Scheduler gathers tasks across multiple pets and provides sorting, filtering, and conflict detection functionality.

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

After reviewing the design with AI, I added duration_minutes to Task because it makes conflict detection more meaningful. I also added build_daily_schedule() to Scheduler to give the scheduler a clear planning role instead of only separate helper methods. I did not add every suggested method because I wanted to keep the design beginner-friendly and focused on the rubric.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
