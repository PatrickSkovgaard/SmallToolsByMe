a_commands = []
b_commands = []
c_commands = []
d_commands = []
e_commands = []
f_commands = []
g_commands = []
h_commands = []
i_commands = []
j_commands = []
k_commands = []
l_commands = []
m_commands = []
n_commands = []
o_commands = []
p_commands = []
q_commands = []
r_commands = []
s_commands = []
t_commands = []
u_commands = []
v_commands = []
w_commands = []
x_commands = []
y_commands = []
z_commands = []


def initalizer():

  for i in open(file="bash-command_files/txt_files/a-z_bash.txt", mode="r").readlines():
    if i.startswith("a"):
      a_commands.append(i.split(" ")[0])
    if i.startswith("b"):
      b_commands.append(i.split(" ")[0])
    if i.startswith("c"):
      c_commands.append(i.split(" ")[0])
    if i.startswith("d"):
      d_commands.append(i.split(" ")[0])
    if i.startswith("e"):
      e_commands.append(i.split(" ")[0])
    if i.startswith("f"):
      f_commands.append(i.split(" ")[0])
    if i.startswith("g"):
      g_commands.append(i.split(" ")[0])
    if i.startswith("h"):
      h_commands.append(i.split(" ")[0])
    if i.startswith("i"):
      i_commands.append(i.split(" ")[0])
    if i.startswith("j"):
      j_commands.append(i.split(" ")[0])
    if i.startswith("k"):
      k_commands.append(i.split(" ")[0])
    if i.startswith("l"):
      l_commands.append(i.split(" ")[0])
    if i.startswith("m"):
      m_commands.append(i.split(" ")[0])
    if i.startswith("n"):
      n_commands.append(i.split(" ")[0])
    if i.startswith("o"):
      o_commands.append(i.split(" ")[0])
    if i.startswith("p"):
      p_commands.append(i.split(" ")[0])
    if i.startswith("q"):
      q_commands.append(i.split(" ")[0])
    if i.startswith("r"):
      r_commands.append(i.split(" ")[0])
    if i.startswith("s"):
      s_commands.append(i.split(" ")[0])
    if i.startswith("t"):
      t_commands.append(i.split(" ")[0])
    if i.startswith("u"):
      u_commands.append(i.split(" ")[0])
    if i.startswith("v"):
      v_commands.append(i.split(" ")[0])
    if i.startswith("w"):
      w_commands.append(i.split(" ")[0])
    if i.startswith("x"):
      x_commands.append(i.split(" ")[0])
    if i.startswith("y"):
      y_commands.append(i.split(" ")[0])
    if i.startswith("z"):
      z_commands.append(i.split(" ")[0])



def search_commands():
  
  #command_dict = {"a": a_commands,"b": b_commands, "c": c_commands, "d": d_commands, "e": e_commands, "f": f_commands, "g": g_commands, "h": h_commands, "i": i_commands, "j": j_commands, "k": k_commands, "l": l_commands, "m": m_commands, "n": n_commands, "o": o_commands, "p": p_commands, "q": q_commands, "r": r_commands, "s": s_commands, "t": t_commands, "u": u_commands, "v": v_commands, "w": w_commands, "x": x_commands, "y": y_commands, "z": z_commands }
  len_dict = {"a": len(a_commands), "b": len(b_commands), "c": len(c_commands), "d": len(d_commands), "e": len(e_commands), "f": len(f_commands), "g": len(g_commands), "h": len(h_commands), "i": len(i_commands), "j": len(j_commands), "k": len(k_commands), "l": len(l_commands), "m": len(m_commands), "n": len(n_commands), "o": len(o_commands), "p": len(p_commands), "q": len(q_commands), "r": len(r_commands), "s": len(s_commands), "t": len(t_commands), "u": len(u_commands), "v": len(v_commands), "w": len(w_commands), "x": len(x_commands), "y": len(y_commands), "z": len(z_commands)}

  choice = input("Choose a letter to search for a command\n")
  choice = choice.lower()
  print("")

  num = 0

  if len(choice) != 1 or choice.isalpha() == False:
    print("bcfind.py: ERROR: Incorrect input. One-letter options only!")
    
  else:
    for l in open("bash-command_files/txt_files/cmd_list.txt", "r").readlines():
        if l.startswith("['" + choice):
          while(num < len_dict.get(choice)):  # type: ignore
            print(l.split(",")[num].split("'")[1])
            num += 1

  num = 0

def main():
  initalizer()
  search_commands()
  
  
main()