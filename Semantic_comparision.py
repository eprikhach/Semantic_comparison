"""In this task we will work with semantic versions comparison, using
python OOP.

Development steps:
1. Override magic comparison methods __lt__ and __ne__.
2. Import functools module, which implement other comparison methods.
3. Convert string representation of the version to list.

Converting and comparison rules:
0 = release version.
1 = strong pre-release = alpha/a/-a .
2 = beta version = beta/b/-b .
3 = release candidate version = rc/-rc .

Version consists of 3 main fields(Major, Minor, Patch) and number
of pre-builds.
Example: 1.0.2.9.3 (1 - Major version, 0 - Minor version, 2 - Patch,
9.3 - release candidate of the ninth version)

If the main fields of two versions are equal,
but the second contains a pre-build, second version is less.

If the build version has a sub-build version, provided that the second
version has the same build version and does not have a
sub-build version, then the second version is larger.

Main version must be auto-filled and always compare.
Example: 1 to 1.0.0
1.2 to 1.2.0

Comparision examples:
1.0.0 == 1
1.0.0.0 < 1 and 1.0.0.0 < 1.0.0
1.0.1.0 < 1.0.1
1.0.0-rc.1(equal 1.0.0.3.1) < 1.0.0
"""

iimport functools


@functools.total_ordering
class Version:
    """Class, which implemented version comparison."""

    def __init__(self, version):
        self.normalized_version = version_normalize(version)

    def __lt__(self, other):
        """Overriding python "Less" magic method.

        :param other: other normalized version
        :return: bool
        """
        version_couples = zip(self.normalized_version,
                              other.normalized_version)

        for version in version_couples:
            if version[0] < version[1]:
                return True

            elif version[0] > version[1]:
                return False

        if len(self.normalized_version) > len(other.normalized_version):
            return True

        return False

    def __ne__(self, other):
        """Overriding python "Not equal" magic method.

        :param other: other normalized version
        :return: bool
        """
        version_couples = zip(self.normalized_version,
                              other.normalized_version)

        for version in version_couples:
            if version[0] > version[1] or version[0] < version[1]:
                return True

        if len(self.normalized_version) != len(
                other.normalized_version):
            return True

        return False


def main():
    to_test = [
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0"),
        # ('1.0.0', '1')
    ]

    for version_1, version_2 in to_test:
        print(version_1, version_2)
        assert Version(version_1) < Version(version_2), "le failed"
        assert Version(version_2) > Version(version_1), "ge failed"
        assert Version(version_2) != Version(version_1), "neq failed"
    print('Semantic versions comparison completed successfully.')


def version_normalize(string: str):
    """Converting the string representation of the version to
    a form that will allow you to comparison versions.

    :param string: string representation of the version.
    :return: list
    """
    version = string
    arg_to_replace = {'-': '', 'beta': '.2', 'b': '.2', 'alpha': '.1',
                      'rc': '.3'}
    for key in arg_to_replace.keys():
        version = version.replace(key, arg_to_replace[key])
    version = version.split('.')

    # This construction needed here to adding one extra rule, which
    # cannot be done with zip_longest.

    while len(version) < 3:
        version.append('0')

    return version


if __name__ == "__main__":
    main()
