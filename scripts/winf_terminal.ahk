#Requires AutoHotkey v2.0

; Open the terminal when pressing the keys Win(SUPER) + D
~LWin & f::
{
    Run "wt.exe"
    Return
}
