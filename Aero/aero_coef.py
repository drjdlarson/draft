# global variables
TRIM_KEYS = ['Mach_o', 'ALPHA_o', 'BETA_o', 'U_o']

BASE_KEYS = ['CLo', 'CDo', 'CYo', 'Clo', 'Cmo', 'Cno']

DERIVATIVE_KEYS = ['CL_alpha', 'CL_beta', 'CL_mach', 'CL_p', 'CL_q', 'CL_r', 'CL_u', 'CL_alpha_2', 'CL_alpha_dot', 'CD_alpha', 'CD_beta', 'CD_mach', 'CD_p', 'CD_q', 'CD_r', 'CD_u', 'CD_alpha_2', 'CD_alpha_dot', 'CY_alpha', 'CY_beta', 'CY_mach', 'CY_p', 'CY_q', 'CY_r', 'CY_u', 'CY_alpha_2', 'CY_alpha_dot', 'Cl_alpha', 'Cl_beta', 'Cl_mach', 'Cl_p', 'Cl_q', 'Cl_r', 'Cl_u', 'Cl_alpha_2', 'Cl_alpha_dot', 'Cm_alpha', 'Cm_beta', 'Cm_mach', 'Cm_p', 'Cm_q', 'Cm_r', 'Cm_u', 'Cm_alpha_2', 'Cm_alpha_dot', 'Cn_alpha', 'Cn_beta', 'Cn_mach', 'Cn_p', 'Cn_q', 'Cn_r', 'Cn_u', 'Cn_alpha_2', 'Cn_alpha_dot']


class StabilityCoefAndDerivatives:
    """Main Class to Handle data management from .stab files"""
    def __init__(self, file):
        
        self.trim_conditions = []
        self.new_trim = None

        with open(file) as fin:
            lines = fin.readlines()

            for line_num, line in enumerate(lines):
                
                if line.__contains__("###########"):
                    
                    # saves the TrimPoint instance in a list attribute trim_conditions 
                    if self.new_trim is not None:
                        self.trim_conditions.append(self.new_trim)

                    # create a new TrimPoint instance every time ###### are found.
                    self.new_trim = TrimPoint()
                
                else:

                    # make sure a new TrimPoint instance is created
                    if self.new_trim is not None:

                        # handle empty lines
                        if line.strip():
                        
                            split_strings = line.split()
                            keyname = (split_strings[0]).split(':')[0]
                            val = split_strings[1]

                            # read the values and save it as dict pairs 
                            if keyname in BASE_KEYS:
                                self.new_trim.base.update({keyname: val})
                            elif keyname in DERIVATIVE_KEYS:
                                self.new_trim.derivatives.update({keyname: val})
                            elif keyname in TRIM_KEYS:
                                self.new_trim.trim.update({keyname: val})
                            else:
                                pass
                                
            
class TrimPoint:
    """Handle data storage for each trim point"""
    def __init__(self):
        self.trim = {}
        self.base = {}
        self.derivatives = {}


if __name__ == "__main__":

    file = 'Aero\DerivativeDataFolder\session_v0_DegenGeom.flt'

    # main instance of the class
    stab_data = StabilityCoefAndDerivatives(file)

    # print(stab_data.trim_conditions)

    print("4th trim point Cn0 base value: {}\n".format(stab_data.trim_conditions[3].base['Cno']))
    print("6th trim point Clq derivative {}".format(stab_data.trim_conditions[5].derivatives['Cl_q']))
