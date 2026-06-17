import re
research_keywords = [
    "research",
    "find",
    "analyze",
    "identify",
    "summarize",
    'importance',
    'give',
    'statistics',
    'stats',
    'analyse',
    'analyze',
]

tool_keywords = [
    "search",
    "retrieve",
    "read",
    'explain',
    'tell'
]

calc_keywords = ['calculate', 'calc', 'calculation',]


def route_tasks(task_ip):
    task = re.sub(r'[^\w\s]', '', task_ip.lower()).split()

    if any(word in research_keywords for word in task):
        return 'research'

    elif any(word in tool_keywords for word in task):
        return 'tool'
    
    elif any(word in calc_keywords for word in task):
        return 'calc'


    return 'unknown'