import re
import unittest
from collections import namedtuple


class VcomRegexTests(unittest.TestCase):
    regex = None

    def test_cases(self):
        for case in _cases:
            match_list = [
                match_tuple(**m.groupdict())
                for m in re.finditer(self.regex, case.output)
            ]

            self.assertListEqual(
                case.matches, match_list,
                "matches not as expected for case {}".format(case.name))


def run_tests(regex):
    VcomRegexTests.regex = regex
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(VcomRegexTests)
    unittest.TextTestRunner().run(suite)


case_tuple = namedtuple(
    "case_tuple",
    ("name", "output", "matches"))


match_tuple = namedtuple(
    "match_tuple",(
    "error", "warning", "file", "line", "message", "near", "code", "quote"))


_cases = []
_cases.append(case_tuple(
    name="message type name 1",
    output="""
** Error: sync.vhd(33): (vcom-1136) Unknown identifier "d_met".
""",
    matches=[match_tuple(
        error="Error",
        warning=None,
        file="sync.vhd",
        line='33',
        message="""(vcom-1136) Unknown identifier "d_met".""",
        near="d_met",
        code="vcom-1136",
        quote='"',
    )]
))

_cases.append(case_tuple(
    name="message type name 2",
    output="""
** Error: src/bus_mux_pipelined.vhd(56): near "elsif": (vcom-1576) expecting ';'.
""",
    matches=[match_tuple(
        error="Error",
        warning=None,
        file="src/bus_mux_pipelined.vhd",
        line='56',
        message="""near "elsif": (vcom-1576) expecting ';'.""",
        near="elsif",
        code=None,
        quote='"',
    )]
))

_cases.append(case_tuple(
    name="message type name 3",
    output="""
** Error: d:\\src\\bus_mux_pipelined.vhd(58): (vcom-1441) ELSIF GENERATE STATEMENT is not defined for this version of the language.
""",
    matches=[match_tuple(
        error="Error",
        warning=None,
        file="d:\\src\\bus_mux_pipelined.vhd",
        line='58',
        message="(vcom-1441) ELSIF GENERATE STATEMENT is not defined for this version of the language.",
        near=None,
        code=None,
        quote=None,
    )]
))

_cases.append(case_tuple(
    name="message type name 4",
    output="""
** Warning: bus_mux_pipelined.vhd(47): (vcom-1400) Synthesis Warning: Signal "sel" is read in the process but is not in the sensitivity list.
""",
    matches=[match_tuple(
        error=None,
        warning="Warning",
        file="bus_mux_pipelined.vhd",
        line='47',
        message="""(vcom-1400) Synthesis Warning: Signal "sel" is read in the process but is not in the sensitivity list.""",
        near="sel",
        code="vcom-1400",
        quote='"',
    )]
))

_cases.append(case_tuple(
    name="message type name 5",
    output="""
** Warning: sync.vhd(22): Synthesis Warning: Reset signal 'rst_n' is not in the sensitivity list of process 'line__22'.
""",
    matches=[match_tuple(
        error=None,
        warning="Warning",
        file="sync.vhd",
        line='22',
        message="Synthesis Warning: Reset signal 'rst_n' is not in the sensitivity list of process 'line__22'.",
        near="rst_n",
        code=None,
        quote="'",
    )]
))

_cases.append(case_tuple(
    name="message type name 6",
    output="""
** Error: demo.vhd(24): VHDL Compiler exiting
""",
    matches=[match_tuple(
        error="Error",
        warning=None,
        file="demo.vhd",
        line='24',
        message='',
        near=None,
        code=None,
        quote=None,
    )]
))
