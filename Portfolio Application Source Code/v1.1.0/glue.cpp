#include <iostream>
#include <string>
#include <map>
#include <iomanip>
#include <algorithm>
#include <cctype>
#include <cstdlib>
#include <ctime>
#include <chrono>

using namespace std;

void june_2019()
{
    map<string, double> pizzaPrices{
        {"small", 3.25},
        {"medium", 5.50},
        {"large", 7.15}
    };

    map<int, double> toppingPrices{
        {0, 0}, {1, 0.75}, {2, 1.35}, {3, 2.00}, {4, 2.50}
    };

    string name, address, size;
    string contact;
    int numPizzas, toppings;
    char delivery;
    double deliveryCharge = 2.50;

    do {
        cout << "Enter customer name: ";
        cin >> name;
    } while (!isalpha(name[0]));

    cin.ignore();
    cout << "Enter address: ";
    getline(cin, address);

    do {
        cout << "Enter contact number: ";
        cin >> contact;
    } while (!isdigit(contact[0]));

    do {
        cout << "How many pizzas (1–6): ";
        cin >> numPizzas;
    } while (numPizzas < 1 || numPizzas > 6);

    do {
        cout << "Pizza size (small/medium/large): ";
        cin >> size;
    } while (!pizzaPrices.count(size));

    do {
        cout << "Extra toppings (0–4): ";
        cin >> toppings;
    } while (toppings < 0 || toppings > 4);

    cout << "Delivery? (y/n): ";
    cin >> delivery;

    double standardCost =
        (pizzaPrices[size] * numPizzas) + toppingPrices[toppings];

    if (standardCost > 20)
        standardCost *= 0.9;

    if (delivery == 'y' || delivery == 'Y')
        standardCost += deliveryCharge;

    cout << fixed << setprecision(2);
    cout << "\nTOTAL COST: £" << standardCost << "\n";
}

void LawnCareCostCalculator()
{
    double luxury = 1.15, standard = 0.80, economy = 0.45;
    string name, address, contact, quality;
    int width, length;

    cout << "Customer name: ";
    cin >> name;

    cout << "Address: ";
    cin.ignore();
    getline(cin, address);

    cout << "Contact info: ";
    cin >> contact;

    do {
        cout << "Lawn width (2–30): ";
        cin >> width;
    } while (width < 2 || width > 30);

    do {
        cout << "Lawn length (2–50): ";
        cin >> length;
    } while (length < 2 || length > 50);

    int area = width * length;

    cout << "Product (Luxury/Standard/Economy): ";
    cin >> quality;

    double rate =
        (quality == "Luxury") ? luxury :
        (quality == "Standard") ? standard : economy;

    double total = area * 0.5 * rate;

    cout << fixed << setprecision(2);
    cout << "Total cost: £" << total << endl;
}

void passwordChecker()
{
    string pw;
    cout << "Enter password: ";
    cin >> pw;

    int lower = 0, upper = 0, digits = 0, special = 0;

    for (char c : pw)
    {
        if (islower(c)) lower++;
        else if (isupper(c)) upper++;
        else if (isdigit(c)) digits++;
        else special++;
    }

    int points = lower * 5 + upper * 5 + digits * 10 + special * 10;

    cout << "\nPassword score: " << points << endl;
}

void currencyConversionCalculator()
{
    double GBP;
    cout << "Enter GBP amount: ";
    cin >> GBP;

    string currency;
    cout << "Convert to (USD/EUR/BRL/JPY/TRY): ";
    cin >> currency;

    map<string, double> rates{
        {"USD",1.40},{"EUR",1.14},{"BRL",4.77},{"JPY",151.05},{"TRY",5.68}
    };

    if (!rates.count(currency))
    {
        cout << "Invalid currency\n";
        return;
    }

    double converted = GBP * rates[currency];
    cout << fixed << setprecision(2);
    cout << "Converted amount: " << converted << endl;
}

void typingSpeedAndAccuracyTest()
{
    string firstname, lastname;

    cout << "Enter first name: ";
    cin >> firstname;

    cout << "Enter last name: ";
    cin >> lastname;

    const string alphabet =
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz";

    const int score = 30;
    string target;

    srand(static_cast<unsigned int>(time(nullptr)));

    // generate random string
    for (int i = 0; i < score; i++)
    {
        target += alphabet[rand() % alphabet.length()];
    }

    cout << "\nType the following as quickly and as accurately as you can:\n";
    cout << target << "\n\n";

    cin.ignore(); // clear newline
    auto start = chrono::high_resolution_clock::now();

    string data;
    cout << "> ";
    getline(cin, data);

    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> time_taken = end - start;

    int correct = 0;
    for (size_t i = 0; i < min(target.length(), data.length()); i++)
    {
        if (target[i] == data[i])
            correct++;
    }

    double accuracy = (static_cast<double>(correct) / score) * 100.0;

    cout << "\n|== RESULTS ==|\n\n";
    cout << "First Name: " << firstname << "\n";
    cout << "Last Name: " << lastname << "\n";
    cout << "Time Taken: " << time_taken.count() << " seconds\n";
    cout << "Correct Letters: " << correct << " / " << score << "\n";
    cout << "Accuracy: " << accuracy << "%\n";
}
