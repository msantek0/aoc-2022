filename = "input.txt"

class Tunnel:
    def __init__(self, name, presure, prev, steps, open, opened_on_path) :
        self.name = name
        self.prev = prev
        self.pressure = presure; 
        self.steps = steps; 
        self.open = open
        self.opened_on_path = opened_on_path
    def __str__(self):
        return  self.prev + "->" + self.name

leads_to = dict()
flow_rate = dict()
queue = []
visited = []
maxed_pressure = 0

def visit(tunnel, parent):  
    global queue, flow_rate, maxed_pressure
    if parent.prev and parent.prev.name == tunnel: return
    if parent.steps > 10 and parent.pressure < maxed_pressure: return
    if parent.steps < 30:
        queue.append(Tunnel(tunnel, parent.pressure, parent, parent.steps + 1, False, parent.opened_on_path[:]))
    if flow_rate[tunnel] > 0:
        if parent.steps < 29:
            if tunnel in parent.opened_on_path: return
            arr = parent.opened_on_path[:]
            arr.append(tunnel)
            tmp_pressure = parent.pressure + flow_rate[tunnel]*(28-parent.steps)
            if tmp_pressure > maxed_pressure:
                maxed_pressure = tmp_pressure
            queue.append(Tunnel(tunnel, tmp_pressure, parent, parent.steps + 2, True, arr))
            visited.append(Tunnel(tunnel, tmp_pressure, parent, parent.steps + 2, True, arr))


with open(filename) as file:

    for line in file:
        row = line.rstrip().split(" ")
        tunnel = row[1]
        flow_rate[tunnel] = int(row[4].split("=")[1][:-1])
        tunnels = row[9:]
        tmp = []
        for i in range(len(tunnels)-1):
            tmp.append(tunnels[i][:-1])
        tmp.append(tunnels[-1])
        leads_to[tunnel] = tmp

print(leads_to)
print(flow_rate)


queue.append(Tunnel('AA', flow_rate['AA'], None, 0, False, []))
p = queue.pop(0)
cnt = 0
while p != None:
    cnt += 1
    print(p.steps)
    for tunnel in leads_to[p.name]:
        visit(tunnel, p)
    print("IDE:", len(queue))
    print("----------")
    #for q in queue:
    #    print("Name:", q.name)
    #    print("Pressure:", q.pressure)
    #    print("Steps:", q.steps)

    p = None
    if len(queue) > 0:
        p = queue.pop(0)

max_pressure = 0
najveci = None
for i in visited:
    if i.pressure > max_pressure:
        max_pressure = i.pressure
        najveci = i
print(max_pressure)
print("Printam array ovaj prvo", najveci.opened_on_path)
print("Krecemo:")
while najveci != None:
    print(najveci.open, ":", najveci.name, end="<-")
    najveci = najveci.prev


print("A mi smo dobili:", maxed_pressure)