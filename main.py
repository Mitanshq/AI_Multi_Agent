from planner import get_tasks
from router import route_tasks
from research_agent import get_response
from memory import Memory
from websearch import wiki_search
from synthesizer import synthesizer
from calc import calci

memory = Memory()

print("Enter Message (exit/e to quit)")

msg = input('You: ')

run = True

while run:
    if msg == 'exit' or msg == 'e':
        run = False
    else:
        tasks = get_tasks(msg)
        for _, task in tasks.items():
            print(repr(task))
            agent = route_tasks(task)
            
            if agent == 'research':
                # print('gemini')
                res = get_response(task)
                memory.save_memory(agent, res)
            elif agent == 'tool':
                # print('tool')
                res = wiki_search(task)
                memory.save_memory(agent, res)
            elif agent == 'calc':
                # print('calci')
                res = calci(task)
                memory.save_memory(agent, res)
            elif agent == 'unknown':
                print("No such Route!")  
                
        final_answer = synthesizer(memory.get_all())
        print("final: ")
        print(final_answer)
        run = False