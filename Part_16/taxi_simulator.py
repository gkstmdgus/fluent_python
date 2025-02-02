import random
import collections
import queue
import argparse
import time

Event = collections.namedtuple("Event", "time proc action")

DEFAULT_NUMBER_OF_TAXIS = 3
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 20
DEPARTURE_INTERVAL = 5

# TAXI_PROCESS 시작 
def taxi_process(ident, trips, start_time=0):
    """각 상태 변화마다 이벤트를 발생시키는 시뮬레이터에 양보한다."""
    time = yield Event(start_time, ident, 'leave garage')
    for _ in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')
    yield Event(time, ident, 'going home')

# TAXI_SIMULATOR 시작 
class Simulator:
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)
    
    def run(self, end_time):
        """시간이 만료될 때까지 이벤트를 스케줄링하고 출력한다."""
        # 각 택시마다 첫 번째 이벤트를 스케줄링하고 출력한다. 
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)
        
        # 시뮬레이션 메인 루프 
        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of evenets ***')
                break
            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print("taxi:", proc_id, proc_id * "    ", current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            print(f'*** end of simulation time: {self.events.qsize()} events pending ***')

def compute_duration(previous_action):
    """지수 분포를 이용해서 행동 기간을 계산한다."""
    if previous_action in ['leave garage', 'drop off passenger']:
        interval = SEARCH_DURATION
    elif previous_action == "pick up passenger":
        interval = TRIP_DURATION
    elif previous_action == "going home":
        interval = 1
    else:
        raise ValueError(f"Unknown previous_action: {previous_action}")
    return int(random.expovariate(1/interval)) + 1

def main(end_time=DEFAULT_END_TIME, num_taxis=DEFAULT_NUMBER_OF_TAXIS, seed=None):
    """난수 생성 초기화"""
    if seed is not None:
        random.seed(seed)
    
    taxis = {i: taxi_process(i, (i+1)*2, i*DEPARTURE_INTERVAL) for i in range(num_taxis)}
    sim = Simulator(taxis)
    sim.run(end_time)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Taxi fleet simulator."
    )
    parser.add_argument('-e', '--end-time', type=int, default=DEFAULT_END_TIME, 
                        help=f'simulation end time; default: {DEFAULT_END_TIME}')
    parser.add_argument('-t', '--taxis', type=int, default=DEFAULT_NUMBER_OF_TAXIS,
                        help=f'number of taxis running; default: {DEFAULT_NUMBER_OF_TAXIS}')
    parser.add_argument('-s', '--seed', type=int, default=None,
                        help='random generator seed (for testing)')
    args = parser.parse_args()
    main(args.end_time, args.taxis, args.seed)
    