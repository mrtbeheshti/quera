class Strint(int):
    def __lt__(self, other):
        if self % 10 < other % 10:
            return True
        return False

    def __gt__(self, other):
        if self % 10 > other % 10:
            return True
        return False

    def __le__(self, other):
        if self % 10 <= other % 10:
            return True
        return False

    def __ge__(self, other):
        if self % 10 >= other % 10:
            return True
        return False

    def __eq__(self, other):
        if self % 10 == other % 10:
            return True
        return False

    def __ne__(self, other):
        if self % 10 != other % 10:
            return True
        return False

    def __add__(self, other):
        return int(str(self) + str(other))

    def __sub__(self, other):
        result = ""
        str1 = str(self)
        str2 = str(other)
        if str1 == str2:
            return 0
        if str1.endswith(str2):
            str1 = str1[: -len(str2)]
            return int(str1)
        raise Exception("The subtraction is not valid!")

    def __len__(self):
        return len(str(self))

    def __call__(self):
        nums = {
            "1": "۱",
            "2": "۲",
            "3": "۳",
            "4": "۴",
            "5": "۵",
            "6": "۶",
            "7": "۷",
            "8": "۸",
            "9": "۹",
            "0": "۰",
        }
        result = ""
        for c in str(self):
            result += nums[c]
        return result
