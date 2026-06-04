from coldtype import *

@renderable(Rect("letter").scale(2), bg=1, fmt="pdf")
def shortcuts(r:Rect):
    column = r.take(430, "CX")
    return (P(
        StSt("For today’s HMCT workshop entitled", "FrankfurterEF-Highlight", 24, multiline=1).xalign(r),
        StSt("Dimensional\nTypography", "Bombere", 82).xalign(r),
        StSt("This is a sheet of", "FrankfurterEF-Highlight", 24, multiline=1).xalign(r),
        StSt("Keyboard Shortcuts", "Pioneer", 72, multiline=1).xalign(r),
        StSt("found useful in the operation of", "FrankfurterEF-Highlight", 24, multiline=1, bs=-2).xalign(r),
        StSt("BLENDER", "Buster", 130, multiline=1).xalign(r),
        P(Rect(0, 12, 800, 4)).addFrame(Rect(0, 0, 800, 24)).xalign(r),
        P(
            StSt("X + D\nshift + D\nshift + A\n\n0 (zero)\nshift + ~\nG then Z then Z\nopt + cmd + 0\n\n1\n3\n7\n\nG (+ x | y | z)\nS (+ x | y | z)\nR (+ x | y | z) ", "Airport_VF", fs:=30, leading=(lead:=24), wght=1, tnum=1).xalign(column, "W"),
            StSt("Delete\nDuplicate\nAdd Object\n\nJump to Camera\nLook Around\nDolly Zoom\nSet Camera\n\nView X Axis\nView Y Axis\nView Z Axis\n\nMove Object\nScale Object\nRotate Object", "Airport_VF", fs, leading=lead).xalign(column, "E"),
        ),
        P(Rect(0, 9, 800, 4)).addFrame(Rect(0, 0, 800, 18)).xalign(r),
        StSt("June 2026\nPasadena", "ToyBox", 44, multiline=1, EDPT=1, tu=100, EHLT=0).xalign(r),
        )
        .f(0)
        .stack(40)
        .align(r)
        .scale(0.85)
        )
