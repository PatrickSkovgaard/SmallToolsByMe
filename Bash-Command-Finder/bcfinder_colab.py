

(a_commands, b_commands, c_commands, d_commands, e_commands, 
f_commands, g_commands, h_commands, i_commands, j_commands, 
k_commands, l_commands, m_commands, n_commands, o_commands, 
p_commands, q_commands, r_commands, s_commands, t_commands, 
u_commands, v_commands, w_commands, x_commands, y_commands, 
z_commands) = ([] for list in range(26))


def append_commands_to_lists():

  for i in open(file='txts/a-z_bash.txt', mode="r", encoding="UTF-8").readlines():
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
      
      
def command_lists_length():
  
  len_dict = {"a": len(a_commands), "b": len(b_commands), "c": len(c_commands), "d": len(d_commands), "e": len(e_commands), 
              "f": len(f_commands), "g": len(g_commands), "h": len(h_commands), "i": len(i_commands), "j": len(j_commands), 
              "k": len(k_commands), "l": len(l_commands), "m": len(m_commands), "n": len(n_commands), "o": len(o_commands), 
              "p": len(p_commands), "q": len(q_commands), "r": len(r_commands), "s": len(s_commands), "t": len(t_commands), 
              "u": len(u_commands), "v": len(v_commands), "w": len(w_commands), "x": len(x_commands), "y": len(y_commands), 
              "z": len(z_commands)}
  
  return len_dict


def command__dict(choice):
  #TODO: lav det samme for descriptions som command_dict
  command_dict = {"a": a_commands,"b": b_commands, "c": c_commands, "d": d_commands, "e": e_commands, "f": f_commands, 
                  "g": g_commands, "h": h_commands, "i": i_commands, "j": j_commands, "k": k_commands, "l": l_commands, 
                  "m": m_commands, "n": n_commands, "o": o_commands, "p": p_commands, "q": q_commands, "r": r_commands, 
                  "s": s_commands, "t": t_commands, "u": u_commands, "v": v_commands, "w": w_commands, "x": x_commands, 
                  "y": y_commands, "z": z_commands }
  
  print(command_dict.get(choice))



def search_commands():
 
  len_dict = command_lists_length()
  
  print("----------------------------------------------------------------")
  choice = input("Choose a letter to search for a command\nTo exit, press Ctrl + C\n--> : ")
  print("----------------------------------------------------------------")
  choice = choice.lower()
  
  num = 0

  if len(choice) != 1 or choice.isalpha() == False:
    print("bcfind.py: ERROR: Incorrect input. One-letter options only!")
    
  else:
    for l in open("txts/cmd_list.txt", "r", encoding="UTF-8").readlines():
        if l.startswith("['" + choice):
          while(num < len_dict.get(choice)):  # type: ignore
            print(l.split(",")[num].split("'")[1])
            num += 1

    num = 0
    print("")
  command__dict(choice)


def main():
  append_commands_to_lists()
  search_commands()
  
  
  
main()


















#Implement this part later perhaps, on top of the actual code running above?

##########################   Info   ############################################
'''
Name: Bash Command Finder
Author: Patrick Skovgaard (Github: PatrickSkovgaard)
Used for: Bash Command Line, with Python.
'''

##########################   Functionality   ###################################
'''
Find by command name (whole or part) or type(?)
Display info and examples about a command  
'''

##########################   Misc   ############################################
'''
Make as a .sh tool?
Make as another extension tool?
'''

##########################   Code   ############################################

'''
print("\nBash Command Finder.") 
print("[Commands and descriptions are from https://github.com/trinib/Linux-Bash-Commands, with some additional ones from myself]") 

print("[This tool is made by me (PatrickSkovgaard on GitHub).]\n")

print("Usage: python bcfind.py [OPTIONS] || [LETTER] || [TYPE]\n")

print("OPTIONS:\n")
print("Type the first letter of the command(s) you are looking for, e.g. 'n' for netstat or nslookup etc.\n")

#Not implemented yet..
print("Only one option allowed:\n" +
      "-lc:         List all bash commands.\n" + 
      "-ltype:      List all types.\n")
'''