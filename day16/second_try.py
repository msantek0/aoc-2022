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

def visit(tunnel, second_tunnel,  parent, second_parent):  
    global queue, flow_rate, maxed_pressure
    if parent.prev and parent.prev.name == tunnel: return
    if parent.prev and parent.prev.name == second_tunnel: return
    if parent.steps > 8 and parent.pressure < maxed_pressure: return
    if second_parent.steps > 8 and second_parent.pressure < maxed_pressure: return
    if parent.steps < 26 and second_parent.steps < 26:
        new_union = parent.opened_on_path.union(second_parent.opened_on_path)
        queue.append([Tunnel(tunnel, parent.pressure, parent, parent.steps + 1, False, new_union), 
        Tunnel(second_tunnel, second_parent.pressure, second_parent, second_parent.steps + 1, False, new_union)])
    if flow_rate[tunnel] > 0:
        if parent.steps < 25 and second_parent.steps < 26:
            if tunnel in parent.opened_on_path: return
            if tunnel in second_parent.opened_on_path: return
            arr = parent.opened_on_path.union(second_parent.opened_on_path)
            arr.add(tunnel)
            tmp_pressure = parent.pressure + flow_rate[tunnel]*(24-parent.steps)
            if tmp_pressure > maxed_pressure:
                maxed_pressure = tmp_pressure
            queue.append([Tunnel(tunnel, tmp_pressure, parent, parent.steps + 2, True, arr), 
            Tunnel(second_tunnel, second_parent.pressure, second_parent, second_parent.steps + 1, False, arr)])
            visited.append([Tunnel(tunnel, tmp_pressure, parent, parent.steps + 2, True, arr), 
            Tunnel(second_tunnel, second_parent.pressure, second_parent, second_parent.steps + 1, False, arr)])
    if flow_rate[second_tunnel] > 0:
        if parent.steps < 26 and second_parent.steps < 25:
            if second_tunnel in parent.opened_on_path: return
            if second_tunnel in second_parent.opened_on_path: return
            arr = parent.opened_on_path.union(second_parent.opened_on_path)
            arr.add(tunnel)
            tmp_pres_ele = second_parent.pressure + flow_rate[second_tunnel]*(24-second_parent.steps)
            if tmp_pres_ele > maxed_pressure:
                maxed_pressure = tmp_pres_ele
            queue.append([Tunnel(tunnel, parent.pressure, parent, parent.steps + 1, False, arr), 
            Tunnel(second_tunnel, tmp_pres_ele, second_parent, second_parent.steps + 2, True, arr)])
            visited.append([Tunnel(tunnel, parent.pressure, parent, parent.steps + 1, False, arr), 
            Tunnel(second_tunnel, tmp_pres_ele, second_parent, second_parent.steps + 2, True, arr)])
    

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


queue.append([Tunnel('AA', flow_rate['AA'], None, 0, False, set()), Tunnel('AA', flow_rate['AA'], None, 0, False, set())])
p, q = queue.pop(0)
cnt = 0
while p != None and q != None:
    cnt += 1
    print(p.steps)
    tmp = leads_to[p.name]
    for tunnel in leads_to[p.name]:
        for second_tunnel in leads_to[q.name]:
            visit(tunnel, second_tunnel, p, q)
    print("IDE:", len(queue))
    print("----------")
    #for q in queue:
    #    print("Name:", q.name)
    #    print("Pressure:", q.pressure)
    #    print("Steps:", q.steps)

    p = None
    q = None
    if len(queue) > 0:
        p, q = queue.pop(0)

max_pressure = [0, 0]
najveci = [None, None]
for i in visited:
    if i[0].pressure > max_pressure[0]:
        max_pressure[0] = i[0].pressure
        najveci[0] = i[0]
    if i[1].pressure > max_pressure[1]:
        max_pressure[1] = i[1].pressure
        najveci[1] = i[1]
print(max_pressure[0])
print(max_pressure[1])
print(max_pressure[1] + max_pressure[0])
print("Printam array ovaj prvo", najveci[0].opened_on_path)
print("Printam array ovaj prvo", najveci[1].opened_on_path)
print("Krecemo:")
n = najveci[0]
while n != None:
    print(n.open, ":", n.name, end="<-")
    n = n.prev
print()

n = najveci[1]
while n != None:
    print(n.open, ":", n.name, end="<-")
    n = n.prev
print()

print("A mi smo dobili:", maxed_pressure)
