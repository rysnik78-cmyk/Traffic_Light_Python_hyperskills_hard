import re
from hstest import StageTest, CheckResult, TestedProgram, dynamic_test


class TrafficLightTest(StageTest):

    @dynamic_test
    def test(self):
        pr = TestedProgram()
        output = pr.start().lower()
        lines = re.split(r"[\r\n]+", output.strip())

        if len(lines) != 6:
            return CheckResult.wrong(
                f"There should be exactly 6 lines in the output, as in example, but there were {len(lines)} instead")
        if ("welcome" not in lines[0]) or ("traffic management system" not in lines[0]):
            return CheckResult.wrong("The first line of output should contain a greeting, as in example")
        if "menu" not in lines[1]:
            return CheckResult.wrong("The second line of output should tell the user, what is the list below for, " +
                                     "containing \"Menu\" substring")
        starts = ["1", "2", "3", "0"]
        contain = ["Add", "Delete", "System", "Quit"]
        for i in range(len(starts)):
            if not lines[2 + i].startswith(starts[i]) or not contain[i].lower() in lines[2 + i]:
                return CheckResult.wrong(
                    f"The {i + 1} line of menu list should start with \"{starts[i]}\" as an option from list and " +
                    f"contain \"{contain[i]}\" substring as in example")
        return CheckResult.correct()


if __name__ == '__main__':
    TrafficLightTest().run_tests()