#Requires AutoHotkey v2.0

; Map Ctrl + \ to print a backtick
^SC029::
{
    Send("{``}")
    Return
}

; Map Ctrl + Shift + \ to print a tilde
^+SC029::
{
    Send("~")
    Return
}
