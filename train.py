import argparse
import sys
import generate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", help="path to the directory "
                                            "with source files")
    parser.add_argument("--model", help="path to save")
    parser.add_argument("--lc", help="lowercase")
    args = parser.parse_args()
    file = None
    model = dict()
    if args.input_dir:
        file = open(args.input_dir, "r")
    else:
        file = sys.stdin
    while True:
        line = str(file.readline())

        if not line:
            break

        if args.lc is not None:
            line = line.lower()

        chars = []
        for i in range(len(line)):
            if line[i].isalpha() or line[i] == " ":
                chars.append(line[i])
        clean_string = "".join(chars)
        words_list = clean_string.split()
        generate.make_higher_order_markov_model(model, 1, words_list)
    print(generate.generate_random_sentence(7, model))
    print(generate.generate_random_sentence(3, model))
    print(generate.generate_random_sentence(4, model))


if __name__ == "__main__":
    main()
