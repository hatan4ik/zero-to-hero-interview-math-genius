#!/usr/bin/env python3
"""FAANG-style System Design Interview Simulator"""

import random
import time
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class InterviewQuestion:
    title: str
    company: str
    level: str
    time_limit: int  # minutes
    key_areas: List[str]
    scale: str

FAANG_QUESTIONS = [
    InterviewQuestion("Design Instagram", "Meta", "L5", 45, 
                     ["Image storage", "Feed generation", "Caching", "CDN"], "1B users"),
    InterviewQuestion("Design YouTube", "Google", "L5", 45,
                     ["Video processing", "Recommendations", "Global CDN", "Analytics"], "2B users"),
    InterviewQuestion("Design Uber", "Uber", "L6", 45,
                     ["Location services", "Matching algorithm", "Pricing", "Real-time tracking"], "100M rides/day"),
    InterviewQuestion("Design WhatsApp", "Meta", "L6", 45,
                     ["Message delivery", "Online presence", "Group chat", "End-to-end encryption"], "2B users"),
    InterviewQuestion("Design Netflix", "Netflix", "L6", 45,
                     ["Content delivery", "Recommendations", "Encoding pipeline", "Global scale"], "230M subscribers"),
]

class InterviewSimulator:
    def __init__(self):
        self.current_question = None
        self.start_time = None
        
    def start_interview(self, company_filter=None, level_filter=None):
        questions = FAANG_QUESTIONS
        if company_filter:
            questions = [q for q in questions if q.company == company_filter]
        if level_filter:
            questions = [q for q in questions if q.level == level_filter]
            
        self.current_question = random.choice(questions)
        self.start_time = time.time()
        
        print(f"\n🎯 FAANG System Design Interview")
        print(f"Company: {self.current_question.company}")
        print(f"Level: {self.current_question.level}")
        print(f"Time Limit: {self.current_question.time_limit} minutes")
        print(f"Scale: {self.current_question.scale}")
        print(f"\n📋 Question: {self.current_question.title}")
        print(f"\n🔑 Key Areas to Cover:")
        for area in self.current_question.key_areas:
            print(f"  • {area}")
        print(f"\n⏰ Timer started! Good luck!")
        
    def check_time(self):
        if not self.start_time:
            print("No interview in progress")
            return
            
        elapsed = (time.time() - self.start_time) / 60
        remaining = self.current_question.time_limit - elapsed
        
        if remaining > 0:
            print(f"⏱️  Time remaining: {remaining:.1f} minutes")
        else:
            print(f"⏰ Time's up! You went {abs(remaining):.1f} minutes over")
            
    def get_evaluation_framework(self):
        return """
🎯 FAANG System Design Evaluation (1-4 scale):

1. Requirements Clarification (5 min)
   - Asked about scale, users, features
   - Identified functional vs non-functional requirements
   - Clarified constraints and assumptions

2. Estimation (5 min)  
   - Calculated QPS, storage, bandwidth
   - Used reasonable assumptions
   - Showed mathematical thinking

3. High-Level Design (15 min)
   - Drew clear system architecture
   - Identified major components
   - Showed data flow

4. Deep Dive (15 min)
   - Detailed database design
   - API design
   - Addressed bottlenecks

5. Scale & Reliability (5 min)
   - Discussed scaling strategies
   - Addressed failure scenarios
   - Monitoring and alerting

Scoring:
4 = Exceeds expectations (hire)
3 = Meets expectations (hire)  
2 = Below expectations (no hire)
1 = Well below expectations (strong no hire)
        """

if __name__ == "__main__":
    simulator = InterviewSimulator()
    
    print("FAANG System Design Interview Simulator")
    print("Commands: start, time, eval, quit")
    
    while True:
        cmd = input("\n> ").strip().lower()
        
        if cmd == "start":
            simulator.start_interview()
        elif cmd == "time":
            simulator.check_time()
        elif cmd == "eval":
            print(simulator.get_evaluation_framework())
        elif cmd == "quit":
            break
        else:
            print("Unknown command. Try: start, time, eval, quit")