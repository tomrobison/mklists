import yaml

def main():
    stream = file('Rulefile','r')
    config = yaml.load(stream)
    print config

def test():
    return 'success'

if __name__ == '__main__':
    main()
