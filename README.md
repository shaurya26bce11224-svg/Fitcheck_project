# FitCheck: Your Personal BMI, BMR & Calorie Companion

A small command-line tool I built in Python that answers the four questions people usually google when they start caring about their health: *What's my BMI? How many calories does my body burn at rest? How many do I burn in a whole day? And roughly how much of me is fat?*

You type in a few numbers, pick an option from a menu, and NutriFit does the maths and tells you the result in plain English.

---

## Overview

Most people know the formulas for BMI or BMR exist, but very few remember them (or want to punch them into a calculator every time). Fitcheck puts the well-known formulas behind a simple menu so anyone can get a quick estimate without needing any technical background.

It runs entirely in the terminal, needs no internet, and stores nothing, so your numbers stay on your machine.

## Features

| # | Module | What it does |
|---|--------|--------------|
| 1 | **BMI calculator** | Takes height (metres) and weight (kg), calculates BMI and tells you whether that falls under underweight, healthy, overweight or obese. |
| 2 | **BMR calculator** | Uses the Mifflin-St Jeor equation (separate versions for male and female) to estimate calories your body burns at complete rest. |
| 3 | **TDEE calculator** | Works out BMR first, then multiplies it by an activity factor (Sedentary to Extra Active) to estimate your total daily calorie burn. |
| 4 | **Body fat estimator** | Uses your BMI and age with the Deurenberg formulas, with separate versions for adult men, adult women, boys and girls. |
| 0 | **Exit** | Closes the program politely. |

The menu keeps looping after every calculation, so you can run several checks in one sitting.

## Technologies Used

- **Python 3** (no third-party libraries needed, only built-in `input()` and `print()`)
- **Git & GitHub** for version control
- Any terminal, IDLE, VS Code or PyCharm to run it

## Project Structure

```
fitcheck/
├── Fitcheck_Project.py   # main program (menu + calculation functions)
├── README.md             # this file
├── statement.md          # problem statement, scope, users, features
└── report/
    └── Fitcheck_Project_Report.pdf
```

## How to Install & Run

1. Make sure Python 3.8 or newer is installed. You can check with:
   ```bash
   python --version
   ```
2. Clone the repository (or just download the ZIP):
   ```bash
   git clone https://github.com/shaurya26bce11224-svg/Fitcheck_project.git
   cd Fitcheck_project
   ```
3. Run the program:
   ```bash
   python Fitcheck_Project.py
   ```
4. Type the number of the option you want and follow the prompts.

### A few things to know while typing inputs

- **BMI (option 1):** height in **metres** (e.g. `1.75`), weight in **kg**.
- **BMR / TDEE (options 2 and 3):** height in **centimetres** (e.g. `175`), weight in **kg**, age in years. Gender must be typed as `male` or `female` (lowercase).
- **Activity level (option 3):** type it exactly as one of `Sedentary`, `Lightly Active`, `Moderately Active`, `Very Active`, `Extra Active`.
- **Body fat (option 4):** height in **metres**, weight in kg, and the person's group typed exactly as `Adult male`, `Adult female`, `Boy` or `Girl`.

## Testing

I tested Fitcheck by running it with inputs where I could work out the answer by hand and then comparing. No test framework is needed; you can repeat these yourself:

| Option | Input | Expected | What NutriFit gave |
|--------|-------|----------|--------------------|
| BMI | 1.75 m, 70 kg | about 22.86, healthy weight | 22.857..., healthy weight |
| BMR (male) | 175 cm, 70 kg, 25 yrs | 1673.75 kcal/day | 1673.75 |
| BMR (female) | 165 cm, 60 kg, 22 yrs | 1360.25 kcal/day | 1360.25 |
| TDEE | male, 175 cm, 70 kg, 25 yrs, Moderately Active | 1673.75 x 1.55 = 2594.31 | 2594.3125 |
| Body fat (adult male) | 1.75 m, 70 kg, 25 yrs | about 16.98 % | 16.978... % |
| Body fat (adult female) | 1.65 m, 60 kg, 22 yrs | about 26.31 % | 26.306... % |
| Invalid menu choice | `9` | asks for a valid choice | "Enter a valid choice" |

To run one quickly without typing, you can pipe the inputs in:

```bash
printf '1\n1.75\n70\n0\n' | python Fitcheck_Project.py
```

## Sample Output

```
=========================================
1. BMI(Body Mass Calculator)
2. BMR(Basal Metabolic Rate)
3. TDEE(Total Daily Energy Expenditure)
4. Bodyfat
0. Exit
=========================================
Enter a choice:1
Enter height in metre:1.75
Enter weight:70
BMI is 22.857142857142858 kg/m² and the person is healthy weight
```

## Known Limitations (being honest here)

- Typing letters where a number is expected (for example `abc` at the menu) crashes the program with a `ValueError`. Input validation is on my to-do list.
- Text inputs like `male` or `Moderately Active` are case-sensitive.
- The units differ between modules (metres for BMI and body fat, centimetres for BMR and TDEE), so you need to read the prompt carefully.
- BMI and body-fat estimates are general guides, not medical diagnoses. Athletes and very muscular people can get misleading results.

## Future Improvements

Input validation and retry loops, a single consistent unit system, splitting the code into separate modules with unit tests, saving history to a file, and maybe a simple GUI.

## Disclaimer

Fitcheckis a student project built for learning. It gives estimates only and is **not** a substitute for advice from a doctor or a registered dietitian.
## Screenshot
<img width="1600" height="900" alt="WhatsApp Image 2026-09-28 at 22 52 13" src="https://github.com/user-attachments/assets/191045b9-a7f0-4694-b1b5-362e01ec3c8c" />
<img width="1600" height="900" alt="WhatsApp Image 2026-09-28 at 22 52 13 (2)" src="https://github.com/user-attachments/assets/013f872b-1b1f-4f73-9709-bf42dfcf78dd" />
<img width="1600" height="900" alt="WhatsApp Image 2026-09-28 at 22 52 13 (1)" src="https://github.com/user-attachments/assets/d02ad2db-0df7-401e-a06a-f02035661a81" />
## Author

**[Shaurya Vashishtha]** | Reg. No. [26BCE11224] | [introduction to problem solving and programming], VIT
