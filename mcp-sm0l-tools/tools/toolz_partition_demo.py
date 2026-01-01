"""toolz.partition_all demo"""

def main():
    try:
        from toolz import partition_all
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    print(list(partition_all(3, range(10))))

if __name__ == "__main__":
    main()
