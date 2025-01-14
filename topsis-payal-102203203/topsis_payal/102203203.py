import numpy as np
import pandas as pd
import argparse
import sys

class Topsis:
    def __init__(self, data, weights, impacts):
        self.data = data
        self.weights = np.array(weights)
        self.impacts = impacts

    def normalize(self):
        norm_data = self.data / np.sqrt((self.data ** 2).sum(axis=0))
        return norm_data

    def weighted_normalized(self, norm_data):
        return norm_data * self.weights

    def ideal_best_worst(self, weighted_data):
        ideal_best = []
        ideal_worst = []
        for i in range(weighted_data.shape[1]):
            if self.impacts[i] == '+':
                ideal_best.append(weighted_data[:, i].max())
                ideal_worst.append(weighted_data[:, i].min())
            else:
                ideal_best.append(weighted_data[:, i].min())
                ideal_worst.append(weighted_data[:, i].max())
        return np.array(ideal_best), np.array(ideal_worst)

    def calculate(self):
        norm_data = self.normalize()
        weighted_data = self.weighted_normalized(norm_data)
        ideal_best, ideal_worst = self.ideal_best_worst(weighted_data)

        dist_to_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
        dist_to_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

        performance_score = dist_to_worst / (dist_to_best + dist_to_worst)
        return performance_score

def main():
    parser = argparse.ArgumentParser(description='TOPSIS Command Line Tool')
    parser.add_argument('input_file', type=str, help='Path to the input CSV file')
    parser.add_argument('weights', type=str, help='Comma-separated list of weights')
    parser.add_argument('impacts', type=str, help='Comma-separated list of impacts (+ or -)')
    parser.add_argument('output_file', type=str, help='Path to save the output CSV file')

    args = parser.parse_args()

    try:
        # Load data
        df = pd.read_csv(args.input_file)

        if df.shape[1] < 3:
            print("Input file must have at least 3 columns: ID and at least two criteria.")
            sys.exit(1)

        # Separate the criteria
        criteria_data = df.iloc[:, 1:].values
        
        # Parse weights and impacts
        weights = list(map(float, args.weights.split(',')))
        impacts = args.impacts.split(',')

        if len(weights) != criteria_data.shape[1] or len(impacts) != criteria_data.shape[1]:
            print("The number of weights and impacts must match the number of criteria.")
            sys.exit(1)

        # Validate impacts
        if not all(impact in ['+', '-'] for impact in impacts):
            print("Impacts must be '+' or '-'.")
            sys.exit(1)

        # Apply TOPSIS
        topsis = Topsis(criteria_data, weights, impacts)
        scores = topsis.calculate()

        # Add scores and rankings to the dataframe
        df['Score'] = scores
        df['Rank'] = scores.argsort()[::-1] + 1

        # Save to output file
        df.to_csv(args.output_file, index=False)
        print(f"Results saved to {args.output_file}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
