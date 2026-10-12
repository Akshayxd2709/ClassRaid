# ClassRaid
A co-op classroom boss battle for any syllabus topic. Students answer together, each answer links to the BIS standard behind it. Live teacher heatmap, auto peer-matching, rematch on weak topics. Python + Flask + SocketIO. MISSION'26, VIT Chennai.
<h1 align="center">⚔️ ClassRaid</h1>
<p align="center"><b>The whole class vs the Boss. Learn the standards that keep you safe.</b></p>
<p align="center">
<img src="https://img.shields.io/badge/Python-3.x-blue">
<img src="https://img.shields.io/badge/Flask-SocketIO-green">
<img src="https://img.shields.io/badge/Theme-Smart%20Education-purple">
<img src="https://img.shields.io/badge/BIS-Standards%20Linked-orange">
<img src="https://img.shields.io/badge/MISSION'26-VIT%20Chennai-red">
</p>

---

##  The Problem
- A teacher asks *"any doubts?"* and gets silence. They only find out who was lost **after the exam**, when it's too late.
- Weak students stay quiet, strong students sit idle, and nobody connects the two.
- Students use helmets, chargers and pressure cookers every day, yet the **BIS standards** behind them stay buried in dense documents.

##  Our Solution
**ClassRaid turns any syllabus topic into a live co-op boss battle.**

The teacher picks a topic they just taught. Every student joins on their phone. A boss appears with a health bar:

-  Correct answer → damages the **Boss**
-  Wrong answer → costs the student **HP**
-  Class reaches 70% accuracy → **Boss defeated**
-  Boss survives → **rematch on only the missed topics**

Every answer shows an instant **"why"** with the **BIS standard** behind the concept.

##  What Makes It Different
- **Co-op, not a race:** the whole class fights one Boss together, so weak students aren't left behind on a leaderboard.
- **Auto peer-matching:** struggling students are paired with a classmate who mastered the topic.
- **Live teacher heatmap:** the teacher sees who is stuck during the session, not after the exam.
- **Any syllabus topic:** built-in BIS packs, plus the teacher's own questions.
- **Rematch on weak topics only:** a loss turns into targeted practice.
- **Works offline:** runs on a local hotspot, no internet needed.

##  How Peer-Matching Works
1. The server tracks every student's score **per topic**.
2. A score below 40% on a topic flags the student as *needs help*.
3. The strongest available student on that topic (70%+) is paired with them.
4. Both phones show: *"Ravi, explain helmet safety marks to Priya."*

No AI guesswork. Simple rules, and every decision is explainable.

##  BIS Integration
Each question carries a `bis_ref` linking the concept to its Indian Standard, for example:
- Applied Chemistry → drinking water quality
- Safety products → helmets, pressure cookers, chargers
- Software → software quality standards

##  Tech Stack
Python · Flask · Flask-SocketIO (WebSockets) · HTML/CSS/JS · JSON question bank

##  Run It
```bash
git clone https://github.com/Akshayxd2709/ClassRaid.git
cd ClassRaid
pip install -r requirements.txt
python app.py
```
Open the teacher page on your laptop, and students join from their phones on the same hotspot.

##  Team
-CtrlC CtrlV

## Team members
-Kanishka S
-Akshay bharath M
-Sai Atish S
-Sameeha
-Arun 
-Shivasubramaniam RM

##  Built For
**MISSION'26 · 8-Hour Hackathon · SCOPE, VIT Chennai** · Theme: Smart Education × BIS Standards
