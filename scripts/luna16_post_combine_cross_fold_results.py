import json
import csv
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Combine JSON results into a CSV file.")
    parser.add_argument(
        "-i",
        "--input",
        nargs="+",
        default=[],
        help="input json files",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="output csv file",
    )

    args = parser.parse_args()

    in_json_list = args.input
    out_csv = args.output

    # Open the output CSV file for writing
    with open(out_csv, "w", newline="") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["seriesuid", "coordX", "coordY", "coordZ", "probability"])

        # Iterate through the input JSON files
        for in_json in in_json_list:
            # Check if the JSON file exists
            if os.path.exists(in_json):
                with open(in_json, "r") as json_file:
                    result = json.load(json_file)
                    for subj in result["validation"]:
                        seriesuid = os.path.split(subj["image"])[-1][:-4]
                        for b in range(len(subj["box"])):
                            spamwriter.writerow([seriesuid] + subj["box"][b][0:3] + [subj["score"][b]])
            else:
                print(f"Warning: The file {in_json} does not exist and will be skipped.")

if __name__ == "__main__":
    main()
