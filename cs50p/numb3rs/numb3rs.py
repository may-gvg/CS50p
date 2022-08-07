def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        parts = ip.split('.')
        return len(parts) == 4 and all(0 <= int(part) < 256 for part in parts)
    except ValueError:

        return False
    except (AttributeError, TypeError):
        return False


if __name__ == "__main__":
    main()
