import sys

def main():

    turn = input("Welke beurt is het? ")
    try:
        if turn == "1":

            


            A_value_1 = float(numbers.get(numbers_A)) * float(resources.get(resource_A))
            B_value_1 = float(numbers.get(numbers_B)) * float(resources.get(resource_B))
            C_value_1 = float(numbers.get(numbers_C)) * float(resources.get(resource_C))
            D_value_1 = float(numbers.get(numbers_D)) * float(resources.get(resource_D))
            E_value_1 = float(numbers.get(numbers_E)) * float(resources.get(resource_E))
            F_value_1 = float(numbers.get(numbers_F)) * float(resources.get(resource_F))
            G_value_1 = float(numbers.get(numbers_G)) * float(resources.get(resource_G))
            H_value_1 = float(numbers.get(numbers_H)) * float(resources.get(resource_H))
            I_value_1 = float(numbers.get(numbers_I)) * float(resources.get(resource_I))
            J_value_1 = float(numbers.get(numbers_J)) * float(resources.get(resource_J))
            K_value_1 = float(numbers.get(numbers_K)) * float(resources.get(resource_K))
            L_value_1 = float(numbers.get(numbers_L)) * float(resources.get(resource_L))
            M_value_1 = float(numbers.get(numbers_M)) * float(resources.get(resource_M))
            N_value_1 = float(numbers.get(numbers_N)) * float(resources.get(resource_N))
            O_value_1 = float(numbers.get(numbers_O)) * float(resources.get(resource_O))
            P_value_1 = float(numbers.get(numbers_P)) * float(resources.get(resource_P))
            Q_value_1 = float(numbers.get(numbers_Q)) * float(resources.get(resource_Q))
            R_value_1 = float(numbers.get(numbers_R)) * float(resources.get(resource_R))
            S_value_1 = float(numbers.get(numbers_S)) * float(resources.get(resource_S))
             


            Spot_Values_Dict = {
                "(-3, 1)": A_value_1,
                "(-2, 1)": A_value_1,
                "(-1, 1)": (A_value_1 + B_value_1) * float(A_B),
                "(0, 1)": B_value_1,
                "(1, 1)": (B_value_1 + C_value_1) * float(B_C),
                "(2, 1)": C_value_1,
                "(3, 1)": C_value_1,
                "(-4, 2)": D_value_1,
                "(-3, 2)": (A_value_1 + D_value_1) * float(A_D),
                "(-2, 2)": ((A_value_1 + D_value_1) * float(A_D) + (A_value_1 + E_value_1) * float(A_E) + (D_value_1 + E_value_1) * float(D_E)) * 0.5,
                "(-1, 2)": ((A_value_1 + B_value_1)* float(A_B) + (A_value_1 + E_value_1) * float(A_E) + (B_value_1 + E_value_1)* float(B_E)) * 0.5,
                "(0, 2)": ((B_value_1 + E_value_1)* float(B_E) + (B_value_1 + F_value_1) * float(B_F) + (E_value_1 + F_value_1)* float(E_F)) * 0.5,
                "(1, 2)": ((B_value_1 + C_value_1)* float(B_C) + (F_value_1 + B_value_1)* float(B_F) + (C_value_1 + F_value_1)* float(C_F)) * 0.5,
                "(2, 2)": ((C_value_1 + F_value_1)* float(C_F) + (C_value_1 + G_value_1)* float(C_G) + (F_value_1 + G_value_1)* float(F_G)) * 0.5,
                "(3, 2)": (C_value_1 + G_value_1)* float(C_G),
                "(4, 2)": G_value_1,
                "(-5, 3)": H_value_1,
                "(-4, 3)": (H_value_1 + D_value_1) * float(D_H),
                "(-3, 3)": ((D_value_1 + H_value_1)* float(D_H) + (I_value_1 + H_value_1)* float(H_I) + (I_value_1 + D_value_1)* float(D_I)) * 0.5,
                "(-2, 3)": ((D_value_1 + I_value_1)* float(D_I) + (D_value_1 + E_value_1)* float(D_E) + (E_value_1 + I_value_1)* float(E_I)) * 0.5,
                "(-1, 3)": ((J_value_1 + I_value_1)* float(I_J) + (I_value_1 + E_value_1)* float(E_I) + (J_value_1 + E_value_1)* float(E_J)) * 0.5,
                "(0, 3)": ((E_value_1 + F_value_1)* float(E_F) + (J_value_1 + E_value_1)* float(E_J) + (J_value_1 + F_value_1)* float(F_J)) * 0.5,
                "(1, 3)": ((J_value_1 + F_value_1)* float(F_J) + (J_value_1 + K_value_1)* float(J_K) + (F_value_1 + K_value_1)* float(F_K)) * 0.5,
                "(2, 3)": ((K_value_1 + F_value_1)* float(F_K) + (G_value_1 + K_value_1)* float(G_K) + (F_value_1 + G_value_1)* float(F_G)) * 0.5,
                "(3, 3)": ((K_value_1 + L_value_1)* float(K_L) + (G_value_1 + L_value_1)* float(G_L) + (G_value_1 + K_value_1)* float(G_K)) * 0.5,
                "(4, 3)": (G_value_1 + L_value_1) * float(G_L),
                "(5, 3)": L_value_1,
                "(-5, 4)": H_value_1,
                "(-4, 4)": (H_value_1 + M_value_1)* float(H_M),
                "(-3, 4)": ((H_value_1 + M_value_1)* float(H_M) + (M_value_1 + I_value_1)* float(I_M) + (I_value_1 + H_value_1)* float(H_I)) * 0.5,
                "(-2, 4)": ((N_value_1 + M_value_1)* float(M_N) + (N_value_1 + I_value_1)* float(I_N) + (I_value_1 + M_value_1)* float(I_M)) * 0.5,
                "(-1, 4)": ((N_value_1 + J_value_1)* float(J_N) + (N_value_1 + I_value_1)* float(I_N) + (I_value_1 + J_value_1)* float(I_J)) * 0.5,
                "(0, 4)": ((N_value_1 + J_value_1)* float(J_N) + (J_value_1 + O_value_1)* float(J_O) + (O_value_1 + N_value_1)* float(N_O)) * 0.5,
                "(1, 4)": ((K_value_1 + J_value_1)* float(J_K) + (J_value_1 + O_value_1)* float(J_O) + (O_value_1 + K_value_1)* float(K_O)) * 0.5,
                "(2, 4)": ((K_value_1 + P_value_1)* float(K_P) + (P_value_1 + O_value_1)* float(O_P) + (O_value_1 + K_value_1)* float(K_O)) * 0.5,
                "(3, 4)": ((K_value_1 + P_value_1)* float(K_P) + (P_value_1 + L_value_1)* float(L_P) + (L_value_1 + K_value_1)* float(K_L)) * 0.5,
                "(4, 4)": (P_value_1 + L_value_1)* float(L_P),
                "(5, 4)": L_value_1,
                "(-4, 5)": M_value_1,
                "(-3, 5)": (M_value_1 + Q_value_1) * float(M_Q),
                "(-2, 5)": ((Q_value_1 + M_value_1)* float(M_Q) + (N_value_1 + M_value_1)* float(M_N) + (N_value_1 + Q_value_1)* float(N_Q)) * 0.5,
                "(-1, 5)": ((Q_value_1 + R_value_1)* float(Q_R) + (N_value_1 + R_value_1)* float(N_R) + (N_value_1 + Q_value_1)* float(N_Q)) * 0.5,
                "(0, 5)": ((N_value_1 + O_value_1)* float(N_O) + (N_value_1 + R_value_1)* float(N_R) + (R_value_1 + O_value_1)* float(O_R)) * 0.5,
                "(1, 5)": ((S_value_1 + O_value_1)* float(O_S) + (S_value_1 + R_value_1)* float(R_S) + (R_value_1 + O_value_1)* float(O_R)) * 0.5,
                "(2, 5)": ((S_value_1 + O_value_1)* float(O_S) + (S_value_1 + P_value_1)* float(P_S) + (P_value_1 + O_value_1)* float(O_P)) * 0.5,
                "(3, 5)": (S_value_1 + P_value_1)* float(P_S),
                "(4, 5)": P_value_1,
                "(-3, 6)": Q_value_1,
                "(-2, 6)": Q_value_1,
                "(-1, 6)": (Q_value_1 + R_value_1) * float(Q_R),
                "(0, 6)": R_value_1,
                "(1, 6)": (R_value_1 + S_value_1) * float(R_S),
                "(2, 6)": S_value_1,
                "(3, 6)": S_value_1,
                "(-7, 3)": 0,
                "(-6, 3)": 0,
                "(-6, 2)": 0,
                "(-5, 2)": 0,
                "(-5, 1)": 0,
                "(-4, 1)": 0,
                "(-4, 0)": 0,
                "(-3, 0)": 0,
                "(-2, 0)": 0,
                "(-1, 0)": 0,
                "(0, 0)": 0,
                "(1, 0)": 0,
                "(2, 0)": 0,
                "(3, 0)": 0,
                "(4, 0)": 0,
                "(4, 1)": 0,
                "(5, 1)": 0,
                "(5, 2)": 0,
                "(6, 2)": 0,
                "(6, 3)": 0,
                "(7, 3)": 0,
                "(7, 4)": 0,
                "(6, 4)": 0,
                "(6, 5)": 0,
                "(5, 5)": 0,
                "(5, 6)": 0,
                "(4, 6)": 0,
                "(4, 7)": 0,
                "(3, 7)": 0,
                "(2, 7)": 0,
                "(1, 7)": 0,
                "(0, 7)": 0,
                "(-1, 7)": 0,
                "(-2, 7)": 0,
                "(-3, 7)": 0,
                "(-4, 7)": 0,
                "(-4, 6)": 0,
                "(-5, 6)": 0,
                "(-5, 5)": 0,
                "(-6, 5)": 0,
                "(-6, 4)": 0,
                "(-7, 4)": 0,
                
            }

        
            sorted_items = sorted(Spot_Values_Dict.items(), key=lambda x: x[1])

            
            


            Player_Number = input("Welke speler ben je? (1, 2, 3 of 4) ")
            
            if Player_Number == "1":
                Unplaceable = ["hi"]
                for spot, value in sorted_items:
                    if value == 0:
                        pass
                    else:
                        print(f"{spot}: {round(value, 3)}")
            elif Player_Number == "2":
                while True:
                    
                    Placement_1 = input("Welke coordinaten was het eerste dorp geplaatst? ")
                    if (Placement_1 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_1) > 0 :
                        Placement_1_x, Placement_1_y = Placement_1.split(", ")
                        Placement_1_x = Placement_1_x.replace("(", "")
                        Placement_1_y = Placement_1_y.replace(")", "")
                        if ((int(Placement_1_x) % 2) == 0) and ((int(Placement_1_y) % 2) != 0) or ((int(Placement_1_x) % 2) != 0) and ((int(Placement_1_y) % 2) == 0):
                            Placement_1_x_Left = int(Placement_1_x) - 1
                            Placement_1_x_Right = int(Placement_1_x) + 1
                            Placement_1_y_Up = int(Placement_1_y) - 1
                            

                            Placement_1_Left = f"({Placement_1_x_Left}, {Placement_1_y})"
                            Placement_1_Right = f"({Placement_1_x_Right}, {Placement_1_y})"
                            Placement_1_Up = f"({Placement_1_x}, {Placement_1_y_Up})"
                            Placement_1_Down = 0


                            Unplaceable = [Placement_1, Placement_1_Left, Placement_1_Right, Placement_1_Up, Placement_1_Down]
                            for spot, value in sorted_items:
                                if value == 0 or spot in Unplaceable:
                                    pass
                                else:
                                    print(f"{spot}: {round(value, 3)}")


                            pass
                        else:
                            Placement_1_x_Left = int(Placement_1_x) - 1
                            Placement_1_x_Right = int(Placement_1_x) + 1
                            Placement_1_y_Down = int(Placement_1_y) + 1
                            Placement_1_y_Up = 0

                            Placement_1_Left = f"({Placement_1_x_Left}, {Placement_1_y})"
                            Placement_1_Right = f"({Placement_1_x_Right}, {Placement_1_y})"
                            Placement_1_Up = 0
                            Placement_1_Down = f"({Placement_1_x}, {Placement_1_y_Down})"

                            Unplaceable = [Placement_1, Placement_1_Left, Placement_1_Right, Placement_1_Up, Placement_1_Down]
                            for spot, value in sorted_items:
                                if value == 0 or spot in Unplaceable:
                                    pass
                                else:
                                    print(f"{spot}: {round(value, 3)}")
                        
                        break
                    else:
                        pass
                    
                    


            elif Player_Number == "3":
                while True:
                    
                    Placement_1 = input("Welke coordinaten was het eerste dorp geplaatst? ")
                    if (Placement_1 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_1) > 0 :
                        Placement_1_x, Placement_1_y = Placement_1.split(", ")
                        Placement_1_x = Placement_1_x.replace("(", "")
                        Placement_1_y = Placement_1_y.replace(")", "")
                        if ((int(Placement_1_x) % 2) == 0) and ((int(Placement_1_y) % 2) != 0) or ((int(Placement_1_x) % 2) != 0) and ((int(Placement_1_y) % 2) == 0):
                            Placement_1_x_Left = int(Placement_1_x) - 1
                            Placement_1_x_Right = int(Placement_1_x) + 1
                            Placement_1_y_Up = int(Placement_1_y) - 1
                            

                            Placement_1_Left = f"({Placement_1_x_Left}, {Placement_1_y})"
                            Placement_1_Right = f"({Placement_1_x_Right}, {Placement_1_y})"
                            Placement_1_Up = f"({Placement_1_x}, {Placement_1_y_Up})"
                            Placement_1_Down = 0

                            pass
                        else:
                            Placement_1_x_Left = int(Placement_1_x) - 1
                            Placement_1_x_Right = int(Placement_1_x) + 1
                            Placement_1_y_Down = int(Placement_1_y) + 1
                            Placement_1_y_Up = 0

                            Placement_1_Left = f"({Placement_1_x_Left}, {Placement_1_y})"
                            Placement_1_Right = f"({Placement_1_x_Right}, {Placement_1_y})"
                            Placement_1_Up = 0
                            Placement_1_Down = f"({Placement_1_x}, {Placement_1_y_Down})"

                            
                        
                        break
                    else:
                        pass

                while True:
                    
                    Placement_2 = input("Welke coordinaten was het tweede dorp geplaatst? ")
                    if (Placement_2 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_2) > 0 :
                        Placement_2_x, Placement_2_y = Placement_2.split(", ")
                        Placement_2_x = Placement_2_x.replace("(", "")
                        Placement_2_y = Placement_2_y.replace(")", "")
                        if ((int(Placement_2_x) % 2) == 0) and ((int(Placement_2_y) % 2) != 0) or ((int(Placement_2_x) % 2) != 0) and ((int(Placement_2_y) % 2) == 0):
                            Placement_2_x_Left = int(Placement_2_x) - 1
                            Placement_2_x_Right = int(Placement_2_x) + 1
                            Placement_2_y_Up = int(Placement_2_y) - 1
                            

                            Placement_2_Left = f"({Placement_2_x_Left}, {Placement_2_y})"
                            Placement_2_Right = f"({Placement_2_x_Right}, {Placement_2_y})"
                            Placement_2_Up = f"({Placement_2_x}, {Placement_2_y_Up})"
                            Placement_2_Down = 0


                            Unplaceable = [Placement_1, Placement_1_Left, Placement_1_Right, Placement_1_Up, Placement_1_Down, Placement_2, Placement_2_Left, Placement_2_Right, Placement_2_Up, Placement_2_Down]
                            for spot, value in sorted_items:
                                if value == 0 or spot in Unplaceable:
                                    pass
                                else:
                                    print(f"{spot}: {round(value, 3)}")


                            pass
                        else:
                            Placement_2_x_Left = int(Placement_2_x) - 1
                            Placement_2_x_Right = int(Placement_2_x) + 1
                            Placement_2_y_Down = int(Placement_2_y) + 1
                            

                            Placement_2_Left = f"({Placement_2_x_Left}, {Placement_2_y})"
                            Placement_2_Right = f"({Placement_2_x_Right}, {Placement_2_y})"
                            Placement_2_Up = 0
                            Placement_2_Down = f"({Placement_2_x}, {Placement_2_y_Down})"


                            Unplaceable = [Placement_1, Placement_1_Left, Placement_1_Right, Placement_1_Up, Placement_1_Down, Placement_2, Placement_2_Left, Placement_2_Right, Placement_2_Up, Placement_2_Down]
                            for spot, value in sorted_items:
                                if value == 0 or spot in Unplaceable:
                                    pass
                                else:
                                    print(f"{spot}: {round(value, 3)}")
                        
                        break
                    else:
                        pass

                
            elif Player_Number == "4":
                
                while True:
                    
                    Placement_1 = input("Welke coordinaten was het eerste dorp geplaatst? ")
                    if (Placement_1 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_1) > 0 :
                        Placement_1_x, Placement_1_y = Placement_1.split(", ")
                        Placement_1_x = Placement_1_x.replace("(", "")
                        Placement_1_y = Placement_1_y.replace(")", "")
                        if ((int(Placement_1_x) % 2) == 0) and ((int(Placement_1_y) % 2) != 0) or ((int(Placement_1_x) % 2) != 0) and ((int(Placement_1_y) % 2) == 0):
                            Placement_1_x_Left = int(Placement_1_x) - 1
                            Placement_1_x_Right = int(Placement_1_x) + 1
                            Placement_1_y_Up = int(Placement_1_y) - 1
                            

                            Placement_1_Left = f"({Placement_1_x_Left}, {Placement_1_y})"
                            Placement_1_Right = f"({Placement_1_x_Right}, {Placement_1_y})"
                            Placement_1_Up = f"({Placement_1_x}, {Placement_1_y_Up})"
                            Placement_1_Down = 0

                            pass
                        else:
                            Placement_1_x_Left = int(Placement_1_x) - 1
                            Placement_1_x_Right = int(Placement_1_x) + 1
                            Placement_1_y_Down = int(Placement_1_y) + 1
                            Placement_1_y_Up = 0

                            Placement_1_Left = f"({Placement_1_x_Left}, {Placement_1_y})"
                            Placement_1_Right = f"({Placement_1_x_Right}, {Placement_1_y})"
                            Placement_1_Up = 0
                            Placement_1_Down = f"({Placement_1_x}, {Placement_1_y_Down})"

                            
                        
                        break
                    else:
                        pass

                while True:
                    
                    Placement_2 = input("Welke coordinaten was het tweede dorp geplaatst? ")
                    if (Placement_2 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_2) > 0 :
                        Placement_2_x, Placement_2_y = Placement_2.split(", ")
                        Placement_2_x = Placement_2_x.replace("(", "")
                        Placement_2_y = Placement_2_y.replace(")", "")
                        if ((int(Placement_2_x) % 2) == 0) and ((int(Placement_2_y) % 2) != 0) or ((int(Placement_2_x) % 2) != 0) and ((int(Placement_2_y) % 2) == 0):
                            Placement_2_x_Left = int(Placement_2_x) - 1
                            Placement_2_x_Right = int(Placement_2_x) + 1
                            Placement_2_y_Up = int(Placement_2_y) - 1
                            

                            Placement_2_Left = f"({Placement_2_x_Left}, {Placement_2_y})"
                            Placement_2_Right = f"({Placement_2_x_Right}, {Placement_2_y})"
                            Placement_2_Up = f"({Placement_2_x}, {Placement_2_y_Up})"
                            Placement_2_Down = 0

                            pass
                        else:
                            Placement_2_x_Left = int(Placement_2_x) - 1
                            Placement_2_x_Right = int(Placement_2_x) + 1
                            Placement_2_y_Down = int(Placement_2_y) + 1
                            Placement_2_y_Up = 0

                            Placement_2_Left = f"({Placement_2_x_Left}, {Placement_2_y})"
                            Placement_2_Right = f"({Placement_2_x_Right}, {Placement_2_y})"
                            Placement_2_Up = 0
                            Placement_2_Down = f"({Placement_2_x}, {Placement_2_y_Down})"

                            
                        
                        break
                    else:
                        pass

                while True:
                    
                    Placement_3 = input("Welke coordinaten was het derde dorp geplaatst? ")
                    if (Placement_3 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_3) > 0 :
                        Placement_3_x, Placement_3_y = Placement_3.split(", ")
                        Placement_3_x = Placement_3_x.replace("(", "")
                        Placement_3_y = Placement_3_y.replace(")", "")
                        if ((int(Placement_3_x) % 2) == 0) and ((int(Placement_3_y) % 2) != 0) or ((int(Placement_3_x) % 2) != 0) and ((int(Placement_3_y) % 2) == 0):
                            Placement_3_x_Left = int(Placement_3_x) - 1
                            Placement_3_x_Right = int(Placement_3_x) + 1
                            Placement_3_y_Up = int(Placement_3_y) - 1
                            

                            Placement_3_Left = f"({Placement_3_x_Left}, {Placement_3_y})"
                            Placement_3_Right = f"({Placement_3_x_Right}, {Placement_3_y})"
                            Placement_3_Up = f"({Placement_3_x}, {Placement_3_y_Up})"
                            Placement_3_Down = 0


                            Unplaceable = [Placement_1, Placement_1_Left, Placement_1_Right, Placement_1_Up, Placement_1_Down, Placement_2, Placement_2_Left, Placement_2_Right, Placement_2_Up, Placement_2_Down, Placement_3, Placement_3_Left, Placement_3_Right, Placement_3_Up, Placement_3_Down]
                            for spot, value in sorted_items:
                                if value == 0 or spot in Unplaceable:
                                    pass
                                else:
                                    print(f"{spot}: {round(value, 3)}")


                            break
                        else:
                            Placement_3_x_Left = int(Placement_3_x) - 1
                            Placement_3_x_Right = int(Placement_3_x) + 1
                            Placement_3_y_Down = int(Placement_3_y) + 1
                            

                            Placement_3_Left = f"({Placement_3_x_Left}, {Placement_3_y})"
                            Placement_3_Right = f"({Placement_3_x_Right}, {Placement_3_y})"
                            Placement_3_Up = 0
                            Placement_3_Down = f"({Placement_3_x}, {Placement_3_y_Down})"


                            Unplaceable = [Placement_1, Placement_1_Left, Placement_1_Right, Placement_1_Up, Placement_1_Down, Placement_2, Placement_2_Left, Placement_2_Right, Placement_2_Up, Placement_2_Down, Placement_3, Placement_3_Left, Placement_3_Right, Placement_3_Up, Placement_3_Down]
                            for spot, value in sorted_items:
                                if value == 0 or spot in Unplaceable:
                                    pass
                                else:
                                    print(f"{spot}: {round(value, 3)}")
                            break

                    else:
                        pass

            else:
                print("Ongeldige speler, vul een getal tussen de 1 en 4 in.")
                sys.exit()


            while True:
                Build_1 = input("Welke coordinaten heb je je eerste dorp geplaatst? ")
                if Build_1 in Spot_Values_Dict.keys() and Spot_Values_Dict.get(Build_1) > 0 :
        
                        

                    Lumber_Production = input("Hoeveel hout productie heb je? ")
                    Clay_Production = input("Hoeveel steen productie heb je? ")
                    Sheep_Production = input("Hoeveel schaap productie heb je? ")
                    Wheat_Production = input("Hoeveel graan productie heb je? ")
                    Ore_Production = input("Hoeveel erts productie heb je? ")

                    Words_Lumber = Lumber_Production.split(", ")
                    Word_Count_Lumber = len(Words_Lumber)
                    
                    if Lumber_Production == "0":
                        Lumber_Production_Value = 0

                    elif Word_Count_Lumber == 1:
                        Lumber_Production_Value = float(numbers.get(Lumber_Production))
                        
                    elif Word_Count_Lumber == 2:
                        Lumber_1, Lumber_2 = Lumber_Production.split(", ")
                        Lumber_Production_Value = float(numbers.get(Lumber_1)) + float(numbers.get(Lumber_2))
                        
                    else:
                        Lumber_1, Lumber_2, Lumber_3 = Lumber_Production.split(", ")
                        Lumber_Production_Value = float(numbers.get(Lumber_1)) + float(numbers.get(Lumber_2)) + float(numbers.get(Lumber_3))
                        
                    Words_Clay = Clay_Production.split(", ")
                    Word_Count_Clay = len(Words_Clay)

                    if Clay_Production == "0":
                        Clay_Production_Value = 0
                    
                    elif Word_Count_Clay == 1:
                        Clay_Production_Value = float(numbers.get(Clay_Production))
                        
                    elif Word_Count_Clay == 2:
                        Clay_1, Clay_2 = Clay_Production.split(", ")
                        Clay_Production_Value = float(numbers.get(Clay_1)) + float(numbers.get(Clay_2))
                        
                    else:
                        Clay_1, Clay_2, Clay_3 = Clay_Production.split(", ")
                        Clay_Production_Value = float(numbers.get(Clay_1)) + float(numbers.get(Clay_2)) + float(numbers.get(Clay_3))
                        

                    Words_Sheep = Sheep_Production.split(", ")
                    Word_Count_Sheep = len(Words_Sheep)

                    if Sheep_Production == "0":
                        Sheep_Production_Value = 0
                    
                    elif Word_Count_Sheep == 1:
                        Sheep_Production_Value = float(numbers.get(Sheep_Production))
                        
                    elif Word_Count_Sheep == 2:
                        Sheep_1, Sheep_2 = Sheep_Production.split(", ")
                        Sheep_Production_Value = float(numbers.get(Sheep_1)) + float(numbers.get(Sheep_2))
                        
                    else:
                        Sheep_1, Sheep_2, Sheep_3 = Sheep_Production.split(", ")
                        Sheep_Production_Value = float(numbers.get(Sheep_1)) + float(numbers.get(Sheep_2)) + float(numbers.get(Sheep_3))
                        
                    Words_Wheat = Wheat_Production.split(", ")
                    Word_Count_Wheat = len(Words_Wheat)

                    if Wheat_Production == "0":
                        Wheat_Production_Value = 0
                    
                    elif Word_Count_Wheat == 1:
                        Wheat_Production_Value = float(numbers.get(Wheat_Production))
                        
                    elif Word_Count_Wheat == 2:
                        Wheat_1, Wheat_2 = Wheat_Production.split(", ")
                        Wheat_Production_Value = float(numbers.get(Wheat_1)) + float(numbers.get(Wheat_2))
                        
                    else:
                        Wheat_1, Wheat_2, Wheat_3 = Wheat_Production.split(", ")
                        Wheat_Production_Value = float(numbers.get(Wheat_1)) + float(numbers.get(Wheat_2)) + float(numbers.get(Wheat_3))
                        

                    Words_Ore = Ore_Production.split(", ")
                    Word_Count_Ore = len(Words_Ore)

                    if Ore_Production == "0":
                        Ore_Production_Value = 0
                    
                    elif Word_Count_Ore == 1:
                        Ore_Production_Value = float(numbers.get(Ore_Production))
                    
                    elif Word_Count_Ore == 2:
                        Ore_1, Ore_2 = Ore_Production.split(", ")
                        Ore_Production_Value = float(numbers.get(Ore_1)) + float(numbers.get(Ore_2))
                        
                    else:
                        Ore_1, Ore_2, Ore_3 = Ore_Production.split(", ")
                        Ore_Production_Value = float(numbers.get(Ore_1)) + float(numbers.get(Ore_2)) + float(numbers.get(Ore_3))
                        
                    Lumber = 16.67
                    Clay = 16.67
                    Sheep = 20.83
                    Wheat = 29.17
                    Ore = 16.67 

                    Lumber2 = 10 * (Clay_Production_Value * 0.5 * Clay + Sheep_Production_Value * 0.2 * Sheep + Wheat_Production_Value * 1/7 * Wheat)
                    
                    Clay2 = 10 * (Lumber_Production_Value * 0.5 * Lumber + Sheep_Production_Value * 0.2 * Sheep + Wheat_Production_Value * 1/7 * Wheat)
                    
                    Sheep2 = 10 * (Lumber_Production_Value * 0.25 * Lumber + Clay_Production_Value * 0.25 * Clay + Wheat_Production_Value * 2/7 * Wheat + Ore_Production_Value * 0.25 * Ore)
                    
                    Wheat2 = 10 * (Lumber_Production_Value * 0.25 * Lumber + Clay_Production_Value * 0.25 * Clay + Sheep_Production_Value * 0.4 * Sheep + Wheat_Production_Value * 1/7 * Wheat + Ore_Production_Value * 0.5 * Ore)
                    
                    Ore2 = 10 * (Sheep_Production_Value * 0.2 * Sheep + Wheat_Production_Value * 2/7 * Wheat + Ore_Production_Value * 0.25 * Ore)
                    
                    resources2 = {
                        "L": Lumber2,
                        "C": Clay2,
                        "S": Sheep2,
                        "W": Wheat2,
                        "O": Ore2,
                        "D": "0"
                    }

                    Port_3_1 =  0.333*(Clay_Production_Value + Lumber_Production_Value + Sheep_Production_Value + Wheat_Production_Value + Ore_Production_Value)
                    Port_Lumber = Lumber_Production_Value * 0.5
                    Port_Clay = Clay_Production_Value * 0.5
                    Port_Sheep = Sheep_Production_Value * 0.5
                    Port_Wheat = Wheat_Production_Value * 0.5
                    Port_Ore = Ore_Production_Value * 0.5




                    A_value_1 = float(numbers.get(numbers_A)) * float(resources2.get(resource_A))
                    B_value_1 = float(numbers.get(numbers_B)) * float(resources2.get(resource_B))
                    C_value_1 = float(numbers.get(numbers_C)) * float(resources2.get(resource_C))
                    D_value_1 = float(numbers.get(numbers_D)) * float(resources2.get(resource_D))
                    E_value_1 = float(numbers.get(numbers_E)) * float(resources2.get(resource_E))
                    F_value_1 = float(numbers.get(numbers_F)) * float(resources2.get(resource_F))
                    G_value_1 = float(numbers.get(numbers_G)) * float(resources2.get(resource_G))
                    H_value_1 = float(numbers.get(numbers_H)) * float(resources2.get(resource_H))
                    I_value_1 = float(numbers.get(numbers_I)) * float(resources2.get(resource_I))
                    J_value_1 = float(numbers.get(numbers_J)) * float(resources2.get(resource_J))
                    K_value_1 = float(numbers.get(numbers_K)) * float(resources2.get(resource_K))
                    L_value_1 = float(numbers.get(numbers_L)) * float(resources2.get(resource_L))
                    M_value_1 = float(numbers.get(numbers_M)) * float(resources2.get(resource_M))
                    N_value_1 = float(numbers.get(numbers_N)) * float(resources2.get(resource_N))
                    O_value_1 = float(numbers.get(numbers_O)) * float(resources2.get(resource_O))
                    P_value_1 = float(numbers.get(numbers_P)) * float(resources2.get(resource_P))
                    Q_value_1 = float(numbers.get(numbers_Q)) * float(resources2.get(resource_Q))
                    R_value_1 = float(numbers.get(numbers_R)) * float(resources2.get(resource_R))
                    S_value_1 = float(numbers.get(numbers_S)) * float(resources2.get(resource_S))

                    
                    
                    

                                
                    Spot_Values_Dict = {
                        "(-3, 1)": A_value_1,
                        "(-2, 1)": A_value_1,
                        "(-1, 1)": (A_value_1 + B_value_1) * float(A_B) + Port_3_1,
                        "(0, 1)": B_value_1 + Port_3_1,
                        "(1, 1)": (B_value_1 + C_value_1) * float(B_C),
                        "(2, 1)": C_value_1 + Port_3_1,
                        "(3, 1)": C_value_1 + Port_3_1,
                        "(-4, 2)": D_value_1 + Port_Sheep,
                        "(-3, 2)": (A_value_1 + D_value_1) * float(A_D) + Port_Sheep,
                        "(-2, 2)": ((A_value_1 + D_value_1) * float(A_D) + (A_value_1 + E_value_1) * float(A_E) + (D_value_1 + E_value_1) * float(D_E)) * 0.5,
                        "(-1, 2)": ((A_value_1 + B_value_1)* float(A_B) + (A_value_1 + E_value_1) * float(A_E) + (B_value_1 + E_value_1)* float(B_E)) * 0.5,
                        "(0, 2)": ((B_value_1 + E_value_1)* float(B_E) + (B_value_1 + F_value_1) * float(B_F) + (E_value_1 + F_value_1)* float(E_F)) * 0.5,
                        "(1, 2)": ((B_value_1 + C_value_1)* float(B_C) + (F_value_1 + B_value_1)* float(B_F) + (C_value_1 + F_value_1)* float(C_F)) * 0.5,
                        "(2, 2)": ((C_value_1 + F_value_1)* float(C_F) + (C_value_1 + G_value_1)* float(C_G) + (F_value_1 + G_value_1)* float(F_G)) * 0.5,
                        "(3, 2)": (C_value_1 + G_value_1)* float(C_G),
                        "(4, 2)": G_value_1 + Port_Clay,
                        "(-5, 3)": H_value_1 + Port_3_1,
                        "(-4, 3)": (H_value_1 + D_value_1) * float(D_H),
                        "(-3, 3)": ((D_value_1 + H_value_1)* float(D_H) + (I_value_1 + H_value_1)* float(H_I) + (I_value_1 + D_value_1)* float(D_I)) * 0.5,
                        "(-2, 3)": ((D_value_1 + I_value_1)* float(D_I) + (D_value_1 + E_value_1)* float(D_E) + (E_value_1 + I_value_1)* float(E_I)) * 0.5,
                        "(-1, 3)": ((J_value_1 + I_value_1)* float(I_J) + (I_value_1 + E_value_1)* float(E_I) + (J_value_1 + E_value_1)* float(E_J)) * 0.5,
                        "(0, 3)": ((E_value_1 + F_value_1)* float(E_F) + (J_value_1 + E_value_1)* float(E_J) + (J_value_1 + F_value_1)* float(F_J)) * 0.5,
                        "(1, 3)": ((J_value_1 + F_value_1)* float(F_J) + (J_value_1 + K_value_1)* float(J_K) + (F_value_1 + K_value_1)* float(F_K)) * 0.5,
                        "(2, 3)": ((K_value_1 + F_value_1)* float(F_K) + (G_value_1 + K_value_1)* float(G_K) + (F_value_1 + G_value_1)* float(F_G)) * 0.5,
                        "(3, 3)": ((K_value_1 + L_value_1)* float(K_L) + (G_value_1 + L_value_1)* float(G_L) + (G_value_1 + K_value_1)* float(G_K)) * 0.5,
                        "(4, 3)": (G_value_1 + L_value_1) * float(G_L) + Port_Clay,
                        "(5, 3)": L_value_1,
                        "(-5, 4)": H_value_1 + Port_3_1,
                        "(-4, 4)": (H_value_1 + M_value_1)* float(H_M),
                        "(-3, 4)": ((H_value_1 + M_value_1)* float(H_M) + (M_value_1 + I_value_1)* float(I_M) + (I_value_1 + H_value_1)* float(H_I)) * 0.5,
                        "(-2, 4)": ((N_value_1 + M_value_1)* float(M_N) + (N_value_1 + I_value_1)* float(I_N) + (I_value_1 + M_value_1)* float(I_M)) * 0.5,
                        "(-1, 4)": ((N_value_1 + J_value_1)* float(J_N) + (N_value_1 + I_value_1)* float(I_N) + (I_value_1 + J_value_1)* float(I_J)) * 0.5,
                        "(0, 4)": ((N_value_1 + J_value_1)* float(J_N) + (J_value_1 + O_value_1)* float(J_O) + (O_value_1 + N_value_1)* float(N_O)) * 0.5,
                        "(1, 4)": ((K_value_1 + J_value_1)* float(J_K) + (J_value_1 + O_value_1)* float(J_O) + (O_value_1 + K_value_1)* float(K_O)) * 0.5,
                        "(2, 4)": ((K_value_1 + P_value_1)* float(K_P) + (P_value_1 + O_value_1)* float(O_P) + (O_value_1 + K_value_1)* float(K_O)) * 0.5,
                        "(3, 4)": ((K_value_1 + P_value_1)* float(K_P) + (P_value_1 + L_value_1)* float(L_P) + (L_value_1 + K_value_1)* float(K_L)) * 0.5,
                        "(4, 4)": (P_value_1 + L_value_1)* float(L_P) + Port_Lumber,
                        "(5, 4)": L_value_1,
                        "(-4, 5)": M_value_1 + Port_Ore,
                        "(-3, 5)": (M_value_1 + Q_value_1) * float(M_Q) + Port_Ore,
                        "(-2, 5)": ((Q_value_1 + M_value_1)* float(M_Q) + (N_value_1 + M_value_1)* float(M_N) + (N_value_1 + Q_value_1)* float(N_Q)) * 0.5,
                        "(-1, 5)": ((Q_value_1 + R_value_1)* float(Q_R) + (N_value_1 + R_value_1)* float(N_R) + (N_value_1 + Q_value_1)* float(N_Q)) * 0.5,
                        "(0, 5)": ((N_value_1 + O_value_1)* float(N_O) + (N_value_1 + R_value_1)* float(N_R) + (R_value_1 + O_value_1)* float(O_R)) * 0.5,
                        "(1, 5)": ((S_value_1 + O_value_1)* float(O_S) + (S_value_1 + R_value_1)* float(R_S) + (R_value_1 + O_value_1)* float(O_R)) * 0.5,
                        "(2, 5)": ((S_value_1 + O_value_1)* float(O_S) + (S_value_1 + P_value_1)* float(P_S) + (P_value_1 + O_value_1)* float(O_P)) * 0.5,
                        "(3, 5)": (S_value_1 + P_value_1)* float(P_S),
                        "(4, 5)": P_value_1 + Port_Lumber,
                        "(-3, 6)": Q_value_1,
                        "(-2, 6)": Q_value_1,
                        "(-1, 6)": (Q_value_1 + R_value_1) * float(Q_R) + Port_Wheat,
                        "(0, 6)": R_value_1 + Port_Wheat,
                        "(1, 6)": (R_value_1 + S_value_1) * float(R_S),
                        "(2, 6)": S_value_1 + Port_3_1,
                        "(3, 6)": S_value_1 + Port_3_1,
                        "(-7, 3)": 0,
                        "(-6, 3)": 0,
                        "(-6, 2)": 0,
                        "(-5, 2)": 0,
                        "(-5, 1)": 0,
                        "(-4, 1)": 0,
                        "(-4, 0)": 0,
                        "(-3, 0)": 0,
                        "(-2, 0)": 0,
                        "(-1, 0)": 0,
                        "(0, 0)": 0,
                        "(1, 0)": 0,
                        "(2, 0)": 0,
                        "(3, 0)": 0,
                        "(4, 0)": 0,
                        "(4, 1)": 0,
                        "(5, 1)": 0,
                        "(5, 2)": 0,
                        "(6, 2)": 0,
                        "(6, 3)": 0,
                        "(7, 3)": 0,
                        "(7, 4)": 0,
                        "(6, 4)": 0,
                        "(6, 5)": 0,
                        "(5, 5)": 0,
                        "(5, 6)": 0,
                        "(4, 6)": 0,
                        "(4, 7)": 0,
                        "(3, 7)": 0,
                        "(2, 7)": 0,
                        "(1, 7)": 0,
                        "(0, 7)": 0,
                        "(-1, 7)": 0,
                        "(-2, 7)": 0,
                        "(-3, 7)": 0,
                        "(-4, 7)": 0,
                        "(-4, 6)": 0,
                        "(-5, 6)": 0,
                        "(-5, 5)": 0,
                        "(-6, 5)": 0,
                        "(-6, 4)": 0,
                        "(-7, 4)": 0,
                        
                    }


                    for key in Spot_Values_Dict:
                        if key in Unplaceable:
                            Spot_Values_Dict[key] = 0
                        else:
                            pass

                    
                
                    if Build_1 in Spot_Values_Dict:
                        Build_1_x, Build_1_y = Build_1.split(", ")
                        Build_1_x = Build_1_x.replace("(", "")
                        Build_1_y = Build_1_y.replace(")", "")
                        print(Build_1_x)
                        print(Build_1_y)
                        Build_1_x_Left = int(Build_1_x) - 1
                        Build_1_x_Left_2 = int(Build_1_x) - 2
                        Build_1_x_Right = int(Build_1_x) + 1
                        Build_1_x_Right_2 = int(Build_1_x) + 2
                        Build_1_y_Up = int(Build_1_y) - 1
                        Build_1_y_Down = int(Build_1_y) + 1
                        if ((int(Build_1_x) % 2) == 0) and ((int(Build_1_y) % 2) != 0) or ((int(Build_1_x) % 2) != 0) and ((int(Build_1_y) % 2) == 0):
                            #up
                            Build_1_Right_2 = f"({Build_1_x_Right_2}, {Build_1_y})"
                            Build_1_Right_Down = f"({Build_1_x_Right}, {Build_1_y_Down})"
                            Road_Right = (Spot_Values_Dict.get(Build_1_Right_2)) + (Spot_Values_Dict.get(Build_1_Right_Down))
                            print("Een straat naar rechts bouwen:", round(Road_Right, 3))
                            Build_1_Left_2 = f"({Build_1_x_Left_2}, {Build_1_y})"
                            Build_1_LeftDown = f"({Build_1_x_Left}, {Build_1_y_Down})"
                            Road_Left = (Spot_Values_Dict.get(Build_1_Left_2)) + (Spot_Values_Dict.get(Build_1_LeftDown))
                            print("Een straat naar links bouwen:", round(Road_Left, 3))
                            Build_1_UpLeft = f"({Build_1_x_Left}, {Build_1_y_Up})"
                            Build_1_UpRight = f"({Build_1_x_Right}, {Build_1_y_Up})"
                            Road_Up = (Spot_Values_Dict.get(Build_1_UpLeft)) + (Spot_Values_Dict.get(Build_1_UpRight))
                            print ("Een straat omhoog bouwen:", round(Road_Up, 3))
                            break
                        else:
                            #down
                            Build_1_Left_2 = f"({Build_1_x_Left_2}, {Build_1_y})"
                            Build_1_Left_Up = f"({Build_1_x_Left}, {Build_1_y_Up})"
                            Road_Left = (Spot_Values_Dict.get(Build_1_Left_2)) + (Spot_Values_Dict.get(Build_1_Left_Up))
                            print("Een straat naar links bouwen:", round(Road_Left, 3))
                            Build_1_Right_2 = f"({Build_1_x_Right_2}, {Build_1_y})"
                            Build_1_RightUp = f"({Build_1_x_Right}, {Build_1_y_Up})"
                            Road_Right = (Spot_Values_Dict.get(Build_1_Right_2)) + (Spot_Values_Dict.get(Build_1_RightUp))
                            print("Een straat naar rechts bouwen:", round(Road_Right, 3))
                            Build_1_DownRight = f"({Build_1_x_Right}, {Build_1_y_Down})"
                            Build_1_DownLeft = f"({Build_1_x_Left}, {Build_1_y_Down})"
                            Road_Down = (Spot_Values_Dict.get(Build_1_DownRight)) + (Spot_Values_Dict.get(Build_1_DownLeft))
                            print ("Een straat naar beneden bouwen:", round(Road_Down, 3))
                            break



                        
                    else:
                        print("Foute coordinaten, formuleer ze in (X, Y)")
                else:
                    print("Foute coordinaten, formuleer ze in (X, Y)")

            

        elif turn == "2":
            Player_Number = input("Welke speler ben je? (1, 2, 3 of 4) ")
            Lumber_Production = input("Hoeveel hout productie heb je? ")
            Clay_Production = input("Hoeveel steen productie heb je? ")
            Sheep_Production = input("Hoeveel schaap productie heb je? ")
            Wheat_Production = input("Hoeveel graan productie heb je? ")
            Ore_Production = input("Hoeveel erts productie heb je? ")


            Words_Lumber = Lumber_Production.split(", ")
            Word_Count_Lumber = len(Words_Lumber)
            
            if Lumber_Production == "0":
                Lumber_Production_Value = 0

            elif Word_Count_Lumber == 1:
                Lumber_Production_Value = float(numbers.get(Lumber_Production))
                
            elif Word_Count_Lumber == 2:
                Lumber_1, Lumber_2 = Lumber_Production.split(", ")
                Lumber_Production_Value = float(numbers.get(Lumber_1)) + float(numbers.get(Lumber_2))
                
            else:
                Lumber_1, Lumber_2, Lumber_3 = Lumber_Production.split(", ")
                Lumber_Production_Value = float(numbers.get(Lumber_1)) + float(numbers.get(Lumber_2)) + float(numbers.get(Lumber_3))
                
            Words_Clay = Clay_Production.split(", ")
            Word_Count_Clay = len(Words_Clay)

            if Clay_Production == "0":
                Clay_Production_Value = 0
            
            elif Word_Count_Clay == 1:
                Clay_Production_Value = float(numbers.get(Clay_Production))
                
            elif Word_Count_Clay == 2:
                Clay_1, Clay_2 = Clay_Production.split(", ")
                Clay_Production_Value = float(numbers.get(Clay_1)) + float(numbers.get(Clay_2))
                
            else:
                Clay_1, Clay_2, Clay_3 = Clay_Production.split(", ")
                Clay_Production_Value = float(numbers.get(Clay_1)) + float(numbers.get(Clay_2)) + float(numbers.get(Clay_3))
                

            Words_Sheep = Sheep_Production.split(", ")
            Word_Count_Sheep = len(Words_Sheep)

            if Sheep_Production == "0":
                Sheep_Production_Value = 0
            
            elif Word_Count_Sheep == 1:
                Sheep_Production_Value = float(numbers.get(Sheep_Production))
                
            elif Word_Count_Sheep == 2:
                Sheep_1, Sheep_2 = Sheep_Production.split(", ")
                Sheep_Production_Value = float(numbers.get(Sheep_1)) + float(numbers.get(Sheep_2))
                
            else:
                Sheep_1, Sheep_2, Sheep_3 = Sheep_Production.split(", ")
                Sheep_Production_Value = float(numbers.get(Sheep_1)) + float(numbers.get(Sheep_2)) + float(numbers.get(Sheep_3))
                
            Words_Wheat = Wheat_Production.split(", ")
            Word_Count_Wheat = len(Words_Wheat)

            if Wheat_Production == "0":
                Wheat_Production_Value = 0
            
            elif Word_Count_Wheat == 1:
                Wheat_Production_Value = float(numbers.get(Wheat_Production))
                
            elif Word_Count_Wheat == 2:
                Wheat_1, Wheat_2 = Wheat_Production.split(", ")
                Wheat_Production_Value = float(numbers.get(Wheat_1)) + float(numbers.get(Wheat_2))
                
            else:
                Wheat_1, Wheat_2, Wheat_3 = Wheat_Production.split(", ")
                Wheat_Production_Value = float(numbers.get(Wheat_1)) + float(numbers.get(Wheat_2)) + float(numbers.get(Wheat_3))
                

            Words_Ore = Ore_Production.split(", ")
            Word_Count_Ore = len(Words_Ore)

            if Ore_Production == "0":
                Ore_Production_Value = 0
            
            elif Word_Count_Ore == 1:
                Ore_Production_Value = float(numbers.get(Ore_Production))
               
            elif Word_Count_Ore == 2:
                Ore_1, Ore_2 = Ore_Production.split(", ")
                Ore_Production_Value = float(numbers.get(Ore_1)) + float(numbers.get(Ore_2))
                
            else:
                Ore_1, Ore_2, Ore_3 = Ore_Production.split(", ")
                Ore_Production_Value = float(numbers.get(Ore_1)) + float(numbers.get(Ore_2)) + float(numbers.get(Ore_3))
                
            Lumber = 16.67
            Clay = 16.67
            Sheep = 20.83
            Wheat = 29.17
            Ore = 16.67 

            Lumber2 = 10 * (Clay_Production_Value * 0.5 * Clay + Sheep_Production_Value * 0.2 * Sheep + Wheat_Production_Value * 1/7 * Wheat)
            
            Clay2 = 10 * (Lumber_Production_Value * 0.5 * Lumber + Sheep_Production_Value * 0.2 * Sheep + Wheat_Production_Value * 1/7 * Wheat)
            
            Sheep2 = 10 * (Lumber_Production_Value * 0.25 * Lumber + Clay_Production_Value * 0.25 * Clay + Wheat_Production_Value * 2/7 * Wheat + Ore_Production_Value * 0.25 * Ore)
            
            Wheat2 = 10 * (Lumber_Production_Value * 0.25 * Lumber + Clay_Production_Value * 0.25 * Clay + Sheep_Production_Value * 0.4 * Sheep + Wheat_Production_Value * 1/7 * Wheat + Ore_Production_Value * 0.5 * Ore)
            
            Ore2 = 10 * (Sheep_Production_Value * 0.2 * Sheep + Wheat_Production_Value * 2/7 * Wheat + Ore_Production_Value * 0.25 * Ore)
            
            resources2 = {
                "L": Lumber2,
                "C": Clay2,
                "S": Sheep2,
                "W": Wheat2,
                "O": Ore2,
                "D": "0"
            }

            Port_3_1 =  0.333*(Clay_Production_Value + Lumber_Production_Value + Sheep_Production_Value + Wheat_Production_Value + Ore_Production_Value)
            Port_Lumber = Lumber_Production_Value * 0.5
            Port_Clay = Clay_Production_Value * 0.5
            Port_Sheep = Sheep_Production_Value * 0.5
            Port_Wheat = Wheat_Production_Value * 0.5
            Port_Ore = Ore_Production_Value * 0.5

            A_value_1 = float(numbers.get(numbers_A)) * float(resources2.get(resource_A))
            B_value_1 = float(numbers.get(numbers_B)) * float(resources2.get(resource_B))
            C_value_1 = float(numbers.get(numbers_C)) * float(resources2.get(resource_C))
            D_value_1 = float(numbers.get(numbers_D)) * float(resources2.get(resource_D))
            E_value_1 = float(numbers.get(numbers_E)) * float(resources2.get(resource_E))
            F_value_1 = float(numbers.get(numbers_F)) * float(resources2.get(resource_F))
            G_value_1 = float(numbers.get(numbers_G)) * float(resources2.get(resource_G))
            H_value_1 = float(numbers.get(numbers_H)) * float(resources2.get(resource_H))
            I_value_1 = float(numbers.get(numbers_I)) * float(resources2.get(resource_I))
            J_value_1 = float(numbers.get(numbers_J)) * float(resources2.get(resource_J))
            K_value_1 = float(numbers.get(numbers_K)) * float(resources2.get(resource_K))
            L_value_1 = float(numbers.get(numbers_L)) * float(resources2.get(resource_L))
            M_value_1 = float(numbers.get(numbers_M)) * float(resources2.get(resource_M))
            N_value_1 = float(numbers.get(numbers_N)) * float(resources2.get(resource_N))
            O_value_1 = float(numbers.get(numbers_O)) * float(resources2.get(resource_O))
            P_value_1 = float(numbers.get(numbers_P)) * float(resources2.get(resource_P))
            Q_value_1 = float(numbers.get(numbers_Q)) * float(resources2.get(resource_Q))
            R_value_1 = float(numbers.get(numbers_R)) * float(resources2.get(resource_R))
            S_value_1 = float(numbers.get(numbers_S)) * float(resources2.get(resource_S))


                        
            Spot_Values_Dict = {
                "(-3, 1)": A_value_1,
                "(-2, 1)": A_value_1,
                "(-1, 1)": (A_value_1 + B_value_1) * float(A_B) + Port_3_1,
                "(0, 1)": B_value_1 + Port_3_1,
                "(1, 1)": (B_value_1 + C_value_1) * float(B_C),
                "(2, 1)": C_value_1 + Port_3_1,
                "(3, 1)": C_value_1 + Port_3_1,
                "(-4, 2)": D_value_1 + Port_Sheep,
                "(-3, 2)": (A_value_1 + D_value_1) * float(A_D) + Port_Sheep,
                "(-2, 2)": ((A_value_1 + D_value_1) * float(A_D) + (A_value_1 + E_value_1) * float(A_E) + (D_value_1 + E_value_1) * float(D_E)) * 0.5,
                "(-1, 2)": ((A_value_1 + B_value_1)* float(A_B) + (A_value_1 + E_value_1) * float(A_E) + (B_value_1 + E_value_1)* float(B_E)) * 0.5,
                "(0, 2)": ((B_value_1 + E_value_1)* float(B_E) + (B_value_1 + F_value_1) * float(B_F) + (E_value_1 + F_value_1)* float(E_F)) * 0.5,
                "(1, 2)": ((B_value_1 + C_value_1)* float(B_C) + (F_value_1 + B_value_1)* float(B_F) + (C_value_1 + F_value_1)* float(C_F)) * 0.5,
                "(2, 2)": ((C_value_1 + F_value_1)* float(C_F) + (C_value_1 + G_value_1)* float(C_G) + (F_value_1 + G_value_1)* float(F_G)) * 0.5,
                "(3, 2)": (C_value_1 + G_value_1)* float(C_G),
                "(4, 2)": G_value_1 + Port_Clay,
                "(-5, 3)": H_value_1 + Port_3_1,
                "(-4, 3)": (H_value_1 + D_value_1) * float(D_H),
                "(-3, 3)": ((D_value_1 + H_value_1)* float(D_H) + (I_value_1 + H_value_1)* float(H_I) + (I_value_1 + D_value_1)* float(D_I)) * 0.5,
                "(-2, 3)": ((D_value_1 + I_value_1)* float(D_I) + (D_value_1 + E_value_1)* float(D_E) + (E_value_1 + I_value_1)* float(E_I)) * 0.5,
                "(-1, 3)": ((J_value_1 + I_value_1)* float(I_J) + (I_value_1 + E_value_1)* float(E_I) + (J_value_1 + E_value_1)* float(E_J)) * 0.5,
                "(0, 3)": ((E_value_1 + F_value_1)* float(E_F) + (J_value_1 + E_value_1)* float(E_J) + (J_value_1 + F_value_1)* float(F_J)) * 0.5,
                "(1, 3)": ((J_value_1 + F_value_1)* float(F_J) + (J_value_1 + K_value_1)* float(J_K) + (F_value_1 + K_value_1)* float(F_K)) * 0.5,
                "(2, 3)": ((K_value_1 + F_value_1)* float(F_K) + (G_value_1 + K_value_1)* float(G_K) + (F_value_1 + G_value_1)* float(F_G)) * 0.5,
                "(3, 3)": ((K_value_1 + L_value_1)* float(K_L) + (G_value_1 + L_value_1)* float(G_L) + (G_value_1 + K_value_1)* float(G_K)) * 0.5,
                "(4, 3)": (G_value_1 + L_value_1) * float(G_L) + Port_Clay,
                "(5, 3)": L_value_1,
                "(-5, 4)": H_value_1 + Port_3_1,
                "(-4, 4)": (H_value_1 + M_value_1)* float(H_M),
                "(-3, 4)": ((H_value_1 + M_value_1)* float(H_M) + (M_value_1 + I_value_1)* float(I_M) + (I_value_1 + H_value_1)* float(H_I)) * 0.5,
                "(-2, 4)": ((N_value_1 + M_value_1)* float(M_N) + (N_value_1 + I_value_1)* float(I_N) + (I_value_1 + M_value_1)* float(I_M)) * 0.5,
                "(-1, 4)": ((N_value_1 + J_value_1)* float(J_N) + (N_value_1 + I_value_1)* float(I_N) + (I_value_1 + J_value_1)* float(I_J)) * 0.5,
                "(0, 4)": ((N_value_1 + J_value_1)* float(J_N) + (J_value_1 + O_value_1)* float(J_O) + (O_value_1 + N_value_1)* float(N_O)) * 0.5,
                "(1, 4)": ((K_value_1 + J_value_1)* float(J_K) + (J_value_1 + O_value_1)* float(J_O) + (O_value_1 + K_value_1)* float(K_O)) * 0.5,
                "(2, 4)": ((K_value_1 + P_value_1)* float(K_P) + (P_value_1 + O_value_1)* float(O_P) + (O_value_1 + K_value_1)* float(K_O)) * 0.5,
                "(3, 4)": ((K_value_1 + P_value_1)* float(K_P) + (P_value_1 + L_value_1)* float(L_P) + (L_value_1 + K_value_1)* float(K_L)) * 0.5,
                "(4, 4)": (P_value_1 + L_value_1)* float(L_P) + Port_Lumber,
                "(5, 4)": L_value_1,
                "(-4, 5)": M_value_1 + Port_Ore,
                "(-3, 5)": (M_value_1 + Q_value_1) * float(M_Q) + Port_Ore,
                "(-2, 5)": ((Q_value_1 + M_value_1)* float(M_Q) + (N_value_1 + M_value_1)* float(M_N) + (N_value_1 + Q_value_1)* float(N_Q)) * 0.5,
                "(-1, 5)": ((Q_value_1 + R_value_1)* float(Q_R) + (N_value_1 + R_value_1)* float(N_R) + (N_value_1 + Q_value_1)* float(N_Q)) * 0.5,
                "(0, 5)": ((N_value_1 + O_value_1)* float(N_O) + (N_value_1 + R_value_1)* float(N_R) + (R_value_1 + O_value_1)* float(O_R)) * 0.5,
                "(1, 5)": ((S_value_1 + O_value_1)* float(O_S) + (S_value_1 + R_value_1)* float(R_S) + (R_value_1 + O_value_1)* float(O_R)) * 0.5,
                "(2, 5)": ((S_value_1 + O_value_1)* float(O_S) + (S_value_1 + P_value_1)* float(P_S) + (P_value_1 + O_value_1)* float(O_P)) * 0.5,
                "(3, 5)": (S_value_1 + P_value_1)* float(P_S),
                "(4, 5)": P_value_1 + Port_Lumber,
                "(-3, 6)": Q_value_1,
                "(-2, 6)": Q_value_1,
                "(-1, 6)": (Q_value_1 + R_value_1) * float(Q_R) + Port_Wheat,
                "(0, 6)": R_value_1 + Port_Wheat,
                "(1, 6)": (R_value_1 + S_value_1) * float(R_S),
                "(2, 6)": S_value_1 + Port_3_1,
                "(3, 6)": S_value_1 + Port_3_1,
                "(-7, 3)": 0,
                "(-6, 3)": 0,
                "(-6, 2)": 0,
                "(-5, 2)": 0,
                "(-5, 1)": 0,
                "(-4, 1)": 0,
                "(-4, 0)": 0,
                "(-3, 0)": 0,
                "(-2, 0)": 0,
                "(-1, 0)": 0,
                "(0, 0)": 0,
                "(1, 0)": 0,
                "(2, 0)": 0,
                "(3, 0)": 0,
                "(4, 0)": 0,
                "(4, 1)": 0,
                "(5, 1)": 0,
                "(5, 2)": 0,
                "(6, 2)": 0,
                "(6, 3)": 0,
                "(7, 3)": 0,
                "(7, 4)": 0,
                "(6, 4)": 0,
                "(6, 5)": 0,
                "(5, 5)": 0,
                "(5, 6)": 0,
                "(4, 6)": 0,
                "(4, 7)": 0,
                "(3, 7)": 0,
                "(2, 7)": 0,
                "(1, 7)": 0,
                "(0, 7)": 0,
                "(-1, 7)": 0,
                "(-2, 7)": 0,
                "(-3, 7)": 0,
                "(-4, 7)": 0,
                "(-4, 6)": 0,
                "(-5, 6)": 0,
                "(-5, 5)": 0,
                "(-6, 5)": 0,
                "(-6, 4)": 0,
                "(-7, 4)": 0,
                        
            }

        
            sorted_items = sorted(Spot_Values_Dict.items(), key=lambda x: x[1])

            
            
            
            if Player_Number == "4":
                while True:
                    
                    Placement_1 = input("Welke coordinaten was het eerste dorp geplaatst? ")
                    if (Placement_1 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_1) > 0 :
                        Placement_1_x, Placement_1_y = Placement_1.split(", ")
                        Placement_1_x = Placement_1_x.replace("(", "")
                        Placement_1_y = Placement_1_y.replace(")", "")
                        if ((int(Placement_1_x) % 2) == 0) and ((int(Placement_1_y) % 2) != 0) or ((int(Placement_1_x) % 2) != 0) and ((int(Placement_1_y) % 2) == 0):
                            Placement_1_x_Left = int(Placement_1_x) - 1
                            Placement_1_x_Right = int(Placement_1_x) + 1
                            Placement_1_y_Up = int(Placement_1_y) - 1
                            

                            Placement_1_Left = f"({Placement_1_x_Left}, {Placement_1_y})"
                            Placement_1_Right = f"({Placement_1_x_Right}, {Placement_1_y})"
                            Placement_1_Up = f"({Placement_1_x}, {Placement_1_y_Up})"
                            Placement_1_Down = 0

                            pass
                        else:
                            Placement_1_x_Left = int(Placement_1_x) - 1
                            Placement_1_x_Right = int(Placement_1_x) + 1
                            Placement_1_y_Down = int(Placement_1_y) + 1
                            Placement_1_y_Up = 0

                            Placement_1_Left = f"({Placement_1_x_Left}, {Placement_1_y})"
                            Placement_1_Right = f"({Placement_1_x_Right}, {Placement_1_y})"
                            Placement_1_Up = 0
                            Placement_1_Down = f"({Placement_1_x}, {Placement_1_y_Down})"

                            
                        
                        break
                    else:
                        pass

                while True:
                    
                    Placement_2 = input("Welke coordinaten was het tweede dorp geplaatst? ")
                    if (Placement_2 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_2) > 0 :
                        Placement_2_x, Placement_2_y = Placement_2.split(", ")
                        Placement_2_x = Placement_2_x.replace("(", "")
                        Placement_2_y = Placement_2_y.replace(")", "")
                        if ((int(Placement_2_x) % 2) == 0) and ((int(Placement_2_y) % 2) != 0) or ((int(Placement_2_x) % 2) != 0) and ((int(Placement_2_y) % 2) == 0):
                            Placement_2_x_Left = int(Placement_2_x) - 1
                            Placement_2_x_Right = int(Placement_2_x) + 1
                            Placement_2_y_Up = int(Placement_2_y) - 1
                            

                            Placement_2_Left = f"({Placement_2_x_Left}, {Placement_2_y})"
                            Placement_2_Right = f"({Placement_2_x_Right}, {Placement_2_y})"
                            Placement_2_Up = f"({Placement_2_x}, {Placement_2_y_Up})"
                            Placement_2_Down = 0

                            pass
                        else:
                            Placement_2_x_Left = int(Placement_2_x) - 1
                            Placement_2_x_Right = int(Placement_2_x) + 1
                            Placement_2_y_Down = int(Placement_2_y) + 1
                            Placement_2_y_Up = 0

                            Placement_2_Left = f"({Placement_2_x_Left}, {Placement_2_y})"
                            Placement_2_Right = f"({Placement_2_x_Right}, {Placement_2_y})"
                            Placement_2_Up = 0
                            Placement_2_Down = f"({Placement_2_x}, {Placement_2_y_Down})"

                            
                        
                        break
                    else:
                        pass


                while True:
                    
                    Placement_3 = input("Welke coordinaten was het derde dorp geplaatst? ")
                    if (Placement_3 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_3) > 0 :
                        Placement_3_x, Placement_3_y = Placement_3.split(", ")
                        Placement_3_x = Placement_3_x.replace("(", "")
                        Placement_3_y = Placement_3_y.replace(")", "")
                        if ((int(Placement_3_x) % 2) == 0) and ((int(Placement_3_y) % 2) != 0) or ((int(Placement_3_x) % 2) != 0) and ((int(Placement_2_y) % 2) == 0):
                            Placement_3_x_Left = int(Placement_3_x) - 1
                            Placement_3_x_Right = int(Placement_3_x) + 1
                            Placement_3_y_Up = int(Placement_3_y) - 1
                            
                            Placement_3_Left = f"({Placement_3_x_Left}, {Placement_3_y})"
                            Placement_3_Right = f"({Placement_3_x_Right}, {Placement_3_y})"
                            Placement_3_Up = f"({Placement_3_x}, {Placement_3_y_Up})"
                            Placement_3_Down = 0

                            pass
                        else:
                            Placement_3_x_Left = int(Placement_3_x) - 1
                            Placement_3_x_Right = int(Placement_3_x) + 1
                            Placement_3_y_Down = int(Placement_3_y) + 1
                            Placement_3_y_Up = 0

                            Placement_3_Left = f"({Placement_3_x_Left}, {Placement_3_y})"
                            Placement_3_Right = f"({Placement_3_x_Right}, {Placement_3_y})"
                            Placement_3_Up = 0
                            Placement_3_Down = f"({Placement_3_x}, {Placement_3_y_Down})"

                                
                            
                        break
                    else:
                        pass

                while True:
                    
                    Placement_4 = input("Welke coordinaten was het vierde dorp geplaatst? ")
                    if (Placement_4 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_4) > 0 :
                        Placement_4_x, Placement_4_y = Placement_4.split(", ")
                        Placement_4_x = Placement_4_x.replace("(", "")
                        Placement_4_y = Placement_4_y.replace(")", "")
                        if ((int(Placement_4_x) % 2) == 0) and ((int(Placement_4_y) % 2) != 0) or ((int(Placement_4_x) % 2) != 0) and ((int(Placement_4_y) % 2) == 0):
                            Placement_4_x_Left = int(Placement_4_x) - 1
                            Placement_4_x_Right = int(Placement_4_x) + 1
                            Placement_4_y_Up = int(Placement_4_y) - 1
                                

                            Placement_4_Left = f"({Placement_4_x_Left}, {Placement_4_y})"
                            Placement_4_Right = f"({Placement_4_x_Right}, {Placement_4_y})"
                            Placement_4_Up = f"({Placement_4_x}, {Placement_4_y_Up})"
                            Placement_4_Down = 0


                            Unplaceable = [Placement_1, Placement_1_Left, Placement_1_Right, Placement_1_Up, Placement_1_Down, Placement_2, Placement_2_Left, Placement_2_Right, Placement_2_Up, Placement_2_Down, Placement_3, Placement_3_Left, Placement_3_Right, Placement_3_Up, Placement_3_Down, Placement_4, Placement_4_Left, Placement_4_Right, Placement_4_Up, Placement_4_Down]
                            for spot, value in sorted_items:
                                if value == 0 or spot in Unplaceable:
                                    pass
                                else:
                                    print(f"{spot}: {round(value, 3)}")


                            pass
                        else:
                            Placement_4_x_Left = int(Placement_4_x) - 1
                            Placement_4_x_Right = int(Placement_4_x) + 1
                            Placement_4_y_Down = int(Placement_4_y) + 1
                            

                            Placement_4_Left = f"({Placement_4_x_Left}, {Placement_4_y})"
                            Placement_4_Right = f"({Placement_4_x_Right}, {Placement_4_y})"
                            Placement_4_Up = 0
                            Placement_4_Down = f"({Placement_4_x}, {Placement_4_y_Down})"


                            Unplaceable = [Placement_1, Placement_1_Left, Placement_1_Right, Placement_1_Up, Placement_1_Down, Placement_2, Placement_2_Left, Placement_2_Right, Placement_2_Up, Placement_2_Down, Placement_3, Placement_3_Left, Placement_3_Right, Placement_3_Up, Placement_3_Down, Placement_4, Placement_4_Left, Placement_4_Right, Placement_4_Up, Placement_4_Down]
                            for spot, value in sorted_items:
                                if value == 0 or spot in Unplaceable:
                                    pass
                                else:
                                    print(f"{spot}: {round(value, 3)}")

                    break
                else:
                    pass

                    
            elif Player_Number == "3":
                while True:
                    
                    Placement_1 = input("Welke coordinaten was het eerste dorp geplaatst? ")
                    if (Placement_1 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_1) > 0 :
                        Placement_1_x, Placement_1_y = Placement_1.split(", ")
                        Placement_1_x = Placement_1_x.replace("(", "")
                        Placement_1_y = Placement_1_y.replace(")", "")
                        if ((int(Placement_1_x) % 2) == 0) and ((int(Placement_1_y) % 2) != 0) or ((int(Placement_1_x) % 2) != 0) and ((int(Placement_1_y) % 2) == 0):
                            Placement_1_x_Left = int(Placement_1_x) - 1
                            Placement_1_x_Right = int(Placement_1_x) + 1
                            Placement_1_y_Up = int(Placement_1_y) - 1
                            

                            Placement_1_Left = f"({Placement_1_x_Left}, {Placement_1_y})"
                            Placement_1_Right = f"({Placement_1_x_Right}, {Placement_1_y})"
                            Placement_1_Up = f"({Placement_1_x}, {Placement_1_y_Up})"
                            Placement_1_Down = 0

                            pass
                        else:
                            Placement_1_x_Left = int(Placement_1_x) - 1
                            Placement_1_x_Right = int(Placement_1_x) + 1
                            Placement_1_y_Down = int(Placement_1_y) + 1
                            Placement_1_y_Up = 0

                            Placement_1_Left = f"({Placement_1_x_Left}, {Placement_1_y})"
                            Placement_1_Right = f"({Placement_1_x_Right}, {Placement_1_y})"
                            Placement_1_Up = 0
                            Placement_1_Down = f"({Placement_1_x}, {Placement_1_y_Down})"

                            
                        
                        break
                    else:
                        pass

                while True:
                    
                    Placement_2 = input("Welke coordinaten was het tweede dorp geplaatst? ")
                    if (Placement_2 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_2) > 0 :
                        Placement_2_x, Placement_2_y = Placement_2.split(", ")
                        Placement_2_x = Placement_2_x.replace("(", "")
                        Placement_2_y = Placement_2_y.replace(")", "")
                        if ((int(Placement_2_x) % 2) == 0) and ((int(Placement_2_y) % 2) != 0) or ((int(Placement_2_x) % 2) != 0) and ((int(Placement_2_y) % 2) == 0):
                            Placement_2_x_Left = int(Placement_2_x) - 1
                            Placement_2_x_Right = int(Placement_2_x) + 1
                            Placement_2_y_Up = int(Placement_2_y) - 1
                            

                            Placement_2_Left = f"({Placement_2_x_Left}, {Placement_2_y})"
                            Placement_2_Right = f"({Placement_2_x_Right}, {Placement_2_y})"
                            Placement_2_Up = f"({Placement_2_x}, {Placement_2_y_Up})"
                            Placement_2_Down = 0

                            pass
                        else:
                            Placement_2_x_Left = int(Placement_2_x) - 1
                            Placement_2_x_Right = int(Placement_2_x) + 1
                            Placement_2_y_Down = int(Placement_2_y) + 1
                            Placement_2_y_Up = 0

                            Placement_2_Left = f"({Placement_2_x_Left}, {Placement_2_y})"
                            Placement_2_Right = f"({Placement_2_x_Right}, {Placement_2_y})"
                            Placement_2_Up = 0
                            Placement_2_Down = f"({Placement_2_x}, {Placement_2_y_Down})"

                            
                        
                        break
                    else:
                        pass


                while True:
                    
                    Placement_3 = input("Welke coordinaten was het derde dorp geplaatst? ")
                    if (Placement_3 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_3) > 0 :
                        Placement_3_x, Placement_3_y = Placement_3.split(", ")
                        Placement_3_x = Placement_3_x.replace("(", "")
                        Placement_3_y = Placement_3_y.replace(")", "")
                        if ((int(Placement_3_x) % 2) == 0) and ((int(Placement_3_y) % 2) != 0) or ((int(Placement_3_x) % 2) != 0) and ((int(Placement_2_y) % 2) == 0):
                            Placement_3_x_Left = int(Placement_3_x) - 1
                            Placement_3_x_Right = int(Placement_3_x) + 1
                            Placement_3_y_Up = int(Placement_3_y) - 1
                            
                            Placement_3_Left = f"({Placement_3_x_Left}, {Placement_3_y})"
                            Placement_3_Right = f"({Placement_3_x_Right}, {Placement_3_y})"
                            Placement_3_Up = f"({Placement_3_x}, {Placement_3_y_Up})"
                            Placement_3_Down = 0

                            pass
                        else:
                            Placement_3_x_Left = int(Placement_3_x) - 1
                            Placement_3_x_Right = int(Placement_3_x) + 1
                            Placement_3_y_Down = int(Placement_3_y) + 1
                            Placement_3_y_Up = 0

                            Placement_3_Left = f"({Placement_3_x_Left}, {Placement_3_y})"
                            Placement_3_Right = f"({Placement_3_x_Right}, {Placement_3_y})"
                            Placement_3_Up = 0
                            Placement_3_Down = f"({Placement_3_x}, {Placement_3_y_Down})"

                                
                            
                        break
                    else:
                        pass

                while True:
                    
                    Placement_4 = input("Welke coordinaten was het vierde dorp geplaatst? ")
                    if (Placement_4 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_4) > 0 :
                        Placement_4_x, Placement_4_y = Placement_4.split(", ")
                        Placement_4_x = Placement_4_x.replace("(", "")
                        Placement_4_y = Placement_4_y.replace(")", "")
                        if ((int(Placement_4_x) % 2) == 0) and ((int(Placement_4_y) % 2) != 0) or ((int(Placement_4_x) % 2) != 0) and ((int(Placement_4_y) % 2) == 0):
                            Placement_4_x_Left = int(Placement_4_x) - 1
                            Placement_4_x_Right = int(Placement_4_x) + 1
                            Placement_4_y_Up = int(Placement_4_y) - 1
                                

                            Placement_4_Left = f"({Placement_4_x_Left}, {Placement_4_y})"
                            Placement_4_Right = f"({Placement_4_x_Right}, {Placement_4_y})"
                            Placement_4_Up = f"({Placement_4_x}, {Placement_4_y_Up})"
                            Placement_4_Down = 0

                        else:
                            Placement_4_x_Left = int(Placement_4_x) - 1
                            Placement_4_x_Right = int(Placement_4_x) + 1
                            Placement_4_y_Down = int(Placement_4_y) + 1
                            

                            Placement_4_Left = f"({Placement_4_x_Left}, {Placement_4_y})"
                            Placement_4_Right = f"({Placement_4_x_Right}, {Placement_4_y})"
                            Placement_4_Up = 0
                            Placement_4_Down = f"({Placement_4_x}, {Placement_4_y_Down})"

                        break
                    else:
                        pass
                
                while True:
                    
                    Placement_5 = input("Welke coordinaten was het vijfde dorp geplaatst? ")
                    if (Placement_5 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_5) > 0 :
                        Placement_5_x, Placement_5_y = Placement_5.split(", ")
                        Placement_5_x = Placement_5_x.replace("(", "")
                        Placement_5_y = Placement_5_y.replace(")", "")
                        if ((int(Placement_5_x) % 2) == 0) and ((int(Placement_5_y) % 2) != 0) or ((int(Placement_5_x) % 2) != 0) and ((int(Placement_5_y) % 2) == 0):
                            Placement_5_x_Left = int(Placement_5_x) - 1
                            Placement_5_x_Right = int(Placement_5_x) + 1
                            Placement_5_y_Up = int(Placement_5_y) - 1
                                

                            Placement_5_Left = f"({Placement_5_x_Left}, {Placement_5_y})"
                            Placement_5_Right = f"({Placement_5_x_Right}, {Placement_5_y})"
                            Placement_5_Up = f"({Placement_5_x}, {Placement_5_y_Up})"
                            Placement_5_Down = 0

                            Unplaceable = [Placement_1, Placement_1_Left, Placement_1_Right, Placement_1_Up, Placement_1_Down, Placement_2, Placement_2_Left, Placement_2_Right, Placement_2_Up, Placement_2_Down, Placement_3, Placement_3_Left, Placement_3_Right, Placement_3_Up, Placement_3_Down, Placement_4, Placement_4_Left, Placement_4_Right, Placement_4_Up, Placement_4_Down, Placement_5, Placement_5_Left, Placement_5_Right, Placement_5_Up, Placement_5_Down]
                            for spot, value in sorted_items:
                                if value == 0 or spot in Unplaceable:
                                    pass
                                else:
                                    print(f"{spot}: {round(value, 3)}")
                            break
                        else:
                            Placement_5_x_Left = int(Placement_5_x) - 1
                            Placement_5_x_Right = int(Placement_5_x) + 1
                            Placement_5_y_Down = int(Placement_5_y) + 1
                            

                            Placement_5_Left = f"({Placement_5_x_Left}, {Placement_5_y})"
                            Placement_5_Right = f"({Placement_5_x_Right}, {Placement_5_y})"
                            Placement_5_Up = 0
                            Placement_5_Down = f"({Placement_5_x}, {Placement_5_y_Down})"

                            Unplaceable = [Placement_1, Placement_1_Left, Placement_1_Right, Placement_1_Up, Placement_1_Down, Placement_2, Placement_2_Left, Placement_2_Right, Placement_2_Up, Placement_2_Down, Placement_3, Placement_3_Left, Placement_3_Right, Placement_3_Up, Placement_3_Down, Placement_4, Placement_4_Left, Placement_4_Right, Placement_4_Up, Placement_4_Down, Placement_5, Placement_5_Left, Placement_5_Right, Placement_5_Up, Placement_5_Down]
                            for spot, value in sorted_items:
                                if value == 0 or spot in Unplaceable:
                                    pass
                                else:
                                    print(f"{spot}: {round(value, 3)}")
                            break

                    
                else:
                    pass

            elif Player_Number == "2":
                while True:
                    
                    Placement_1 = input("Welke coordinaten was het eerste dorp geplaatst? ")
                    if (Placement_1 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_1) > 0 :
                        Placement_1_x, Placement_1_y = Placement_1.split(", ")
                        Placement_1_x = Placement_1_x.replace("(", "")
                        Placement_1_y = Placement_1_y.replace(")", "")
                        if ((int(Placement_1_x) % 2) == 0) and ((int(Placement_1_y) % 2) != 0) or ((int(Placement_1_x) % 2) != 0) and ((int(Placement_1_y) % 2) == 0):
                            Placement_1_x_Left = int(Placement_1_x) - 1
                            Placement_1_x_Right = int(Placement_1_x) + 1
                            Placement_1_y_Up = int(Placement_1_y) - 1
                            

                            Placement_1_Left = f"({Placement_1_x_Left}, {Placement_1_y})"
                            Placement_1_Right = f"({Placement_1_x_Right}, {Placement_1_y})"
                            Placement_1_Up = f"({Placement_1_x}, {Placement_1_y_Up})"
                            Placement_1_Down = 0

                            pass
                        else:
                            Placement_1_x_Left = int(Placement_1_x) - 1
                            Placement_1_x_Right = int(Placement_1_x) + 1
                            Placement_1_y_Down = int(Placement_1_y) + 1
                            Placement_1_y_Up = 0

                            Placement_1_Left = f"({Placement_1_x_Left}, {Placement_1_y})"
                            Placement_1_Right = f"({Placement_1_x_Right}, {Placement_1_y})"
                            Placement_1_Up = 0
                            Placement_1_Down = f"({Placement_1_x}, {Placement_1_y_Down})"

                            
                        
                        break
                    else:
                        pass

                while True:
                    
                    Placement_2 = input("Welke coordinaten was het tweede dorp geplaatst? ")
                    if (Placement_2 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_2) > 0 :
                        Placement_2_x, Placement_2_y = Placement_2.split(", ")
                        Placement_2_x = Placement_2_x.replace("(", "")
                        Placement_2_y = Placement_2_y.replace(")", "")
                        if ((int(Placement_2_x) % 2) == 0) and ((int(Placement_2_y) % 2) != 0) or ((int(Placement_2_x) % 2) != 0) and ((int(Placement_2_y) % 2) == 0):
                            Placement_2_x_Left = int(Placement_2_x) - 1
                            Placement_2_x_Right = int(Placement_2_x) + 1
                            Placement_2_y_Up = int(Placement_2_y) - 1
                            

                            Placement_2_Left = f"({Placement_2_x_Left}, {Placement_2_y})"
                            Placement_2_Right = f"({Placement_2_x_Right}, {Placement_2_y})"
                            Placement_2_Up = f"({Placement_2_x}, {Placement_2_y_Up})"
                            Placement_2_Down = 0

                            pass
                        else:
                            Placement_2_x_Left = int(Placement_2_x) - 1
                            Placement_2_x_Right = int(Placement_2_x) + 1
                            Placement_2_y_Down = int(Placement_2_y) + 1
                            Placement_2_y_Up = 0

                            Placement_2_Left = f"({Placement_2_x_Left}, {Placement_2_y})"
                            Placement_2_Right = f"({Placement_2_x_Right}, {Placement_2_y})"
                            Placement_2_Up = 0
                            Placement_2_Down = f"({Placement_2_x}, {Placement_2_y_Down})"

                            
                        
                        break
                    else:
                        pass


                while True:
                    
                    Placement_3 = input("Welke coordinaten was het derde dorp geplaatst? ")
                    if (Placement_3 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_3) > 0 :
                        Placement_3_x, Placement_3_y = Placement_3.split(", ")
                        Placement_3_x = Placement_3_x.replace("(", "")
                        Placement_3_y = Placement_3_y.replace(")", "")
                        if ((int(Placement_3_x) % 2) == 0) and ((int(Placement_3_y) % 2) != 0) or ((int(Placement_3_x) % 2) != 0) and ((int(Placement_2_y) % 2) == 0):
                            Placement_3_x_Left = int(Placement_3_x) - 1
                            Placement_3_x_Right = int(Placement_3_x) + 1
                            Placement_3_y_Up = int(Placement_3_y) - 1
                            
                            Placement_3_Left = f"({Placement_3_x_Left}, {Placement_3_y})"
                            Placement_3_Right = f"({Placement_3_x_Right}, {Placement_3_y})"
                            Placement_3_Up = f"({Placement_3_x}, {Placement_3_y_Up})"
                            Placement_3_Down = 0

                            pass
                        else:
                            Placement_3_x_Left = int(Placement_3_x) - 1
                            Placement_3_x_Right = int(Placement_3_x) + 1
                            Placement_3_y_Down = int(Placement_3_y) + 1
                            Placement_3_y_Up = 0

                            Placement_3_Left = f"({Placement_3_x_Left}, {Placement_3_y})"
                            Placement_3_Right = f"({Placement_3_x_Right}, {Placement_3_y})"
                            Placement_3_Up = 0
                            Placement_3_Down = f"({Placement_3_x}, {Placement_3_y_Down})"

                                
                            
                        break
                    else:
                        pass

                while True:
                    
                    Placement_4 = input("Welke coordinaten was het vierde dorp geplaatst? ")
                    if (Placement_4 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_4) > 0 :
                        Placement_4_x, Placement_4_y = Placement_4.split(", ")
                        Placement_4_x = Placement_4_x.replace("(", "")
                        Placement_4_y = Placement_4_y.replace(")", "")
                        if ((int(Placement_4_x) % 2) == 0) and ((int(Placement_4_y) % 2) != 0) or ((int(Placement_4_x) % 2) != 0) and ((int(Placement_4_y) % 2) == 0):
                            Placement_4_x_Left = int(Placement_4_x) - 1
                            Placement_4_x_Right = int(Placement_4_x) + 1
                            Placement_4_y_Up = int(Placement_4_y) - 1
                                

                            Placement_4_Left = f"({Placement_4_x_Left}, {Placement_4_y})"
                            Placement_4_Right = f"({Placement_4_x_Right}, {Placement_4_y})"
                            Placement_4_Up = f"({Placement_4_x}, {Placement_4_y_Up})"
                            Placement_4_Down = 0


                            


                            break
                        else:
                            Placement_4_x_Left = int(Placement_4_x) - 1
                            Placement_4_x_Right = int(Placement_4_x) + 1
                            Placement_4_y_Down = int(Placement_4_y) + 1
                            

                            Placement_4_Left = f"({Placement_4_x_Left}, {Placement_4_y})"
                            Placement_4_Right = f"({Placement_4_x_Right}, {Placement_4_y})"
                            Placement_4_Up = 0
                            Placement_4_Down = f"({Placement_4_x}, {Placement_4_y_Down})"

                        break
                    else:
                        pass
                        
                
                while True:
                    
                    Placement_5 = input("Welke coordinaten was het vijfde dorp geplaatst? ")
                    if (Placement_5 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_5) > 0 :
                        Placement_5_x, Placement_5_y = Placement_5.split(", ")
                        Placement_5_x = Placement_5_x.replace("(", "")
                        Placement_5_y = Placement_5_y.replace(")", "")
                        if ((int(Placement_5_x) % 2) == 0) and ((int(Placement_5_y) % 2) != 0) or ((int(Placement_5_x) % 2) != 0) and ((int(Placement_5_y) % 2) == 0):
                            Placement_5_x_Left = int(Placement_5_x) - 1
                            Placement_5_x_Right = int(Placement_5_x) + 1
                            Placement_5_y_Up = int(Placement_5_y) - 1
                                    

                            Placement_5_Left = f"({Placement_5_x_Left}, {Placement_5_y})"
                            Placement_5_Right = f"({Placement_5_x_Right}, {Placement_5_y})"
                            Placement_5_Up = f"({Placement_5_x}, {Placement_5_y_Up})"
                            Placement_5_Down = 0


                                


                                
                        else:
                            Placement_5_x_Left = int(Placement_5_x) - 1
                            Placement_5_x_Right = int(Placement_5_x) + 1
                            Placement_5_y_Down = int(Placement_5_y) + 1
                                

                            Placement_5_Left = f"({Placement_5_x_Left}, {Placement_5_y})"
                            Placement_5_Right = f"({Placement_5_x_Right}, {Placement_5_y})"
                            Placement_5_Up = 0
                            Placement_5_Down = f"({Placement_5_x}, {Placement_5_y_Down})"

                        break
                    else:
                        pass        


                                

                while True:
                    
                    Placement_6 = input("Welke coordinaten was het zesde dorp geplaatst? ")
                    if (Placement_6 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_6) > 0 :
                        Placement_6_x, Placement_6_y = Placement_6.split(", ")
                        Placement_6_x = Placement_6_x.replace("(", "")
                        Placement_6_y = Placement_6_y.replace(")", "")
                        if ((int(Placement_6_x) % 2) == 0) and ((int(Placement_6_y) % 2) != 0) or ((int(Placement_6_x) % 2) != 0) and ((int(Placement_6_y) % 2) == 0):
                            Placement_6_x_Left = int(Placement_6_x) - 1
                            Placement_6_x_Right = int(Placement_6_x) + 1
                            Placement_6_y_Up = int(Placement_6_y) - 1
                                    

                            Placement_6_Left = f"({Placement_6_x_Left}, {Placement_6_y})"
                            Placement_6_Right = f"({Placement_6_x_Right}, {Placement_6_y})"
                            Placement_6_Up = f"({Placement_6_x}, {Placement_6_y_Up})"
                            Placement_6_Down = 0


                            Unplaceable = [Placement_1, Placement_1_Left, Placement_1_Right, Placement_1_Up, Placement_1_Down, Placement_2, Placement_2_Left, Placement_2_Right, Placement_2_Up, Placement_2_Down, Placement_3, Placement_3_Left, Placement_3_Right, Placement_3_Up, Placement_3_Down, Placement_4, Placement_4_Left, Placement_4_Right, Placement_4_Up, Placement_4_Down, Placement_5, Placement_5_Left, Placement_5_Right, Placement_5_Up, Placement_5_Down, Placement_6, Placement_6_Left, Placement_6_Right, Placement_6_Up, Placement_6_Down]
                            for spot, value in sorted_items:
                                if value == 0 or spot in Unplaceable:
                                    pass
                                else:
                                    print(f"{spot}: {round(value, 3)}")


                            pass
                        else:
                            Placement_6_x_Left = int(Placement_6_x) - 1
                            Placement_6_x_Right = int(Placement_6_x) + 1
                            Placement_6_y_Down = int(Placement_6_y) + 1
                                

                            Placement_6_Left = f"({Placement_6_x_Left}, {Placement_6_y})"
                            Placement_6_Right = f"({Placement_6_x_Right}, {Placement_6_y})"
                            Placement_6_Up = 0
                            Placement_6_Down = f"({Placement_6_x}, {Placement_6_y_Down})"


                            Unplaceable = [Placement_1, Placement_1_Left, Placement_1_Right, Placement_1_Up, Placement_1_Down, Placement_2, Placement_2_Left, Placement_2_Right, Placement_2_Up, Placement_2_Down, Placement_3, Placement_3_Left, Placement_3_Right, Placement_3_Up, Placement_3_Down, Placement_4, Placement_4_Left, Placement_4_Right, Placement_4_Up, Placement_4_Down, Placement_5, Placement_5_Left, Placement_5_Right, Placement_5_Up, Placement_5_Down, Placement_6, Placement_6_Left, Placement_6_Right, Placement_6_Up, Placement_6_Down]
                            for spot, value in sorted_items:
                                if value == 0 or spot in Unplaceable:
                                    pass
                                else:
                                    print(f"{spot}: {round(value, 3)}")

                        break
                    else:
                        pass

            elif Player_Number == "1":
                
                while True:
                    
                    Placement_1 = input("Welke coordinaten was het eerste dorp geplaatst? ")
                    if (Placement_1 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_1) > 0 :
                        Placement_1_x, Placement_1_y = Placement_1.split(", ")
                        Placement_1_x = Placement_1_x.replace("(", "")
                        Placement_1_y = Placement_1_y.replace(")", "")
                        if ((int(Placement_1_x) % 2) == 0) and ((int(Placement_1_y) % 2) != 0) or ((int(Placement_1_x) % 2) != 0) and ((int(Placement_1_y) % 2) == 0):
                            Placement_1_x_Left = int(Placement_1_x) - 1
                            Placement_1_x_Right = int(Placement_1_x) + 1
                            Placement_1_y_Up = int(Placement_1_y) - 1
                            

                            Placement_1_Left = f"({Placement_1_x_Left}, {Placement_1_y})"
                            Placement_1_Right = f"({Placement_1_x_Right}, {Placement_1_y})"
                            Placement_1_Up = f"({Placement_1_x}, {Placement_1_y_Up})"
                            Placement_1_Down = 0

                            pass
                        else:
                            Placement_1_x_Left = int(Placement_1_x) - 1
                            Placement_1_x_Right = int(Placement_1_x) + 1
                            Placement_1_y_Down = int(Placement_1_y) + 1
                            Placement_1_y_Up = 0

                            Placement_1_Left = f"({Placement_1_x_Left}, {Placement_1_y})"
                            Placement_1_Right = f"({Placement_1_x_Right}, {Placement_1_y})"
                            Placement_1_Up = 0
                            Placement_1_Down = f"({Placement_1_x}, {Placement_1_y_Down})"

                            
                        
                        break
                    else:
                        pass

                while True:
                    
                    Placement_2 = input("Welke coordinaten was het tweede dorp geplaatst? ")
                    if (Placement_2 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_2) > 0 :
                        Placement_2_x, Placement_2_y = Placement_2.split(", ")
                        Placement_2_x = Placement_2_x.replace("(", "")
                        Placement_2_y = Placement_2_y.replace(")", "")
                        if ((int(Placement_2_x) % 2) == 0) and ((int(Placement_2_y) % 2) != 0) or ((int(Placement_2_x) % 2) != 0) and ((int(Placement_2_y) % 2) == 0):
                            Placement_2_x_Left = int(Placement_2_x) - 1
                            Placement_2_x_Right = int(Placement_2_x) + 1
                            Placement_2_y_Up = int(Placement_2_y) - 1
                            

                            Placement_2_Left = f"({Placement_2_x_Left}, {Placement_2_y})"
                            Placement_2_Right = f"({Placement_2_x_Right}, {Placement_2_y})"
                            Placement_2_Up = f"({Placement_2_x}, {Placement_2_y_Up})"
                            Placement_2_Down = 0

                            pass
                        else:
                            Placement_2_x_Left = int(Placement_2_x) - 1
                            Placement_2_x_Right = int(Placement_2_x) + 1
                            Placement_2_y_Down = int(Placement_2_y) + 1
                            Placement_2_y_Up = 0

                            Placement_2_Left = f"({Placement_2_x_Left}, {Placement_2_y})"
                            Placement_2_Right = f"({Placement_2_x_Right}, {Placement_2_y})"
                            Placement_2_Up = 0
                            Placement_2_Down = f"({Placement_2_x}, {Placement_2_y_Down})"

                            
                        
                        break
                    else:
                        pass


                while True:
                    
                    Placement_3 = input("Welke coordinaten was het derde dorp geplaatst? ")
                    if (Placement_3 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_3) > 0 :
                        Placement_3_x, Placement_3_y = Placement_3.split(", ")
                        Placement_3_x = Placement_3_x.replace("(", "")
                        Placement_3_y = Placement_3_y.replace(")", "")
                        if ((int(Placement_3_x) % 2) == 0) and ((int(Placement_3_y) % 2) != 0) or ((int(Placement_3_x) % 2) != 0) and ((int(Placement_2_y) % 2) == 0):
                            Placement_3_x_Left = int(Placement_3_x) - 1
                            Placement_3_x_Right = int(Placement_3_x) + 1
                            Placement_3_y_Up = int(Placement_3_y) - 1
                            
                            Placement_3_Left = f"({Placement_3_x_Left}, {Placement_3_y})"
                            Placement_3_Right = f"({Placement_3_x_Right}, {Placement_3_y})"
                            Placement_3_Up = f"({Placement_3_x}, {Placement_3_y_Up})"
                            Placement_3_Down = 0

                            pass
                        else:
                            Placement_3_x_Left = int(Placement_3_x) - 1
                            Placement_3_x_Right = int(Placement_3_x) + 1
                            Placement_3_y_Down = int(Placement_3_y) + 1
                            Placement_3_y_Up = 0

                            Placement_3_Left = f"({Placement_3_x_Left}, {Placement_3_y})"
                            Placement_3_Right = f"({Placement_3_x_Right}, {Placement_3_y})"
                            Placement_3_Up = 0
                            Placement_3_Down = f"({Placement_3_x}, {Placement_3_y_Down})"

                                
                            
                        break
                    else:
                        pass

                while True:
                    
                    Placement_4 = input("Welke coordinaten was het vierde dorp geplaatst? ")
                    if (Placement_4 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_4) > 0 :
                        Placement_4_x, Placement_4_y = Placement_4.split(", ")
                        Placement_4_x = Placement_4_x.replace("(", "")
                        Placement_4_y = Placement_4_y.replace(")", "")
                        if ((int(Placement_4_x) % 2) == 0) and ((int(Placement_4_y) % 2) != 0) or ((int(Placement_4_x) % 2) != 0) and ((int(Placement_4_y) % 2) == 0):
                            Placement_4_x_Left = int(Placement_4_x) - 1
                            Placement_4_x_Right = int(Placement_4_x) + 1
                            Placement_4_y_Up = int(Placement_4_y) - 1
                                

                            Placement_4_Left = f"({Placement_4_x_Left}, {Placement_4_y})"
                            Placement_4_Right = f"({Placement_4_x_Right}, {Placement_4_y})"
                            Placement_4_Up = f"({Placement_4_x}, {Placement_4_y_Up})"
                            Placement_4_Down = 0


                            


                            pass
                        else:
                            Placement_4_x_Left = int(Placement_4_x) - 1
                            Placement_4_x_Right = int(Placement_4_x) + 1
                            Placement_4_y_Down = int(Placement_4_y) + 1
                            

                            Placement_4_Left = f"({Placement_4_x_Left}, {Placement_4_y})"
                            Placement_4_Right = f"({Placement_4_x_Right}, {Placement_4_y})"
                            Placement_4_Up = 0
                            Placement_4_Down = f"({Placement_4_x}, {Placement_4_y_Down})"

                        break
                    else:
                        pass
                        
                
                while True:
                    
                    Placement_5 = input("Welke coordinaten was het vijfde dorp geplaatst? ")
                    if (Placement_5 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_5) > 0 :
                        Placement_5_x, Placement_5_y = Placement_5.split(", ")
                        Placement_5_x = Placement_5_x.replace("(", "")
                        Placement_5_y = Placement_5_y.replace(")", "")
                        if ((int(Placement_5_x) % 2) == 0) and ((int(Placement_5_y) % 2) != 0) or ((int(Placement_5_x) % 2) != 0) and ((int(Placement_5_y) % 2) == 0):
                            Placement_5_x_Left = int(Placement_5_x) - 1
                            Placement_5_x_Right = int(Placement_5_x) + 1
                            Placement_5_y_Up = int(Placement_5_y) - 1
                                    

                            Placement_5_Left = f"({Placement_5_x_Left}, {Placement_5_y})"
                            Placement_5_Right = f"({Placement_5_x_Right}, {Placement_5_y})"
                            Placement_5_Up = f"({Placement_5_x}, {Placement_5_y_Up})"
                            Placement_5_Down = 0


                                


                                
                        else:
                            Placement_5_x_Left = int(Placement_5_x) - 1
                            Placement_5_x_Right = int(Placement_5_x) + 1
                            Placement_5_y_Down = int(Placement_5_y) + 1
                                

                            Placement_5_Left = f"({Placement_5_x_Left}, {Placement_5_y})"
                            Placement_5_Right = f"({Placement_5_x_Right}, {Placement_5_y})"
                            Placement_5_Up = 0
                            Placement_5_Down = f"({Placement_5_x}, {Placement_5_y_Down})"

                        break
                    else:
                        pass        


                                

                while True:
                    
                    Placement_6 = input("Welke coordinaten was het zesde dorp geplaatst? ")
                    if (Placement_6 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_6) > 0 :
                        Placement_6_x, Placement_6_y = Placement_6.split(", ")
                        Placement_6_x = Placement_6_x.replace("(", "")
                        Placement_6_y = Placement_6_y.replace(")", "")
                        if ((int(Placement_6_x) % 2) == 0) and ((int(Placement_6_y) % 2) != 0) or ((int(Placement_6_x) % 2) != 0) and ((int(Placement_6_y) % 2) == 0):
                            Placement_6_x_Left = int(Placement_6_x) - 1
                            Placement_6_x_Right = int(Placement_6_x) + 1
                            Placement_6_y_Up = int(Placement_6_y) - 1
                                    

                            Placement_6_Left = f"({Placement_6_x_Left}, {Placement_6_y})"
                            Placement_6_Right = f"({Placement_6_x_Right}, {Placement_6_y})"
                            Placement_6_Up = f"({Placement_6_x}, {Placement_6_y_Up})"
                            Placement_6_Down = 0


                                


                            pass
                        else:
                            Placement_6_x_Left = int(Placement_6_x) - 1
                            Placement_6_x_Right = int(Placement_6_x) + 1
                            Placement_6_y_Down = int(Placement_6_y) + 1
                                

                            Placement_6_Left = f"({Placement_6_x_Left}, {Placement_6_y})"
                            Placement_6_Right = f"({Placement_6_x_Right}, {Placement_6_y})"
                            Placement_6_Up = 0
                            Placement_6_Down = f"({Placement_6_x}, {Placement_6_y_Down})"


                        break
                    else:
                        pass        

                while True:
                    
                    Placement_7 = input("Welke coordinaten was het zevende dorp geplaatst? ")
                    if (Placement_7 in Spot_Values_Dict.keys()) and Spot_Values_Dict.get(Placement_7) > 0 :
                        Placement_7_x, Placement_7_y = Placement_7.split(", ")
                        Placement_7_x = Placement_7_x.replace("(", "")
                        Placement_7_y = Placement_7_y.replace(")", "")
                        if ((int(Placement_7_x) % 2) == 0) and ((int(Placement_7_y) % 2) != 0) or ((int(Placement_7_x) % 2) != 0) and ((int(Placement_7_y) % 2) == 0):
                            Placement_7_x_Left = int(Placement_7_x) - 1
                            Placement_7_x_Right = int(Placement_7_x) + 1
                            Placement_7_y_Up = int(Placement_7_y) - 1
                                    

                            Placement_7_Left = f"({Placement_7_x_Left}, {Placement_7_y})"
                            Placement_7_Right = f"({Placement_7_x_Right}, {Placement_7_y})"
                            Placement_7_Up = f"({Placement_7_x}, {Placement_7_y_Up})"
                            Placement_7_Down = 0


                            Unplaceable = [Placement_1, Placement_1_Left, Placement_1_Right, Placement_1_Up, Placement_1_Down, Placement_2, Placement_2_Left, Placement_2_Right, Placement_2_Up, Placement_2_Down, Placement_3, Placement_3_Left, Placement_3_Right, Placement_3_Up, Placement_3_Down, Placement_4, Placement_4_Left, Placement_4_Right, Placement_4_Up, Placement_4_Down, Placement_5, Placement_5_Left, Placement_5_Right, Placement_5_Up, Placement_5_Down, Placement_6, Placement_6_Left, Placement_6_Right, Placement_6_Up, Placement_6_Down, Placement_7, Placement_7_Left, Placement_7_Right, Placement_7_Up, Placement_7_Down]
                            for spot, value in sorted_items:
                                if value == 0 or spot in Unplaceable:
                                    pass
                                else:
                                    print(f"{spot}: {round(value, 3)}")


                            pass
                        else:
                            Placement_7_x_Left = int(Placement_7_x) - 1
                            Placement_7_x_Right = int(Placement_7_x) + 1
                            Placement_7_y_Down = int(Placement_7_y) + 1
                                

                            Placement_7_Left = f"({Placement_7_x_Left}, {Placement_7_y})"
                            Placement_7_Right = f"({Placement_7_x_Right}, {Placement_7_y})"
                            Placement_7_Up = 0
                            Placement_7_Down = f"({Placement_7_x}, {Placement_7_y_Down})"


                            Unplaceable = [Placement_1, Placement_1_Left, Placement_1_Right, Placement_1_Up, Placement_1_Down, Placement_2, Placement_2_Left, Placement_2_Right, Placement_2_Up, Placement_2_Down, Placement_3, Placement_3_Left, Placement_3_Right, Placement_3_Up, Placement_3_Down, Placement_4, Placement_4_Left, Placement_4_Right, Placement_4_Up, Placement_4_Down, Placement_5, Placement_5_Left, Placement_5_Right, Placement_5_Up, Placement_5_Down, Placement_6, Placement_6_Left, Placement_6_Right, Placement_6_Up, Placement_6_Down, Placement_7, Placement_7_Left, Placement_7_Right, Placement_7_Up, Placement_7_Down]
                            for spot, value in sorted_items:
                                if value == 0 or spot in Unplaceable:
                                    pass
                                else:
                                    print(f"{spot}: {round(value, 3)}")

                        break
                    else:
                        pass

            else:
                print("Ongeldige speler, vul een getal tussen de 1 en 4 in.")
                sys.exit()



            while True:
                Build_1 = input("Op welke coordinaten is je tweede dorp geplaatst? ")
                if Build_1 in Spot_Values_Dict.keys() and Spot_Values_Dict.get(Build_1) > 0 :

                

                    Lumber_Production = input("Hoeveel hout productie heb je? ")
                    Clay_Production = input("Hoeveel steen productie heb je? ")
                    Sheep_Production = input("Hoeveel schaap productie heb je? ")
                    Wheat_Production = input("Hoeveel graan productie heb je? ")
                    Ore_Production = input("Hoeveel erts productie heb je? ")


                    Words_Lumber = Lumber_Production.split(", ")
                    Word_Count_Lumber = len(Words_Lumber)
                    
                    if Lumber_Production == "0":
                        Lumber_Production_Value = 0

                    elif Word_Count_Lumber == 1:
                        Lumber_Production_Value = float(numbers.get(Lumber_Production))
                        
                    elif Word_Count_Lumber == 2:
                        Lumber_1, Lumber_2 = Lumber_Production.split(", ")
                        Lumber_Production_Value = float(numbers.get(Lumber_1)) + float(numbers.get(Lumber_2))
                        
                    else:
                        Lumber_1, Lumber_2, Lumber_3 = Lumber_Production.split(", ")
                        Lumber_Production_Value = float(numbers.get(Lumber_1)) + float(numbers.get(Lumber_2)) + float(numbers.get(Lumber_3))
                        
                    Words_Clay = Clay_Production.split(", ")
                    Word_Count_Clay = len(Words_Clay)

                    if Clay_Production == "0":
                        Clay_Production_Value = 0
                    
                    elif Word_Count_Clay == 1:
                        Clay_Production_Value = float(numbers.get(Clay_Production))
                        
                    elif Word_Count_Clay == 2:
                        Clay_1, Clay_2 = Clay_Production.split(", ")
                        Clay_Production_Value = float(numbers.get(Clay_1)) + float(numbers.get(Clay_2))
                        
                    else:
                        Clay_1, Clay_2, Clay_3 = Clay_Production.split(", ")
                        Clay_Production_Value = float(numbers.get(Clay_1)) + float(numbers.get(Clay_2)) + float(numbers.get(Clay_3))
                        

                    Words_Sheep = Sheep_Production.split(", ")
                    Word_Count_Sheep = len(Words_Sheep)

                    if Sheep_Production == "0":
                        Sheep_Production_Value = 0
                    
                    elif Word_Count_Sheep == 1:
                        Sheep_Production_Value = float(numbers.get(Sheep_Production))
                        
                    elif Word_Count_Sheep == 2:
                        Sheep_1, Sheep_2 = Sheep_Production.split(", ")
                        Sheep_Production_Value = float(numbers.get(Sheep_1)) + float(numbers.get(Sheep_2))
                        
                    else:
                        Sheep_1, Sheep_2, Sheep_3 = Sheep_Production.split(", ")
                        Sheep_Production_Value = float(numbers.get(Sheep_1)) + float(numbers.get(Sheep_2)) + float(numbers.get(Sheep_3))
                        
                    Words_Wheat = Wheat_Production.split(", ")
                    Word_Count_Wheat = len(Words_Wheat)

                    if Wheat_Production == "0":
                        Wheat_Production_Value = 0
                    
                    elif Word_Count_Wheat == 1:
                        Wheat_Production_Value = float(numbers.get(Wheat_Production))
                        
                    elif Word_Count_Wheat == 2:
                        Wheat_1, Wheat_2 = Wheat_Production.split(", ")
                        Wheat_Production_Value = float(numbers.get(Wheat_1)) + float(numbers.get(Wheat_2))
                        
                    else:
                        Wheat_1, Wheat_2, Wheat_3 = Wheat_Production.split(", ")
                        Wheat_Production_Value = float(numbers.get(Wheat_1)) + float(numbers.get(Wheat_2)) + float(numbers.get(Wheat_3))
                        

                    Words_Ore = Ore_Production.split(", ")
                    Word_Count_Ore = len(Words_Ore)

                    if Ore_Production == "0":
                        Ore_Production_Value = 0
                    
                    elif Word_Count_Ore == 1:
                        Ore_Production_Value = float(numbers.get(Ore_Production))
                    
                    elif Word_Count_Ore == 2:
                        Ore_1, Ore_2 = Ore_Production.split(", ")
                        Ore_Production_Value = float(numbers.get(Ore_1)) + float(numbers.get(Ore_2))
                        
                    else:
                        Ore_1, Ore_2, Ore_3 = Ore_Production.split(", ")
                        Ore_Production_Value = float(numbers.get(Ore_1)) + float(numbers.get(Ore_2)) + float(numbers.get(Ore_3))

                    Lumber = 16.67
                    Clay = 16.67
                    Sheep = 20.83
                    Wheat = 29.17
                    Ore = 16.67 

                    Lumber2 = 10 * (Clay_Production_Value * 0.5 * Clay + Sheep_Production_Value * 0.2 * Sheep + Wheat_Production_Value * 1/7 * Wheat)
                    
                    Clay2 = 10 * (Lumber_Production_Value * 0.5 * Lumber + Sheep_Production_Value * 0.2 * Sheep + Wheat_Production_Value * 1/7 * Wheat)
                    
                    Sheep2 = 10 * (Lumber_Production_Value * 0.25 * Lumber + Clay_Production_Value * 0.25 * Clay + Wheat_Production_Value * 2/7 * Wheat + Ore_Production_Value * 0.25 * Ore)
                    
                    Wheat2 = 10 * (Lumber_Production_Value * 0.25 * Lumber + Clay_Production_Value * 0.25 * Clay + Sheep_Production_Value * 0.4 * Sheep + Wheat_Production_Value * 1/7 * Wheat + Ore_Production_Value * 0.5 * Ore)
                    
                    Ore2 = 10 * (Sheep_Production_Value * 0.2 * Sheep + Wheat_Production_Value * 2/7 * Wheat + Ore_Production_Value * 0.25 * Ore)
                    
                    resources2 = {
                        "L": Lumber2,
                        "C": Clay2,
                        "S": Sheep2,
                        "W": Wheat2,
                        "O": Ore2,
                        "D": "0"
                    }

                    Port_3_1 =  0.333*(Clay_Production_Value + Lumber_Production_Value + Sheep_Production_Value + Wheat_Production_Value + Ore_Production_Value)
                    Port_Lumber = Lumber_Production_Value * 0.5
                    Port_Clay = Clay_Production_Value * 0.5
                    Port_Sheep = Sheep_Production_Value * 0.5
                    Port_Wheat = Wheat_Production_Value * 0.5
                    Port_Ore = Ore_Production_Value * 0.5




                    A_value_1 = float(numbers.get(numbers_A)) * float(resources2.get(resource_A))
                    B_value_1 = float(numbers.get(numbers_B)) * float(resources2.get(resource_B))
                    C_value_1 = float(numbers.get(numbers_C)) * float(resources2.get(resource_C))
                    D_value_1 = float(numbers.get(numbers_D)) * float(resources2.get(resource_D))
                    E_value_1 = float(numbers.get(numbers_E)) * float(resources2.get(resource_E))
                    F_value_1 = float(numbers.get(numbers_F)) * float(resources2.get(resource_F))
                    G_value_1 = float(numbers.get(numbers_G)) * float(resources2.get(resource_G))
                    H_value_1 = float(numbers.get(numbers_H)) * float(resources2.get(resource_H))
                    I_value_1 = float(numbers.get(numbers_I)) * float(resources2.get(resource_I))
                    J_value_1 = float(numbers.get(numbers_J)) * float(resources2.get(resource_J))
                    K_value_1 = float(numbers.get(numbers_K)) * float(resources2.get(resource_K))
                    L_value_1 = float(numbers.get(numbers_L)) * float(resources2.get(resource_L))
                    M_value_1 = float(numbers.get(numbers_M)) * float(resources2.get(resource_M))
                    N_value_1 = float(numbers.get(numbers_N)) * float(resources2.get(resource_N))
                    O_value_1 = float(numbers.get(numbers_O)) * float(resources2.get(resource_O))
                    P_value_1 = float(numbers.get(numbers_P)) * float(resources2.get(resource_P))
                    Q_value_1 = float(numbers.get(numbers_Q)) * float(resources2.get(resource_Q))
                    R_value_1 = float(numbers.get(numbers_R)) * float(resources2.get(resource_R))
                    S_value_1 = float(numbers.get(numbers_S)) * float(resources2.get(resource_S))
                                
                    Spot_Values_Dict = {
                        "(-3, 1)": A_value_1,
                        "(-2, 1)": A_value_1,
                        "(-1, 1)": (A_value_1 + B_value_1) * float(A_B) + Port_3_1,
                        "(0, 1)": B_value_1 + Port_3_1,
                        "(1, 1)": (B_value_1 + C_value_1) * float(B_C),
                        "(2, 1)": C_value_1 + Port_3_1,
                        "(3, 1)": C_value_1 + Port_3_1,
                        "(-4, 2)": D_value_1 + Port_Sheep,
                        "(-3, 2)": (A_value_1 + D_value_1) * float(A_D) + Port_Sheep,
                        "(-2, 2)": ((A_value_1 + D_value_1) * float(A_D) + (A_value_1 + E_value_1) * float(A_E) + (D_value_1 + E_value_1) * float(D_E)) * 0.5,
                        "(-1, 2)": ((A_value_1 + B_value_1)* float(A_B) + (A_value_1 + E_value_1) * float(A_E) + (B_value_1 + E_value_1)* float(B_E)) * 0.5,
                        "(0, 2)": ((B_value_1 + E_value_1)* float(B_E) + (B_value_1 + F_value_1) * float(B_F) + (E_value_1 + F_value_1)* float(E_F)) * 0.5,
                        "(1, 2)": ((B_value_1 + C_value_1)* float(B_C) + (F_value_1 + B_value_1)* float(B_F) + (C_value_1 + F_value_1)* float(C_F)) * 0.5,
                        "(2, 2)": ((C_value_1 + F_value_1)* float(C_F) + (C_value_1 + G_value_1)* float(C_G) + (F_value_1 + G_value_1)* float(F_G)) * 0.5,
                        "(3, 2)": (C_value_1 + G_value_1)* float(C_G),
                        "(4, 2)": G_value_1 + Port_Clay,
                        "(-5, 3)": H_value_1 + Port_3_1,
                        "(-4, 3)": (H_value_1 + D_value_1) * float(D_H),
                        "(-3, 3)": ((D_value_1 + H_value_1)* float(D_H) + (I_value_1 + H_value_1)* float(H_I) + (I_value_1 + D_value_1)* float(D_I)) * 0.5,
                        "(-2, 3)": ((D_value_1 + I_value_1)* float(D_I) + (D_value_1 + E_value_1)* float(D_E) + (E_value_1 + I_value_1)* float(E_I)) * 0.5,
                        "(-1, 3)": ((J_value_1 + I_value_1)* float(I_J) + (I_value_1 + E_value_1)* float(E_I) + (J_value_1 + E_value_1)* float(E_J)) * 0.5,
                        "(0, 3)": ((E_value_1 + F_value_1)* float(E_F) + (J_value_1 + E_value_1)* float(E_J) + (J_value_1 + F_value_1)* float(F_J)) * 0.5,
                        "(1, 3)": ((J_value_1 + F_value_1)* float(F_J) + (J_value_1 + K_value_1)* float(J_K) + (F_value_1 + K_value_1)* float(F_K)) * 0.5,
                        "(2, 3)": ((K_value_1 + F_value_1)* float(F_K) + (G_value_1 + K_value_1)* float(G_K) + (F_value_1 + G_value_1)* float(F_G)) * 0.5,
                        "(3, 3)": ((K_value_1 + L_value_1)* float(K_L) + (G_value_1 + L_value_1)* float(G_L) + (G_value_1 + K_value_1)* float(G_K)) * 0.5,
                        "(4, 3)": (G_value_1 + L_value_1) * float(G_L) + Port_Clay,
                        "(5, 3)": L_value_1,
                        "(-5, 4)": H_value_1 + Port_3_1,
                        "(-4, 4)": (H_value_1 + M_value_1)* float(H_M),
                        "(-3, 4)": ((H_value_1 + M_value_1)* float(H_M) + (M_value_1 + I_value_1)* float(I_M) + (I_value_1 + H_value_1)* float(H_I)) * 0.5,
                        "(-2, 4)": ((N_value_1 + M_value_1)* float(M_N) + (N_value_1 + I_value_1)* float(I_N) + (I_value_1 + M_value_1)* float(I_M)) * 0.5,
                        "(-1, 4)": ((N_value_1 + J_value_1)* float(J_N) + (N_value_1 + I_value_1)* float(I_N) + (I_value_1 + J_value_1)* float(I_J)) * 0.5,
                        "(0, 4)": ((N_value_1 + J_value_1)* float(J_N) + (J_value_1 + O_value_1)* float(J_O) + (O_value_1 + N_value_1)* float(N_O)) * 0.5,
                        "(1, 4)": ((K_value_1 + J_value_1)* float(J_K) + (J_value_1 + O_value_1)* float(J_O) + (O_value_1 + K_value_1)* float(K_O)) * 0.5,
                        "(2, 4)": ((K_value_1 + P_value_1)* float(K_P) + (P_value_1 + O_value_1)* float(O_P) + (O_value_1 + K_value_1)* float(K_O)) * 0.5,
                        "(3, 4)": ((K_value_1 + P_value_1)* float(K_P) + (P_value_1 + L_value_1)* float(L_P) + (L_value_1 + K_value_1)* float(K_L)) * 0.5,
                        "(4, 4)": (P_value_1 + L_value_1)* float(L_P) + Port_Lumber,
                        "(5, 4)": L_value_1,
                        "(-4, 5)": M_value_1 + Port_Ore,
                        "(-3, 5)": (M_value_1 + Q_value_1) * float(M_Q) + Port_Ore,
                        "(-2, 5)": ((Q_value_1 + M_value_1)* float(M_Q) + (N_value_1 + M_value_1)* float(M_N) + (N_value_1 + Q_value_1)* float(N_Q)) * 0.5,
                        "(-1, 5)": ((Q_value_1 + R_value_1)* float(Q_R) + (N_value_1 + R_value_1)* float(N_R) + (N_value_1 + Q_value_1)* float(N_Q)) * 0.5,
                        "(0, 5)": ((N_value_1 + O_value_1)* float(N_O) + (N_value_1 + R_value_1)* float(N_R) + (R_value_1 + O_value_1)* float(O_R)) * 0.5,
                        "(1, 5)": ((S_value_1 + O_value_1)* float(O_S) + (S_value_1 + R_value_1)* float(R_S) + (R_value_1 + O_value_1)* float(O_R)) * 0.5,
                        "(2, 5)": ((S_value_1 + O_value_1)* float(O_S) + (S_value_1 + P_value_1)* float(P_S) + (P_value_1 + O_value_1)* float(O_P)) * 0.5,
                        "(3, 5)": (S_value_1 + P_value_1)* float(P_S),
                        "(4, 5)": P_value_1 + Port_Lumber,
                        "(-3, 6)": Q_value_1,
                        "(-2, 6)": Q_value_1,
                        "(-1, 6)": (Q_value_1 + R_value_1) * float(Q_R) + Port_Wheat,
                        "(0, 6)": R_value_1 + Port_Wheat,
                        "(1, 6)": (R_value_1 + S_value_1) * float(R_S),
                        "(2, 6)": S_value_1 + Port_3_1,
                        "(3, 6)": S_value_1 + Port_3_1,
                        "(-7, 3)": 0,
                        "(-6, 3)": 0,
                        "(-6, 2)": 0,
                        "(-5, 2)": 0,
                        "(-5, 1)": 0,
                        "(-4, 1)": 0,
                        "(-4, 0)": 0,
                        "(-3, 0)": 0,
                        "(-2, 0)": 0,
                        "(-1, 0)": 0,
                        "(0, 0)": 0,
                        "(1, 0)": 0,
                        "(2, 0)": 0,
                        "(3, 0)": 0,
                        "(4, 0)": 0,
                        "(4, 1)": 0,
                        "(5, 1)": 0,
                        "(5, 2)": 0,
                        "(6, 2)": 0,
                        "(6, 3)": 0,
                        "(7, 3)": 0,
                        "(7, 4)": 0,
                        "(6, 4)": 0,
                        "(6, 5)": 0,
                        "(5, 5)": 0,
                        "(5, 6)": 0,
                        "(4, 6)": 0,
                        "(4, 7)": 0,
                        "(3, 7)": 0,
                        "(2, 7)": 0,
                        "(1, 7)": 0,
                        "(0, 7)": 0,
                        "(-1, 7)": 0,
                        "(-2, 7)": 0,
                        "(-3, 7)": 0,
                        "(-4, 7)": 0,
                        "(-4, 6)": 0,
                        "(-5, 6)": 0,
                        "(-5, 5)": 0,
                        "(-6, 5)": 0,
                        "(-6, 4)": 0,
                        "(-7, 4)": 0,
                        
                    }

                    for key in Spot_Values_Dict:
                        if key in Unplaceable:
                            Spot_Values_Dict[key] = 0
                        else:
                            pass
                
                    if Build_1 in Spot_Values_Dict:
                        Build_1_x, Build_1_y = Build_1.split(", ")
                        Build_1_x = Build_1_x.replace("(", "")
                        Build_1_y = Build_1_y.replace(")", "")
                        print(Build_1_x)
                        print(Build_1_y)
                        Build_1_x_Left = int(Build_1_x) - 1
                        Build_1_x_Left_2 = int(Build_1_x) - 2
                        Build_1_x_Right = int(Build_1_x) + 1
                        Build_1_x_Right_2 = int(Build_1_x) + 2
                        Build_1_y_Up = int(Build_1_y) - 1
                        Build_1_y_Down = int(Build_1_y) + 1
                        if ((int(Build_1_x) % 2) == 0) and ((int(Build_1_y) % 2) != 0) or ((int(Build_1_x) % 2) != 0) and ((int(Build_1_y) % 2) == 0):
                            #up
                            Build_1_Right_2 = f"({Build_1_x_Right_2}, {Build_1_y})"
                            Build_1_Right_Down = f"({Build_1_x_Right}, {Build_1_y_Down})"
                            Road_Right = (Spot_Values_Dict.get(Build_1_Right_2)) + (Spot_Values_Dict.get(Build_1_Right_Down))
                            print("Een straat naar rechts bouwen:", round(Road_Right, 3))
                            Build_1_Left_2 = f"({Build_1_x_Left_2}, {Build_1_y})"
                            Build_1_LeftDown = f"({Build_1_x_Left}, {Build_1_y_Down})"
                            Road_Left = (Spot_Values_Dict.get(Build_1_Left_2)) + (Spot_Values_Dict.get(Build_1_LeftDown))
                            print("Een straat naar links bouwen:", round(Road_Left, 3))
                            Build_1_UpLeft = f"({Build_1_x_Left}, {Build_1_y_Up})"
                            Build_1_UpRight = f"({Build_1_x_Right}, {Build_1_y_Up})"
                            Road_Up = (Spot_Values_Dict.get(Build_1_UpLeft)) + (Spot_Values_Dict.get(Build_1_UpRight))
                            print ("Een straat naar boven bouwen:", round(Road_Up, 3))
                        else:
                            #down
                            Build_1_Left_2 = f"({Build_1_x_Left_2}, {Build_1_y})"
                            Build_1_Left_Up = f"({Build_1_x_Left}, {Build_1_y_Up})"
                            Road_Left = (Spot_Values_Dict.get(Build_1_Left_2)) + (Spot_Values_Dict.get(Build_1_Left_Up))
                            print("Een straat naar links bouwen:", round(Road_Left, 3))
                            Build_1_Right_2 = f"({Build_1_x_Right_2}, {Build_1_y})"
                            Build_1_RightUp = f"({Build_1_x_Right}, {Build_1_y_Up})"
                            Road_Right = (Spot_Values_Dict.get(Build_1_Right_2)) + (Spot_Values_Dict.get(Build_1_RightUp))
                            print("Een straat naar rechts bouwen:", round(Road_Right, 3))
                            Build_1_DownRight = f"({Build_1_x_Right}, {Build_1_y_Down})"
                            Build_1_DownLeft = f"({Build_1_x_Left}, {Build_1_y_Down})"
                            Road_Down = (Spot_Values_Dict.get(Build_1_DownRight)) + (Spot_Values_Dict.get(Build_1_DownLeft))
                            print ("Een straat naar beneden bouwen:", round(Road_Down, 3))



                        break
                    else:
                        print("Foute coordinaten, formuleer ze in (X, Y)")

                else:
                    print("Foute coordinaten, formuleer ze in (X, Y)")
            
                if Build_1 in Spot_Values_Dict:
                    Build_1_x, Build_1_y = Build_1.split(", ")
                    Build_1_x = Build_1_x.replace("(", "")
                    Build_1_y = Build_1_y.replace(")", "")
                    print(Build_1_x)
                    print(Build_1_y)
                    Build_1_x_Left = int(Build_1_x) - 1
                    Build_1_x_Left_2 = int(Build_1_x) - 2
                    Build_1_x_Right = int(Build_1_x) + 1
                    Build_1_x_Right_2 = int(Build_1_x) + 2
                    Build_1_y_Up = int(Build_1_y) - 1
                    Build_1_y_Down = int(Build_1_y) + 1
                    if ((int(Build_1_x) % 2) == 0) and ((int(Build_1_y) % 2) != 0) or ((int(Build_1_x) % 2) != 0) and ((int(Build_1_y) % 2) == 0):
                        #up
                        Build_1_Right_2 = f"({Build_1_x_Right_2}, {Build_1_y})"
                        Build_1_Right_Down = f"({Build_1_x_Right}, {Build_1_y_Down})"
                        Road_Right = (Spot_Values_Dict.get(Build_1_Right_2)) + (Spot_Values_Dict.get(Build_1_Right_Down))
                        print("Building a road right:", round(Road_Right, 3))
                        Build_1_Left_2 = f"({Build_1_x_Left_2}, {Build_1_y})"
                        Build_1_LeftDown = f"({Build_1_x_Left}, {Build_1_y_Down})"
                        Road_Left = (Spot_Values_Dict.get(Build_1_Left_2)) + (Spot_Values_Dict.get(Build_1_LeftDown))
                        print("Building a road left:", round(Road_Left, 3))
                        Build_1_UpLeft = f"({Build_1_x_Left}, {Build_1_y_Up})"
                        Build_1_UpRight = f"({Build_1_x_Right}, {Build_1_y_Up})"
                        Road_Up = (Spot_Values_Dict.get(Build_1_UpLeft)) + (Spot_Values_Dict.get(Build_1_UpRight))
                        print ("Building a road up:", round(Road_Up, 3))
                    else:
                        #down
                        Build_1_Left_2 = f"({Build_1_x_Left_2}, {Build_1_y})"
                        Build_1_Left_Up = f"({Build_1_x_Left}, {Build_1_y_Up})"
                        Road_Left = (Spot_Values_Dict.get(Build_1_Left_2)) + (Spot_Values_Dict.get(Build_1_Left_Up))
                        print("Building a road left:", round(Road_Left, 3))
                        Build_1_Right_2 = f"({Build_1_x_Right_2}, {Build_1_y})"
                        Build_1_RightUp = f"({Build_1_x_Right}, {Build_1_y_Up})"
                        Road_Right = (Spot_Values_Dict.get(Build_1_Right_2)) + (Spot_Values_Dict.get(Build_1_RightUp))
                        print("Building a road right:", round(Road_Right, 3))
                        Build_1_DownRight = f"({Build_1_x_Right}, {Build_1_y_Down})"
                        Build_1_DownLeft = f"({Build_1_x_Left}, {Build_1_y_Down})"
                        Road_Down = (Spot_Values_Dict.get(Build_1_DownRight)) + (Spot_Values_Dict.get(Build_1_DownLeft))
                        print ("Building a road down:", round(Road_Down, 3))



                    break
                else:
                    print("Invalid coordinates, please format in X, Y")
            
        else:
            print("Invalid turn")
    except IndexError: 
        print("Invalid turn") 

#Voeg hier alle resources in (L(umber), C(lay), S(heep), W(heat), O(re) and D(essert))
board_resources = {
    "A": "W",
    "B": "W",
    "C": "L" ,
    "D": "C",
    "E": "S", 
    "F": "S",
    "G": "L", 
    "H": "W",
    "I": "O" ,
    "J": "L",
    "K": "O" ,
    "L": "S",
    "M": "C" ,
    "N": "D",
    "O": "O" ,
    "P": "C",
    "Q": "L" ,
    "R": "W",
    "S": "S" ,
    }


#Voeg hier alle nummers in (Gewoon de nummers op de tiles en D(essert))
board_numbers = {
    "A": "5",
    "B": "8",
    "C": "12",
    "D": "3",
    "E": "4", 
    "F": "11",
    "G": "5", 
    "H": "9",
    "I": "2",
    "J": "9",
    "K": "6",
    "L": "11",
    "M": "10",
    "N": "D",
    "O": "10",
    "P": "3",
    "Q": "8",
    "R": "4",
    "S": "6",
    }

resource_A = (board_resources.get("A"))
resource_B = (board_resources.get("B"))
resource_C = (board_resources.get("C"))
resource_D = (board_resources.get("D"))
resource_E = (board_resources.get("E"))
resource_F = (board_resources.get("F"))
resource_G = (board_resources.get("G"))
resource_H = (board_resources.get("H"))
resource_I = (board_resources.get("I"))
resource_J = (board_resources.get("J"))
resource_K = (board_resources.get("K"))
resource_L = (board_resources.get("L"))
resource_M = (board_resources.get("M"))
resource_N = (board_resources.get("N"))
resource_O = (board_resources.get("O"))
resource_P = (board_resources.get("P"))
resource_Q = (board_resources.get("Q"))
resource_R = (board_resources.get("R"))
resource_S = (board_resources.get("S"))

numbers_A = (board_numbers.get("A"))
numbers_B = (board_numbers.get("B"))
numbers_C = (board_numbers.get("C"))
numbers_D = (board_numbers.get("D"))
numbers_E = (board_numbers.get("E"))
numbers_F = (board_numbers.get("F"))
numbers_G = (board_numbers.get("G"))
numbers_H = (board_numbers.get("H"))
numbers_I = (board_numbers.get("I"))
numbers_J = (board_numbers.get("J"))
numbers_K = (board_numbers.get("K"))
numbers_L = (board_numbers.get("L"))
numbers_M = (board_numbers.get("M"))
numbers_N = (board_numbers.get("N"))
numbers_O = (board_numbers.get("O"))
numbers_P = (board_numbers.get("P"))
numbers_Q = (board_numbers.get("Q"))
numbers_R = (board_numbers.get("R"))
numbers_S = (board_numbers.get("S"))

resources = {"L": "16.67",
             "C": "16.67",
             "S": "20.83",
             "W": "29.17",
             "O": "16.67",
             "D": "0",
}

numbers = {"D": "0",
           "2": "0.0278",
           "3": "0.0556",
           "4": "0.0833",
           "5": "0.1111",
           "6": "0.1389",
           "8": "0.1389",
           "9": "0.1111",
           "10": "0.0833",
           "11": "0.0556",
           "12": "0.0278",
           }


A_value_1 = float(numbers.get(numbers_A)) * float(resources.get(resource_A))
B_value_1 = float(numbers.get(numbers_B)) * float(resources.get(resource_B))
C_value_1 = float(numbers.get(numbers_C)) * float(resources.get(resource_C))
D_value_1 = float(numbers.get(numbers_D)) * float(resources.get(resource_D))
E_value_1 = float(numbers.get(numbers_E)) * float(resources.get(resource_E))
F_value_1 = float(numbers.get(numbers_F)) * float(resources.get(resource_F))
G_value_1 = float(numbers.get(numbers_G)) * float(resources.get(resource_G))
H_value_1 = float(numbers.get(numbers_H)) * float(resources.get(resource_H))
I_value_1 = float(numbers.get(numbers_I)) * float(resources.get(resource_I))
J_value_1 = float(numbers.get(numbers_J)) * float(resources.get(resource_J))
K_value_1 = float(numbers.get(numbers_K)) * float(resources.get(resource_K))
L_value_1 = float(numbers.get(numbers_L)) * float(resources.get(resource_L))
M_value_1 = float(numbers.get(numbers_M)) * float(resources.get(resource_M))
N_value_1 = float(numbers.get(numbers_N)) * float(resources.get(resource_N))
O_value_1 = float(numbers.get(numbers_O)) * float(resources.get(resource_O))
P_value_1 = float(numbers.get(numbers_P)) * float(resources.get(resource_P))
Q_value_1 = float(numbers.get(numbers_Q)) * float(resources.get(resource_Q))
R_value_1 = float(numbers.get(numbers_R)) * float(resources.get(resource_R))
S_value_1 = float(numbers.get(numbers_S)) * float(resources.get(resource_S))

if resource_A == resource_B:
    A_B = "0.833"
else:
    A_B = "1"
if resource_B == resource_C:
    B_C = "0.833"
else:
    B_C = "1"
if resource_A == resource_D:
    A_D = "0.833"
else:
    A_D = "1"
if resource_A == resource_E:
    A_E = "0.833"
else:
    A_E = "1"
if resource_D == resource_E:
    D_E = "0.833"
else:
    D_E = "1"
if resource_B == resource_E:
    B_E = "0.833"
else:
    B_E = "1"
if resource_E == resource_F:
    E_F = "0.833"
else:
    E_F = "1"
if resource_B == resource_F:
    B_F = "0.833"
else:
    B_F = "1"
if resource_C == resource_F:
    C_F = "0.833"
else:
    C_F = "1"
if resource_C == resource_F: 
    C_F = "0.833"
else:
    C_F = "1"
if resource_C == resource_G:
    C_G = "0.833"
else:
    C_G = "1"
if resource_G == resource_F:
    F_G = "0.833"
else:
    F_G = "1"
if resource_H == resource_D:
    D_H = "0.833"
else:
    D_H = "1"
if resource_D == resource_I:
    D_I = "0.833"
else:
    D_I = "1"
if resource_H == resource_I:
    H_I = "0.833"
else:
    H_I = "1"
if resource_E == resource_I:
    E_I = "0.833"
else:
    E_I = "1"
if resource_I == resource_J:
    I_J = "0.833"
else:
    I_J = "1"
if resource_E == resource_J:
    E_J = "0.833"
else:
    E_J = "1"
if resource_J == resource_F:
    F_J = "0.833"
else:
    F_J = "1"
if resource_J == resource_K:
    J_K = "0.833"
else:
    J_K = "1"
if resource_F == resource_K:
    F_K = "0.833"
else:
    F_K = "1"
if resource_K == resource_G:
    G_K = "0.833"
else:
    G_K = "1"
if resource_K == resource_L:
    K_L = "0.833"
else:
    K_L = "1"
if resource_G == resource_L:
    G_L = "0.833"
else:
    G_L = "1"
if resource_M == resource_Q:
    M_Q = "0.833"
else:
    M_Q = "1"
if resource_M == resource_N:
    M_N = "0.833"
else:
    M_N = "1"
if resource_N == resource_Q:
    N_Q = "0.833"
else:
    N_Q = "1"
if resource_Q == resource_R:
    Q_R = "0.833"
else:
    Q_R = "1"
if resource_N == resource_R:
    N_R = "0.833"
else:
    N_R = "1"
if resource_N == resource_O:
    N_O = "0.833"
else:
    N_O = "1"
if resource_R == resource_O:
    O_R = "0.833"
else:
    O_R = "1"
if resource_O == resource_S:
    O_S = "0.833"
else:
    O_S = "1"
if resource_R == resource_S:
    R_S = "0.833"
else:
    R_S = "1"
if resource_O == resource_P:
    O_P = "0.833"
else:
    O_P = "1"
if resource_S == resource_P:
    P_S = "0.833"
else:
    P_S = "1"
if resource_H == resource_M:
    H_M = "0.833"
else:
    H_M = "1"
if resource_I == resource_M:
    I_M = "0.833"
else:
    I_M = "1"
if resource_I == resource_N:
    I_N = "0.833"
else:
    I_N = "1"
if resource_J == resource_N:
    J_N = "0.833"
else:
    J_N = "1"
if resource_J == resource_O:
    J_O = "0.833"
else:
    J_O = "1"
if resource_O == resource_K:
    K_O = "0.833"
else:
    K_O = "1"
if resource_K == resource_P:
    K_P = "0.833"
else:
    K_P = "1"
if resource_P == resource_L:
    L_P = "0.833"
else:
    L_P = "1"


letter_to_value_map = {
    "A": A_value_1,
    "B": B_value_1,
    "C": C_value_1,
    "D": D_value_1,
    "E": E_value_1,
    "F": F_value_1,
    "G": G_value_1,
    "H": H_value_1,
    "I": I_value_1,
    "J": J_value_1,
    "K": K_value_1,
    "L": L_value_1,
    "M": M_value_1,
    "N": N_value_1,
    "O": O_value_1,
    "P": P_value_1,
    "Q": Q_value_1,
    "R": R_value_1,
    "S": S_value_1
}

if __name__ == main():
    main()
