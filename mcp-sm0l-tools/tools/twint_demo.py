"""twint minimal config object demo"""

def main():
    try:
        import twint
    except Exception as e:
        print("Missing dependency or import failed:", e)
        return
    c = twint.Config()
    c.Search = "python"
    c.Limit = 1
    print("twint config ready")

if __name__ == "__main__":
    main()
