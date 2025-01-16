# TOPSIS Command-Line Tool

## PyPI Link

You can view the project on PyPI [here](https://pypi.org/project/topsis-payal-102203203/).

## Project Description

The **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** command-line tool implements the TOPSIS method, which is used in multi-criteria decision-making (MCDM) problems. The method ranks alternatives based on their relative closeness to the ideal solution. This package allows users to perform TOPSIS analysis on a dataset provided in a CSV format, specifying weights and impacts for each criterion.

## Features

- Normalizes the data to compare different criteria on the same scale.
- Applies weights to different criteria.
- Identifies the ideal and worst solutions for each criterion based on impact direction (`+` for benefit, `-` for cost).
- Ranks the alternatives based on their closeness to the ideal solution.

## Installation

1. Clone the repository or download the script.
2. Ensure you have the necessary Python dependencies installed:

   ```bash
   pip install numpy pandas

# How to Use

## Command-Line Usage

The tool can be run via the command line and accepts four arguments:

1. **input_file**: Path to the input CSV file containing the data.
2. **weights**: Comma-separated list of weights for each criterion.
3. **impacts**: Comma-separated list of impacts (`+` or `-`) for each criterion.
4. **output_file**: Path to save the output CSV file with the rankings and performance scores.

## Input Data Format

The input CSV file must have the following structure:

| ID  | Criterion 1 | Criterion 2 | Criterion 3 | ... |
|-----|-------------|-------------|-------------|-----|
| 1   | value       | value       | value       | ... |
| 2   | value       | value       | value       | ... |
| ... | ...         | ...         | ...         | ... |

- The first column (`ID`) should be an identifier for the alternatives.
- The subsequent columns should represent the criteria for each alternative.
- The number of criteria should be at least two.

## Running the Script

Once the input CSV file is ready, you can run the script via the command line:

```bash
python topsis.py input_file.csv "0.4,0.3,0.3" "+,+,-" output_file.csv

```
- `input_file.csv`: Path to the input CSV file containing the data.
- `"0.4,0.3,0.3"`: A comma-separated list of weights for each criterion.
- `"+,+,-"`: A comma-separated list of impacts for each criterion (`+` indicates a benefit, `-` indicates a cost).
- `output_file.csv`: Path to save the output CSV file with the rankings and performance scores.

## Output

The output file (`output_file.csv`) will contain the following columns:

- `ID`: The alternative identifier.
- The original criteria columns.
- `Score`: The performance score for each alternative.
- `Rank`: The rank based on the performance score (1 being the best).

## Example

For an input CSV file:

| ID  | Criterion 1 | Criterion 2 | Criterion 3 |
|-----|-------------|-------------|-------------|
| 1   | 7           | 8           | 6           |
| 2   | 9           | 7           | 8           |
| 3   | 6           | 5           | 7           |

And the following arguments:

```bash
python topsis.py input_file.csv "0.5,0.3,0.2" "+,-,+"