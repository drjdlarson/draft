

class derivativeWriter:
    def __init__(File):

        with open(File,'r') as reader:

            dictionary = {}
            trim = {}
            LiftCoeff = {}
            DragCoeff = {}
            SideCoeff = {}
            RollCoeff = {}
            PitchCoeff = {}
            YawCoeff = {}


            for row in reader:

                if row.__contains__('MACH_o:'):
                    Mach = float(row.split()[1])
                    trim.update({'Mach':Mach})

                elif row.__contains__('ALPHA_o:'):
                    Alpha = float(row.split()[1])
                    trim.update({'Alpha':Alpha})

                elif row.__contains__('BETA_o:'):
                    Beta = float(row.split()[1])
                    trim.update({'Beta':Beta})

                elif row.__contains__('U_o:'):
                    Airspeed = float(row.split()[1])
                    trim.update({'Airspeed':Airspeed})

                elif row.__contains__('CL_'):
                    if row.__contains__('alpha'):
                        if row.__contains__('alpha_2'):
                            LiftCoeff['alpha_2'] = float(row.split()[1])
                        elif row.__contains__('alpha_dot'):
                            LiftCoeff['alpha_dot'] = float(row.split()[1]) 
                        else:
                            LiftCoeff['alpha'] = float(row.split()[1])
                    elif row.__contains__('beta'):
                        LiftCoeff['beta'] = float(row.split()[1])
                    elif row.__contains__('mach'):
                        LiftCoeff['mach'] = float(row.split()[1])
                    elif row.__contains__('p'):
                        LiftCoeff['p'] = float(row.split()[1])
                    elif row.__contains__('q'):
                        LiftCoeff['q'] = float(row.split()[1])
                    elif row.__contains__('r'):
                        LiftCoeff['r'] = float(row.split()[1])
                    elif row.__contains__('u'):
                        LiftCoeff['u'] = float(row.split()[1])
                    

                elif row.__contains__('CD_'):
                    if row.__contains__('alpha'):
                        if row.__contains__('alpha_2'):
                            DragCoeff['alpha_2'] = float(row.split()[1])
                        elif row.__contains__('alpha_dot'):
                            DragCoeff['alpha_dot'] = float(row.split()[1])
                        else:
                            DragCoeff['alpha'] = float(row.split()[1])
                    elif row.__contains__('beta'):
                        DragCoeff['beta'] = float(row.split()[1])
                    elif row.__contains__('mach'):
                        DragCoeff['mach'] = float(row.split()[1])
                    elif row.__contains__('p'):
                        DragCoeff['p'] = float(row.split()[1])
                    elif row.__contains__('q'):
                        DragCoeff['q'] = float(row.split()[1])
                    elif row.__contains__('r'):
                        DragCoeff['r'] = float(row.split()[1])
                    elif row.__contains__('u'):
                        DragCoeff['u'] = float(row.split()[1])
                    

                elif row.__contains__('CY_'):
                    if row.__contains__('alpha'):
                        if row.__contains__('alpha_2'):
                            SideCoeff['alpha_2'] = float(row.split()[1])
                        elif row.__contains__('alpha_dot'):
                            SideCoeff['alpha_dot'] = float(row.split()[1])    
                        else:
                            SideCoeff['alpha'] = float(row.split()[1])
                    elif row.__contains__('beta'):
                        SideCoeff['beta'] = float(row.split()[1])
                    elif row.__contains__('mach'):
                        SideCoeff['mach'] = float(row.split()[1])
                    elif row.__contains__('p'):
                        SideCoeff['p'] = float(row.split()[1])
                    elif row.__contains__('q'):
                        SideCoeff['q'] = float(row.split()[1])
                    elif row.__contains__('r'):
                        SideCoeff['r'] = float(row.split()[1])
                    elif row.__contains__('u'):
                        SideCoeff['u'] = float(row.split()[1])
                    

                elif row.__contains__('Cl_'):
                    if row.__contains__('alpha'):
                        if row.__contains__('alpha_2'):
                            RollCoeff['alpha_2'] = float(row.split()[1])
                        elif row.__contains__('alpha_dot'):
                            RollCoeff['alpha_dot'] = float(row.split()[1])    
                        else:
                            RollCoeff['alpha'] = float(row.split()[1])
                    elif row.__contains__('beta'):
                        RollCoeff['beta'] = float(row.split()[1])
                    elif row.__contains__('mach'):
                        RollCoeff['mach'] = float(row.split()[1])
                    elif row.__contains__('p'):
                        RollCoeff['p'] = float(row.split()[1])
                    elif row.__contains__('q'):
                        RollCoeff['q'] = float(row.split()[1])
                    elif row.__contains__('r'):
                        RollCoeff['r'] = float(row.split()[1])
                    elif row.__contains__('u'):
                        RollCoeff['u'] = float(row.split()[1])
                    

                elif row.__contains__('Cm_'):
                    if row.__contains__('alpha'):
                        if row.__contains__('alpha_2'):
                            PitchCoeff['alpha_2'] = float(row.split()[1])
                        elif row.__contains__('alpha_dot'):
                            PitchCoeff['alpha_dot'] = float(row.split()[1])
                        else:
                            PitchCoeff['alpha'] = float(row.split()[1])
                    elif row.__contains__('beta'):
                        PitchCoeff['beta'] = float(row.split()[1])
                    elif row.__contains__('mach'):
                        PitchCoeff['mach'] = float(row.split()[1])
                    elif row.__contains__('p'):
                        PitchCoeff['p'] = float(row.split()[1])
                    elif row.__contains__('q'):
                        PitchCoeff['q'] = float(row.split()[1])
                    elif row.__contains__('r'):
                        PitchCoeff['r'] = float(row.split()[1])
                    elif row.__contains__('u'):
                        PitchCoeff['u'] = float(row.split()[1])
                    

                elif row.__contains__('Cn_'):
                    if row.__contains__('alpha'):
                        if row.__contains__('alpha_2'):
                            YawCoeff['alpha_2'] = float(row.split()[1])
                        elif row.__contains__('alpha_dot'):
                            YawCoeff['alpha_dot'] = float(row.split()[1])
                            # This will be the last thing in the chunk, so update the dictionaries here:
                            dictionary.update({Alpha : [trim, LiftCoeff, DragCoeff, SideCoeff, RollCoeff, PitchCoeff, YawCoeff]})
                        else:
                            YawCoeff['alpha'] = float(row.split()[1])
                    elif row.__contains__('beta'):
                        YawCoeff['beta'] = float(row.split()[1])
                    elif row.__contains__('mach'):
                        YawCoeff['mach'] = float(row.split()[1])
                    elif row.__contains__('p'):
                        YawCoeff['p'] = float(row.split()[1])
                    elif row.__contains__('q'):
                        YawCoeff['q'] = float(row.split()[1])
                    elif row.__contains__('r'):
                        YawCoeff['r'] = float(row.split()[1])
                    elif row.__contains__('u'):
                        YawCoeff['u'] = float(row.split()[1])

        return dictionary



if __name__ == "__main__":

    file_name = "session_v0_DegenGeom.flt"

    path = "Aero\DerivativeDataFolder\\"

    dictionary = derivativeWriter.__init__(path+file_name)

    print('\n')

    print('The dictionary varies with angle of attack: ', dictionary.keys())
    
    print('\nThe trim conditions are found using index 0: ',dictionary[-2][0])

    print('\nThe CL derivatives are found using index 1: ',dictionary[-2][1])

    print('\nThe CD derivatives are found using index 2: ',dictionary[-2][2])

    print('\nThe CY derivatives are found using index 3: ',dictionary[-2][3])

    print('\nThe Cl derivatives are found using index 4: ',dictionary[-2][4])

    print('\nThe Cm derivatives are found using index 5: ',dictionary[-2][5])

    print('\nThe Cn derivatives are found using index 6: ',dictionary[-2][6])


    print('\nTo grab a value from one of these indices, include the name as a key. For example, the alpha derivative at alpha=-2 is dictionary[-2][4][''alpha'']: ',dictionary[-2][4]['alpha'])

    print('\n\n')



