#include <iostream>
#include <cstdlib>
#include <limits>

using namespace std;

/* Forward declarations */
void june_2019();
void LawnCareCostCalculator();
void passwordChecker();
void currencyConversionCalculator();
void typingSpeedAndAccuracyTest();

/* MAIN MENU */
void show_menu()
{
    cout << "|| ===== PORTFOLIO APPLICATION ===== ||\n";
    cout << "|| =====   v1.1.0 MAIN MENU    ===== ||\n\n";
    cout << "Please select an option to proceed:\n";
    cout << "1. 2025 Programs\n";
    cout << "2. 2026 Programs\n";
    cout << "3. Exit Portfolio Application\n";
}

/* 2025 SUB-MENU */
void show_2025_submenu()
{
    cout << "\n|| ===== 2025 PROGRAMS SUB-MENU ===== ||\n";
    cout << "Please select an option below:\n";
    cout << "1. Pizza Delivery Program\n";
    cout << "2. LawnCareCostCalculator Program\n";
    cout << "3. Password Checker Program\n";
    cout << "4. Currency Conversion Calculator Program\n";
    cout << "5. <-- Back to Main Menu\n";
}

void show_2026_submenu()
{
    cout << "\n|| ===== 2026 PROGRAMS SUB-MENU ===== ||\n";
    cout << "Please select an option below:\n";
    cout << "1. Typing Speed and Accuracy Test\n";
    cout << "2. <-- Back  to Main Menu\n";
}

void clearScreen()
{
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}

int main()
{
    int data;

    while (true)
    {
        clearScreen();
        show_menu();
        cout << "\n> ";
        cin >> data;

        if (cin.fail())
        {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "[X][X] CATASTROPHIC ERROR!! Invalid input.\n\n";
            continue;
        }

        if (data == 1)
        {
            while (true)
            {
                clearScreen();

                int choice;
                show_2025_submenu();
                cout << "\n> ";
                cin >> choice;

                if (cin.fail())
                {
                    cin.clear();
                    cin.ignore(numeric_limits<streamsize>::max(), '\n');
                    cout << "[!] ERROR!! Invalid input.\n\n";
                    continue;
                }

                if (choice == 1)
                    june_2019();
                else if (choice == 2)
                    LawnCareCostCalculator();
                else if (choice == 3)
                    passwordChecker();
                else if (choice == 4)
                    currencyConversionCalculator();
                else if (choice == 5)
                    break;
                else
                    cout << "[!] Invalid Selection.\n\n";

                cout << "\nPress [ENTER] to continue...";
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                cin.get();
            }
        }
        else if (data == 2)
        {
            while (true)
            {
                clearScreen();

                int choice;
                show_2026_submenu();
                cout << "\n> ";
                cin >> choice;

                if (cin.fail())
                {
                    cin.clear();
                    cin.ignore(numeric_limits<streamsize>::max(), '\n');
                    cout << "[!] Invalid input.\n\n";
                }

                if (choice == 1)
                {
                    typingSpeedAndAccuracyTest();
                }
                else if (choice == 2)
                {
                    break;
                }
                else
                {
                    cout << "[!] Invalid Selection.\n\n";
                }

                cout << "\nPress [ENTER] to continue...\n";
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                cin.get();
            }
        }
        else if (data == 3)
        {
            char confirm;
            cout << "Are you sure you want to leave the application (y/n): ";
            cin >> confirm;

            if (confirm == 'y' || confirm == 'Y')
            {
                cout << "Exiting...\n";
                exit(0);
            }
        }
        else
        {
            cout << "[!] Invalid Selection.\n\n";
        }
    }
}
