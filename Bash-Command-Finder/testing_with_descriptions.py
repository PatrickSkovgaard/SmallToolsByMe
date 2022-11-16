(a_commands, b_commands, c_commands, d_commands, e_commands, 
f_commands, g_commands, h_commands, i_commands, j_commands, 
k_commands, l_commands, m_commands, n_commands, o_commands, 
p_commands, q_commands, r_commands, s_commands, t_commands, 
u_commands, v_commands, w_commands, x_commands, y_commands, 
z_commands) = ([] for list in range(26))


(a_descr, b_descr, c_descr, d_descr, e_descr, 
f_descr, g_descr, h_descr, i_descr, j_descr, 
k_descr, l_descr, m_descr, n_descr, o_descr, 
p_descr, q_descr, r_descr, s_descr, t_descr, 
u_descr, v_descr, w_descr, x_descr, y_descr, 
z_descr) = ([] for list in range(26))


for i in open(file="txts/a-z_bash.txt", mode="r", encoding="UTF-8").readlines():
    if i.startswith("a"):
      a_commands.append(i.split(" ")[0])
      a_descr.append(i.split(" "))
    if i.startswith("b"):
      b_commands.append(i.split(" ")[0])
      b_descr.append(i.split(" ")[1])
    if i.startswith("c"):
      c_commands.append(i.split(" ")[0])
      c_descr.append(i.split(" ")[1])
    if i.startswith("d"):
      d_commands.append(i.split(" ")[0])
      d_descr.append(i.split(" ")[1])
    if i.startswith("e"):
      e_commands.append(i.split(" ")[0])
      e_descr.append(i.split(" ")[1])
    if i.startswith("f"):
      f_commands.append(i.split(" ")[0])
      f_descr.append(i.split(" ")[1])
    if i.startswith("g"):
      g_commands.append(i.split(" ")[0])
      g_descr.append(i.split(" ")[1])
    if i.startswith("h"):
      h_commands.append(i.split(" ")[0])
      h_descr.append(i.split(" ")[1])
    if i.startswith("i"):
      i_commands.append(i.split(" ")[0])
      i_descr.append(i.split(" ")[1])
    if i.startswith("j"):
      j_commands.append(i.split(" ")[0])
      j_descr.append(i.split(" ")[1])
    if i.startswith("k"):
      k_commands.append(i.split(" ")[0])
      k_descr.append(i.split(" ")[1])
    if i.startswith("l"):
      l_commands.append(i.split(" ")[0])
      l_descr.append(i.split(" ")[1])
    if i.startswith("m"):
      m_commands.append(i.split(" ")[0])
      m_descr.append(i.split(" ")[1])
    if i.startswith("n"):
      n_commands.append(i.split(" ")[0])
      n_descr.append(i.split(" ")[1])
    if i.startswith("o"):
      o_commands.append(i.split(" ")[0])
      o_descr.append(i.split(" ")[1])
    if i.startswith("p"):
      p_commands.append(i.split(" ")[0])
      p_descr.append(i.split(" ")[1])
    if i.startswith("q"):
      q_commands.append(i.split(" ")[0])
      q_descr.append(i.split(" ")[1])
    if i.startswith("r"):
      r_commands.append(i.split(" ")[0])
      r_descr.append(i.split(" ")[1])
    if i.startswith("s"):
      s_commands.append(i.split(" ")[0])
      s_descr.append(i.split(" ")[1])
    if i.startswith("t"):
      t_commands.append(i.split(" ")[0])
      t_descr.append(i.split(" ")[1])
    if i.startswith("u"):
      u_commands.append(i.split(" ")[0])
      u_descr.append(i.split(" ")[1])
    if i.startswith("v"):
      v_commands.append(i.split(" ")[0])
      v_descr.append(i.split(" ")[1])
    if i.startswith("w"):
      w_commands.append(i.split(" ")[0])
      w_descr.append(i.split(" ")[1])
    if i.startswith("x"):
      x_commands.append(i.split(" ")[0])
      x_descr.append(i.split(" ")[1])
    if i.startswith("y"):
      y_commands.append(i.split(" ")[0])
      y_descr.append(i.split(" ")[1])
    if i.startswith("z"):
      z_commands.append(i.split(" ")[0])
      z_descr.append(i.split(" ")[1])
      
      
for i in range(len(a_commands)):
    print(a_commands[i] + a_descr[i])