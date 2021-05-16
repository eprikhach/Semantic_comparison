import functools


@functools.total_ordering
class Version:

    def __init__(self, version):
        self.ver = version

    def __le__(self, other):
        if len(self.ver) <= len(other.ver):
            lowest = self.ver
        else:
            lowest = other.ver

        for i in range(len(lowest)):
            if len(self.ver) >= len(other.ver):
                if i == len(lowest) - 1 and self.ver[i] == other.ver[i]:
                    return True

            elif len(self.ver) < len(other.ver):
                if i == len(lowest) - 1 and self.ver[i] == other.ver[i]:
                    return False

            if self.ver[i] == other.ver[i]:
                continue

            elif self.ver[i] < other.ver[i]:
                return True

            elif self.ver[i] > other.ver[i]:
                return False

    def __neq__(self, other):
        if len(self.ver) != len(other.ver):
            return False

        for v in self.ver:
            if v == len(self.ver - 1) and self.ver[v] != other.ver[v]:
                print(self.ver, other.ver, True)
                return True

            if self.ver[v] == other.ver[v]:
                print(self.ver, other.ver, 'continue')
                continue

            elif self.ver[v] > other.ver[v] or self.ver[v] <  \
                    other.ver[v]:
                print(self.ver, other.ver, False)
                return True


def main():
    to_test = [
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0"),
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), "le failed"
        assert Version(version_2) > Version(version_1), "ge failed"
        assert Version(version_2) != Version(version_1), "neq failed"
    print('Semantic versions comparison completed successfully.')


def version_replace(string):
    arg_to_replace = {'beta': '.1', 'b': '.2', '-alpha': '.0.0',
                      '-rc': '.0.2'}
    for key in arg_to_replace.keys():
        string = string.replace(key, arg_to_replace[key])
    return string.split('.')


if __name__ == "__main__":
    main()
