const SYSTEM_DATA = {
    "profile": {
        "current_role": "Candidate",
        "skills": [
            "Basic Math",
            "pytorch",
            "java",
            "git",
            "tensorflow",
            "sql",
            "python",
            "Python",
            "Git"
        ],
        "target_role": "Machine Learning Engineer",
        "roadmap": [
            {
                "phase": 1,
                "goal": "Urgent Foundational Reconstruction",
                "duration_months": 6.0,
                "milestones": [
                    "Intensive 0-to-1 Bootcamp: React, JavaScript, CSS",
                    "Pass fundamental assessments",
                    "Build 'Hello World' equivalent for each stack"
                ]
            },
            {
                "phase": 2,
                "goal": "Competency & Application",
                "duration_months": 2,
                "milestones": [
                    "Building Mini-Projects for: SQL, Git",
                    "Refactoring existing codebases",
                    "Contributing to relevant documentation"
                ]
            },
            {
                "phase": 3,
                "goal": "Capstone: Market Readiness",
                "duration_months": 2,
                "milestones": [
                    "Deploy full-stack portfolio project",
                    "Technical Interview Prep (System Design)",
                    "Outreach and networking"
                ]
            }
        ],
        "activity_log": [
            {
                "timestamp": "2025-12-30T20:24:08.974782",
                "agent": "ResumeAgent",
                "action": "Parse",
                "details": "Extracted 6 skills"
            },
            {
                "timestamp": "2025-12-30T20:24:08.977921",
                "agent": "PersonaAgent",
                "action": "Update",
                "details": "Target set to: Full Stack Developer"
            },
            {
                "timestamp": "2025-12-30T20:24:08.978841",
                "agent": "AssessmentAgent",
                "action": "Verify",
                "details": "Verified 9 skills"
            },
            {
                "timestamp": "2025-12-30T20:24:08.979255",
                "agent": "GapAnalysisAgent",
                "action": "Analyze",
                "details": "Found 6 gaps"
            },
            {
                "timestamp": "2025-12-30T20:24:08.991563",
                "agent": "PlannerAgent",
                "action": "Plan",
                "details": "Generated 3 phases"
            },
            {
                "timestamp": "2025-12-30T20:24:08.991879",
                "agent": "ExecutionAgent",
                "action": "Search",
                "details": "Found resources for Phase 1"
            },
            {
                "timestamp": "2025-12-30T20:24:08.992194",
                "agent": "ReviewAgent",
                "action": "Evaluate",
                "details": "Convergence Score: 0.23"
            }
        ],
        "convergence_score": 0.2333333333333333,
        "verified_skills": {
            "Basic Math": "Intermediate",
            "pytorch": "Basic",
            "java": "Advanced",
            "git": "Intermediate",
            "tensorflow": "Basic",
            "sql": "Intermediate",
            "Python": "Advanced",
            "python": "Advanced",
            "Git": "Advanced"
        },
        "gaps": [
            {
                "skill": "React",
                "skill_strength": 0.0,
                "required_level": 1.0,
                "gap_value": 1.0,
                "gap_type": "Critical Deficit",
                "severity": "High",
                "signals": []
            },
            {
                "skill": "JavaScript",
                "skill_strength": 0.0,
                "required_level": 1.0,
                "gap_value": 1.0,
                "gap_type": "Critical Deficit",
                "severity": "High",
                "signals": []
            },
            {
                "skill": "CSS",
                "skill_strength": 0.0,
                "required_level": 1.0,
                "gap_value": 1.0,
                "gap_type": "Critical Deficit",
                "severity": "High",
                "signals": []
            },
            {
                "skill": "Node.js",
                "skill_strength": 0.0,
                "required_level": 1.0,
                "gap_value": 1.0,
                "gap_type": "Critical Deficit",
                "severity": "High",
                "signals": []
            },
            {
                "skill": "SQL",
                "skill_strength": 0.6,
                "required_level": 1.0,
                "gap_value": 0.4,
                "gap_type": "Weak Foundation",
                "severity": "Medium",
                "signals": []
            },
            {
                "skill": "Git",
                "skill_strength": 0.6,
                "required_level": 1.0,
                "gap_value": 0.4,
                "gap_type": "Weak Foundation",
                "severity": "Medium",
                "signals": []
            }
        ],
        "resources": [
            {
                "milestone": "Intensive 0-to-1 Bootcamp: React, JavaScript, CSS",
                "resources": [
                    {
                        "type": "Course",
                        "title": "Advanced 0-to-1 Guide",
                        "url": "http://mooc.com/course"
                    },
                    {
                        "type": "Project",
                        "title": "Intensive 0-to-1 Bootcamp: React, JavaScript, CSS Practice Repo",
                        "url": "http://github.com/practice"
                    }
                ]
            },
            {
                "milestone": "Pass fundamental assessments",
                "resources": [
                    {
                        "type": "Course",
                        "title": "Advanced fundamental Guide",
                        "url": "http://mooc.com/course"
                    },
                    {
                        "type": "Project",
                        "title": "Pass fundamental assessments Practice Repo",
                        "url": "http://github.com/practice"
                    }
                ]
            },
            {
                "milestone": "Build 'Hello World' equivalent for each stack",
                "resources": [
                    {
                        "type": "Course",
                        "title": "Advanced 'Hello Guide",
                        "url": "http://mooc.com/course"
                    },
                    {
                        "type": "Project",
                        "title": "Build 'Hello World' equivalent for each stack Practice Repo",
                        "url": "http://github.com/practice"
                    }
                ]
            }
        ]
    },
    "roadmap": [
        {
            "phase": 1,
            "goal": "Urgent Foundational Reconstruction",
            "duration_months": 4.5,
            "milestones": [
                "Intensive 0-to-1 Bootcamp: Model Deployment, Scikit-learn, Statistics",
                "Pass fundamental assessments",
                "Build 'Hello World' equivalent for each stack"
            ]
        },
        {
            "phase": 2,
            "goal": "Competency & Application",
            "duration_months": 1,
            "milestones": [
                "Building Mini-Projects for: SQL",
                "Refactoring existing codebases",
                "Contributing to relevant documentation"
            ]
        },
        {
            "phase": 3,
            "goal": "System Optimization & Scaling",
            "duration_months": 3,
            "milestones": [
                "Production-grade deployment of: TensorFlow, Python",
                "Performance auditing and latency optimization",
                "Implementing CI/CD pipelines"
            ]
        },
        {
            "phase": 4,
            "goal": "Capstone: Market Readiness",
            "duration_months": 2,
            "milestones": [
                "Deploy full-stack portfolio project",
                "Technical Interview Prep (System Design)",
                "Outreach and networking"
            ]
        }
    ],
    "convergence": 0.39999999999999997,
    "verified_skills": {
        "Basic Math": "Intermediate",
        "pytorch": "Advanced",
        "java": "Basic",
        "git": "Intermediate",
        "tensorflow": "Intermediate",
        "sql": "Intermediate",
        "python": "Advanced",
        "Python": "Basic",
        "Git": "Intermediate"
    },
    "gaps": [
        {
            "skill": "Model Deployment",
            "skill_strength": 0.0,
            "required_level": 1.0,
            "gap_value": 1.0,
            "gap_type": "Critical Deficit",
            "severity": "High",
            "signals": []
        },
        {
            "skill": "Scikit-learn",
            "skill_strength": 0.0,
            "required_level": 1.0,
            "gap_value": 1.0,
            "gap_type": "Critical Deficit",
            "severity": "High",
            "signals": []
        },
        {
            "skill": "Statistics",
            "skill_strength": 0.0,
            "required_level": 1.0,
            "gap_value": 1.0,
            "gap_type": "Critical Deficit",
            "severity": "High",
            "signals": []
        },
        {
            "skill": "SQL",
            "skill_strength": 0.6,
            "required_level": 1.0,
            "gap_value": 0.4,
            "gap_type": "Weak Foundation",
            "severity": "Medium",
            "signals": []
        },
        {
            "skill": "TensorFlow",
            "skill_strength": 0.8,
            "required_level": 1.0,
            "gap_value": 0.2,
            "gap_type": "Refinement Needed",
            "severity": "Low",
            "signals": [
                "gan"
            ]
        },
        {
            "skill": "Python",
            "skill_strength": 0.9,
            "required_level": 1.0,
            "gap_value": 0.1,
            "gap_type": "Refinement Needed",
            "severity": "Low",
            "signals": []
        }
    ],
    "activity_log": [
        {
            "timestamp": "2025-12-30T20:24:23.472923",
            "agent": "ResumeAgent",
            "action": "Parse",
            "details": "Extracted 6 skills"
        },
        {
            "timestamp": "2025-12-30T20:24:23.475811",
            "agent": "PersonaAgent",
            "action": "Update",
            "details": "Target set to: Machine Learning Engineer"
        },
        {
            "timestamp": "2025-12-30T20:24:23.477917",
            "agent": "AssessmentAgent",
            "action": "Verify",
            "details": "Verified 9 skills"
        },
        {
            "timestamp": "2025-12-30T20:24:23.478363",
            "agent": "GapAnalysisAgent",
            "action": "Analyze",
            "details": "Found 6 gaps"
        },
        {
            "timestamp": "2025-12-30T20:24:23.490397",
            "agent": "PlannerAgent",
            "action": "Plan",
            "details": "Generated 4 phases"
        },
        {
            "timestamp": "2025-12-30T20:24:23.490712",
            "agent": "ExecutionAgent",
            "action": "Search",
            "details": "Found resources for Phase 1"
        },
        {
            "timestamp": "2025-12-30T20:24:23.491040",
            "agent": "ReviewAgent",
            "action": "Evaluate",
            "details": "Convergence Score: 0.40"
        }
    ],
    "resources": [
        {
            "milestone": "Intensive 0-to-1 Bootcamp: Model Deployment, Scikit-learn, Statistics",
            "resources": [
                {
                    "type": "Course",
                    "title": "Advanced 0-to-1 Guide",
                    "url": "http://mooc.com/course"
                },
                {
                    "type": "Project",
                    "title": "Intensive 0-to-1 Bootcamp: Model Deployment, Scikit-learn, Statistics Practice Repo",
                    "url": "http://github.com/practice"
                }
            ]
        },
        {
            "milestone": "Pass fundamental assessments",
            "resources": [
                {
                    "type": "Course",
                    "title": "Advanced fundamental Guide",
                    "url": "http://mooc.com/course"
                },
                {
                    "type": "Project",
                    "title": "Pass fundamental assessments Practice Repo",
                    "url": "http://github.com/practice"
                }
            ]
        },
        {
            "milestone": "Build 'Hello World' equivalent for each stack",
            "resources": [
                {
                    "type": "Course",
                    "title": "Advanced 'Hello Guide",
                    "url": "http://mooc.com/course"
                },
                {
                    "type": "Project",
                    "title": "Build 'Hello World' equivalent for each stack Practice Repo",
                    "url": "http://github.com/practice"
                }
            ]
        }
    ]
};