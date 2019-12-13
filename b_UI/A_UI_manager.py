from c_Logic.A_LL_API import LL_API
from b_UI.UI_employee import Employee_UI
from b_UI.UI_Aircraft import UI_Aircraft
from b_UI.UI_destination import UI_Destination
from b_UI.UI_display import Display_UI
from b_UI.UI_Voyage import voyage_UI

class Manager_UI :
    def __init__(self) :
        self.__la = LL_API()
        self.em = Employee_UI( self.__la )
        self.aircraft = UI_Aircraft(self.__la )
        self.destination = UI_Destination(self.__la)
        self.disp = Display_UI( self.__la )
        self.voyage = voyage_UI(self.__la)
        
        
    def main_menu(self) :
        ''' Displays main menu and lets the user traverse the program '''
        print("""\                                         
                                            MMMMMMMMMMM
                                       MMMMMMMMMMMMMMMMM
                                   NMMMMMMMMMMMMMMMMMMMMMMMM
                                 MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                                MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                                MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                               MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                               MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMD
                              DMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                              MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                              MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                             MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                             MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                           MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                           MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
      NM                  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
      MMMMM              MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMMMMMMMM8MMMMMMMMMIMMMMM8,. ...........OMMMMMMMMMMMMMMMMMMMMMMMMMMMM
           MMMMMMMMMMMMMMMMMMMMMMM ..N. .....~MMMM...............:MMMMNMMMMMMMMMMMMMMMMMMMMMMM
             NMMMMMMMMMMMMMMMMMMMMM.....:..DMMMMMNZ Z.... .......M$MMMMMMMMMMMMMMMMMMMMMMMMMMM
                 MMMMMMMMMMNMMMMMMM....... 7=MMMMMMO....Z .......MM7MMMMMMMMMMMMMMMMMMMMMMMMM
                    MMMMMMMMMMMMMMMMM  Z...MMMZ .. .,M..,........MMMMMMMMMMMMMMMMMMMMMMMMMMMM
                        MMMMMM.......DOM ....N7..................MMMMMMMMMMMMMMMMMMMMMMMMMMM
                           MMM....... M. ... .  ... ..............M...$MMMMMMMMMMMMMMMMMMMM
                             ........... ........~. ..............M..=....+MMMMMMMMMMMMMM
                             ......+.NMI~........ . ..............M.,.I...MMMMMMMMMMMMMMN
                             ......$... ...... O..................,.....$MMMMMMMMMMMMN
                             .....M.......... M M.. .............. 8  .OMMMMMMMMMMMN
                              ..=7I,,.,,IMI...M.................. ..MMMMMMMMMMM
                              ....DMMMMMMMMMMMMMMMO..............D...MMMMMMMMM
                               .MMMMMMMMMMMMMMDDMM:,N..............DMMMMMMMMMMM
                               NMMMMMNMM8 . .... ...,~............  MMMMMMMMM
                               MMMMM,:......::~..M8M8MM...............MMMMMM
                               MMMM ... . .........,MM..............MMMMMO$
                               MMMMM... =.=. .. . . MM ....... . ...MMMMMMM
                                NMMMMMMMMMM?  ..O.?NM7 ....... ......MMMMMM
                                 NMMMMMMMMMMMMMMMMM........  $ . ...MMMNMMM
                                  MMMMMMMMMMMMMMM.........,, ......MMMMMMMM
                                   OMMMMMMMM8 , .. .. .,N.... ...:MMMMMMMMMMN
                                    MMMMMMMM?N. ...~MD.:MNI8MMMMMMMMMMMMMMMMMN
                               MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                            NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                           MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                     MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                    NMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                   """)

        
        print("\033[94m + """"\
                                 _   _          _   _            _____ _____   
                                | \ | |   /\   | \ | |     /\   |_   _|  __ \  
                                |  \| |  /  \  |  \| |    /  \    | | | |__) | 
                                | . ` | / /\ \ | . ` |   / /\ \   | | |  _  /  
                                | |\  |/ ____ \| |\  |  / ____ \ _| |_| | \ \  
                                |_| \_/_/    \_\_| \_| /_/    \_\_____|_|  \_\ 
                                                    
                                                    
""""\033[0m + ")
        choice = ""
        while choice != "q" :
            print("-=x="*15)
            print(" "*25 +"Main Menu")
            print("-=x="*15)
            print("\nShift manager:")
            print("\t(1) - Register employee") #1
            print("\t(2) - Change employee info") #2
            print("\t(3) - Assign cabin/pilot and aircraft to voyage") #3 #4
            print("\t(4) - Display information\n")
            print("Registration manager:")
            print("\t(5) - Register destination") #5
            print("\t(6) - Register airplanes") #6
            print("\t(7) - Create voyage") #7
            print("\t(8) - Change emergency contact")
            print("\t Press Q to quit\n")
            choice = input("Select an operation with a corresponding number: ").lower()
            print()

            if choice == "1":
                self.em.register_employee_UI()
            elif choice == "2":
                self.em.change_employee_info()
            elif choice == "3":
                self.voyage.create_crew_air_voyage()
            elif choice == "4":
                self.disp.display_info()
            elif choice == "5":
                self.destination.register_destination_UI()
            elif choice == "6":
                self.aircraft.register_aircraft_UI()
            elif choice == "7":
                self.voyage.register_voyage_UI()
            elif choice == "8" :
                self.destination.change_em_info()
            elif choice == "q" :
                quit
            else:
                print("Input error! Try again")
                self.main_menu()