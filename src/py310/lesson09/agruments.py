import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="file name to process")
    args = parser.parse_args()
    print(args.filename)
    with open(args.filename, 'w') as f:
        f.write("hello")


if __name__ == "__main__":
    main()
